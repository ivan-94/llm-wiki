---
name: ai-wiki-pdf-ingest
description: Preview-ingest raw PDF files into this AI Obsidian wiki by rendering the first three pages as images for Agent vision. Use when processing PDF sources under the AI raw source root into lightweight source notes, index coverage, and log entries; especially for long, scanned, or image-only PDFs where only a rough topic summary is required.
---

# AI Wiki PDF Ingest

Use this skill whenever ingesting a raw `.pdf` file for this AI wiki. This skill owns PDF-specific ingest behavior; `AGENTS.md` owns global wiki rules, raw boundaries, source mapping, metadata, index/log, and question-page policy.

Current mode is preview ingest: render only the first three pages as PNG images, use Agent vision, and write a lightweight source note about what the PDF appears to cover. Do not present preview findings as a complete reading of the PDF.

## Required Context

Before writing, read `AGENTS.md`, `docs/wiki-templates.md`, and `index.md`.

## Fast Path

1. Pick or receive a raw `.pdf` under the raw source root from `AGENTS.md`.
2. Render only the first three pages:

```bash
python3 ".codex/skills/ai-wiki-pdf-ingest/scripts/render_pdf_preview.py" "$RAW_PDF" --json
```

3. Open every returned `rendered_pages[*].image_path` with Agent vision.
4. Use the helper output for raw metadata; no separate stat step is needed when the helper succeeds.
5. Synthesize the preview pages together: likely topic, document type, visible claims, visible external links, and what remains unread because only preview pages were inspected.
6. Create or update the mirrored source note, update `index.md`, and append one `log.md` line.

## PDF Source Rules

Use the source-note template from `docs/wiki-templates.md`. PDF-specific requirements:

- Set `source_type: pdf`.
- Set `status: ingested` only when the first three pages render and give enough signal for a topic summary.
- Use `partial` when pages render but are too sparse, blurry, image-only, or ambiguous.
- Use `blocked` when the PDF cannot be opened or rendered.
- Include raw metadata from the helper output in frontmatter.
- Record total page count and processed pages, usually `Preview pages processed: 1-3 of N`.
- Write `Source Digest` as a short LLM-digested preview summary, not extracted text.
- In `Key Claims`, prefer `inferred:` because the ingest usually sees only a preview. Use `explicit:` only for clear visible text on rendered pages.
- In `External Links`, include URLs that are clearly visible in the rendered preview pages; otherwise write `No external links found in extracted content.`
- In `Maintenance Notes`, state that this is a first-three-page visual preview and not full-PDF OCR, text extraction, or complete reading.

## Compile Boundary

Default to source-note-only ingest. Create or update concept/entity/synthesis/map pages only when the preview pages contain stable, reusable knowledge that is worth preserving with low confidence and clear evidence.

Do not create `questions/` pages unless the user explicitly asks to save a question or answer.

## Temporary Files

The helper writes rendered PNGs under `tmp/pdf-preview/` by default. Treat them as temporary reading material for Agent vision. Do not register them as long-term assets unless the user asks for stable Obsidian previews or annotations.

## Failure Path

- If Poppler tools are missing, still create or update the mirrored source note with `status: blocked`, raw metadata collected by stat, the helper install hint, and a concrete human next step. Do not write a misleading preview digest.
- If the PDF has fewer than three pages, process all available pages and record the actual count.
- If rendering fails for one PDF, create a `blocked` or `partial` finding for that source and continue other sources when applicable.
- Never edit, rename, move, delete, repair, or write next to the raw PDF.
