---
name: ai-wiki-excalidraw-ingest
description: Ingest raw Excalidraw files into this AI Obsidian wiki. Use when processing .excalidraw JSON sources under the AI raw source root into source notes, index coverage, log entries, and optional compiled concept, entity, synthesis, or map pages.
---

# AI Wiki Excalidraw Ingest

Use this skill whenever ingesting a raw `.excalidraw` file for this AI wiki. This skill owns Excalidraw-specific ingest behavior; `AGENTS.md` owns global wiki rules, raw boundaries, source mapping, metadata, index/log, and question-page policy.

## Required Context

Before writing, read `AGENTS.md`, `docs/wiki-templates.md`, and `index.md`.

## Fast Path

1. Pick or receive a raw `.excalidraw` file under the raw source root from `AGENTS.md`.
2. Parse the file as JSON with a structured parser. Do not use ad hoc string matching.
3. Extract readable text elements, URLs, element types, grouping/frame hints, and rough spatial relationships from coordinates when useful.
4. Stat the raw file and collect the raw metadata required by `AGENTS.md`.
5. Create or update the mirrored source note, update `index.md`, append one `log.md` line, then compile only reusable concept/entity/synthesis/map updates.

## Excalidraw Source Rules

Use the source-note template from `docs/wiki-templates.md`. Excalidraw-specific requirements:

- Set `source_type: excalidraw`.
- Set `status: ingested` when the JSON parses and the meaningful text/link elements are processed.
- Use `partial` when the JSON parses but important relationships, embedded files, handwriting, or visual structure cannot be confidently recovered.
- Use `blocked` when the file is not valid readable JSON or cannot be opened.
- Record the extraction method, element counts, processed text/link coverage, and limitations in `Source` or `Maintenance Notes`.
- `Source Digest` must synthesize the diagram's visible concepts, relationships, workflow, or map structure. Do not hand-write a complete diagram reconstruction when the JSON does not support it.
- In `Key Claims`, use `explicit:` for visible text or directly represented diagram relationships and `inferred:` for agent interpretation of structure or intent.
- In `External Links`, preserve URLs from element links or visible text; if none are found, write `No external links found in extracted content.`

## Failure Path

If parsing fails, still create or update the mirrored source note with `status: blocked`, raw metadata, parser error summary, and a concrete human next step. Use `partial` only when parsing recovers enough text, links, or structure for a limited digest. Do not edit or repair the raw `.excalidraw` file.

Do not create `questions/` pages unless the user explicitly asks to save a question or answer.
