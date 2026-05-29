#!/usr/bin/env python3
"""Render the first pages of one AI wiki raw PDF for vision-based preview ingest."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


RAW_ROOT = Path("/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI")
WIKI_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT_DIR = WIKI_ROOT / "tmp" / "pdf-preview"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", help="Raw PDF path")
    parser.add_argument("--raw-root", default=str(RAW_ROOT), help="AI wiki raw root")
    parser.add_argument("--wiki-root", default=str(WIKI_ROOT), help="AI wiki root")
    parser.add_argument("--output-dir", default=None, help="Directory for rendered preview PNGs")
    parser.add_argument("--pages", type=int, default=3, help="Maximum leading pages to render")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def iso_from_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, timezone.utc).isoformat()


def fingerprint(size: int, created_at: str, modified_at: str) -> str:
    return f"size={size};birth={created_at};mtime={modified_at}"


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(
            f"Missing required tool: {name}. Install Poppler, for example `brew install poppler` on macOS."
        )
    return path


def page_count(pdfinfo: str, pdf_path: Path) -> int:
    result = subprocess.run([pdfinfo, str(pdf_path)], check=True, text=True, capture_output=True)
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise SystemExit("Unable to determine PDF page count from pdfinfo output.")


def raw_metadata(path: Path) -> dict[str, object]:
    stat = path.stat()
    created_at = iso_from_timestamp(getattr(stat, "st_birthtime", stat.st_mtime))
    modified_at = iso_from_timestamp(stat.st_mtime)
    size = stat.st_size
    snapshot_at = datetime.now(timezone.utc).isoformat()
    return {
        "raw_created_at": created_at,
        "raw_modified_at": modified_at,
        "raw_size": size,
        "raw_fingerprint": fingerprint(size, created_at, modified_at),
        "raw_snapshot_at": snapshot_at,
    }


def render_pages(pdftoppm: str, pdf_path: Path, destination: Path, max_pages: int) -> list[Path]:
    destination.mkdir(parents=True, exist_ok=True)
    for stale in destination.glob("page-*.png"):
        stale.unlink()
    prefix = destination / "page"
    subprocess.run(
        [pdftoppm, "-f", "1", "-l", str(max_pages), "-png", str(pdf_path), str(prefix)],
        check=True,
        text=True,
        capture_output=True,
    )
    return sorted(destination.glob("page-*.png"))


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf).expanduser().resolve()
    raw_root = Path(args.raw_root).expanduser().resolve()
    wiki_root = Path(args.wiki_root).expanduser().resolve()
    output_root = Path(args.output_dir).expanduser().resolve() if args.output_dir else DEFAULT_OUTPUT_DIR.resolve()
    if args.pages < 1:
        raise SystemExit("--pages must be at least 1")
    if pdf_path.suffix.lower() != ".pdf":
        raise SystemExit(f"Expected a .pdf file, got: {pdf_path}")
    if not pdf_path.is_file():
        raise SystemExit(f"PDF does not exist: {pdf_path}")
    try:
        source_relpath = pdf_path.relative_to(raw_root).as_posix()
    except ValueError as exc:
        raise SystemExit(f"PDF is not under raw root: {raw_root}") from exc

    pdfinfo = require_tool("pdfinfo")
    pdftoppm = require_tool("pdftoppm")
    total_pages = page_count(pdfinfo, pdf_path)
    max_pages = min(args.pages, total_pages)
    render_dir = output_root / source_relpath
    rendered = render_pages(pdftoppm, pdf_path, render_dir, max_pages)
    processed_pages = list(range(1, max_pages + 1))
    target_relpath = Path("sources") / f"{source_relpath}.md"
    target_source_note = wiki_root / target_relpath

    payload: dict[str, object] = {
        "source_relpath": source_relpath,
        "raw_path": str(pdf_path),
        "target_source_note": str(target_source_note),
        "target_source_note_relpath": target_relpath.as_posix(),
        "page_count": total_pages,
        "processed_pages": processed_pages,
        "rendered_pages": [
            {"page_number": page_number, "image_path": str(path)}
            for page_number, path in zip(processed_pages, rendered, strict=False)
        ],
        **raw_metadata(pdf_path),
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Rendered pages {processed_pages} from {source_relpath}")
        for page in payload["rendered_pages"]:
            print(f"- page {page['page_number']}: {page['image_path']}")


if __name__ == "__main__":
    main()
