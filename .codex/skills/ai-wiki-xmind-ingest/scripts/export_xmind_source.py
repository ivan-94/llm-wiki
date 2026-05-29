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
    command = [args.xmind_bin, "export", str(raw_path), "--format", "markdown"]

    result = subprocess.run(command, text=True, capture_output=True)
    payload = {
        "ok": result.returncode == 0,
        "raw_path": str(raw_path),
        "source_relpath": str(relpath),
        "target_source_note": str(target),
        "command": command,
        "markdown": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode,
    }

    if args.markdown_only:
        print(result.stdout, end="")
    elif args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"raw_path: {payload['raw_path']}")
        print(f"source_relpath: {payload['source_relpath']}")
        print(f"target_source_note: {payload['target_source_note']}")
        print("--- markdown ---")
        print(result.stdout, end="")
        if result.stderr:
            print("\n--- stderr ---", file=sys.stderr)
            print(result.stderr, end="", file=sys.stderr)

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
