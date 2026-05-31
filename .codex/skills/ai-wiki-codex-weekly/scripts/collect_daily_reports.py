#!/usr/bin/env python3
"""Collect existing Codex daily reports for weekly synthesis."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any


DEFAULT_DAILY_DIR = Path("human/raw/codex-daily")
DEFAULT_WEEKLY_DIR = Path("human/raw/codex-weekly")
DEFAULT_MAX_SECTION_CHARS = 2400
KEY_SECTIONS = (
    "今日概览",
    "工作日报（对上汇报）",
    "分析与洞察",
    "启发与下一步",
    "待跟进",
)


@dataclass
class DailyReport:
    date: str
    status: str
    expected_path: str
    path: str | None = None
    wikilink: str | None = None
    title: str | None = None
    frontmatter_type: str | None = None
    warnings: list[str] | None = None
    missing_sections: list[str] | None = None
    sections: dict[str, str] | None = None


def parse_iso_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid date {value!r}; expected YYYY-MM-DD") from exc


def resolve_range(
    target: date,
    start_date: date | None = None,
    end_date: date | None = None,
    recent_days: int | None = None,
) -> tuple[date, date, str]:
    if (start_date is None) ^ (end_date is None):
        raise ValueError("--start-date and --end-date must be provided together")
    if recent_days is not None and start_date is not None:
        raise ValueError("--recent-days cannot be combined with explicit date range")
    if recent_days is not None:
        if recent_days < 1:
            raise ValueError("--recent-days must be >= 1")
        return target - timedelta(days=recent_days - 1), target, f"recent-{recent_days}-days"
    if start_date is not None and end_date is not None:
        if end_date < start_date:
            raise ValueError("--end-date must be on or after --start-date")
        return start_date, end_date, "explicit"
    week_start = target - timedelta(days=target.weekday())
    return week_start, target, "natural-week-to-date"


def each_day(start: date, end: date) -> list[date]:
    days: list[date] = []
    current = start
    while current <= end:
        days.append(current)
        current += timedelta(days=1)
    return days


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def split_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, ["missing_frontmatter"]
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            raw_frontmatter = lines[1:index]
            body = "\n".join(lines[index + 1 :])
            data: dict[str, str] = {}
            for line in raw_frontmatter:
                if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
                    continue
                key, value = line.split(":", 1)
                data[key.strip()] = strip_quotes(value)
            return data, body, []
    return {}, text, ["unterminated_frontmatter"]


def extract_h2_sections(body: str, max_chars: int = DEFAULT_MAX_SECTION_CHARS) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1).strip()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)

    extracted: dict[str, str] = {}
    for name, lines in sections.items():
        text = "\n".join(lines).strip()
        if max_chars > 0 and len(text) > max_chars:
            text = f"{text[: max_chars - 3].rstrip()}..."
        extracted[name] = text
    return extracted


def find_daily_report(day: date, daily_dir: Path) -> tuple[Path | None, list[str]]:
    warnings: list[str] = []
    exact = daily_dir / f"{day.isoformat()}_Codex日报.md"
    if exact.exists():
        return exact, warnings

    candidates = sorted(daily_dir.glob(f"{day.isoformat()}_*.md"))
    if not candidates:
        return None, warnings
    if len(candidates) > 1:
        warnings.append("multiple_daily_candidates")
    warnings.append("non_default_daily_filename")
    return candidates[0], warnings


def vault_relative_path(path: Path, cwd: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(cwd.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def obsidian_wikilink(path: Path, day: date, cwd: Path) -> str:
    rel = vault_relative_path(path, cwd)
    target = rel[:-3] if rel.endswith(".md") else rel
    return f"[[{target}|{day.isoformat()}]]"


def read_report(day: date, daily_dir: Path, cwd: Path, max_section_chars: int) -> DailyReport:
    expected = daily_dir / f"{day.isoformat()}_Codex日报.md"
    path, warnings = find_daily_report(day, daily_dir)
    if path is None:
        return DailyReport(date=day.isoformat(), status="missing", expected_path=expected.as_posix())

    text = path.read_text(encoding="utf-8")
    frontmatter, body, frontmatter_warnings = split_frontmatter(text)
    warnings.extend(frontmatter_warnings)

    report_type = frontmatter.get("type")
    if report_type != "codex-daily":
        warnings.append("type_warning")

    sections = extract_h2_sections(body, max_chars=max_section_chars)
    missing_sections = [section for section in KEY_SECTIONS if section not in sections]
    if missing_sections:
        warnings.append("missing_sections")

    return DailyReport(
        date=day.isoformat(),
        status="found",
        expected_path=expected.as_posix(),
        path=path.as_posix(),
        wikilink=obsidian_wikilink(path, day, cwd),
        title=frontmatter.get("title"),
        frontmatter_type=report_type,
        warnings=warnings or None,
        missing_sections=missing_sections or None,
        sections={name: sections.get(name, "") for name in KEY_SECTIONS if name in sections} or None,
    )


def collect_reports(
    start: date,
    end: date,
    daily_dir: Path = DEFAULT_DAILY_DIR,
    weekly_dir: Path = DEFAULT_WEEKLY_DIR,
    max_section_chars: int = DEFAULT_MAX_SECTION_CHARS,
    cwd: Path | None = None,
    mode: str = "natural-week",
) -> dict[str, Any]:
    root = cwd or Path.cwd()
    reports = [read_report(day, daily_dir, root, max_section_chars) for day in each_day(start, end)]
    found = sum(1 for report in reports if report.status == "found")
    output_path = weekly_dir / f"{start.isoformat()}_to_{end.isoformat()}_Codex周报.md"
    return {
        "range": {
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "mode": mode,
            "expected_days": len(reports),
            "found_days": found,
            "missing_days": len(reports) - found,
            "output_path": output_path.as_posix(),
        },
        "reports": [asdict(report) for report in reports],
    }


def emit_multiline(text: str, indent: int) -> list[str]:
    prefix = " " * indent
    if not text:
        return [f"{prefix}|-"]
    lines = [f"{prefix}|-"]
    lines.extend(f"{prefix}  {line}" if line else f"{prefix}  " for line in text.splitlines())
    return lines


def emit_yaml_like(payload: dict[str, Any]) -> str:
    lines: list[str] = ["range:"]
    for key, value in payload["range"].items():
        lines.append(f"  {key}: {value}")
    lines.append("reports:")
    for report in payload["reports"]:
        lines.append(f"  - date: {report['date']}")
        lines.append(f"    status: {report['status']}")
        lines.append(f"    expected_path: {report['expected_path']}")
        if report.get("path"):
            lines.append(f"    path: {report['path']}")
        if report.get("wikilink"):
            lines.append(f"    wikilink: {report['wikilink']}")
        if report.get("title"):
            lines.append(f"    title: {report['title']}")
        if report.get("frontmatter_type"):
            lines.append(f"    frontmatter_type: {report['frontmatter_type']}")
        if report.get("warnings"):
            lines.append("    warnings:")
            for warning in report["warnings"]:
                lines.append(f"      - {warning}")
        if report.get("missing_sections"):
            lines.append("    missing_sections:")
            for section in report["missing_sections"]:
                lines.append(f"      - {section}")
        if report.get("sections"):
            lines.append("    sections:")
            for name, text in report["sections"].items():
                lines.append(f"      {name}:")
                lines.extend(emit_multiline(text, 8))
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=parse_iso_date, default=date.today(), help="Target date YYYY-MM-DD")
    parser.add_argument("--start-date", type=parse_iso_date)
    parser.add_argument("--end-date", type=parse_iso_date)
    parser.add_argument("--recent-days", type=int)
    parser.add_argument("--daily-dir", type=Path, default=DEFAULT_DAILY_DIR)
    parser.add_argument("--weekly-dir", type=Path, default=DEFAULT_WEEKLY_DIR)
    parser.add_argument("--max-section-chars", type=int, default=DEFAULT_MAX_SECTION_CHARS)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        start, end, mode = resolve_range(args.date, args.start_date, args.end_date, args.recent_days)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    payload = collect_reports(
        start,
        end,
        daily_dir=args.daily_dir,
        weekly_dir=args.weekly_dir,
        max_section_chars=args.max_section_chars,
        mode=mode,
    )
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(emit_yaml_like(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
