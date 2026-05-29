# AI Wiki Log

## [2026-05-29] schema | move wiki to git workspace and reset generated artifacts

- Sources:
  - User instruction to move the wiki into the current directory, manage it with git, and reset `sources` plus derived artifacts to a blank wiki.
- Produced:
  - `AGENTS.md`
  - `.codex/skills/ai-wiki-xmind-ingest/`
  - `index.md`
  - `log.md`
  - `sources/`
  - `concepts/`
  - `entities/`
  - `synthesis/`
  - `questions/`
  - `maps/`
  - `outputs/`
  - `assets/`
- Summary:
  - Initialized the current directory as the canonical wiki workspace.
  - Preserved the operating rules and XMind ingest skill.
  - Reset generated knowledge artifacts to empty directories.
- Issues:
  - No sources have been ingested in this git-managed wiki yet.

## [2026-05-29] ingest | 提示语工程:上下文工程/上下文工程.xmind

- Sources:
  - `raw:提示语工程:上下文工程/上下文工程.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/上下文工程.xmind.md`
- Summary:
  - Ingested context engineering as the practice of selecting, maintaining, compressing, and isolating the information visible to an LLM during agent execution.
  - Extracted key failure modes: context poisoning, distraction, confusion, clash, and rot.
- Issues:
  - Extension reading titles were not externally verified in this ingest.

## [2026-05-29] ingest | 提示语工程:上下文工程/提示语工程.xmind

- Sources:
  - `raw:提示语工程:上下文工程/提示语工程.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/提示语工程.xmind.md`
- Summary:
  - Ingested prompt engineering as a learning outline covering foundations, structures, common techniques, prompt libraries, learning sources, troubleshooting, Agent mode, long context, and advanced techniques.
- Issues:
  - Source is mostly an outline and needs follow-up detailed sources.

## [2026-05-29] ingest | 提示语工程:上下文工程/案例.xmind

- Sources:
  - `raw:提示语工程:上下文工程/案例.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/案例.xmind.md`
- Summary:
  - Ingested prompt cases, especially Anthropic/Claude system prompt patterns, image safety behavior, model-family information blocks, and a code-structured creative prompt example.
- Issues:
  - Long prompt originals were not copied into the source note; raw remains the full evidence source.

## [2026-05-29] ingest | 提示语工程:上下文工程/公文提示词优化.xmind

- Sources:
  - `raw:提示语工程:上下文工程/公文提示词优化.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/公文提示词优化.xmind.md`
- Summary:
  - Ingested a vertical prompt optimization framework for official documents, covering document type, input/output cases, topic content, length testing, model comparison, and instruction-following.
- Issues:
  - Source has no concrete prompt, sample output, or evaluation result yet.

## [2026-05-29] ingest | 提示语工程:上下文工程/LLM 评估.xmind

- Sources:
  - `raw:提示语工程:上下文工程/LLM 评估.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/LLM 评估.xmind.md`
- Summary:
  - Ingested Langfuse-based LLM evaluation concepts: offline/online evaluation, Scores, Evaluation Methods, Datasets, Experiments, LLM-as-a-Judge, annotation queues, score analytics, and local SDK evaluation workflow.
- Issues:
  - Langfuse implementation details need official-document verification before being used as current API facts.

## [2026-05-29] compile | 提示语工程:上下文工程

- Sources:
  - `raw:提示语工程:上下文工程/上下文工程.xmind`
  - `raw:提示语工程:上下文工程/提示语工程.xmind`
  - `raw:提示语工程:上下文工程/案例.xmind`
  - `raw:提示语工程:上下文工程/公文提示词优化.xmind`
  - `raw:提示语工程:上下文工程/LLM 评估.xmind`
- Produced:
  - `concepts/提示语工程.md`
  - `concepts/上下文工程.md`
  - `concepts/LLM 评估.md`
  - `concepts/LLM-as-a-Judge.md`
  - `entities/Anthropic.md`
  - `entities/Langfuse.md`
  - `synthesis/提示语工程与上下文工程.md`
  - `maps/提示语与上下文工程学习地图.md`
