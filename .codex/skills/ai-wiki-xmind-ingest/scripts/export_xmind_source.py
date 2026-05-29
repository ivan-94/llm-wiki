#!/usr/bin/env python3
"""Export one AI wiki raw XMind file to Markdown and report its wiki mapping."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


RAW_ROOT = Path("/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI")
WIKI_ROOT = Path(__file__).resolve().parents[4]


def _under_root(path: Path, root: Path) -> Path:
    try:
        return path.relative_to(root)
    except ValueError:
        print(f"error: raw xmind is not under raw root: {root}", file=sys.stderr)
        sys.exit(2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export an AI wiki raw .xmind file with xmind export --format markdown."
    )
    parser.add_argument("raw_xmind", help="Absolute or relative path to a raw .xmind file")
    parser.add_argument("--raw-root", default=str(RAW_ROOT), help="Raw source root")
    parser.add_argument("--wiki-root", default=str(WIKI_ROOT), help="Wiki root")
    parser.add_argument("--xmind-bin", default="xmind", help="xmind CLI binary")
    parser.add_argument("--json", action="store_true", help="Emit JSON with mapping and markdown")
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Emit only exported Markdown to stdout",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_root = Path(args.raw_root).expanduser().resolve()
    wiki_root = Path(args.wiki_root).expanduser().resolve()
    raw_path = Path(args.raw_xmind).expanduser().resolve()

    if raw_path.suffix.lower() != ".xmind":
        print("error: raw path must end with .xmind", file=sys.stderr)
        return 2
    if not raw_path.exists():
        print(f"error: raw file does not exist: {raw_path}", file=sys.stderr)
        return 2

    relpath = _under_root(raw_path, raw_root)
    target = wiki_root / "sources" / relpath.parent / f"{relpath.name}.md"
    sheets_command = [args.xmind_bin, "sheets", str(raw_path), "--json"]
    sheets_result = subprocess.run(sheets_command, text=True, capture_output=True)
    sheets = []
    if sheets_result.returncode == 0:
        try:
            sheets_payload = json.loads(sheets_result.stdout)
            sheets = sheets_payload.get("result", {}).get("sheets", [])
        except json.JSONDecodeError:
            sheets = []

    export_results = []
    if sheets:
        for sheet in sheets:
            index = sheet.get("index")
            command = [
                args.xmind_bin,
                "export",
                str(raw_path),
                "--sheet-index",
                str(index),
                "--format",
                "markdown",
            ]
            result = subprocess.run(command, text=True, capture_output=True)
            export_results.append(
                {
                    "sheet": sheet,
                    "command": command,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode,
                }
            )
    else:
        command = [args.xmind_bin, "export", str(raw_path), "--format", "markdown"]
        result = subprocess.run(command, text=True, capture_output=True)
        export_results.append(
            {
                "sheet": None,
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            }
        )

    markdown_parts = []
    for export in export_results:
        sheet = export["sheet"]
        if sheet:
            markdown_parts.append(
                f"<!-- Sheet {sheet.get('index')}: {sheet.get('title')} -->\n\n{export['stdout']}"
            )
        else:
            markdown_parts.append(export["stdout"])

    returncode = 0
    for export in export_results:
        if export["returncode"] != 0:
            returncode = export["returncode"]
            break
    if sheets_result.returncode != 0:
        returncode = sheets_result.returncode

    stderr = "".join(
        part
        for part in [sheets_result.stderr, *(export["stderr"] for export in export_results)]
        if part
    )
    payload = {
        "ok": returncode == 0,
        "raw_path": str(raw_path),
        "source_relpath": str(relpath),
        "target_source_note": str(target),
        "sheets_command": sheets_command,
        "sheet_count": len(sheets),
        "sheets": sheets,
        "exports": export_results,
        "markdown": "\n\n".join(markdown_parts),
        "stderr": stderr,
        "returncode": returncode,
    }

    if args.markdown_only:
        print(payload["markdown"], end="")
    elif args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"raw_path: {payload['raw_path']}")
        print(f"source_relpath: {payload['source_relpath']}")
        print(f"target_source_note: {payload['target_source_note']}")
        print("--- markdown ---")
        print(payload["markdown"], end="")
        if payload["stderr"]:
            print("\n--- stderr ---", file=sys.stderr)
            print(payload["stderr"], end="", file=sys.stderr)

    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
