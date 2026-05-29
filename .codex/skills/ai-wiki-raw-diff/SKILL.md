---
name: ai-wiki-raw-diff
description: Diff the AI wiki iCloud raw source root against mirrored source notes. Use when checking added, deleted, updated, moved, unchanged, unsupported, metadata-missing, or iCloud-unavailable raw .xmind/image/Markdown/PDF/Excalidraw files before ingest, refresh, lint, or source maintenance.
---

# AI Wiki Raw Diff

## Overview

This skill compares the AI wiki raw source root with `sources/` without reading raw file contents. It is read-only and uses filesystem metadata so it can run safely against the iCloud raw directory.

Use it before bulk ingest, re-ingest, source coverage review, or maintenance work that needs to know whether raw files were added, deleted, updated, or moved.

## Quick Start

From the wiki root:

```bash
python3 .codex/skills/ai-wiki-raw-diff/scripts/diff_raw_sources.py --json --include-unsupported
```

For a human-readable report:

```bash
python3 .codex/skills/ai-wiki-raw-diff/scripts/diff_raw_sources.py --markdown --include-unsupported
```

Override roots for tests or dry runs:

```bash
python3 .codex/skills/ai-wiki-raw-diff/scripts/diff_raw_sources.py \
  --raw-root "/path/to/raw" \
  --wiki-root "/path/to/wiki" \
  --json
```

## Report Buckets

- `added`: supported raw `.xmind`, image, Markdown, PDF, or Excalidraw file exists, but no mirrored source note exists.
- `deleted`: source note exists, but the raw file path no longer exists and no move candidate was found.
- `updated`: mirrored raw file exists and its `raw_modified_at` is newer than the source note metadata, or its size changed.
- `moved`: source note path disappeared, and a different supported raw path has the same lightweight fingerprint.
- `unchanged`: mirrored raw file exists and stored source metadata still matches.
- `needs_metadata`: source note exists but lacks required raw metadata, so reliable update or move detection is not possible.
- `unsupported`: files outside the supported raw types found under raw when `--include-unsupported` is set.
- `icloud_unavailable`: iCloud placeholder files such as `.Name.xmind.icloud`; download them in Finder before ingesting.

## Metadata Contract

Every new or refreshed source note should include these frontmatter fields:

```yaml
raw_created_at: 2026-05-29T00:00:00+00:00
raw_modified_at: 2026-05-29T00:00:00+00:00
raw_size: 123456
raw_fingerprint: "size=123456;birth=2026-05-29T00:00:00+00:00;mtime=2026-05-29T00:00:00+00:00"
raw_snapshot_at: 2026-05-29T00:00:00+00:00
```

Raw Markdown has one special mapping rule: `raw/path/name.md` maps directly to `sources/path/name.md`. Other supported types map to `<raw filename including extension>.md`, for example `Survey.pdf` -> `Survey.pdf.md`.

`raw_modified_at` is the update signal. The script uses filesystem `mtime`, not `ctime`, because iCloud and local metadata changes can alter `ctime` without content changes.

`moved` uses a lightweight fingerprint of size + birth time + modified time. It is a conservative candidate signal, not proof of semantic equivalence.

## Workflow

1. Run the diff script before ingesting or refreshing sources.
2. Ingest `added` files with the normal wiki ingest workflow.
3. Re-ingest or inspect `updated` files before compiling downstream pages.
4. Review `moved` candidates manually, then rename or regenerate the mirrored source note as appropriate.
5. Treat `deleted` as a maintenance finding; do not remove source notes unless the user explicitly requests cleanup.
6. Backfill or refresh `needs_metadata` source notes before relying on future update/move detection.
7. Record unsupported or iCloud-unavailable findings in `index.md` Needs Attention or `log.md` when they affect the task.

## iCloud Handling

The script avoids content hashing and does not open raw files for parsing. It scans paths and stat metadata only, detects `.icloud` placeholders explicitly, and never writes to the raw directory.

If an iCloud placeholder is reported, do not try to fix it from the wiki workflow. Ask the user to download the file locally or wait for iCloud to hydrate it, then rerun the diff.
