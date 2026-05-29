---
name: ai-wiki-xmind-ingest
description: Export, digest, and ingest raw .xmind files for this AI Obsidian wiki. Use when processing XMind sources under the AI raw source root into wiki sources, concepts, entities, synthesis, maps, index, or log pages; when the user asks to run an XMind ingest; or when avoiding unnecessary inspect, tree, or validate steps during source conversion.
---

# AI Wiki XMind Ingest

Use this skill for this project's XMind source ingestion. The fast path is a single export command used as temporary reading material, then wiki writing from an LLM-digested summary of that exported Markdown.

## Fixed Paths

- Raw source root: `/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI`
- Wiki root: `/Users/ivan/workspace/ai/ai_llm_wiki`
- Source notes live under `sources/` and mirror the raw relative path.
- A raw `.xmind` maps to `sources/<raw-relative-path>.md`, preserving the original filename including `.xmind`.

Example:

```text
raw:  Agent/AI  编排引擎调研.xmind
wiki: sources/Agent/AI  编排引擎调研.xmind.md
```

## Fast Path

1. Pick or receive a raw `.xmind` under the raw source root.
2. Run the helper once:

```bash
python3 ".codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py" "$RAW_XMIND" --json
```

3. Use `source_relpath`, `target_source_note`, and `markdown` from the output to create or update the source note.
4. Treat `markdown` as intermediate reading material. Read it, understand it, then write a digest in your own words; do not paste or mechanically truncate it into the wiki.
5. Update `index.md` and append to `log.md`.
6. Create or update only the concept/entity/synthesis/map pages that have enough reusable content. Do not create empty entity pages just because a product name appears.

If the helper is unavailable, use the direct command:

```bash
xmind export "$RAW_XMIND" --format markdown
```

Do not start with `inspect`, `tree`, or `validate` during normal ingest. They are diagnostic commands, not the default export route.

## Source Note Rules

Use the project source-note template from `AGENTS.md`. For normal exports:

- `source_type: xmind`
- `status: ingested`
- Cite the raw file with the FinderX iCloud link format from `AGENTS.md`.
- Put an LLM-digested synthesis under `Source Digest`.
- Do not paste the complete exported Markdown into `sources/`; the raw `.xmind` remains the source of truth.
- For large maps, explain the main theme, the meaning of important branches, critical paths, reusable knowledge, and placeholder/anomaly notes. A typical digest is 30-80 lines, but density and understanding matter more than line count.
- Do not make `Source Digest` a mechanical outline, first-N-lines sample, text preview, or truncated export. Those are intermediate materials, not wiki output.
- Put interpretation and reusable claims under `Key Claims`.
- List every page created or modified under `Links`.
- Record placeholder titles, partial content, parse limits, and cleanup needs under `Maintenance Notes`.

Also update:

- `index.md`: `Recently Updated`, `Source Coverage`, relevant page lists, and `Needs Attention`.
- `log.md`: append one `## [YYYY-MM-DD] ingest | <source_relpath>` entry.

## Boundaries

- Treat raw files as read-only.
- Never edit, rename, move, delete, unzip, or repair raw `.xmind` files.
- Never write intermediate files in or next to the raw source tree.
- Preserve spaces, Chinese characters, punctuation, and original filenames in paths.

## Failure Path

Run diagnostics only when export fails, returns empty/garbled content, or the user asks for workbook metadata:

```bash
xmind inspect "$RAW_XMIND" --json
xmind validate "$RAW_XMIND" --json
xmind tree "$RAW_XMIND" --depth 4 --format markdown
```

If diagnostics still fail, create a `partial` or `blocked` source note with the attempted command, error summary, and a concrete human next step. Continue with other sources when possible.
