---
name: ai-wiki-vault-sync
description: Publish this AI wiki repository to the official Obsidian iCloud container for read-only iOS viewing. Use when syncing, publishing, dry-running, applying, pruning, or checking conflicts between `/Users/ivan/workspace/ai/ai_llm_wiki` and the Obsidian app iCloud vault target `iCloud~md~obsidian/Documents/ai`.
---

# AI Wiki Vault Sync

Use this skill to publish the compiled AI wiki from the repo to the official Obsidian iCloud container used on iOS. The repo remains canonical; the iCloud vault is a read-only mirror.

This skill does not ingest raw sources, compile concepts, lint the wiki, or sync edits back from iCloud. Use the other AI wiki skills for those workflows before publishing.

## Quick Start

From the wiki repo root:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --json
```

Apply the plan:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --apply --json
```

Apply and remove stale files from managed wiki areas:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/sync_vault.py --apply --prune --json
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

The direction is always repo to iCloud vault. Treat the vault as an iOS reading surface, not an editing source.

The helper syncs:

- `index.md`, `log.md`, `AGENTS.md`
- `docs/wiki-templates.md`
- `sources/`, `concepts/`, `entities/`, `synthesis/`, `questions/`, `maps/`
- `outputs/`, `assets/`

The helper does not sync `.git/`, `.codex/`, `.obsidian/`, raw source directories, temporary files outside managed wiki paths, or agent runtime artifacts.

## Safety Rules

- Run a dry-run first unless the user explicitly asks to apply.
- Use `--apply` only after reviewing `copy`, `update`, and `conflict`.
- Use `--prune` only when the user wants the iCloud mirror to remove stale managed files.
- Do not treat `--prune` as permission to remove vault settings; `.obsidian/` is not managed.
- If a target file is newer than the repo copy and contents differ, the helper reports `conflict` and does not overwrite it.
- Resolve conflicts manually by deciding whether the repo or the vault copy should win; do not add bidirectional merge behavior to this skill.

## Output Buckets

- `copy`: source exists in the repo and not in the vault.
- `update`: source and target differ, and the repo copy is at least as new as the vault copy.
- `skip`: source and target contents are identical.
- `conflict`: target differs and is newer than the repo copy.
- `delete`: stale files under managed wiki paths, reported only with `--prune`.

## Validation

Run the bundled tests after changing the helper:

```bash
python3 .codex/skills/ai-wiki-vault-sync/scripts/test_sync_vault.py
```
