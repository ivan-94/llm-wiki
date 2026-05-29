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
            (repo_root / "concepts" / "RAG.md").write_text("# RAG\n", encoding="utf-8")
            (repo_root / "concepts" / ".gitkeep").write_text("", encoding="utf-8")
            (repo_root / ".codex" / "skills" / "internal.md").write_text("skip", encoding="utf-8")

            payload = run_sync(repo_root, vault_root)

        self.assertEqual(payload["mode"], "dry-run")
        self.assertEqual([item["relpath"] for item in payload["copy"]], ["concepts/RAG.md"])
        self.assertEqual(payload["update"], [])
        self.assertEqual(payload["conflict"], [])
        self.assertFalse((vault_root / "concepts" / "RAG.md").exists())
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

    def test_prune_deletes_only_stale_managed_files_and_keeps_obsidian_config(self):
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

            self.assertEqual([item["relpath"] for item in dry_run["delete"]], ["concepts/.gitkeep", "concepts/Old.md"])
            self.assertEqual([item["relpath"] for item in apply["delete"]], ["concepts/.gitkeep", "concepts/Old.md"])
            self.assertFalse((vault_root / "concepts" / "Old.md").exists())
            self.assertFalse((vault_root / "concepts" / ".gitkeep").exists())
            self.assertTrue((vault_root / "concepts" / "Current.md").exists())
            self.assertTrue((vault_root / ".obsidian" / "app.json").exists())


if __name__ == "__main__":
    unittest.main()
