#!/usr/bin/env python3
"""Tests for Codex weekly report helpers."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("collect_daily_reports.py")
SPEC = importlib.util.spec_from_file_location("collect_daily_reports", SCRIPT_PATH)
assert SPEC and SPEC.loader
collector = importlib.util.module_from_spec(SPEC)
sys.modules["collect_daily_reports"] = collector
SPEC.loader.exec_module(collector)


DAILY_TEXT = """---
title: "2026-05-25 Codex日报"
date: 2026-05-25
type: codex-daily
ingest_policy: on-request
inbox_status: unread
inbox_created_at: 2026-05-25
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: codex-report
---

# 2026-05-25 Codex日报

## 今日概览

- 一句话总结: 完成多个工作流收尾。

## 工作日报（对上汇报）

- 今日推进:
  - 推进关键任务。

## 分析与洞察

这一天暴露了一个工作方式问题。

## 启发与下一步

- 下次提前定义验收边界。

## 待跟进

- [ ] 沉淀检查点。
"""


class WeeklyHelperTests(unittest.TestCase):
    def test_natural_week_range(self) -> None:
        start, end, mode = collector.resolve_range(date(2026, 5, 27))
        self.assertEqual(start, date(2026, 5, 25))
        self.assertEqual(end, date(2026, 5, 27))
        self.assertEqual(mode, "natural-week-to-date")

    def test_sunday_natural_week_is_complete_week(self) -> None:
        start, end, mode = collector.resolve_range(date(2026, 5, 31))
        self.assertEqual(start, date(2026, 5, 25))
        self.assertEqual(end, date(2026, 5, 31))
        self.assertEqual(mode, "natural-week-to-date")

    def test_recent_days_range(self) -> None:
        start, end, mode = collector.resolve_range(date(2026, 5, 27), recent_days=7)
        self.assertEqual(start, date(2026, 5, 21))
        self.assertEqual(end, date(2026, 5, 27))
        self.assertEqual(mode, "recent-7-days")

    def test_explicit_range(self) -> None:
        start, end, mode = collector.resolve_range(
            date(2026, 5, 27),
            start_date=date(2026, 5, 20),
            end_date=date(2026, 5, 26),
        )
        self.assertEqual(start, date(2026, 5, 20))
        self.assertEqual(end, date(2026, 5, 26))
        self.assertEqual(mode, "explicit")

    def test_collects_report_with_wikilink_and_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            daily_dir = root / "human/inbox/codex-daily"
            daily_dir.mkdir(parents=True)
            report_path = daily_dir / "2026-05-25_Codex日报.md"
            report_path.write_text(DAILY_TEXT, encoding="utf-8")

            payload = collector.collect_reports(
                date(2026, 5, 25),
                date(2026, 5, 25),
                daily_dir=daily_dir,
                weekly_dir=root / "human/inbox/codex-weekly",
                cwd=root,
            )

            report = payload["reports"][0]
            self.assertEqual(report["status"], "found")
            self.assertEqual(report["frontmatter_type"], "codex-daily")
            self.assertEqual(
                report["wikilink"],
                "[[human/inbox/codex-daily/2026-05-25_Codex日报|2026-05-25]]",
            )
            self.assertIn("今日概览", report["sections"])
            self.assertEqual(report["warnings"], None)

    def test_collects_raw_status_report_from_inbox_workflow(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            daily_dir = root / "human/raw/inbox/codex-daily"
            daily_dir.mkdir(parents=True)
            report_path = daily_dir / "2026-05-25_Codex日报.md"
            report_path.write_text(DAILY_TEXT, encoding="utf-8")

            payload = collector.collect_reports(
                date(2026, 5, 25),
                date(2026, 5, 25),
                daily_dir=(root / "human/inbox/codex-daily", daily_dir),
                weekly_dir=root / "human/inbox/codex-weekly",
                cwd=root,
            )

            report = payload["reports"][0]
            self.assertEqual(report["status"], "found")
            self.assertEqual(
                report["wikilink"],
                "[[human/raw/inbox/codex-daily/2026-05-25_Codex日报|2026-05-25]]",
            )

    def test_missing_report_is_soft_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            daily_dir = root / "human/inbox/codex-daily"
            daily_dir.mkdir(parents=True)
            payload = collector.collect_reports(
                date(2026, 5, 25),
                date(2026, 5, 26),
                daily_dir=daily_dir,
                weekly_dir=root / "human/inbox/codex-weekly",
                cwd=root,
            )
            self.assertEqual([report["status"] for report in payload["reports"]], ["missing", "missing"])
            self.assertEqual(payload["range"]["missing_days"], 2)

    def test_wrong_type_and_missing_sections_warn_without_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            daily_dir = root / "human/inbox/codex-daily"
            daily_dir.mkdir(parents=True)
            (daily_dir / "2026-05-25_Codex日报.md").write_text(
                """---
title: "Wrong"
type: note
---

# Wrong

## 今日概览

Only one section.
""",
                encoding="utf-8",
            )
            payload = collector.collect_reports(
                date(2026, 5, 25),
                date(2026, 5, 25),
                daily_dir=daily_dir,
                weekly_dir=root / "human/inbox/codex-weekly",
                cwd=root,
            )
            report = payload["reports"][0]
            self.assertIn("type_warning", report["warnings"])
            self.assertIn("missing_sections", report["warnings"])
            self.assertIn("分析与洞察", report["missing_sections"])


if __name__ == "__main__":
    unittest.main()
