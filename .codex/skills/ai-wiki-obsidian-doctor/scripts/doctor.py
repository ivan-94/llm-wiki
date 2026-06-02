#!/usr/bin/env python3
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


CANONICAL_DIRS = (
    "sources",
    "human/sources",
    "concepts",
    "entities",
    "synthesis",
    "questions",
    "maps",
    "outputs",
)
IGNORED_LINK_PREFIXES = ("http://", "https://", "mailto:", "obsidian://", "finderx://", "raw:", "human-raw:")
INDEX_SECTIONS = (
    "Recently Updated",
    "Source Coverage",
    "Concepts",
    "Entities",
    "Synthesis",
    "Maps",
    "Questions",
    "Outputs",
    "Review Queue",
    "Needs Attention",
)
LOG_RE = re.compile(
    r"^## \[\d{4}-\d{2}-\d{2}\] "
    r"(ingest|compile|query|output|review|lint|maintenance|schema) "
    r"\| .+ .+; issues: .+$"
)
WIKILINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")
EMPTY_CLI_MESSAGES = (
    "No unresolved links found.",
    "No orphan files found.",
    "No dead-end files found.",
)


@dataclass
class Finding:
    severity: str
    category: str
    path: str
    message: str
    detail: str = ""


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def is_canonical(relpath: str) -> bool:
    return relpath == "index.md" or relpath == "log.md" or any(
        relpath == prefix or relpath.startswith(f"{prefix}/") for prefix in CANONICAL_DIRS
    )


def iter_markdown(root: Path) -> Iterable[Path]:
    ignored_parts = {".git", ".codex", ".obsidian", ".scratch", "tmp"}
    for path in root.rglob("*.md"):
        if any(part in ignored_parts for part in path.relative_to(root).parts):
            continue
        yield path


def check_index(root: Path) -> list[Finding]:
    path = root / "index.md"
    if not path.exists():
        return [Finding("P0", "index", "index.md", "缺少 index.md")]

    text = path.read_text(errors="replace")
    findings: list[Finding] = []
    positions = []
    for section in INDEX_SECTIONS:
        match = re.search(rf"^## {re.escape(section)}$", text, flags=re.MULTILINE)
        if not match:
            findings.append(Finding("P1", "index", "index.md", f"缺少章节：{section}"))
        else:
            positions.append((section, match.start()))

    if len(positions) == len(INDEX_SECTIONS):
        ordered = sorted(positions, key=lambda item: item[1])
        if [name for name, _ in ordered] != list(INDEX_SECTIONS):
            findings.append(Finding("P1", "index", "index.md", "index 章节顺序不符合契约"))
    return findings


def check_log(root: Path) -> list[Finding]:
    path = root / "log.md"
    if not path.exists():
        return [Finding("P0", "log", "log.md", "缺少 log.md")]

    findings: list[Finding] = []
    for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), start=1):
        if line.startswith("## [") and not LOG_RE.match(line):
            findings.append(
                Finding(
                    "P1",
                    "log",
                    f"log.md:{lineno}",
                    "append-only log 记录格式错误",
                    line,
                )
            )
    return findings


def link_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target


def resolve_path_style_link(root: Path, target: str) -> bool | None:
    if not target or target.startswith(IGNORED_LINK_PREFIXES):
        return True
    if "<" in target and ">" in target:
        return True
    if ":" in target and not target.startswith(("/", "./", "../")):
        return True
    if "/" not in target:
        return None

    candidate = root / target
    candidates = [candidate]
    if candidate.suffix != ".md":
        candidates.append(candidate.with_suffix(".md"))
        candidates.append(Path(f"{candidate}.md"))
    return any(path.exists() for path in candidates)


