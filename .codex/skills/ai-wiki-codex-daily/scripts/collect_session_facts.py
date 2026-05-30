#!/usr/bin/env python3
"""Collect local Codex session facts for daily-review fallback."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date as date_type
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


DEFAULT_SESSIONS_ROOT = Path.home() / ".codex" / "sessions"
DEFAULT_TIMEZONE = "Asia/Shanghai"
MAX_TEXT_CHARS = 1200
MAX_AGENT_UPDATE_CHARS = 500
MAX_TOOL_ARG_CHARS = 500


@dataclass
class TurnFacts:
    turn_id: str | None = None
    started_at: int | None = None
    completed_at: int | None = None
    status: str = "started"
    user_messages: list[str] = field(default_factory=list)
    agent_updates: list[str] = field(default_factory=list)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    file_changes: list[dict[str, str | None]] = field(default_factory=list)
    messages: list[dict[str, Any]] = field(default_factory=list)
    last_agent_message: str | None = None
    duration_ms: int | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date_type.today().isoformat(), help="Target date YYYY-MM-DD")
    parser.add_argument("--sessions-root", default=str(DEFAULT_SESSIONS_ROOT))
    parser.add_argument("--timezone", default=DEFAULT_TIMEZONE, help="Local timezone for date attribution")
    parser.add_argument("--group-id", help="Emit one YAML timeline group by id")
    parser.add_argument("--compact", action="store_true", help="Emit compact daily-review facts (default)")
    parser.add_argument("--full", action="store_true", help="Emit full parsed fallback facts for debugging")
    parser.add_argument("--json", action="store_true", help="Emit machine JSON instead of YAML group output")
    return parser.parse_args()


def truncate(value: object, limit: int = MAX_TEXT_CHARS) -> str:
    text = str(value or "").strip()
    if len(text) <= limit:
        return text
    return f"{text[: limit - 3].rstrip()}..."


def parse_tool_arguments(payload: dict[str, Any]) -> dict[str, Any]:
    raw_args = payload.get("arguments")
    if raw_args is None:
        raw_args = payload.get("args")
    if raw_args is None:
        return {}
    if isinstance(raw_args, dict):
        return raw_args
    if isinstance(raw_args, str):
        try:
            parsed = json.loads(raw_args)
        except json.JSONDecodeError:
            return {"raw": truncate(raw_args, MAX_TOOL_ARG_CHARS)}
        return parsed if isinstance(parsed, dict) else {}
    return {}


def compact_arg(value: object, limit: int = MAX_TOOL_ARG_CHARS) -> object:
    if isinstance(value, str):
        return truncate(value, limit)
    if isinstance(value, (int, float, bool)) or value is None:
        return value
    return truncate(json.dumps(value, ensure_ascii=False, sort_keys=True), limit)


def compact_tool_call(payload: dict[str, Any]) -> dict[str, Any]:
    name = payload.get("name") or payload.get("call_id") or "function_call"
    if not isinstance(name, str):
        name = "function_call"

    args = parse_tool_arguments(payload)
    if name == "apply_patch":
        return {"name": name, "args": {}}

    kept: dict[str, Any] = {}
    for key in ("cmd", "threadId", "query", "path", "ref_id", "file", "id", "session_id"):
        if key in args:
            kept[key] = compact_arg(args[key])
    if "cursor" in args:
        kept["has_cursor"] = bool(args.get("cursor"))
    return {"name": name, "args": kept}


def compact_file_changes(payload: dict[str, Any]) -> list[dict[str, str | None]]:
    changes = payload.get("changes")
    if not isinstance(changes, list):
        return []
    compacted: list[dict[str, str | None]] = []
    for change in changes:
        if not isinstance(change, dict):
            continue
        kind = change.get("kind")
        if isinstance(kind, dict):
            kind_type = kind.get("type")
        elif isinstance(kind, str):
            kind_type = kind
        else:
            kind_type = None
        path = change.get("path")
        compacted.append({"path": path if isinstance(path, str) else None, "kind": kind_type})
    return compacted


def parse_json_line(line: str, path: Path, lineno: int) -> dict[str, Any] | None:
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return {"type": "parse_error", "path": str(path), "lineno": lineno}


def event_type(record: dict[str, Any]) -> str | None:
    payload = record.get("payload")
    if isinstance(payload, dict):
        return payload.get("type")
    return None


def get_text_content(content: object) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for item in content:
        if isinstance(item, dict):
            text = item.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)


def ensure_turn(turns: list[TurnFacts], current: TurnFacts | None = None) -> TurnFacts:
    if current is not None:
        return current
    if turns:
        return turns[-1]
    turn = TurnFacts(status="unknown")
    turns.append(turn)
    return turn


def nested_dict(value: object) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def extract_subagent_meta(meta: dict[str, Any]) -> dict[str, Any]:
    source = nested_dict(meta.get("source"))
    subagent = nested_dict(source.get("subagent"))
    spawn = nested_dict(subagent.get("thread_spawn"))
    return {
        "thread_source": meta.get("thread_source"),
        "parent_thread_id": spawn.get("parent_thread_id"),
        "subagent_depth": spawn.get("depth"),
        "agent_role": meta.get("agent_role") or spawn.get("agent_role"),
        "agent_nickname": meta.get("agent_nickname") or spawn.get("agent_nickname"),
    }


def latest_user_messages(turns: list[TurnFacts]) -> list[str]:
    messages: list[str] = []
    for turn in turns:
        messages.extend(turn.user_messages)
    return messages


def session_status(turns: list[TurnFacts]) -> str:
    if not turns:
        return "unknown"
    last = turns[-1]
    if last.status == "complete":
        return "complete"
    return "incomplete"


def parse_rollout(path: Path) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    context: dict[str, Any] = {}
    turns: list[TurnFacts] = []
    current_turn: TurnFacts | None = None
    parse_errors: list[dict[str, Any]] = []

    with path.open(encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = parse_json_line(line, path, lineno)
            if record is None:
                continue
            if record.get("type") == "parse_error":
                parse_errors.append(record)
                continue

            payload = record.get("payload")
            if not isinstance(payload, dict):
                continue

            record_type = record.get("type")
            if record_type == "session_meta":
                meta = payload
                continue
            if record_type == "turn_context":
                context = payload
                continue

            if record_type == "event_msg":
                kind = event_type(record)
                if kind == "task_started":
                    current_turn = TurnFacts(
                        turn_id=payload.get("turn_id"),
                        started_at=payload.get("started_at"),
                        status="started",
                    )
                    turns.append(current_turn)
                elif kind == "user_message":
                    turn = ensure_turn(turns, current_turn)
                    message = payload.get("message") or get_text_content(payload.get("content"))
                    if message:
                        text = str(message).strip()
                        turn.user_messages.append(text)
                        turn.messages.append({"type": "user", "text": text})
                elif kind == "agent_message":
                    turn = ensure_turn(turns, current_turn)
                    message = payload.get("message") or payload.get("text")
                    if message:
                        text = truncate(message, MAX_AGENT_UPDATE_CHARS)
                        turn.agent_updates.append(text)
                        turn.messages.append({"type": "assistant", "text": text})
                elif kind == "task_complete":
                    turn = ensure_turn(turns, current_turn)
                    turn.status = "complete"
                    turn.completed_at = payload.get("completed_at")
                    turn.duration_ms = payload.get("duration_ms")
                    if payload.get("last_agent_message"):
                        turn.last_agent_message = truncate(payload["last_agent_message"])
                        if turn.messages and turn.messages[-1].get("type") == "assistant" and turn.messages[-1].get("text") == turn.last_agent_message:
                            turn.messages[-1]["type"] = "assistant_final"
                        else:
                            turn.messages.append({"type": "assistant_final", "text": turn.last_agent_message})
                    current_turn = None
                elif kind and kind not in {"token_count"}:
                    turn = ensure_turn(turns, current_turn)
                    turn.agent_updates.append(f"event:{kind}")
                    turn.messages.append({"type": "event", "name": kind})
                continue

            if record_type == "response_item" and payload.get("type") == "function_call":
                turn = ensure_turn(turns, current_turn)
                tool_call = compact_tool_call(payload)
                turn.tool_calls.append(tool_call)
                turn.messages.append({"type": "tool_call", **tool_call})
                continue

            if record_type == "response_item" and payload.get("type") in {"fileChange", "file_change"}:
                turn = ensure_turn(turns, current_turn)
                file_changes = compact_file_changes(payload)
                turn.file_changes.extend(file_changes)
                if file_changes:
                    turn.messages.append({"type": "file_change", "changes": file_changes})
                continue

    serialized_turns = []
    for turn in turns:
        serialized_turns.append(
            {
                "turn_id": turn.turn_id,
                "status": turn.status,
                "started_at": turn.started_at,
                "completed_at": turn.completed_at,
                "duration_ms": turn.duration_ms,
                "user_messages": turn.user_messages,
                "agent_updates": turn.agent_updates[:8],
                "tool_calls": turn.tool_calls,
                "file_changes": turn.file_changes,
                "messages": turn.messages,
                "last_agent_message": turn.last_agent_message,
            }
        )

    subagent_meta = extract_subagent_meta(meta)
    return {
        "thread_id": meta.get("id"),
        "session_timestamp": meta.get("timestamp"),
        "cwd": context.get("cwd") or meta.get("cwd"),
        "model": context.get("model") or meta.get("model_provider"),
        **subagent_meta,
        "path": str(path),
        "status": session_status(turns),
        "user_messages": latest_user_messages(turns),
        "last_agent_message": next((turn.last_agent_message for turn in reversed(turns) if turn.last_agent_message), None),
        "turns": serialized_turns,
        "parse_errors": parse_errors,
    }


def session_dir_for_date(root: Path, target_date: str) -> Path:
    parsed = datetime.strptime(target_date, "%Y-%m-%d")
    return root.expanduser() / f"{parsed.year:04d}" / f"{parsed.month:02d}" / f"{parsed.day:02d}"


def collect(target_date: str, sessions_root: Path) -> dict[str, Any]:
    session_dir = session_dir_for_date(sessions_root, target_date)
    files = sorted(session_dir.glob("rollout-*.jsonl")) if session_dir.exists() else []
    return {
        "date": target_date,
        "source_strategy": "fallback-local-session-jsonl-full",
        "sessions_root": str(sessions_root.expanduser()),
        "session_dir": str(session_dir),
        "sessions": [parse_rollout(path) for path in files],
    }


def local_date_for_timestamp(timestamp: str | None, timezone: str) -> str | None:
    if not timestamp:
        return None
    try:
        text = timestamp.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=ZoneInfo("UTC"))
        return parsed.astimezone(ZoneInfo(timezone)).date().isoformat()
    except (ValueError, ZoneInfoNotFoundError):
        return None


def is_worker_like(session: dict[str, Any]) -> bool:
    text = "\n".join(session.get("user_messages") or [])
    patterns = [
        r"\bworker\b",
        r"Read-only exploration task",
        r"Repair source note",
        r"repairing source note",
        r"Scope [A-Z]",
        r"batch \d+",
    ]
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def normalize_status(session: dict[str, Any]) -> dict[str, str]:
    raw = str(session.get("status") or "unknown")
    turns = session.get("turns") or []
    turn_statuses = [str(turn.get("status")) for turn in turns if isinstance(turn, dict)]
    last_agent_message = session.get("last_agent_message")
    if any(status == "interrupted" for status in turn_statuses):
        return {"normalized": "中断", "raw": raw, "reason": "turn status is interrupted"}
    if raw == "incomplete":
        return {"normalized": "活跃", "raw": raw, "reason": "no task_complete event in latest turn"}
    if raw == "complete":
        if not last_agent_message and is_worker_like(session):
            return {
                "normalized": "中断",
                "raw": raw,
                "reason": "complete record without final agent message for worker-like task",
            }
        return {"normalized": "已完成", "raw": raw, "reason": "complete record with sufficient closing signal"}
    return {"normalized": "未知", "raw": raw, "reason": "unrecognized fallback status"}


def classify_group(session: dict[str, Any]) -> tuple[str, str, int | None]:
    text = "\n".join(session.get("user_messages") or [])
    vibe = re.search(r"Vibe ingest batch ([0-9]+)(?:-([0-9]+))?", text, flags=re.IGNORECASE)
    if vibe:
        return ("vibe-ingest-batches", "Vibe ingest batch", int(vibe.group(2) or vibe.group(1)))
    if re.search(r"metadata backfill unsynced AI wiki raw batch", text, flags=re.IGNORECASE):
        batch = re.search(r"batch ([0-9]+)", text, flags=re.IGNORECASE)
        return ("raw-metadata-backfill-batches", "Raw metadata backfill batch", int(batch.group(1)) if batch else None)
    if re.search(r"unsynced AI wiki raw batch", text, flags=re.IGNORECASE):
        batch = re.search(r"batch ([0-9]+)", text, flags=re.IGNORECASE)
        return ("unsynced-raw-ingest-batches", "Unsynced raw ingest batch", int(batch.group(1)) if batch else None)
    if "Read-only exploration task" in text and "Links" in text:
        return ("source-links-readonly-exploration", "Source Links read-only exploration", None)
    if re.search(r"Repair source note|repairing source note", text, flags=re.IGNORECASE):
        return ("source-links-repair-workers", "Source Links repair workers", None)
    thread_id = session.get("thread_id") or Path(str(session.get("path") or "")).stem
    return (f"session-{thread_id}", f"Session {thread_id}", None)


def summarize_agent_updates(updates: list[str], limit: int = 5) -> dict[str, Any]:
    if len(updates) <= limit:
        items = updates
    else:
        head_count = max(1, limit - 2)
        items = updates[:head_count] + updates[-2:]
    return {"count": len(updates), "items": items, "truncated": max(0, len(updates) - len(items))}


def summarize_tool_calls(tool_calls: list[dict[str, Any]], limit: int = 4) -> dict[str, Any]:
    counts: dict[str, int] = {}
    examples: list[dict[str, Any]] = []
    for call in tool_calls:
        if not isinstance(call, dict):
            continue
        name = str(call.get("name") or "unknown")
        counts[name] = counts.get(name, 0) + 1
        if len(examples) < limit:
            examples.append(call)
    total = sum(counts.values())
    return {
        "count": total,
        "names": dict(sorted(counts.items())),
        "examples": examples,
        "truncated": max(0, total - len(examples)),
    }


def compact_session(session: dict[str, Any], target_date: str, timezone: str) -> dict[str, Any]:
    local_date = local_date_for_timestamp(session.get("session_timestamp"), timezone)
    status = normalize_status(session)
    compact_turns = []
    for turn in session.get("turns") or []:
        if not isinstance(turn, dict):
            continue
        compact_turns.append(
            {
                "turn_id": turn.get("turn_id"),
                "status": turn.get("status"),
                "started_at": turn.get("started_at"),
                "completed_at": turn.get("completed_at"),
                "duration_ms": turn.get("duration_ms"),
                "user_message_count": len(turn.get("user_messages") or []),
                "agent_updates": summarize_agent_updates(turn.get("agent_updates") or []),
                "tool_calls": summarize_tool_calls(turn.get("tool_calls") or []),
                "file_changes": turn.get("file_changes") or [],
            }
        )
    return {
        "thread_id": session.get("thread_id"),
        "path": session.get("path"),
        "cwd": session.get("cwd"),
        "model": session.get("model"),
        "thread_source": session.get("thread_source"),
        "parent_thread_id": session.get("parent_thread_id"),
        "subagent_depth": session.get("subagent_depth"),
        "agent_role": session.get("agent_role"),
        "agent_nickname": session.get("agent_nickname"),
        "session_timestamp_utc": session.get("session_timestamp"),
        "local_date": local_date,
        "date_mismatch": bool(local_date and local_date != target_date),
        "status": status,
        "user_messages": session.get("user_messages") or [],
        "last_agent_message": truncate(session.get("last_agent_message"), 800),
        "turns": compact_turns,
        "parse_errors": session.get("parse_errors") or [],
    }


def summarize_group_title(base_title: str, batch_numbers: list[int | None]) -> str:
    numbers = sorted(number for number in batch_numbers if number is not None)
    if not numbers:
        return base_title
    if len(numbers) == 1:
        return f"{base_title} {numbers[0]}"
    return f"{base_title} {numbers[0]}-{numbers[-1]}"


def compact_groups(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for session in sessions:
        group_id, base_title, batch_number = classify_group(session)
        bucket = buckets.setdefault(
            group_id,
            {
                "group_id": group_id,
                "base_title": base_title,
                "batch_numbers": [],
                "thread_ids": [],
                "parent_thread_ids": [],
                "status_summary": {},
                "session_count": 0,
                "exceptions": [],
            },
        )
        bucket["batch_numbers"].append(batch_number)
        if session.get("thread_id"):
            bucket["thread_ids"].append(session["thread_id"])
        if session.get("parent_thread_id") and session.get("parent_thread_id") not in bucket["parent_thread_ids"]:
            bucket["parent_thread_ids"].append(session["parent_thread_id"])
        normalized = session.get("status", {}).get("normalized", "未知")
        bucket["status_summary"][normalized] = bucket["status_summary"].get(normalized, 0) + 1
        bucket["session_count"] += 1
        if normalized in {"中断", "阻塞", "未知"}:
            bucket["exceptions"].append(
                {
                    "thread_id": session.get("thread_id"),
                    "status": normalized,
                    "reason": session.get("status", {}).get("reason"),
                }
            )

    groups: list[dict[str, Any]] = []
    for bucket in buckets.values():
        groups.append(
            {
                "group_id": bucket["group_id"],
                "title": summarize_group_title(bucket["base_title"], bucket["batch_numbers"]),
                "session_count": bucket["session_count"],
                "thread_ids": bucket["thread_ids"],
                "parent_thread_ids": bucket["parent_thread_ids"],
                "status_summary": bucket["status_summary"],
                "exceptions": bucket["exceptions"],
            }
        )
    return groups


def ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def infer_parent_workflow_title(parent_thread_id: str, parent_session: dict[str, Any] | None, group_ids: list[str]) -> str:
    text = "\n".join(parent_session.get("user_messages") or []) if parent_session else ""
    if "Links" in text or "links" in text or "链接" in text:
        return "Source Links 修复工作流"
    group_set = set(group_ids)
    if {
        "vibe-ingest-batches",
        "unsynced-raw-ingest-batches",
    } & group_set:
        return "Full raw ingest workflow"
    return f"Parent workflow {parent_thread_id}"


def compact_parent_workflows(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sessions_by_thread = {session.get("thread_id"): session for session in sessions if session.get("thread_id")}
    parent_ids = ordered_unique(
        [
            str(session.get("parent_thread_id"))
            for session in sessions
            if session.get("parent_thread_id")
        ]
    )
    workflows: list[dict[str, Any]] = []
    for parent_id in parent_ids:
        child_sessions = [session for session in sessions if session.get("parent_thread_id") == parent_id]
        parent_session = sessions_by_thread.get(parent_id)
        workflow_sessions = ([parent_session] if parent_session else []) + child_sessions
        group_ids = ordered_unique([classify_group(session)[0] for session in workflow_sessions])
        thread_ids = ordered_unique([str(session.get("thread_id")) for session in workflow_sessions if session.get("thread_id")])
        status_summary: dict[str, int] = {}
        exceptions: list[dict[str, str | None]] = []
        for session in workflow_sessions:
            status = session.get("status", {}) if isinstance(session.get("status"), dict) else {}
            normalized = str(status.get("normalized") or "未知")
            status_summary[normalized] = status_summary.get(normalized, 0) + 1
            if normalized in {"中断", "阻塞", "未知"}:
                exceptions.append(
                    {
                        "thread_id": session.get("thread_id"),
                        "status": normalized,
                        "reason": status.get("reason"),
                    }
                )
        workflows.append(
            {
                "workflow_id": f"parent-{parent_id}",
                "parent_thread_id": parent_id,
                "title": infer_parent_workflow_title(parent_id, parent_session, group_ids),
                "session_count": len(workflow_sessions),
                "child_session_count": len(child_sessions),
                "group_ids": group_ids,
                "thread_ids": thread_ids,
                "status_summary": status_summary,
                "exceptions": exceptions,
            }
        )
    return workflows


def compact_payload(full_payload: dict[str, Any], target_date: str, timezone: str) -> dict[str, Any]:
    sessions = [compact_session(session, target_date, timezone) for session in full_payload.get("sessions", [])]
    groups = compact_groups(sessions)
    return {
        "date": target_date,
        "timezone": timezone,
        "format": "compact",
        "source_strategy": "fallback-local-session-jsonl-compact",
        "sessions_root": full_payload.get("sessions_root"),
        "session_dir": full_payload.get("session_dir"),
        "parent_workflows": compact_parent_workflows(sessions),
        "groups": groups,
        "sessions": sessions,
    }


def yaml_scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    if re.fullmatch(r"[\w\u4e00-\u9fff./@:+() \-]+", text) and not text.startswith(("-", "?", "@", "&", "*", "!")):
        return text
    return json.dumps(text, ensure_ascii=False)


def block_text(text: object, indent: int) -> list[str]:
    padding = " " * indent
    body = str(text or "")
    if not body:
        return [padding]
    return [f"{padding}{line}" if line else padding for line in body.splitlines()]


def render_mapping(mapping: dict[str, Any], indent: int = 0) -> list[str]:
    lines: list[str] = []
    padding = " " * indent
    for key, value in mapping.items():
        if isinstance(value, dict):
            lines.append(f"{padding}{key}:")
            lines.extend(render_mapping(value, indent + 2))
        elif isinstance(value, list):
            lines.append(f"{padding}{key}:")
            if not value:
                lines.append(f"{padding}  []")
            else:
                for item in value:
                    if isinstance(item, dict):
                        lines.append(f"{padding}  -")
                        lines.extend(render_mapping(item, indent + 4))
                    else:
                        lines.append(f"{padding}  - {yaml_scalar(item)}")
        else:
            lines.append(f"{padding}{key}: {yaml_scalar(value)}")
    return lines


def render_group_index(compact: dict[str, Any]) -> str:
    lines = [
        f"date: {yaml_scalar(compact.get('date'))}",
        f"timezone: {yaml_scalar(compact.get('timezone'))}",
        "format: group-index",
        f"session_count: {len(compact.get('sessions') or [])}",
    ]
    workflows = compact.get("parent_workflows") or []
    lines.append("parent_workflows:")
    if workflows:
        for workflow in workflows:
            lines.append(f"  - workflow_id: {yaml_scalar(workflow.get('workflow_id'))}")
            lines.append(f"    title: {yaml_scalar(workflow.get('title'))}")
            lines.append(f"    parent_thread_id: {yaml_scalar(workflow.get('parent_thread_id'))}")
            lines.append(f"    session_count: {yaml_scalar(workflow.get('session_count'))}")
            lines.append(f"    child_session_count: {yaml_scalar(workflow.get('child_session_count'))}")
            lines.append("    groups:")
            for group_id in workflow.get("group_ids") or []:
                lines.append(f"      - {yaml_scalar(group_id)}")
            lines.append("    status_summary:")
            status_summary = workflow.get("status_summary") or {}
            if status_summary:
                for key, value in status_summary.items():
                    lines.append(f"      {key}: {yaml_scalar(value)}")
            else:
                lines.append("      {}")
            exceptions = workflow.get("exceptions") or []
            lines.append(f"    exception_count: {len(exceptions)}")
    else:
        lines.append("  []")
    lines.append("groups:")
    for group in compact.get("groups") or []:
        lines.append(f"  - group_id: {yaml_scalar(group.get('group_id'))}")
        lines.append(f"    title: {yaml_scalar(group.get('title'))}")
        parent_thread_ids = group.get("parent_thread_ids") or []
        if parent_thread_ids:
            lines.append("    parent_thread_ids:")
            for parent_thread_id in parent_thread_ids:
                lines.append(f"      - {yaml_scalar(parent_thread_id)}")
        lines.append(f"    session_count: {yaml_scalar(group.get('session_count'))}")
        lines.append("    status_summary:")
        status_summary = group.get("status_summary") or {}
        if status_summary:
            for key, value in status_summary.items():
                lines.append(f"      {key}: {yaml_scalar(value)}")
        else:
            lines.append("      {}")
        exceptions = group.get("exceptions") or []
        lines.append(f"    exception_count: {len(exceptions)}")
        lines.append(f"    read_command: {yaml_scalar(f'collect_session_facts.py --date {compact.get('date')} --group-id {group.get('group_id')}')}")
    return "\n".join(lines) + "\n"


def flush_tool_run(lines: list[str], run: list[dict[str, Any]], indent: int) -> None:
    if not run:
        return
    padding = " " * indent
    name = str(run[0].get("name") or "tool")
    suffix = f" x{len(run)}" if len(run) > 1 else ""
    lines.append(f"{padding}- tool_call: {yaml_scalar(name + suffix)}")
    examples = run[:3]
    if examples:
        lines.append(f"{padding}  examples:")
        for item in examples:
            lines.append(f"{padding}    -")
            args = item.get("args") if isinstance(item.get("args"), dict) else {}
            if args:
                lines.extend(render_mapping(args, indent + 6))
            else:
                lines.append(f"{padding}      args: {{}}")
    if len(run) > len(examples):
        lines.append(f"{padding}  truncated: {len(run) - len(examples)}")


def render_messages(messages: list[dict[str, Any]], indent: int) -> list[str]:
    lines: list[str] = []
    tool_run: list[dict[str, Any]] = []
    for message in messages:
        kind = message.get("type")
        if kind == "tool_call":
            name = message.get("name")
            if tool_run and tool_run[-1].get("name") != name:
                flush_tool_run(lines, tool_run, indent)
                tool_run = []
            tool_run.append(message)
            continue
        flush_tool_run(lines, tool_run, indent)
        tool_run = []
        padding = " " * indent
        if kind in {"user", "assistant", "assistant_final"}:
            label = "assistant_final" if kind == "assistant_final" else kind
            lines.append(f"{padding}- {label}: |-")
            lines.extend(block_text(message.get("text"), indent + 4))
        elif kind == "file_change":
            lines.append(f"{padding}- file_change:")
            for change in message.get("changes") or []:
                lines.append(f"{padding}    - path: {yaml_scalar(change.get('path'))}")
                lines.append(f"{padding}      kind: {yaml_scalar(change.get('kind'))}")
        elif kind == "event":
            lines.append(f"{padding}- event: {yaml_scalar(message.get('name'))}")
    flush_tool_run(lines, tool_run, indent)
    return lines


def session_messages(session: dict[str, Any]) -> list[dict[str, Any]]:
    messages: list[dict[str, Any]] = []
    for turn in session.get("turns") or []:
        if isinstance(turn, dict):
            messages.extend(turn.get("messages") or [])
    return messages


def compact_session_for_status(session: dict[str, Any], target_date: str, timezone: str) -> dict[str, Any]:
    return compact_session(session, target_date, timezone)


def render_session_timeline(session: dict[str, Any], compact_session_item: dict[str, Any], indent: int) -> list[str]:
    padding = " " * indent
    lines = [
        f"{padding}thread_id: {yaml_scalar(session.get('thread_id'))}",
        f"{padding}cwd: {yaml_scalar(session.get('cwd'))}",
        f"{padding}status: {yaml_scalar(compact_session_item.get('status', {}).get('normalized'))}",
        f"{padding}status_reason: {yaml_scalar(compact_session_item.get('status', {}).get('reason'))}",
    ]
    if session.get("parent_thread_id"):
        lines.append(f"{padding}parent_thread_id: {yaml_scalar(session.get('parent_thread_id'))}")
    if session.get("agent_role"):
        lines.append(f"{padding}agent_role: {yaml_scalar(session.get('agent_role'))}")
    if session.get("agent_nickname"):
        lines.append(f"{padding}agent_nickname: {yaml_scalar(session.get('agent_nickname'))}")
    lines.append(f"{padding}messages:")
    rendered_messages = render_messages(session_messages(session), indent + 2)
    lines.extend(rendered_messages if rendered_messages else [f"{padding}  []"])
    return lines


def render_group_document(full_payload: dict[str, Any], target_date: str, timezone: str, group_id: str) -> str:
    compact = compact_payload(full_payload, target_date, timezone)
    groups = {group.get("group_id"): group for group in compact.get("groups") or []}
    if group_id not in groups:
        available = ", ".join(str(group.get("group_id")) for group in compact.get("groups") or [])
        raise SystemExit(f"Unknown group_id: {group_id}. Available: {available}")
    group = groups[group_id]
    sessions = full_payload.get("sessions") or []
    compact_sessions = [compact_session_for_status(session, target_date, timezone) for session in sessions]
    selected: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for session, compact_item in zip(sessions, compact_sessions):
        current_group_id, _, _ = classify_group(compact_item)
        if current_group_id == group_id:
            selected.append((session, compact_item))

    lines = [
        f"group_id: {yaml_scalar(group.get('group_id'))}",
        f"title: {yaml_scalar(group.get('title'))}",
        f"date: {yaml_scalar(target_date)}",
        f"timezone: {yaml_scalar(timezone)}",
        f"session_count: {yaml_scalar(group.get('session_count'))}",
        "status_summary:",
    ]
    for key, value in (group.get("status_summary") or {}).items():
        lines.append(f"  {key}: {yaml_scalar(value)}")

    if len(selected) == 1:
        lines.extend(render_session_timeline(selected[0][0], selected[0][1], 0))
        lines.append("subagents: {}")
        return "\n".join(lines) + "\n"

    lines.append("messages:")
    lines.append("  - assistant: |-")
    lines.append(f"      Group contains {len(selected)} subagent/session timelines. Read `subagents` for ordered messages.")
    lines.append("subagents:")
    for session, compact_item in selected:
        thread_id = str(session.get("thread_id") or "unknown")
        lines.append(f"  {yaml_scalar(thread_id)}:")
        lines.extend(render_session_timeline(session, compact_item, 4))
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    try:
        ZoneInfo(args.timezone)
    except ZoneInfoNotFoundError as exc:
        raise SystemExit(f"Unknown timezone: {args.timezone}") from exc
    full_payload = collect(args.date, Path(args.sessions_root))
    if args.full:
        try:
            print(json.dumps(full_payload, ensure_ascii=False, indent=2))
        except BrokenPipeError:
            sys.exit(0)
        return

    compact = compact_payload(full_payload, args.date, args.timezone)
    if args.json:
        try:
            print(json.dumps(compact, ensure_ascii=False, indent=2))
        except BrokenPipeError:
            sys.exit(0)
        return

    try:
        if args.group_id:
            print(render_group_document(full_payload, args.date, args.timezone, args.group_id), end="")
        else:
            print(render_group_index(compact), end="")
    except BrokenPipeError:
        sys.exit(0)
    return


if __name__ == "__main__":
    main()
