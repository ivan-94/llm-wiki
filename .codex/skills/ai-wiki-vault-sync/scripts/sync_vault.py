#!/usr/bin/env python3
"""Publish this AI wiki to an iCloud Obsidian vault for read-only iOS use."""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
VAULT_ROOT = Path("/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/obsidian/ai")
TOP_LEVEL_FILES = ("index.md", "log.md", "AGENTS.md")
DIRECTORIES = ("sources", "concepts", "entities", "synthesis", "questions", "maps", "outputs", "assets")
DOC_FILES = ("docs/wiki-templates.md",)
SOURCE_IGNORE_NAMES = {".DS_Store", ".gitkeep"}
TARGET_IGNORE_NAMES = {".DS_Store"}


@dataclass(frozen=True)
class SyncItem:
    relpath: str
    source_path: Path
    target_path: Path

    def report(self) -> dict[str, str]:
        return {
            "relpath": self.relpath,
            "source_path": str(self.source_path),
            "target_path": str(self.target_path),
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--vault-root", default=str(VAULT_ROOT))
    parser.add_argument("--apply", action="store_true", help="Write planned copy/update/delete operations")
    parser.add_argument("--prune", action="store_true", help="Delete stale managed files from the vault during apply")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def iter_source_files(repo_root: Path) -> list[SyncItem]:
    items: list[SyncItem] = []

    for relpath in TOP_LEVEL_FILES + DOC_FILES:
        path = repo_root / relpath
        if path.is_file():
            items.append(SyncItem(relpath, path, Path(relpath)))

    for dirname in DIRECTORIES:
        root = repo_root / dirname
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.name in SOURCE_IGNORE_NAMES:
                continue
            relpath = path.relative_to(repo_root).as_posix()
            items.append(SyncItem(relpath, path, Path(relpath)))

    return sorted(items, key=lambda item: item.relpath)


def iter_managed_target_files(vault_root: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []

    for relpath in TOP_LEVEL_FILES + DOC_FILES:
        path = vault_root / relpath
        if path.is_file():
            items.append({"relpath": relpath, "target_path": str(path)})

    for dirname in DIRECTORIES:
        root = vault_root / dirname
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.name in TARGET_IGNORE_NAMES:
                continue
            items.append({"relpath": path.relative_to(vault_root).as_posix(), "target_path": str(path)})

    return sorted(items, key=lambda item: item["relpath"])


def same_file(source: Path, target: Path) -> bool:
    return target.exists() and filecmp.cmp(source, target, shallow=False)


def plan(repo_root: Path, vault_root: Path, prune: bool) -> dict[str, list[dict[str, str]]]:
    repo_root = repo_root.expanduser().resolve()
    vault_root = vault_root.expanduser()
    source_items = iter_source_files(repo_root)
    source_relpaths = {item.relpath for item in source_items}

    copy: list[SyncItem] = []
    update: list[SyncItem] = []
    skip: list[SyncItem] = []
    conflict: list[SyncItem] = []

    for item in source_items:
        target_path = vault_root / item.target_path
        planned = SyncItem(item.relpath, item.source_path, target_path)
        if not target_path.exists():
            copy.append(planned)
        elif same_file(item.source_path, target_path):
            skip.append(planned)
        elif target_path.stat().st_mtime > item.source_path.stat().st_mtime + 0.000001:
            conflict.append(planned)
        else:
            update.append(planned)

    delete = []
    if prune:
        delete = [item for item in iter_managed_target_files(vault_root) if item["relpath"] not in source_relpaths]

    return {
        "copy": [item.report() for item in copy],
        "update": [item.report() for item in update],
        "skip": [item.report() for item in skip],
        "conflict": [item.report() for item in conflict],
        "delete": delete,
    }


def apply_plan(payload: dict[str, list[dict[str, str]]]) -> None:
    for bucket in ("copy", "update"):
        for item in payload[bucket]:
            source = Path(item["source_path"])
            target = Path(item["target_path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    for item in payload["delete"]:
        Path(item["target_path"]).unlink(missing_ok=True)


def main() -> int:
    args = parse_args()
    payload = plan(Path(args.repo_root), Path(args.vault_root), args.prune)
    if args.apply:
        apply_plan(payload)

    output: dict[str, object] = {
        "mode": "apply" if args.apply else "dry-run",
        "repo_root": str(Path(args.repo_root).expanduser().resolve()),
        "vault_root": str(Path(args.vault_root).expanduser()),
        "prune": bool(args.prune),
        **payload,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
