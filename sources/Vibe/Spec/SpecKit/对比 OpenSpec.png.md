---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Spec/SpecKit/对比 OpenSpec.png"
source_relpath: "Vibe/Spec/SpecKit/对比 OpenSpec.png"
raw_created_at: 2026-05-05T10:42:51.812596+00:00
raw_modified_at: 2026-05-05T10:42:51.812828+00:00
raw_size: 1672086
raw_fingerprint: "size=1672086;birth=2026-05-05T10:42:51.812596+00:00;mtime=2026-05-05T10:42:51.812828+00:00"
raw_snapshot_at: 2026-05-29T15:53:48.258177+00:00
ingested_at: 2026-05-29
status: ingested
---

# 对比 OpenSpec.png

## Source

- Raw file: [Vibe/Spec/SpecKit/对比 OpenSpec.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Spec/SpecKit/%E5%AF%B9%E6%AF%94%20OpenSpec.png>)
- Raw ref: `raw:Vibe/Spec/SpecKit/对比 OpenSpec.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T10:42:51.812596+00:00`; modified `2026-05-05T10:42:51.812828+00:00`; size `1672086`; snapshot `2026-05-29T15:53:48.258177+00:00`
- Coverage: Opened with Agent vision; inspected one 1672x941 comparison diagram covering visible labels, layout, workflow arrows, directory examples, selection guidance, and limitations.

## Summary

这张图把 OpenSpec 和 SpecKit 放在同一张 Spec-Driven 工作流对比图中：OpenSpec 被描述为 change-driven / delta-driven，更像规格变更账本；SpecKit 被描述为 feature-driven / branch-driven，更像从想法到实现的 feature 生命周期脚手架。图中还给出理想组合：先用 SpecKit 做 planning 和 implementation，再用 OpenSpec specs 沉淀当前事实，并用 future changes / delta / archive 维护未来变更历史。

## Source Digest

图的左侧是 OpenSpec，核心对象是 `openspec/specs` 当前事实和 `openspec/changes` 变更提案，主要问题是管理需求变更、规格演进与归档历史。它强调 Git patch、RFC、living spec ledger，以及维护 Current Truth 与 Proposed Future 的边界。工作流从 `init/update`、`propose/new`、`proposal.md`、`design.md`、`tasks.md`、`delta specs`，再到 `apply`、`sync/archive`、`openspec/specs`，关键动作是通过 `archive` 把 delta 合并为当前事实。

图的右侧是 SpecKit，核心对象是 `specs/<feature>` 的单个 feature 生命周期，主要问题是把模糊想法推进成可执行实现计划。它强调 PRD、Design Doc、Task breakdown、agent scaffold，以及 `spec/research/contracts/tasks` 的交付链。工作流包括 `specify init`、`constitution`、`specify`、`clarify?`、`plan`、`checklist?`、`tasks`、`analyze?`、`implement`，关键动作是通过 `plan/tasks/implement` 把 spec 推进到实现。

在产物与规范层面，OpenSpec 示例目录包括 `specs/<capability>/spec.md`、`changes/<change-id>/proposal.md`、`design.md`、`tasks.md`、`specs/...` 中的 ADDED / MODIFIED / REMOVED / RENAMED，以及 `archive` 历史；它的约束包括 SHALL / MUST、Scenario、Given / When / Then、MODIFIED 段落完整 block。SpecKit 示例目录包括 `spec.md`、`checklists/requirements.md`、`plan.md`、`research.md`、`data-model.md`、`contracts/`、`quickstart.md`、`tasks.md`，约束包括 Constitution Check、按 User Story 拆任务、完成标记 `[X]`。图底部给出的选择建议是：已有系统长期维护、需求变更审计、防止 AI 偏离当前事实、规格演进历史更适合 OpenSpec；新 feature 启动、从 0 到 1、需要补齐 research/data model/contracts/quickstart/tasks 更适合 SpecKit；理想组合是互补协同。

## Key Claims

- explicit: OpenSpec 的定位是 change-driven / delta-driven，面向“当前事实 + 未来变更 + 归档历史”。
- explicit: SpecKit 的定位是 feature-driven / branch-driven，面向“想法 -> 规格 -> 计划 -> 任务 -> 实现”。
- explicit: OpenSpec 的关键能力是维护 Current Truth 与 Proposed Future 的边界，并通过 archive 把 delta 合并为当前事实。
- explicit: SpecKit 的关键能力是补齐 PRD、Design Doc、Task breakdown、agent scaffold，以及 spec / research / contracts / tasks 交付链。
- explicit: OpenSpec 更适合已有系统长期维护、需求变更审计、防止 AI 偏离当前事实、规格演进历史。
- explicit: SpecKit 更适合新 feature 启动、从 0 到 1、需要补齐 research、data model、contracts、quickstart、tasks。
- inferred: 这张图把两者差异归纳为“存量系统规格治理”与“增量 feature 交付脚手架”的互补，而不是二选一替代关系。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Spec-Driven Development|Spec-Driven Development]] — 本图提供 OpenSpec 与 SpecKit 两种 SDD 工作流的对象、流程、产物和适用边界对比。
- compiled-entity: OpenSpec — 候选实体；本图描述其 change-driven / delta-driven 规格账本定位。
- compiled-entity: SpecKit — 候选实体；本图描述其 feature-driven / branch-driven 交付脚手架定位。
- compiled-synthesis: OpenSpec 与 SpecKit 工作流对比 — 候选综合；本图可作为两种 spec workflow 的核心对照证据。
- map-entry: Vibe Coding 与 Spec-Driven Development 学习地图 — 候选学习地图入口；本图适合作为 OpenSpec/SpecKit 选择与组合路径的总览。

## Maintenance Notes

- Vision ingest 完成；图中文字整体清晰，但小号目录项和图标说明若需逐字引用，应回看原图确认。
- 未联网核验 OpenSpec 或 SpecKit 当前项目事实；本 note 只记录图片可见内容。
