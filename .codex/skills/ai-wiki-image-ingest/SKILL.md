---
name: ai-wiki-image-ingest
description: Ingest raw image files into this AI Obsidian wiki. Use when processing PNG, JPG, JPEG, WEBP, GIF, HEIC, or other supported image sources under the AI raw source root into source notes, index coverage, log entries, and optional compiled concept, entity, synthesis, or map pages.
---

# AI Wiki Image Ingest

Use this skill whenever ingesting a raw image file for this AI wiki. This skill owns image-specific ingest behavior; `AGENTS.md` owns global wiki rules, raw boundaries, source mapping, metadata, index/log, asset policy, and question-page policy.

## Required Context

Before writing, read `AGENTS.md`, `docs/wiki-templates.md`, and `index.md`.

## Fast Path

1. Pick or receive a supported raw image under the raw source root from `AGENTS.md`.
2. Open the image with Agent vision.
3. Inspect the full image for document/screenshot/photo/diagram type, reliable visible text, layout, visual relationships, knowledge points, and limitations.
4. Stat the raw file and collect the raw metadata required by `AGENTS.md`.
5. Create or update the mirrored source note, update `index.md`, append one `log.md` line, then compile only reusable concept/entity/synthesis/map updates.

## Image Source Rules

Use the source-note template from `docs/wiki-templates.md`. Image-specific requirements:

- Set `source_type: image`.
- Set `status: ingested` when the image opens and gives enough signal for a source note.
- Use `partial` when the image is blurry, cropped, low-resolution, mostly unreadable, animated with uninspected frames, or otherwise ambiguous.
- Use `blocked` when the image cannot be opened or viewed.
- Record image type and visual coverage in `Source` or `Maintenance Notes`; include dimensions when cheap to determine.
- `Source Digest` must describe the visual structure, reliable visible text, relationships, knowledge points, and limits. Do not present uncertain OCR as fact.
- In `Key Claims`, use `explicit:` for claims directly visible in the image and `inferred:` for agent interpretation of the visual content.
- In `External Links`, include URLs that are clearly visible in the image; otherwise write `No external links found in extracted content.`
- Mark uncertain visible text with `uncertain`.

## Group Boundary

When multiple images in the same raw directory clearly belong to one set, create or update one source note per image first. Then compile a concept or synthesis page for the group only if the set contributes reusable knowledge beyond individual source notes.

## Failure Path

If the image cannot be opened or viewed, still create or update the mirrored source note with `status: blocked`, raw metadata, the view/open error summary, and a concrete human next step. If the image opens but the content is too blurry, cropped, low-resolution, or otherwise unreliable, use `partial` and describe the limitation. Do not edit, convert, repair, or write next to the raw image.

Do not create `questions/` pages unless the user explicitly asks to save a question or answer.
