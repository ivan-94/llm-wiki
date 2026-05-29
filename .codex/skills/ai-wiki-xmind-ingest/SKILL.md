---
name: ai-wiki-xmind-ingest
description: Export, digest, and ingest raw .xmind files for this AI Obsidian wiki. Use when processing XMind sources under the AI raw source root into wiki sources, concepts, entities, synthesis, maps, index, or log pages; when the user asks to run an XMind ingest; or when avoiding unnecessary inspect, tree, or validate steps during source conversion.
---

# AI Wiki XMind Ingest

Use this skill whenever ingesting a raw `.xmind` file for this AI wiki. This skill owns XMind-specific ingest behavior; `AGENTS.md` owns global wiki rules, raw boundaries, source mapping, metadata, index/log, and question-page policy.

## Required Context

Before writing, read `AGENTS.md`, `docs/wiki-templates.md`, and `index.md`. Do not bypass this skill with ad hoc `xmind-cli` commands; use the commands here as the approved path.

## Fast Path

1. Pick or receive a raw `.xmind` under the raw source root from `AGENTS.md`.
2. Run the helper once. It must discover and export all sheets, not only the workbook default sheet:

```bash
python3 ".codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py" "$RAW_XMIND" --json
```

3. Check `ok` and `sheets_error`. If `ok` is false, follow the Failure Path below instead of treating `markdown` as complete content.
4. Use `source_relpath`, `target_source_note`, raw metadata fields, `sheet_count`, `sheets`, `exports`, and combined `markdown` from the output to create or update the source note.
5. Treat per-sheet Markdown as temporary reading material. Read all exported sheets, understand them, then write an LLM-digested source note.
6. Update `index.md`, append one `log.md` line, then compile only reusable concept/entity/synthesis/map updates.

If the helper is unavailable, use this fallback sequence and still account for every sheet:

```bash
xmind sheets "$RAW_XMIND" --json
xmind export "$RAW_XMIND" --sheet-index 0 --format markdown
xmind export "$RAW_XMIND" --sheet-index 1 --format markdown
# ...repeat for every sheet index returned by xmind sheets
```

Do not rely on default `xmind export "$RAW_XMIND" --format markdown` for multi-sheet workbooks. A trailing `xmind:#...` link is only a sheet reference; it does not mean the linked sheet content was read.

## XMind Source Rules

Use the source-note template from `docs/wiki-templates.md`. XMind-specific requirements:

- `source_type: xmind`
- `status: ingested` only when every sheet was discovered, exported, read, and digested.
- `status: partial` when any sheet export is missing, failed, empty, or unreadable; record the affected sheet and next step.
- `status: blocked` when sheet discovery/export cannot produce useful content.
- Record sheet count and sheet titles in `Source` or `Maintenance Notes`; every sheet must be accounted for.
- `Source Digest` must synthesize the workbook across sheets. Do not paste the complete exported Markdown, mechanical outline, first-N-lines sample, or truncated export.
- Preserve high-signal XMind details somewhere: important branches, second-level taxonomies, critical paths, named frameworks, step lists, metric dimensions, placeholder/anomaly nodes, and numbering/structure problems.
- Preserve every URL found in exported Markdown in `External Links` with brief context; if none are found, write `No external links found in extracted content.`
- Use `explicit:` for claims directly stated or strongly supported by exported content; use `inferred:` for agent synthesis, classification, or implications.
- Record placeholder titles, partial content, parse limits, and cleanup needs under `Maintenance Notes`.

## Failure Path

Run diagnostics only when export fails, returns empty/garbled content, or the user asks for workbook metadata:

```bash
xmind inspect "$RAW_XMIND" --json
xmind validate "$RAW_XMIND" --json
xmind tree "$RAW_XMIND" --depth 4 --format markdown
```

If sheet discovery fails, do not treat a default export as complete. If diagnostics still fail, create a `partial` or `blocked` source note with attempted commands, error summary, and a concrete human next step. Continue with other sources when possible.

Do not create `questions/` pages unless the user explicitly asks to save a question or answer.
