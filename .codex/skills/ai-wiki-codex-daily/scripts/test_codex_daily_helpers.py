import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
COLLECT_SCRIPT = SCRIPT_DIR / "collect_session_facts.py"


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(record) for record in records), encoding="utf-8")


class CodexDailyHelperTests(unittest.TestCase):
    def test_default_output_lists_groups_as_yaml(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / "2026" / "05" / "30" / "rollout-2026-05-30T10-00-00-thread-1.jsonl"
            write_jsonl(
                rollout,
                [
                    {
                        "type": "session_meta",
                        "payload": {
                            "id": "thread-1",
                            "timestamp": "2026-05-30T10:00:00Z",
                            "cwd": "/repo",
                            "model_provider": "openai",
                        },
                    },
                    {
                        "type": "turn_context",
                        "payload": {"turn_id": "turn-1", "cwd": "/repo", "model": "gpt-test"},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_started", "turn_id": "turn-1", "started_at": 1},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "user_message", "message": "生成今天的 Codex 日报"},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "agent_message", "message": "先读取 thread 列表。"},
                    },
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "exec_command",
                            "arguments": json.dumps(
                                {
                                    "cmd": "python3 collect_session_facts.py --date 2026-05-30 --json",
                                    "workdir": "/repo",
                                    "max_output_tokens": 99999,
                                }
                            ),
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "completed_at": 2,
                            "duration_ms": 1000,
                            "last_agent_message": "日报已生成。",
                        },
                    },
                ],
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                ],
                text=True,
                capture_output=True,
                check=True,
            )

        self.assertIn("date: 2026-05-30", result.stdout)
        self.assertIn("format: group-index", result.stdout)
        self.assertIn("group_id: session-thread-1", result.stdout)
        self.assertIn("title: Session thread-1", result.stdout)
        self.assertIn("session_count: 1", result.stdout)
        self.assertNotIn('{\n', result.stdout)

    def test_group_output_keeps_timeline_and_compresses_adjacent_tools(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / "2026" / "05" / "30" / "rollout-2026-05-30T10-00-00-thread-1.jsonl"
            long_user_message = "生成今天的 Codex 日报：" + ("保留完整用户输入。" * 120)
            write_jsonl(
                rollout,
                [
                    {
                        "type": "session_meta",
                        "payload": {"id": "thread-1", "timestamp": "2026-05-30T10:00:00Z", "cwd": "/repo"},
                    },
                    {"type": "turn_context", "payload": {"turn_id": "turn-1", "cwd": "/repo"}},
                    {"type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1", "started_at": 1}},
                    {"type": "event_msg", "payload": {"type": "user_message", "message": long_user_message}},
                    {"type": "event_msg", "payload": {"type": "agent_message", "message": "先读取 thread 列表。"}},
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "exec_command",
                            "arguments": json.dumps({"cmd": "rg daily", "workdir": "/repo"}),
                        },
                    },
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "exec_command",
                            "arguments": json.dumps({"cmd": "sed -n '1,80p' SKILL.md", "workdir": "/repo"}),
                        },
                    },
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "function_call",
                            "name": "read_thread",
                            "arguments": json.dumps({"threadId": "abc", "cursor": "secret-cursor"}),
                        },
                    },
                    {
                        "type": "event_msg",
                        "payload": {
                            "type": "task_complete",
                            "completed_at": 2,
                            "duration_ms": 1000,
                            "last_agent_message": "日报已生成。",
                        },
                    },
                ],
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--group-id",
                    "session-thread-1",
                ],
                text=True,
                capture_output=True,
                check=True,
            )

        self.assertIn("group_id: session-thread-1", result.stdout)
        self.assertIn("messages:", result.stdout)
        self.assertIn("user: |-", result.stdout)
        self.assertIn(long_user_message, result.stdout)
        self.assertLess(result.stdout.index("user: |-"), result.stdout.index("assistant: |-"))
        self.assertLess(result.stdout.index("assistant: |-"), result.stdout.index("tool_call: exec_command x2"))
        self.assertIn("tool_call: read_thread", result.stdout)
        self.assertIn("has_cursor: true", result.stdout)
        self.assertNotIn("workdir:", result.stdout)
        self.assertIn("assistant_final: |-", result.stdout)

    def test_full_output_is_available_for_debugging(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / "2026" / "05" / "30" / "rollout-2026-05-30T10-00-00-thread-1.jsonl"
            write_jsonl(
                rollout,
                [
                    {"type": "session_meta", "payload": {"id": "thread-1"}},
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_started", "turn_id": "turn-1", "started_at": 1},
                    },
                    {"type": "event_msg", "payload": {"type": "user_message", "message": "完整调试"}},
                    {"type": "event_msg", "payload": {"type": "task_complete", "last_agent_message": "done"}},
                ],
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--full",
                ],
                text=True,
                capture_output=True,
                check=True,
            )
            payload = json.loads(result.stdout)

        self.assertEqual(payload["source_strategy"], "fallback-local-session-jsonl-full")
        self.assertNotIn("groups", payload)
        self.assertEqual(payload["sessions"][0]["user_messages"], ["完整调试"])

    def test_normalizes_incomplete_and_worker_without_final_message(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            incomplete = root / "2026" / "05" / "30" / "rollout-2026-05-30T11-00-00-thread-2.jsonl"
            write_jsonl(
                incomplete,
                [
                    {"type": "session_meta", "payload": {"id": "thread-2"}},
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_started", "turn_id": "turn-2", "started_at": 1},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "user_message", "message": "跑一个很长的任务"},
                    },
                ],
            )
            interrupted_worker = root / "2026" / "05" / "30" / "rollout-2026-05-30T12-00-00-thread-3.jsonl"
            write_jsonl(
                interrupted_worker,
                [
                    {"type": "session_meta", "payload": {"id": "thread-3"}},
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_started", "turn_id": "turn-3", "started_at": 1},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "user_message", "message": "你是 Vibe ingest batch 11 worker。"},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_complete", "completed_at": 2, "duration_ms": 1000},
                    },
                ],
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )
            payload = json.loads(result.stdout)

        statuses = {session["thread_id"]: session["status"] for session in payload["sessions"]}
        self.assertEqual(statuses["thread-2"]["normalized"], "活跃")
        self.assertEqual(statuses["thread-3"]["normalized"], "中断")
        self.assertIn("worker-like", statuses["thread-3"]["reason"])

    def test_groups_worker_batches_but_preserves_sessions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for batch, thread_id in [("11", "thread-11"), ("12", "thread-12"), ("20-21", "thread-20-21")]:
                rollout = root / "2026" / "05" / "30" / f"rollout-2026-05-30T12-00-00-{thread_id}.jsonl"
                write_jsonl(
                    rollout,
                    [
                        {"type": "session_meta", "payload": {"id": thread_id}},
                        {
                            "type": "event_msg",
                            "payload": {"type": "task_started", "turn_id": f"turn-{batch}", "started_at": 1},
                        },
                        {
                            "type": "event_msg",
                            "payload": {"type": "user_message", "message": f"你是 Vibe ingest batch {batch} worker。"},
                        },
                        {
                            "type": "event_msg",
                            "payload": {
                                "type": "task_complete",
                                "completed_at": 2,
                                "duration_ms": 1000,
                                "last_agent_message": f"batch {batch} done",
                            },
                        },
                    ],
                )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )
            payload = json.loads(result.stdout)

        self.assertEqual(len(payload["sessions"]), 3)
        self.assertEqual(len(payload["groups"]), 1)
        group = payload["groups"][0]
        self.assertEqual(group["group_id"], "vibe-ingest-batches")
        self.assertEqual(group["title"], "Vibe ingest batch 11-21")
        self.assertEqual(group["thread_ids"], ["thread-11", "thread-12", "thread-20-21"])
        self.assertEqual(group["status_summary"], {"已完成": 3})

    def test_parent_workflows_group_subagent_batches(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            parent = root / "2026" / "05" / "30" / "rollout-2026-05-30T09-00-00-parent-1.jsonl"
            write_jsonl(
                parent,
                [
                    {"type": "session_meta", "payload": {"id": "parent-1", "timestamp": "2026-05-30T09:00:00Z"}},
                    {"type": "event_msg", "payload": {"type": "task_started", "turn_id": "parent-turn", "started_at": 1}},
                    {"type": "event_msg", "payload": {"type": "user_message", "message": "父 Agent 规划 full unsynced ingest"}},
                    {"type": "event_msg", "payload": {"type": "task_complete", "last_agent_message": "parent done"}},
                ],
            )
            for thread_id, message in [
                ("child-1", "Task: ingest unsynced AI wiki raw batch 01 in an isolated worktree."),
                ("child-15", "Task: metadata backfill unsynced AI wiki raw batch 15 in an isolated worktree."),
            ]:
                rollout = root / "2026" / "05" / "30" / f"rollout-2026-05-30T10-00-00-{thread_id}.jsonl"
                write_jsonl(
                    rollout,
                    [
                        {
                            "type": "session_meta",
                            "payload": {
                                "id": thread_id,
                                "timestamp": "2026-05-30T10:00:00Z",
                                "source": {
                                    "subagent": {
                                        "thread_spawn": {
                                            "parent_thread_id": "parent-1",
                                            "depth": 1,
                                            "agent_nickname": "Worker",
                                            "agent_role": "worker",
                                        }
                                    }
                                },
                                "thread_source": "subagent",
                                "agent_nickname": "Worker",
                                "agent_role": "worker",
                            },
                        },
                        {"type": "event_msg", "payload": {"type": "task_started", "turn_id": thread_id, "started_at": 1}},
                        {"type": "event_msg", "payload": {"type": "user_message", "message": message}},
                        {"type": "event_msg", "payload": {"type": "task_complete", "last_agent_message": "done"}},
                    ],
                )

            result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )
            payload = json.loads(result.stdout)

            yaml_result = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                ],
                text=True,
                capture_output=True,
                check=True,
            )

        workflow = payload["parent_workflows"][0]
        self.assertEqual(workflow["parent_thread_id"], "parent-1")
        self.assertEqual(workflow["session_count"], 3)
        self.assertEqual(workflow["child_session_count"], 2)
        self.assertEqual(
            workflow["group_ids"],
            ["session-parent-1", "unsynced-raw-ingest-batches", "raw-metadata-backfill-batches"],
        )
        child = next(session for session in payload["sessions"] if session["thread_id"] == "child-1")
        self.assertEqual(child["parent_thread_id"], "parent-1")
        self.assertEqual(child["agent_role"], "worker")
        self.assertIn("parent_workflows:", yaml_result.stdout)
        self.assertIn("parent_thread_id: parent-1", yaml_result.stdout)
        self.assertIn("unsynced-raw-ingest-batches", yaml_result.stdout)

    def test_timezone_records_date_mismatch_without_dropping_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rollout = root / "2026" / "05" / "30" / "rollout-2026-05-30T00-30-00-thread-1.jsonl"
            write_jsonl(
                rollout,
                [
                    {
                        "type": "session_meta",
                        "payload": {"id": "thread-1", "timestamp": "2026-05-29T16:30:00Z"},
                    },
                    {
                        "type": "event_msg",
                        "payload": {"type": "task_started", "turn_id": "turn-1", "started_at": 1},
                    },
                    {"type": "event_msg", "payload": {"type": "user_message", "message": "跨时区任务"}},
                    {"type": "event_msg", "payload": {"type": "task_complete", "last_agent_message": "done"}},
                ],
            )

            shanghai = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--timezone",
                    "Asia/Shanghai",
                    "--json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )
            utc = subprocess.run(
                [
                    sys.executable,
                    str(COLLECT_SCRIPT),
                    "--date",
                    "2026-05-30",
                    "--sessions-root",
                    str(root),
                    "--timezone",
                    "UTC",
                    "--json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )

        shanghai_payload = json.loads(shanghai.stdout)
        utc_payload = json.loads(utc.stdout)
        self.assertEqual(shanghai_payload["sessions"][0]["local_date"], "2026-05-30")
        self.assertFalse(shanghai_payload["sessions"][0]["date_mismatch"])
        self.assertEqual(utc_payload["sessions"][0]["local_date"], "2026-05-29")
        self.assertTrue(utc_payload["sessions"][0]["date_mismatch"])


if __name__ == "__main__":
    unittest.main()
