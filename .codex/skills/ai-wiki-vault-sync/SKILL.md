---
name: ai-wiki-vault-sync
description: Sync this AI wiki repository with the official Obsidian iCloud container. Use when publishing repo-managed wiki content to iCloud, pulling human-authored Obsidian notes back from iCloud, dry-running, applying, pruning repo-managed mirror files, or checking conflicts between `/Users/ivan/workspace/ai/ai_llm_wiki` and the Obsidian app iCloud vault target `iCloud~md~obsidian/Documents/ai`.
---

# AI Wiki Vault Sync

Use this skill to publish the compiled AI wiki from the repo to the official Obsidian iCloud container used on iOS. The repo remains canonical for compiled wiki content. The only supported reverse direction is explicit `--pull-human`, which copies human-authored Obsidian notes from the vault back into repo `human/inbox` and `human/raw`.

This skill does not ingest raw sources, compile concepts, or lint the wiki. It also does not perform general bidirectional sync: `--pull-human` is limited to human original note areas and excludes `human/sources` and all compiled wiki areas.

## Quick Start

From the wiki repo root:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --json
```

Apply the plan:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --apply --json
```

Install the repo post-commit hook for the current clone/worktree:

```bash
.githooks/install.sh
```

Apply and remove stale files from managed wiki areas:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --apply --prune --json
```

Pull human-authored notes from the iCloud vault into the repo:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --pull-human --json
```

Apply the human-note pull:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --pull-human --apply --json
```

The default target is:

```text
/Users/ivan/Library/Mobile Documents/iCloud~md~obsidian/Documents/ai
```

Override roots for testing or a temporary vault:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py \
  --repo-root "/path/to/ai_llm_wiki" \
  --vault-root "/path/to/iCloud~md~obsidian/Documents/ai" \
  --json
```

## Sync Contract

The default direction is repo to iCloud vault. Treat compiled wiki areas in the vault as an iOS reading surface, not an editing source.

The helper syncs:

- `index.md`, `log.md`, `AGENTS.md`
- `docs/wiki-templates.md`
- `sources/`, `concepts/`, `entities/`, `synthesis/`, `questions/`, `maps/`
- `outputs/`, `assets/`
- `human/`

With `--pull-human`, the helper copies from the vault back to the repo only:

- `human/inbox/`
- `human/raw/`

Git does not auto-install hooks from a repository checkout. Run `.githooks/install.sh` once per clone or worktree that should auto-sync after commit. The hook runs repo-to-vault `--apply` after each commit and keeps the commit even if sync fails.

The helper does not sync `.git/`, `.codex/`, `.obsidian/`, external raw source directories, compiled wiki directories during `--pull-human`, temporary files outside managed paths, or agent runtime artifacts.

## Safety Rules

- Run a dry-run first unless the user explicitly asks to apply.
- Use `--apply` only after reviewing `copy`, `update`, and `conflict`.
- Use `--prune` only when the user wants the iCloud mirror to remove stale managed files.
- Do not combine `--pull-human` and `--prune`; human-note deletes are intentionally not synced.
- Do not treat `--prune` as permission to remove vault settings; `.obsidian/` is not managed.
- If a target file is newer than the repo copy and contents differ, the helper reports `conflict` and does not overwrite it.
- In `--pull-human`, if a repo human note is newer than the vault copy and contents differ, the helper reports `conflict` and does not overwrite it.
- Resolve conflicts manually by deciding whether the repo or the vault copy should win; do not add general bidirectional merge behavior to this skill.

## Output Buckets

- `copy`: source exists in the repo and not in the vault.
- `update`: source and target differ, and the repo copy is at least as new as the vault copy.
- `skip`: source and target contents are identical.
- `conflict`: target differs and is newer than the repo copy.
- `delete`: stale files under managed wiki paths, reported only with `--prune`.

`--pull-human` uses the same buckets, but `source_path` points at the vault file and `target_path` points at the repo file. `delete` is always empty in this mode.

## Validation

Run the bundled tests after changing the helper:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/test_sync_vault.py
```
