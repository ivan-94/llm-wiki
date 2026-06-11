import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


SCRIPT = Path(__file__).with_name("diff_human_raw_sources.py")


def run_diff(workdir, *extra_args):
    raw_root = workdir / "human" / "raw"
    wiki_root = workdir / "wiki"
    (wiki_root / "human" / "sources").mkdir(parents=True, exist_ok=True)
    raw_root.mkdir(parents=True, exist_ok=True)

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


def birth_timestamp(path):
    stat = path.stat()
    return getattr(stat, "st_birthtime", stat.st_mtime)


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat()


def write_human_raw(raw_root, relpath, *, ingest_policy="allowed", body="Human note"):
    path = raw_root / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    if ingest_policy is None:
        path.write_text(f"# {Path(relpath).stem}\n\n{body}\n")
    else:
        path.write_text(
            "\n".join(
                [
                    "---",
                    f"ingest_policy: {ingest_policy}",
                    "---",
                    "",
                    f"# {Path(relpath).stem}",
                    "",
                    body,
                    "",
                ]
            )
        )
    return path


def write_source(wiki_root, relpath, **frontmatter):
    path = wiki_root / "human" / "sources" / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "source_type": "human_markdown",
        "source_origin": "human",
        "raw_path": f"human/raw/{relpath}",
        "source_relpath": relpath,
        "ingested_at": "2026-05-30",
        "status": "ingested",
    }
    fields.update(frontmatter)
    body = ["---"]
    for key, value in fields.items():
        body.append(f'{key}: "{value}"')
    body.extend(["---", "", f"# {Path(relpath).stem}", ""])
    path.write_text("\n".join(body))
    return path


class DiffHumanRawSourcesTests(unittest.TestCase):
    def test_reports_added_allowed_markdown_unapproved_markdown_and_unsupported_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, _, _ = run_diff(workdir, "--include-unsupported", "--include-unapproved")
            write_human_raw(raw_root, "allowed.md")
            write_human_raw(raw_root, "private.md", ingest_policy=None)
            (raw_root / "assets").mkdir()
            (raw_root / "assets" / "infographic.webp").write_text("unsupported")

            _, _, payload = run_diff(workdir, "--include-unsupported", "--include-unapproved")

        self.assertEqual(
            [(item["source_relpath"], item["target_source_note"]) for item in payload["added"]],
            [("allowed.md", "human/sources/allowed.md")],
        )
        self.assertEqual(
            [(item["source_relpath"], item["reason"]) for item in payload["unapproved"]],
            [("private.md", "missing-ingest_policy-allowed")],
        )
        self.assertEqual(
            [item["source_relpath"] for item in payload["unsupported"]],
            ["assets/infographic.webp"],
        )

    def test_reports_deleted_updated_moved_unchanged_and_missing_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)

            unchanged = write_human_raw(raw_root, "unchanged.md", body="same")
            unchanged_stat = unchanged.stat()
            write_source(
                wiki_root,
                "unchanged.md",
                raw_created_at=iso(birth_timestamp(unchanged)),
                raw_modified_at=iso(unchanged_stat.st_mtime),
                raw_size=unchanged_stat.st_size,
            )

            updated = write_human_raw(raw_root, "updated.md", body="new")
            os.utime(updated, (1_800_000_000, 1_800_000_000))
            updated_stat = updated.stat()
            write_source(
                wiki_root,
                "updated.md",
                raw_created_at=iso(birth_timestamp(updated)),
                raw_modified_at=iso(1_700_000_000),
                raw_size=updated_stat.st_size,
            )

            write_human_raw(raw_root, "missing-metadata.md", body="needs metadata")
            write_source(wiki_root, "missing-metadata.md")

            write_source(
                wiki_root,
                "deleted.md",
                raw_created_at=iso(1_700_000_000),
                raw_modified_at=iso(1_700_000_000),
                raw_size=7,
            )

            moved = write_human_raw(raw_root, "new-place.md", body="moved")
            moved_stat = moved.stat()
            write_source(
                wiki_root,
                "old-place.md",
                raw_created_at=iso(birth_timestamp(moved)),
                raw_modified_at=iso(moved_stat.st_mtime),
                raw_size=moved_stat.st_size,
            )

            _, _, payload = run_diff(workdir)

        self.assertEqual([item["source_relpath"] for item in payload["unchanged"]], ["unchanged.md"])
        self.assertEqual([item["source_relpath"] for item in payload["updated"]], ["updated.md"])
        self.assertEqual(
            [item["source_relpath"] for item in payload["needs_metadata"]],
            ["missing-metadata.md"],
        )
        self.assertEqual([item["source_relpath"] for item in payload["deleted"]], ["deleted.md"])
        self.assertEqual(
            [(item["from_source_relpath"], item["to_source_relpath"]) for item in payload["moved"]],
            [("old-place.md", "new-place.md")],
        )

    def test_unapproved_existing_source_is_not_reported_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)
            raw = write_human_raw(raw_root, "not-allowed.md", ingest_policy=None)
            raw_stat = raw.stat()
            write_source(
                wiki_root,
                "not-allowed.md",
                raw_created_at=iso(birth_timestamp(raw)),
                raw_modified_at=iso(raw_stat.st_mtime),
                raw_size=raw_stat.st_size,
            )

            _, _, payload = run_diff(workdir, "--include-unapproved")

        self.assertEqual(payload["deleted"], [])
        self.assertEqual(
            [(item["source_relpath"], item["reason"]) for item in payload["unapproved"]],
            [("not-allowed.md", "missing-ingest_policy-allowed")],
        )
        self.assertIn("source_note", payload["unapproved"][0])

    def test_ignores_subsecond_mtime_drift_when_size_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)
            raw = write_human_raw(raw_root, "same-second.md", body="same")
            os.utime(raw, (1_800_000_000.5, 1_800_000_000.5))
            raw_stat = raw.stat()
            write_source(
                wiki_root,
                "same-second.md",
                raw_created_at=iso(birth_timestamp(raw)),
                raw_modified_at=iso(1_800_000_000),
                raw_size=raw_stat.st_size,
            )

            _, _, payload = run_diff(workdir)

        self.assertEqual([item["source_relpath"] for item in payload["unchanged"]], ["same-second.md"])
        self.assertEqual(payload["updated"], [])

    def test_reports_size_change_even_with_subsecond_mtime_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            raw_root, wiki_root, _ = run_diff(workdir)
            raw = write_human_raw(raw_root, "size-changed.md", body="changed")
            os.utime(raw, (1_800_000_000.5, 1_800_000_000.5))
            raw_stat = raw.stat()
            write_source(
                wiki_root,
                "size-changed.md",
                raw_created_at=iso(birth_timestamp(raw)),
                raw_modified_at=iso(1_800_000_000),
                raw_size=raw_stat.st_size - 1,
            )

            _, _, payload = run_diff(workdir)

        self.assertEqual([item["source_relpath"] for item in payload["updated"]], ["size-changed.md"])


if __name__ == "__main__":
    unittest.main()
