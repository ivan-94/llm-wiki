#!/usr/bin/env python3
"""Diff AI wiki human/raw Markdown files against mirrored human source notes."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


WIKI_ROOT = Path(__file__).resolve().parents[4]
HUMAN_RAW_ROOT = WIKI_ROOT / "human" / "raw"
SUPPORTED_SUFFIXES = {".md"}
REQUIRED_METADATA = ("raw_created_at", "raw_modified_at", "raw_size")
MTIME_TOLERANCE_SECONDS = 1.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-root", default=str(HUMAN_RAW_ROOT))
    parser.add_argument("--wiki-root", default=str(WIKI_ROOT))
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument("--markdown", action="store_true", help="Emit Markdown output")
    parser.add_argument(
        "--include-unsupported",
        action="store_true",
        help="Include unsupported files under human/raw in the report",
    )
    parser.add_argument(
        "--include-unapproved",
        action="store_true",
        help="Include human raw Markdown files without ingest_policy: allowed",
    )
    return parser.parse_args()


def is_supported_raw(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_SUFFIXES


def source_note_relpath_for_raw_relpath(relpath: str) -> str:
    return relpath


def iso_from_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, timezone.utc).isoformat()


def parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def parse_int(value: object) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def strip_frontmatter_value(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = strip_frontmatter_value(value)
    return frontmatter


def fingerprint(size: int, created_at: str, modified_at: str) -> str:
    return f"size={size};birth={created_at};mtime={modified_at}"


def ingest_policy(frontmatter: dict[str, str]) -> str:
    return frontmatter.get("ingest_policy", "").strip().lower()


def is_ingest_allowed(frontmatter: dict[str, str]) -> bool:
    return ingest_policy(frontmatter) == "allowed"


def unapproved_reason(frontmatter: dict[str, str]) -> str:
    policy = ingest_policy(frontmatter)
    if not policy:
        return "missing-ingest_policy-allowed"
    return f"ingest_policy={policy}"


def raw_item(raw_root: Path, path: Path, frontmatter: dict[str, str]) -> dict[str, object]:
    stat = path.stat()
    relpath = path.relative_to(raw_root).as_posix()
    created_at = iso_from_timestamp(getattr(stat, "st_birthtime", stat.st_mtime))
    modified_at = iso_from_timestamp(stat.st_mtime)
    return {
        "source_relpath": relpath,
        "raw_path": str(path),
        "target_source_note": str(Path("human") / "sources" / source_note_relpath_for_raw_relpath(relpath)),
        "raw_created_at": created_at,
        "raw_modified_at": modified_at,
        "raw_size": stat.st_size,
        "raw_fingerprint": fingerprint(stat.st_size, created_at, modified_at),
        "ingest_policy": ingest_policy(frontmatter) or None,
    }


def source_relpath_for_note(human_sources_root: Path, path: Path, frontmatter: dict[str, str]) -> str:
    return frontmatter.get("source_relpath") or path.relative_to(human_sources_root).as_posix()


def source_note_item(human_sources_root: Path, path: Path, frontmatter: dict[str, str]) -> dict[str, object]:
    relpath = source_relpath_for_note(human_sources_root, path, frontmatter)
    return {
        "source_relpath": relpath,
        "source_note": str(path),
        "frontmatter": frontmatter,
    }


def missing_metadata_fields(frontmatter: dict[str, str]) -> list[str]:
    missing = [key for key in REQUIRED_METADATA if not frontmatter.get(key)]
    if frontmatter.get("raw_modified_at") and parse_datetime(frontmatter.get("raw_modified_at")) is None:
        missing.append("raw_modified_at:invalid")
    if frontmatter.get("raw_created_at") and parse_datetime(frontmatter.get("raw_created_at")) is None:
        missing.append("raw_created_at:invalid")
    if frontmatter.get("raw_size") and parse_int(frontmatter.get("raw_size")) is None:
        missing.append("raw_size:invalid")
    return missing


def source_fingerprint(frontmatter: dict[str, str]) -> str | None:
    size = parse_int(frontmatter.get("raw_size"))
    created_at = parse_datetime(frontmatter.get("raw_created_at"))
    modified_at = parse_datetime(frontmatter.get("raw_modified_at"))
    if size is None or created_at is None or modified_at is None:
        return None
    return fingerprint(size, created_at.isoformat(), modified_at.isoformat())


def is_updated(raw: dict[str, object], frontmatter: dict[str, str]) -> bool:
    source_modified_at = parse_datetime(frontmatter.get("raw_modified_at"))
    source_size = parse_int(frontmatter.get("raw_size"))
    raw_modified_at = parse_datetime(raw.get("raw_modified_at"))
    if source_modified_at is None or raw_modified_at is None:
        return False
    if source_size is not None and int(raw["raw_size"]) != source_size:
        return True
    return raw_modified_at.timestamp() - source_modified_at.timestamp() >= MTIME_TOLERANCE_SECONDS


def scan(
    raw_root: Path,
    wiki_root: Path,
    include_unsupported: bool,
    include_unapproved: bool,
) -> dict[str, list[dict[str, object]]]:
    raw_root = raw_root.expanduser().resolve()
    wiki_root = wiki_root.expanduser().resolve()
    human_sources_root = wiki_root / "human" / "sources"

    eligible_raw: dict[str, dict[str, object]] = {}
    all_markdown_relpaths: set[str] = set()
    unapproved: list[dict[str, object]] = []
    unsupported: list[dict[str, object]] = []

    for path in sorted(raw_root.rglob("*")):
        if not path.is_file():
            continue
        if path.name.startswith(".") or path.name == ".DS_Store":
            continue
        relpath = path.relative_to(raw_root).as_posix()
        if not is_supported_raw(path):
            if include_unsupported:
                unsupported.append({"source_relpath": relpath, "raw_path": str(path), "reason": "unsupported-type"})
            continue

        all_markdown_relpaths.add(relpath)
        try:
            frontmatter = parse_frontmatter(path)
            item = raw_item(raw_root, path, frontmatter)
        except OSError as exc:
            if include_unsupported:
                unsupported.append({"source_relpath": relpath, "raw_path": str(path), "reason": str(exc)})
            continue

        if is_ingest_allowed(frontmatter):
            eligible_raw[relpath] = item
        elif include_unapproved:
            unapproved.append({**item, "reason": unapproved_reason(frontmatter)})

    source_notes: dict[str, dict[str, object]] = {}
    if human_sources_root.exists():
        for path in sorted(human_sources_root.rglob("*.md")):
            if path.name == ".gitkeep":
                continue
            frontmatter = parse_frontmatter(path)
            item = source_note_item(human_sources_root, path, frontmatter)
            source_notes[str(item["source_relpath"])] = item

    if include_unapproved:
        for item in unapproved:
            source = source_notes.get(str(item["source_relpath"]))
            if source:
                item["source_note"] = source["source_note"]

    raw_relpaths = set(eligible_raw)
    source_relpaths = set(source_notes)
    raw_without_same_source = sorted(raw_relpaths - source_relpaths)
    source_without_raw = sorted(source_relpaths - all_markdown_relpaths)

    moved: list[dict[str, object]] = []
    moved_targets: set[str] = set()
    raw_by_fingerprint: dict[str, dict[str, object]] = {
        str(item["raw_fingerprint"]): item for relpath, item in eligible_raw.items() if relpath in raw_without_same_source
    }
    for relpath in source_without_raw:
        source = source_notes[relpath]
        frontmatter = source["frontmatter"]
        if not isinstance(frontmatter, dict) or missing_metadata_fields(frontmatter):
            continue
        match = raw_by_fingerprint.get(source_fingerprint(frontmatter) or "")
        if not match:
            continue
        moved.append(
            {
                "from_source_relpath": relpath,
                "to_source_relpath": match["source_relpath"],
                "source_note": source["source_note"],
                "raw_path": match["raw_path"],
                "reason": "same-size-created-at-modified-at",
            }
        )
        moved_targets.add(str(match["source_relpath"]))

    added = [eligible_raw[relpath] for relpath in raw_without_same_source if relpath not in moved_targets]
    deleted = [
        {"source_relpath": relpath, "source_note": source_notes[relpath]["source_note"]}
        for relpath in source_without_raw
        if relpath not in {str(item["from_source_relpath"]) for item in moved}
    ]

    updated: list[dict[str, object]] = []
    unchanged: list[dict[str, object]] = []
    needs_metadata: list[dict[str, object]] = []
    for relpath in sorted(raw_relpaths & source_relpaths):
        raw = eligible_raw[relpath]
        source = source_notes[relpath]
        frontmatter = source["frontmatter"]
        if not isinstance(frontmatter, dict):
            frontmatter = {}
        missing = missing_metadata_fields(frontmatter)
        if missing:
            needs_metadata.append(
                {
                    "source_relpath": relpath,
                    "source_note": source["source_note"],
                    "raw_path": raw["raw_path"],
                    "missing_fields": missing,
                }
            )
            continue
        if is_updated(raw, frontmatter):
            updated.append({**raw, "source_note": source["source_note"], "previous_raw_modified_at": frontmatter.get("raw_modified_at")})
        else:
            unchanged.append({**raw, "source_note": source["source_note"]})

    return {
        "added": added,
        "deleted": deleted,
        "updated": updated,
        "moved": moved,
        "unchanged": unchanged,
        "needs_metadata": needs_metadata,
        "unapproved": unapproved,
        "unsupported": unsupported,
    }


def print_markdown(payload: dict[str, list[dict[str, object]]]) -> None:
    for key, items in payload.items():
        print(f"## {key}")
        if not items:
            print("- none")
            continue
        for item in items:
            if key == "moved":
                print(f"- `{item['from_source_relpath']}` -> `{item['to_source_relpath']}`")
            elif key == "unapproved":
                print(f"- `{item['source_relpath']}` ({item['reason']})")
            else:
                print(f"- `{item['source_relpath']}`")


def main() -> int:
    args = parse_args()
    payload = scan(Path(args.raw_root), Path(args.wiki_root), args.include_unsupported, args.include_unapproved)
    if args.markdown and not args.json:
        print_markdown(payload)
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