- Summary:
  - Compiled the first prompt/context/evaluation learning cluster with typed relations, review questions, and a map-level study path.
- Issues:
  - Several pages remain low-confidence because the raw set contains outlines and historical product/model examples.

## [2026-05-29] compile | 提示语工程:上下文工程 prompt evaluation pass

- Sources:
  - `raw:提示语工程:上下文工程/案例.xmind`
  - `raw:提示语工程:上下文工程/公文提示词优化.xmind`
  - `raw:提示语工程:上下文工程/LLM 评估.xmind`
- Produced:
  - `concepts/系统提示语.md`
  - `questions/如何评估提示词优化是否有效.md`
  - `synthesis/公文提示词优化评估清单.md`
- Summary:
  - Promoted system prompts into a reusable concept based on Claude/Anthropic prompt cases.
  - Filed a reusable prompt-evaluation question that connects prompt optimization with offline/online LLM evaluation.
  - Built a public-document prompt optimization checklist from the public-document and LLM-evaluation sources.
- Issues:
  - The checklist still lacks real public-document examples, expected outputs, and scoring rubrics.

## [2026-05-29] schema | require external links and typed source links

- Sources:
  - User feedback on ingest/source-note quality rules.
- Produced:
  - `AGENTS.md`
  - `.codex/skills/ai-wiki-xmind-ingest/SKILL.md`
  - `sources/提示语工程:上下文工程/*.md`
- Summary:
  - Added a rule that raw/exported external URLs must be preserved in source notes under `External Links`.
  - Added a rule that source-note `Links` must use relationship types and short contribution descriptions.
  - Updated existing source notes from the first ingest to include `External Links` and typed `Links`.
- Issues:
  - Current extracted XMind Markdown contained no URLs, only some external-reading titles without URLs.

## [2026-05-29] schema | restrict question page creation

- Sources:
  - User feedback that `questions/` pages must be explicitly asked for or created by the user.
- Produced:
  - `AGENTS.md`
  - `.codex/skills/ai-wiki-xmind-ingest/SKILL.md`
  - removed `questions/如何评估提示词优化是否有效.md`
- Summary:
  - Added the rule that agents must not create question pages during ingest or compile unless the user explicitly asks to save/create that question.
  - Removed auto-created question links from concepts, source notes, map, synthesis, index, and review queue.
- Issues:
  - The removed question's reusable content remains represented by `synthesis/公文提示词优化评估清单.md`.

## [2026-05-29] schema | require all XMind sheets during ingest

- Sources:
  - User feedback after xmind-cli markdown export started preserving hyperlinks.
  - `raw:提示语工程:上下文工程/上下文工程.xmind`
- Produced:
  - `AGENTS.md`
  - `.codex/skills/ai-wiki-xmind-ingest/SKILL.md`
  - `.codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py`
- Summary:
  - Verified `xmind export --format markdown` now preserves topic hyperlinks.
  - Confirmed default export still reads the selected/default sheet only, while multi-sheet workbooks need explicit per-sheet export.
  - Updated XMind ingest rules to require sheet inspection and all-sheet reading.
  - Updated the wiki XMind ingest helper to collect sheet metadata and export every sheet by index.
- Issues:
  - Existing source notes from the earlier ingest have not been re-digested in this maintenance step.

## [2026-05-29] ingest | re-ingest existing 提示语工程:上下文工程 sources

- Sources:
  - `raw:提示语工程:上下文工程/上下文工程.xmind`
  - `raw:提示语工程:上下文工程/提示语工程.xmind`
  - `raw:提示语工程:上下文工程/案例.xmind`
  - `raw:提示语工程:上下文工程/公文提示词优化.xmind`
  - `raw:提示语工程:上下文工程/LLM 评估.xmind`
