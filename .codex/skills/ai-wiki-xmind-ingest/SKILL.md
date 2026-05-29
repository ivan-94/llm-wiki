---
name: ai-wiki-xmind-ingest
description: Export, digest, and ingest raw .xmind files for this AI Obsidian wiki. Use when processing XMind sources under the AI raw source root into wiki sources, concepts, entities, synthesis, maps, index, or log pages; when the user asks to run an XMind ingest; or when avoiding unnecessary inspect, tree, or validate steps during source conversion.
---

# AI Wiki XMind Ingest

Use this skill for this project's XMind source ingestion. The fast path is a single export command used as temporary reading material, then wiki writing from an LLM-digested summary of that exported Markdown.

## Fixed Paths

- Raw source root: `/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI`
- Wiki root: 当前项目根目录。
- Source notes live under `sources/` and mirror the raw relative path.
- A raw `.xmind` maps to `sources/<raw-relative-path>.md`, preserving the original filename including `.xmind`.

Example:

```text
raw:  Agent/AI  编排引擎调研.xmind
wiki: sources/Agent/AI  编排引擎调研.xmind.md
```

## Fast Path

1. Pick or receive a raw `.xmind` under the raw source root.
2. Run the helper once. The helper must discover and export all sheets, not only the workbook default sheet:

```bash
python3 ".codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py" "$RAW_XMIND" --json
```

3. Use `source_relpath`, `target_source_note`, `sheet_count`, `sheets`, and combined `markdown` from the output to create or update the source note.
4. Treat per-sheet Markdown as intermediate reading material. Read all sheets, understand them, then write a digest in your own words; do not paste or mechanically truncate it into the wiki.
5. Preserve external links found in the raw/exported Markdown in the source note's `External Links` section. If none are found, explicitly say so.
6. Update `index.md` and append to `log.md`.
7. Create or update only the concept/entity/synthesis/map pages that have enough reusable content. Do not create empty entity pages just because a product name appears.

If the helper is unavailable, use the direct command:

```bash
xmind sheets "$RAW_XMIND" --json
xmind export "$RAW_XMIND" --sheet-index 0 --format markdown
xmind export "$RAW_XMIND" --sheet-index 1 --format markdown
# ...repeat for every sheet index returned by xmind sheets
```

Do not rely on default `xmind export "$RAW_XMIND" --format markdown` for multi-sheet workbooks. A trailing `xmind:#...` link is only a sheet reference; it does not mean the linked sheet content was read.

## Source Note Rules

Use the hard rules in `AGENTS.md` and the source-note template in `docs/wiki-templates.md`. For normal exports:

- `source_type: xmind`
- `status: ingested`
- Cite the raw file with the FinderX iCloud link format from `AGENTS.md`.
- Record sheet count and sheet titles in `Source` or `Maintenance Notes`; every sheet must be accounted for.
- Put an LLM-digested synthesis under `Source Digest`.
- Add `External Links`; preserve every URL found in the raw/exported content with brief context, or write `No external links found in extracted content.`
- Do not paste the complete exported Markdown into `sources/`; the raw `.xmind` remains the source of truth.
- For large or multi-sheet maps, explain the main theme, the meaning of important branches, critical paths, reusable knowledge, high-signal second-level distinctions, and placeholder/anomaly notes. A typical digest is 30-80 lines, but density and understanding matter more than line count.
- Before finalizing a large or multi-sheet source note, check that reusable high-signal details are preserved somewhere: second-level taxonomies, named frameworks, step lists, metric dimensions, anomaly nodes, and numbering/structure problems. If they are not in `Source Digest`, place them in `Key Claims`, `Maintenance Notes`, or the downstream compiled page.
- Do not make `Source Digest` a mechanical outline, first-N-lines sample, text preview, or truncated export. Those are intermediate materials, not wiki output.
- Put interpretation and reusable claims under `Key Claims`. Mark claims as `explicit:` when directly stated or strongly supported by the raw/exported content, and `inferred:` when they are the agent's synthesis, classification, or implication. Sparse sources and heavily interpreted sources must use these prefixes.
- List every page created or modified under `Links` with a relationship type and a short contribution note. Bare wikilink lists are invalid.
- Record placeholder titles, partial content, parse limits, and cleanup needs under `Maintenance Notes`.

Recommended `Links` relation types for source notes:

- `compiled-concept`: the source produced or materially updated a concept page.
- `compiled-entity`: the source produced or materially updated an entity page.
- `compiled-synthesis`: the source contributed to a synthesis page.
- `user-question`: the source relates to a question page explicitly requested or created by the user. Do not create question pages during ingest/compile unless the user explicitly asks for that question to be saved.
- `map-entry`: the source was added to a learning map.
- `updates`: the source updated an existing page.

Also update:

- `index.md`: `Recently Updated`, `Source Coverage`, relevant page lists, and `Needs Attention`.
- `log.md`: append one single-line `## [YYYY-MM-DD] ingest | <source_relpath> — <summary>; issues: <issue or none>` entry.

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
