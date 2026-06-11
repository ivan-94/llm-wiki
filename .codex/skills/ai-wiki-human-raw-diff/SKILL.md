---
name: ai-wiki-human-raw-diff
description: Diff the AI wiki human/raw Markdown source root against mirrored human/sources notes. Use when checking added, deleted, updated, moved, unchanged, metadata-missing, unapproved, or unsupported human raw files before human source ingest, refresh, lint, or source maintenance.
---

# AI Wiki Human Raw Diff

## Overview

This skill compares `human/raw/` with `human/sources/` for the AI wiki. It is read-only and uses Markdown frontmatter plus filesystem metadata to respect the human source boundary.

Use it before bulk human source ingest, re-ingest, human source coverage review, or maintenance work that needs to know whether human raw Markdown notes were added, deleted, updated, or moved.

## Quick Start

From the wiki root:

```bash
python3 .codex/skills/ai-wiki-human-raw-diff/scripts/diff_human_raw_sources.py --json --include-unsupported --include-unapproved
```

For a human-readable report:

```bash
python3 .codex/skills/ai-wiki-human-raw-diff/scripts/diff_human_raw_sources.py --markdown --include-unsupported --include-unapproved
```

Override roots for tests or dry runs:

```bash
python3 .codex/skills/ai-wiki-human-raw-diff/scripts/diff_human_raw_sources.py \
  --raw-root "/path/to/wiki/human/raw" \
  --wiki-root "/path/to/wiki" \
  --json
```

## Report Buckets

- `added`: Markdown file under `human/raw/` has `ingest_policy: allowed`, but no mirrored `human/sources/` note exists.
- `deleted`: human source note exists, but the human raw Markdown path no longer exists and no move candidate was found.
- `updated`: mirrored human raw Markdown exists, has `ingest_policy: allowed`, and its `raw_modified_at` is newer than source note metadata, or its size changed.
- `moved`: source note path disappeared, and a different allowed human raw Markdown path has the same lightweight fingerprint.
- `unchanged`: mirrored human raw Markdown exists, has `ingest_policy: allowed`, and stored source metadata still matches.
- `needs_metadata`: human source note exists but lacks required raw metadata, so reliable update or move detection is not possible.
- `unapproved`: Markdown exists under `human/raw/`, but does not declare `ingest_policy: allowed`; shown only with `--include-unapproved`.
- `unsupported`: non-Markdown files found under `human/raw/` when `--include-unsupported` is set.

## Metadata Contract

Every new or refreshed human source note should include these frontmatter fields:

```yaml
source_type: human_markdown
source_origin: human
raw_path: "human/raw/path/name.md"
source_relpath: "path/name.md"
raw_created_at: 2026-05-30T00:00:00+00:00
raw_modified_at: 2026-05-30T00:00:00+00:00
raw_size: 12345
raw_fingerprint: "size=12345;birth=2026-05-30T00:00:00+00:00;mtime=2026-05-30T00:00:00+00:00"
raw_snapshot_at: 2026-05-30T00:00:00+00:00
```

Human raw Markdown maps directly from `human/raw/path/name.md` to `human/sources/path/name.md`.

`raw_modified_at` is the update signal. The script uses filesystem `mtime`, not `ctime`, because local metadata changes can alter `ctime` without content changes.

When `raw_size` still matches, sub-second `mtime` drift is ignored so source notes written with second-level timestamps do not produce false `updated` findings.

`moved` uses a lightweight fingerprint of size + birth time + modified time. It is a conservative candidate signal, not proof of semantic equivalence.

## Workflow

1. Run the diff script before ingesting or refreshing human sources.
2. Ingest `added` files only through the normal human source workflow.
3. Re-ingest or inspect `updated` files before compiling downstream pages.
4. Review `moved` candidates manually, then rename or regenerate the mirrored human source note as appropriate.
5. Treat `deleted` as a maintenance finding; do not remove source notes unless the user explicitly requests cleanup.
6. Backfill or refresh `needs_metadata` source notes before relying on future update/move detection.
7. Treat `unapproved` as outside automatic coverage unless the user explicitly requests ingest or the note declares `ingest_policy: allowed`.
8. Record unsupported findings in `index.md` Needs Attention or `log.md` when they affect the task.

## Human Boundary

The script never modifies `human/raw/`, `human/inbox/`, or `human/sources/`. It does not consider `human/inbox/` part of source coverage. Non-Markdown files under `human/raw/` are reported only as unsupported attachments or future-rule candidates.