- Produced:
  - `sources/提示语工程:上下文工程/上下文工程.xmind.md`
  - `sources/提示语工程:上下文工程/提示语工程.xmind.md`
  - `sources/提示语工程:上下文工程/案例.xmind.md`
  - `sources/提示语工程:上下文工程/公文提示词优化.xmind.md`
  - `sources/提示语工程:上下文工程/LLM 评估.xmind.md`
- Summary:
  - Re-ran the existing XMind sources through the all-sheets helper.
  - Updated sheet coverage metadata for every source note.
  - Added extracted external links for `上下文工程.xmind`, `提示语工程.xmind`, `案例.xmind`, and `LLM 评估.xmind`.
  - Expanded `上下文工程.xmind` with its second sheet, `Anthroipic 实践`.
  - Expanded `提示语工程.xmind` from the previous outline-level digest to an 11-sheet digest.
- Issues:
  - External links were extracted from XMind hyperlink metadata but not browsed or verified.
  - `公文提示词优化.xmind` still lacks concrete prompt, sample output, and evaluation result examples.

## [2026-05-29] compile | refresh prompt and context pages after re-ingest

- Sources:
  - `raw:提示语工程:上下文工程/上下文工程.xmind`
  - `raw:提示语工程:上下文工程/提示语工程.xmind`
- Produced:
  - `concepts/提示语工程.md`
  - `concepts/上下文工程.md`
  - `synthesis/提示语工程与上下文工程.md`
  - `maps/提示语与上下文工程学习地图.md`
- Summary:
  - Refreshed prompt engineering with evaluation-driven iteration, advanced prompting techniques, troubleshooting, Agent mode, long context, and 12-law material.
  - Refreshed context engineering with JIT retrieval, structured note-taking, compaction, and sub-agent/multi-agent context isolation from the second sheet.
- Issues:
  - No question pages were created because `questions/` now requires explicit user request.

## [2026-05-29] schema | distinguish source claims and preserve high-signal details

- Sources:
  - User accepted audit recommendations 2 and 3 after source/raw sampling.
- Produced:
  - `AGENTS.md`
  - `.codex/skills/ai-wiki-xmind-ingest/SKILL.md`
  - `index.md`
- Summary:
  - Added a rule that source-note `Key Claims` should distinguish `explicit:` claims from `inferred:` agent synthesis.
  - Added a rule that large or multi-sheet source digesting must preserve high-signal details such as reusable taxonomies, step lists, metric dimensions, named frameworks, anomaly nodes, and structure problems.
- Issues:
  - Existing source notes were not mass-rewritten; the rule applies to future ingest and targeted refreshes.

## [2026-05-29] schema | normalize AGENTS guide and split templates

- Sources:
  - User asked to reduce AGENTS.md noise, redundancy, and confusion while preserving rule meaning.
- Produced:
  - `AGENTS.md`
  - `docs/wiki-templates.md`
  - `.codex/skills/ai-wiki-xmind-ingest/SKILL.md`
  - `index.md`
- Summary:
  - Reorganized AGENTS.md into rule priority, hard rules, workflow matrix, workflow details, relation types, and index/log contracts.
  - Moved long page templates and examples into `docs/wiki-templates.md`.
  - Clarified the normal XMind path as sheet-listing plus per-sheet export, with inspect/tree/validate reserved for diagnostics.
  - Updated the XMind ingest skill to point agents at the new template appendix.
- Issues:
  - Existing wiki pages were not rewritten; this was a schema/documentation normalization only.

## [2026-05-29] schema | restore AGENTS execution-safety details after split review

- Sources:
  - User asked to review deleted AGENTS.md content for accidental rule loss.
- Produced:
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Summary:
  - Restored explicit raw-allowed operations and raw repair registration requirements.
  - Restored XMind failure handling details: summarize failures, record human next steps, and continue other sources.
  - Restored the rule that source digest must synthesize all readable sheets.
  - Restored review guidance that review output must expose recall gaps rather than become a generic summary.
- Issues:
  - No existing wiki knowledge pages were changed.