def check_path_wikilinks(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_markdown(root):
        text = path.read_text(errors="replace")
        for match in WIKILINK_RE.finditer(text):
            target = link_target(match.group(1))
            resolved = resolve_path_style_link(root, target)
            if resolved is False:
                relpath = rel(path, root)
                severity = "P1" if is_canonical(relpath) else "P2"
                findings.append(
                    Finding(
                        severity,
                        "wikilink",
                        relpath,
                        f"path-style wikilink 坏链：[[{target}]]",
                    )
                )
    return findings


def canonical_cli_lines(stdout: str) -> list[str]:
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    return [line for line in lines if is_canonical(line)]


def run_cli_command(root: Path, obsidian_bin: str, command: list[str], timeout: int) -> dict:
    env = os.environ.copy()
    try:
        completed = subprocess.run(
            [obsidian_bin, *command],
            cwd=root,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "command": command,
            "ok": False,
            "returncode": None,
            "stdout": exc.stdout or "",
            "stderr": exc.stderr or "",
            "error": "timeout",
        }
    except OSError as exc:
        return {
            "command": command,
            "ok": False,
            "returncode": None,
            "stdout": "",
            "stderr": str(exc),
            "error": "oserror",
        }

    parsed = None
    if completed.stdout.strip().startswith(("{", "[")):
        try:
            parsed = json.loads(completed.stdout)
        except json.JSONDecodeError:
            parsed = None

    return {
        "command": command,
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "json": parsed,
    }


def run_obsidian_checks(root: Path, obsidian_bin: str, timeout: int) -> tuple[list[Finding], list[dict]]:
    if not shutil.which(obsidian_bin) and not Path(obsidian_bin).exists():
        return (
            [Finding("P0", "obsidian-cli", "", f"找不到 Obsidian CLI：{obsidian_bin}")],
            [],
        )

    commands = [
        ["unresolved", "verbose", "counts", "format=json"],
        ["orphans"],
        ["deadends"],
    ]
    results = [run_cli_command(root, obsidian_bin, command, timeout) for command in commands]
    findings: list[Finding] = []

    for result in results:
        label = " ".join(result["command"])
        if not result["ok"]:
            findings.append(
                Finding(
                    "P0",
                    "obsidian-cli",
                    "",
                    f"Obsidian CLI 命令失败：{label}",
                    (result.get("stderr") or result.get("stdout") or result.get("error") or "").strip(),
                )
            )
            continue

        stdout = (result.get("stdout") or "").strip()
        if result["command"][0] == "unresolved" and stdout and stdout not in ("[]", "{}") and stdout not in EMPTY_CLI_MESSAGES:
            findings.append(
                Finding(
                    "P1",
                    "obsidian-unresolved",
                    "",
                    "Obsidian 报告 unresolved 链接",
                    stdout[:4000],
                )
            )
        if result["command"][0] in {"orphans", "deadends"} and stdout and stdout not in EMPTY_CLI_MESSAGES:
            canonical_lines = canonical_cli_lines(stdout)
            if not canonical_lines:
                continue
            findings.append(
                Finding(
                    "P2",
                    f"obsidian-{result['command'][0]}",
                    "",
                    f"Obsidian 报告 canonical {result['command'][0]}",
                    "\n".join(canonical_lines)[:4000],
                )
            )

    return findings, results


def build_payload(args: argparse.Namespace) -> dict:
    root = Path(args.wiki_root).expanduser().resolve()
    findings: list[Finding] = []
    cli_results: list[dict] = []

    if not root.exists():
        findings.append(Finding("P0", "root", str(root), "wiki 根目录不存在"))
    else:
        findings.extend(check_index(root))
        findings.extend(check_log(root))
        findings.extend(check_path_wikilinks(root))
        if not args.skip_obsidian:
            cli_findings, cli_results = run_obsidian_checks(root, args.obsidian_bin, args.timeout)
            findings.extend(cli_findings)

    order = {"P0": 0, "P1": 1, "P2": 2}
    findings.sort(key=lambda item: (order.get(item.severity, 9), item.category, item.path, item.message))
    return {
        "wiki_root": str(root),
        "skip_obsidian": args.skip_obsidian,
        "summary": {
            "P0": sum(1 for item in findings if item.severity == "P0"),
            "P1": sum(1 for item in findings if item.severity == "P1"),
            "P2": sum(1 for item in findings if item.severity == "P2"),
            "total": len(findings),
        },
        "findings": [asdict(item) for item in findings],
        "obsidian_cli": cli_results,
    }


def render_markdown(payload: dict) -> str:
    lines = [
        "# Obsidian Doctor 报告",
        "",
        "## Source Manifest",
        "",
        f"- wiki_root: `{payload['wiki_root']}`",
        f"- obsidian_cli: `{'已跳过' if payload['skip_obsidian'] else '已启用'}`",
        "- local_checks: `index.md`、`log.md`、path-style wikilinks",
        "",
        "## 摘要",
        "",
    ]
    summary = payload["summary"]
    lines.append(f"- P0: {summary['P0']}")
    lines.append(f"- P1: {summary['P1']}")
    lines.append(f"- P2: {summary['P2']}")
    lines.append(f"- total: {summary['total']}")
    lines.extend(["", "## 发现", ""])

    if not payload["findings"]:
        lines.append("未发现问题。")
    else:
        for finding in payload["findings"]:
            location = f" `{finding['path']}`" if finding["path"] else ""
            lines.append(f"- **{finding['severity']}** `{finding['category']}`{location}: {finding['message']}")
            if finding["detail"]:
                detail = finding["detail"].replace("\n", "\n  ")
                lines.append(f"  - 详情：{detail}")

    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="为 AI wiki 运行只读 Obsidian doctor 检查。")
    parser.add_argument("--wiki-root", default=".", help="AI wiki 仓库/vault 根目录，默认当前目录。")
    parser.add_argument("--obsidian-bin", default="obsidian", help="Obsidian CLI 可执行文件。")
    parser.add_argument("--timeout", type=int, default=30, help="每条 Obsidian CLI 命令的超时时间，单位秒。")
    parser.add_argument("--skip-obsidian", action="store_true", help="只运行仓库本地检查。")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="输出 JSON。")
    output.add_argument("--markdown", action="store_true", help="输出 Markdown，默认。")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    payload = build_payload(args)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(payload), end="")
    return 1 if payload["summary"]["P0"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
