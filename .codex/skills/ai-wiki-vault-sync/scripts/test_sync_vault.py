import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("sync_vault.py")


def run_sync(repo_root, vault_root, *extra_args):
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo-root",
            str(repo_root),
            "--vault-root",
            str(vault_root),
            "--json",
            *extra_args,
        ],
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(result.stdout)


class SyncVaultTests(unittest.TestCase):
    def test_default_vault_root_uses_official_obsidian_app_container(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(Path.cwd()), "--json"],
            text=True,
            capture_output=True,
            check=True,
        )
        payload = json.loads(result.stdout)

        self.assertTrue(payload["vault_root"].endswith("/iCloud~md~obsidian/Documents/ai"))

    def test_dry_run_reports_allowed_files_without_writing_or_syncing_skill_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (repo_root / "concepts").mkdir(parents=True)
            (repo_root / ".codex" / "skills").mkdir(parents=True)
            (repo_root / ".obsidian").mkdir(parents=True)
            (repo_root / "concepts" / "RAG.md").write_text("# RAG\n", encoding="utf-8")
            (repo_root / "concepts" / ".gitkeep").write_text("", encoding="utf-8")
            (repo_root / ".codex" / "skills" / "internal.md").write_text("skip", encoding="utf-8")
            (repo_root / ".obsidian" / "app.json").write_text("{}", encoding="utf-8")

            payload = run_sync(repo_root, vault_root)

        self.assertEqual(payload["mode"], "dry-run")
        self.assertEqual([item["relpath"] for item in payload["copy"]], [".obsidian/app.json", "concepts/RAG.md"])
        self.assertEqual(payload["update"], [])
        self.assertEqual(payload["conflict"], [])
        self.assertFalse((vault_root / "concepts" / "RAG.md").exists())
        self.assertFalse((vault_root / ".obsidian" / "app.json").exists())
        self.assertFalse((vault_root / ".codex" / "skills" / "internal.md").exists())

    def test_apply_copies_allowed_files_and_does_not_overwrite_newer_target_conflicts(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (repo_root / "concepts").mkdir(parents=True)
            (repo_root / "concepts" / "RAG.md").write_text("# RAG\n", encoding="utf-8")
            os.utime(repo_root / "concepts" / "RAG.md", (1_700_000_000, 1_700_000_000))

            (repo_root / "index.md").write_text("# Index from repo\n", encoding="utf-8")
            (vault_root / "index.md").parent.mkdir(parents=True, exist_ok=True)
            (vault_root / "index.md").write_text("# Edited on iOS\n", encoding="utf-8")
            os.utime(repo_root / "index.md", (1_700_000_000, 1_700_000_000))
            os.utime(vault_root / "index.md", (1_800_000_000, 1_800_000_000))

            payload = run_sync(repo_root, vault_root, "--apply")

            self.assertEqual(payload["mode"], "apply")
            self.assertEqual([item["relpath"] for item in payload["copy"]], ["concepts/RAG.md"])
            self.assertEqual([item["relpath"] for item in payload["conflict"]], ["index.md"])
            self.assertEqual((vault_root / "concepts" / "RAG.md").read_text(encoding="utf-8"), "# RAG\n")
            self.assertEqual((vault_root / "index.md").read_text(encoding="utf-8"), "# Edited on iOS\n")

    def test_obsidian_config_is_repo_source_of_truth_even_when_target_is_newer(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (repo_root / ".obsidian").mkdir(parents=True)
            (vault_root / ".obsidian").mkdir(parents=True)
            (repo_root / ".obsidian" / "app.json").write_text('{"repo": true}\n', encoding="utf-8")
            (vault_root / ".obsidian" / "app.json").write_text('{"vault": true}\n', encoding="utf-8")
            os.utime(repo_root / ".obsidian" / "app.json", (1_700_000_000, 1_700_000_000))
            os.utime(vault_root / ".obsidian" / "app.json", (1_800_000_000, 1_800_000_000))

            payload = run_sync(repo_root, vault_root, "--apply")

            self.assertEqual([item["relpath"] for item in payload["update"]], [".obsidian/app.json"])
            self.assertEqual(payload["conflict"], [])
            self.assertEqual((vault_root / ".obsidian" / "app.json").read_text(encoding="utf-8"), '{"repo": true}\n')

    def test_prune_deletes_stale_managed_files_including_obsidian_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (repo_root / "concepts").mkdir(parents=True)
            (repo_root / "concepts" / "Current.md").write_text("# Current\n", encoding="utf-8")
            (vault_root / "concepts").mkdir(parents=True)
            (vault_root / "concepts" / "Old.md").write_text("# Old\n", encoding="utf-8")
            (vault_root / "concepts" / ".gitkeep").write_text("", encoding="utf-8")
            (vault_root / ".obsidian").mkdir(parents=True)
            (vault_root / ".obsidian" / "app.json").write_text("{}", encoding="utf-8")

            dry_run = run_sync(repo_root, vault_root, "--prune")
            apply = run_sync(repo_root, vault_root, "--apply", "--prune")

            self.assertEqual([item["relpath"] for item in dry_run["delete"]], [".obsidian/app.json", "concepts/.gitkeep", "concepts/Old.md"])
            self.assertEqual([item["relpath"] for item in apply["delete"]], [".obsidian/app.json", "concepts/.gitkeep", "concepts/Old.md"])
            self.assertFalse((vault_root / "concepts" / "Old.md").exists())
            self.assertFalse((vault_root / "concepts" / ".gitkeep").exists())
            self.assertTrue((vault_root / "concepts" / "Current.md").exists())
            self.assertFalse((vault_root / ".obsidian" / "app.json").exists())

    def test_pull_human_dry_run_reports_vault_human_notes_without_writing_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (vault_root / "human" / "inbox").mkdir(parents=True)
            (vault_root / "human" / "raw" / "Obsidian").mkdir(parents=True)
            (vault_root / "human" / "sources").mkdir(parents=True)
            (vault_root / "sources").mkdir(parents=True)
            (vault_root / "human" / "inbox" / "capture.md").write_text("draft", encoding="utf-8")
            (vault_root / "human" / "raw" / "Obsidian" / "note.md").write_text("source", encoding="utf-8")
            (vault_root / "human" / "sources" / "note.md").write_text("derived", encoding="utf-8")
            (vault_root / "sources" / "external.md").write_text("external", encoding="utf-8")

            payload = run_sync(repo_root, vault_root, "--pull-human")

        self.assertEqual(payload["mode"], "dry-run")
        self.assertEqual(payload["direction"], "vault-to-repo-human")
        self.assertEqual(
            [item["relpath"] for item in payload["copy"]],
            ["human/inbox/capture.md", "human/raw/Obsidian/note.md"],
        )
        self.assertFalse((repo_root / "human" / "inbox" / "capture.md").exists())
        self.assertFalse((repo_root / "human" / "raw" / "Obsidian" / "note.md").exists())

    def test_pull_human_rejects_prune(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo-root",
                    str(repo_root),
                    "--vault-root",
                    str(vault_root),
                    "--json",
                    "--pull-human",
                    "--prune",
                ],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--pull-human does not support --prune", result.stderr)

    def test_pull_human_apply_copies_notes_and_preserves_newer_repo_conflicts(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            repo_root = workdir / "repo"
            vault_root = workdir / "vault"
            (vault_root / "human" / "inbox").mkdir(parents=True)
            (vault_root / "human" / "raw").mkdir(parents=True)
            (repo_root / "human" / "raw").mkdir(parents=True)
            (vault_root / "human" / "inbox" / "capture.md").write_text("draft from ios", encoding="utf-8")
            (vault_root / "human" / "raw" / "note.md").write_text("older vault note", encoding="utf-8")
            (repo_root / "human" / "raw" / "note.md").write_text("newer repo note", encoding="utf-8")
            os.utime(vault_root / "human" / "raw" / "note.md", (1_700_000_000, 1_700_000_000))
            os.utime(repo_root / "human" / "raw" / "note.md", (1_800_000_000, 1_800_000_000))

            payload = run_sync(repo_root, vault_root, "--pull-human", "--apply")
            self.assertEqual(payload["mode"], "apply")
            self.assertEqual([item["relpath"] for item in payload["copy"]], ["human/inbox/capture.md"])
            self.assertEqual([item["relpath"] for item in payload["conflict"]], ["human/raw/note.md"])
            self.assertEqual((repo_root / "human" / "inbox" / "capture.md").read_text(encoding="utf-8"), "draft from ios")
            self.assertEqual((repo_root / "human" / "raw" / "note.md").read_text(encoding="utf-8"), "newer repo note")


if __name__ == "__main__":
    unittest.main()
