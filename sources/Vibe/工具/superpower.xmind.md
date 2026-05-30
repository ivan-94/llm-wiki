---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/superpower.xmind"
source_relpath: "Vibe/工具/superpower.xmind"
raw_created_at: 2026-04-29T02:37:41.273552+00:00
raw_modified_at: 2026-04-29T09:48:00.444252+00:00
raw_size: 21974611
raw_fingerprint: "size=21974611;birth=2026-04-29T02:37:41.273552+00:00;mtime=2026-04-29T09:48:00.444252+00:00"
raw_snapshot_at: 2026-05-29T16:12:50.215203+00:00
ingested_at: 2026-05-30
status: partial
---

# superpower.xmind

## Source

- Raw file: [Vibe/工具/superpower.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/superpower.xmind>)
- Raw ref: `raw:Vibe/工具/superpower.xmind`
- Type: xmind
- Status: partial
- Raw metadata: created `2026-04-29T02:37:41.273552+00:00`; modified `2026-04-29T09:48:00.444252+00:00`; size `21974611`; snapshot `2026-05-29T16:12:50.215203+00:00`
- Coverage: exported with `.codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py`; 7 sheets discovered and exported: `superpower` (82 topics), `brainstorming` (2), `writing planning` (3), `executing` (6), `systematic-debugging` (2), `test-driven-development ` (3), `writing-skills` (3). Main sheet provides substantive content; several child sheets contain only titles or empty placeholder nodes.

## Summary

这份 XMind 把 Superpowers 描述为一个 agentic skills framework 和软件开发方法论：通过目标澄清、规格书、计划、子代理执行、TDD、代码审查和收尾流程，把 AI 编码从一次性对话变成受约束的工程工作流。

## Source Digest

主 sheet 的核心是把一组 skills 组织成框架。Superpowers 的工作流从目标澄清开始：当代理意识到用户在构建项目时，不直接编码，而是先追问真实目标。随后它把对话整理成规格说明，并拆成用户能阅读和确认的片段。设计确认后，代理生成足够明确的实现计划，强调红/绿 TDD、YAGNI 和 DRY。执行阶段通过子代理逐项完成工程任务、检查和评审，目标是在较长时间内仍不偏离计划。

方法论强调四条原则：永远先写测试，系统化流程优于临时猜测，简洁优先降低复杂度，以及证据胜过宣称。基本 workflow 包括 brainstorming、using-git-worktrees、writing-plans、subagent-driven-development 或 executing-plans、test-driven-development、requesting-code-review、finishing-a-development-branch。skills 库进一步分为测试、Debugging、协作和元 skills，其中包括 systematic-debugging、verification-before-completion、dispatching-parallel-agents、receiving-code-review、writing-skills、using-superpowers 等。

运行原理以 Claude Code 为例：通过 hooks/session-start 注入 using-superpowers，强制引导整体工作流和相关提示；同时注册 `agents/code-reviewer.md` 子 Agent 做代码评审。XMind 内的子 sheet 主要作为技能主题入口，部分只保留标题或空节点，因此当前 source 更适合作为 Superpowers 总览，而不是单个 skill 的详细说明。

## Key Claims

- explicit: Superpowers 被定义为 agentic skills framework，也被视为一套软件开发方法论。
- explicit: 核心工作流包括目标澄清、规格书编写、计划实施和子代理执行。
- explicit: 方法论强调 TDD、系统化流程、降低复杂度和验证证据。
- explicit: 执行阶段可通过子代理逐项完成任务，并用评审机制检查计划符合性和代码质量。
- explicit: 在 Claude Code 示例中，Superpowers 通过 session-start hook 注入 using-superpowers，并注册 code-reviewer 子 Agent。
- inferred: 这份 source 将“skills”从单个提示技巧提升为可编排、可审查、可长期运行的 agent workflow 框架。

## External Links

No external links found in extracted content.

## Links

- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 适合归入 agent skills/workflow 工具。

## Maintenance Notes

- `partial`: helper 成功导出 7 个 sheet，但 `brainstorming`、`writing planning`、`systematic-debugging`、`test-driven-development `、`writing-skills` 等子 sheet 基本只有标题或空节点；当前 note 未把这些占位页当作完整技能说明。
- XMind 内存在 `xmind:#...` 内部链接，属于 workbook sheet 引用，不作为 External Links。

- Link cleanup candidate: compiled-concept: Agent Skills Framework — 本 source 提供 skills 作为框架和方法论的总览。.
- Link cleanup candidate: compiled-concept: 子代理驱动开发 — 本 source 描述任务拆分、子代理执行和两阶段评审。.
- Link cleanup candidate: compiled-concept: TDD for AI Coding — 本 source 把红绿重构作为 AI 编码约束。.
