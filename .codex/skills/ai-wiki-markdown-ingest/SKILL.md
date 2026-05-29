---
name: ai-wiki-markdown-ingest
description: Ingest raw Markdown files into this AI Obsidian wiki. Use when processing .md sources under the AI raw source root into source notes, index coverage, log entries, and optional compiled concept, entity, synthesis, or map pages without copying the raw document into the wiki.
---

# AI Wiki Markdown Ingest

Use this skill whenever ingesting a raw Markdown file for this AI wiki. This skill owns Markdown-specific ingest behavior; `AGENTS.md` owns global wiki rules, raw boundaries, source mapping, metadata, index/log, and question-page policy.

## Required Context

Before writing, read `AGENTS.md`, `docs/wiki-templates.md`, and `index.md`.

## Fast Path

1. Pick or receive a raw `.md` file under the raw source root from `AGENTS.md`.
2. Read the full Markdown file as raw source material.
3. Extract its theme, structure, key claims, definitions, examples, URLs, and reusable knowledge. Preserve headings as context, not as a copied outline.
4. Stat the raw file and collect the raw metadata required by `AGENTS.md`.
5. Create or update the mirrored source note, update `index.md`, append one `log.md` line, then compile only reusable concept/entity/synthesis/map updates.

## Markdown Source Rules

Use the source-note template from `docs/wiki-templates.md`. Markdown-specific requirements:

- Set `source_type: markdown`.
- Set `status: ingested` when the full Markdown file is readable and digested.
- Use `partial` when the file is readable but has encoding problems, missing referenced context, truncated sections, or other limitations.
- Use `blocked` when the file cannot be read.
- Record `Coverage: full raw Markdown file read` in `Source` when the whole file was read; describe unreadable sections or limits when status is `partial`.
- `Source Digest` must be an LLM-digested summary of the document's purpose, structure, key ideas, and reusable knowledge. Do not copy the raw Markdown, paste a mechanical heading outline, or save a long excerpt cache.
- In `Key Claims`, use `explicit:` for claims directly stated by the Markdown and `inferred:` for agent synthesis, classification, or implications.
- In `External Links`, preserve URLs from the raw Markdown with title/anchor/context when available; if none are found, write `No external links found in extracted content.`
- Record missing assets, broken local references, ambiguous frontmatter, or context gaps under `Maintenance Notes`.

## Compile Boundary

Create or update concept/entity/synthesis/map pages only when the Markdown contains stable, reusable knowledge. Do not create `questions/` pages unless the user explicitly asks to save a question or answer.

## Failure Path

If the Markdown file cannot be read, still create or update the mirrored source note with `status: blocked`, raw metadata, the read/encoding error summary, and a concrete human next step. If the file is partially readable, use `partial` and record unreadable sections, encoding ambiguity, missing referenced context, or truncation under `Maintenance Notes`. Do not edit, repair, normalize, or write next to the raw Markdown file.
