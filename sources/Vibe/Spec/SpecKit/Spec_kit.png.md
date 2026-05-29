---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Spec/SpecKit/Spec_kit.png"
source_relpath: "Vibe/Spec/SpecKit/Spec_kit.png"
raw_created_at: 2026-05-05T10:28:36.218483+00:00
raw_modified_at: 2026-05-05T10:28:36.218729+00:00
raw_size: 1667851
raw_fingerprint: "size=1667851;birth=2026-05-05T10:28:36.218483+00:00;mtime=2026-05-05T10:28:36.218729+00:00"
raw_snapshot_at: 2026-05-29T23:54:22+08:00
ingested_at: 2026-05-29
status: ingested
---

# Spec_kit.png

## Source

- Raw file: [Vibe/Spec/SpecKit/Spec_kit.png](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Spec/SpecKit/Spec_kit.png)
- Raw ref: `raw:Vibe/Spec/SpecKit/Spec_kit.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T10:28:36.218483+00:00`; modified `2026-05-05T10:28:36.218729+00:00`; size `1667851`; snapshot `2026-05-29T23:54:22+08:00`
- Coverage: Agent vision inspected the full 1672x941 infographic. Core commands, main ideas, artifact tree, quality loop, and OpenSpec comparison are readable; smaller tree labels were summarized.

## Summary

这张图概览 SpecKit 的 specification-driven development 流程：从 `/specify init`、constitution、specify、clarify、plan、checklist、tasks、analyze 到 implement，把想法推进为 feature 目录、技术计划、可执行任务和实现。图中强调“规格成为 source of truth”，并把 SpecKit 与 OpenSpec 对比为 feature 分支式 SDD 脚手架，而 OpenSpec 更像 delta spec 加 archive 的账本。

## Source Digest

左侧“核心流程”列出 SpecKit 命令序列：`specify init`、`/speckit.constitution`、`/speckit.specify`、可选 `/speckit.clarify`、`/speckit.plan`、可选 `/speckit.checklist`、`/speckit.tasks`、可选 `/speckit.analyze`、`/speckit.implement`。底部小流程把自然语言想法推进为 feature 规格目录、技术计划、可执行任务和实现。

中间“主要思想”围绕“规格成为 Source of Truth”，包括 power inversion（不是 spec 服务代码，而是代码服务 spec）、executable specifications、continuous refinement、research-driven context、constitution gates 和 branching for exploration。右侧“产物链”区分项目级基础和 feature 级目录：项目级包括 `.specify/scripts/`、`.specify/templates/`、`.specify/memory/constitution.md`、`.specify/init-options.json` 和 agent commands / skills；feature 目录位于 `specs/<NNN-feature-name>/`，包含 `spec.md`、`checklists/requirements.md`、`plan.md`、`research.md`、`data-model.md`、`contracts/`、`quickstart.md`、`tasks.md` 等。底部质量闭环表现为 clarify 写回 spec、plan 生成研究和契约、tasks 映射 user story、analyze 只读检查 spec/plan/tasks、implement 标记完成并验证。

## Key Claims

- explicit: SpecKit 的流程命令包括 init、constitution、specify、clarify、plan、checklist、tasks、analyze 和 implement，其中 clarify/checklist/analyze 被标为可选。
- explicit: SpecKit 的核心思想是 specification-driven development，规格是源头，代码是规格的表达。
- explicit: SpecKit 项目级基础包括 `.specify/scripts/`、`.specify/templates/`、`.specify/memory/constitution.md`、`.specify/init-options.json` 和 agent commands / skills。
- explicit: 每个 feature 对应 `specs/<NNN-feature-name>/` 目录，并包含 spec、requirements checklist、plan、research、data model、contracts、quickstart、tasks 等产物。
- explicit: 质量闭环从 clarify 到 plan、tasks、analyze、implement，且 implement 阶段标记 `[X]` 并验证。
- explicit: 图中对比指出 SpecKit 是 feature 分支式 SDD 脚手架，OpenSpec 更像 delta spec + archive 账本。
- inferred: SpecKit 更偏向单个 feature 的规格化实施流水线，OpenSpec 更偏向长期维护当前行为规范和变更历史。

## External Links

No external links found in extracted content.

## Links

- related: SpecKit 工作流 — 可沉淀 SpecKit 命令序列、产物链和质量闭环。
- related: Specification-Driven Development — 可沉淀“规格是 source of truth，代码是规格表达”的开发模型。
- compiled-synthesis: [[synthesis/OpenSpec 与 SpecKit 对比|OpenSpec 与 SpecKit 对比]] — 可支撑 OpenSpec 与 SpecKit 在账本/脚手架定位上的差异。
- related: Vibe Spec 工作流学习地图 — 可作为 SpecKit 入口节点。

## Maintenance Notes

- 图片为 1672x941 信息图，主体可读；feature 目录树小字号较多，已按结构关系提炼。
- 未联网核验 SpecKit 当前命令名或目录结构是否已变化。
- 未修改 `index.md`、`log.md` 或编译页；本批 worker 只记录 compile 候选关系。
