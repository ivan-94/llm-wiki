import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


SCRIPT = Path(__file__).with_name("diff_raw_sources.py")


def run_diff(workdir, *extra_args):
    raw_root = workdir / "raw"
    wiki_root = workdir / "wiki"
    (wiki_root / "sources").mkdir(parents=True, exist_ok=True)
    raw_root.mkdir(exist_ok=True)

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--raw-root",
            str(raw_root),
            "--wiki-root",
            str(wiki_root),
            "--json",
            *extra_args,
        ],
        text=True,
        capture_output=True,
        check=True,
    )
    return raw_root, wiki_root, json.loads(result.stdout)


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat()


def write_source(wiki_root, relpath, **frontmatter):
    path = wiki_root / "sources" / (relpath if relpath.endswith(".md") else f"{relpath}.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "source_type": Path(relpath).suffix.lower().lstrip(".") or "other",
        "source_relpath": relpath,
        "ingested_at": "2026-05-29",
        "status": "ingested",
    }
    fields.update(frontmatter)
    body = ["---"]
    for key, value in fields.items():
        body.append(f'{key}: "{value}"')
    body.extend(["---", "", f"# {Path(relpath).name}", ""])
    path.write_text("\n".join(body))
    return path


class DiffRawSourcesTests(unittest.TestCase):
    def test_reports_added_supported_files_and_unsupported_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, _, _ = run_diff(workdir, "--include-unsupported")
            (raw_root / "Agent.xmind").write_text("xmind placeholder")
            (raw_root / "Guide.pdf").write_text("pdf placeholder")
            (raw_root / "Board.excalidraw").write_text("{}")
            (raw_root / "notes.md").write_text("markdown")
            (raw_root / "archive.zip").write_text("unsupported")

            _, _, payload = run_diff(workdir, "--include-unsupported")

        self.assertEqual(
            [(item["source_relpath"], item["target_source_note"]) for item in payload["added"]],
            [
                ("Agent.xmind", "sources/Agent.xmind.md"),
                ("Board.excalidraw", "sources/Board.excalidraw.md"),
                ("Guide.pdf", "sources/Guide.pdf.md"),
                ("notes.md", "sources/notes.md"),
            ],
        )
        self.assertEqual(
            [item["source_relpath"] for item in payload["unsupported"]],
            ["archive.zip"],
        )

    def test_reports_deleted_updated_moved_unchanged_and_missing_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)

            unchanged = raw_root / "unchanged.xmind"
            unchanged.write_text("same")
            unchanged_stat = unchanged.stat()
            write_source(
                wiki_root,
                "unchanged.xmind",
                raw_created_at=iso(unchanged_stat.st_birthtime),
                raw_modified_at=iso(unchanged_stat.st_mtime),
                raw_size=unchanged_stat.st_size,
            )

            updated = raw_root / "updated.xmind"
            updated.write_text("new")
            os.utime(updated, (1_800_000_000, 1_800_000_000))
            updated_stat = updated.stat()
            write_source(
                wiki_root,
                "updated.xmind",
                raw_created_at=iso(updated_stat.st_birthtime),
                raw_modified_at=iso(1_700_000_000),
                raw_size=updated_stat.st_size,
            )

            missing_metadata = raw_root / "missing-metadata.xmind"
            missing_metadata.write_text("needs metadata")
            write_source(wiki_root, "missing-metadata.xmind")

            write_source(
                wiki_root,
                "deleted.xmind",
                raw_created_at=iso(1_700_000_000),
                raw_modified_at=iso(1_700_000_000),
                raw_size=7,
            )

            moved = raw_root / "new-place.xmind"
            moved.write_text("moved")
            moved_stat = moved.stat()
            write_source(
                wiki_root,
                "old-place.xmind",
                raw_created_at=iso(moved_stat.st_birthtime),
                raw_modified_at=iso(moved_stat.st_mtime),
                raw_size=moved_stat.st_size,
            )

            _, _, payload = run_diff(workdir)

        self.assertEqual([item["source_relpath"] for item in payload["unchanged"]], ["unchanged.xmind"])
        self.assertEqual([item["source_relpath"] for item in payload["updated"]], ["updated.xmind"])
        self.assertEqual(
            [item["source_relpath"] for item in payload["needs_metadata"]],
            ["missing-metadata.xmind"],
        )
        self.assertEqual([item["source_relpath"] for item in payload["deleted"]], ["deleted.xmind"])
        self.assertEqual(
            [(item["from_source_relpath"], item["to_source_relpath"]) for item in payload["moved"]],
            [("old-place.xmind", "new-place.xmind")],
        )

    def test_reports_icloud_placeholder_without_hydrating_raw_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)
            (raw_root / ".Cloud.xmind.icloud").write_text("")
            write_source(
                wiki_root,
                "Cloud.xmind",
                raw_created_at=iso(1_700_000_000),
                raw_modified_at=iso(1_700_000_000),
                raw_size=0,
            )

            _, _, payload = run_diff(workdir)

        self.assertEqual(payload["added"], [])
        self.assertEqual(payload["deleted"], [])
        self.assertEqual(
            [(item["source_relpath"], item["reason"]) for item in payload["icloud_unavailable"]],
            [("Cloud.xmind", "icloud-placeholder")],
        )


if __name__ == "__main__":
    unittest.main()
