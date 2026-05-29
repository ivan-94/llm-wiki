---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Spec/SpecKit/Spec_kit_产物.png"
source_relpath: "Vibe/Spec/SpecKit/Spec_kit_产物.png"
raw_created_at: 2026-05-05T18:34:03+08:00
raw_modified_at: 2026-05-05T18:34:03+08:00
raw_size: 1731097
raw_fingerprint: "size=1731097;birth=2026-05-05T18:34:03+08:00;mtime=2026-05-05T18:34:03+08:00"
raw_snapshot_at: 2026-05-29T23:54:22+08:00
ingested_at: 2026-05-29
status: ingested
---

# Spec_kit_产物.png

## Source

- Raw file: [Vibe/Spec/SpecKit/Spec_kit_产物.png](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Spec/SpecKit/Spec_kit_%E4%BA%A7%E7%89%A9.png)
- Raw ref: `raw:Vibe/Spec/SpecKit/Spec_kit_产物.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T18:34:03+08:00`; modified `2026-05-05T18:34:03+08:00`; size `1731097`; snapshot `2026-05-29T23:54:22+08:00`
- Coverage: Agent vision inspected the full 1672x941 artifact map. Project-level artifacts, feature directory artifacts, and specification relationship chain are readable; dense formatting constraints were summarized.

## Summary

这张图展开 SpecKit 产物规范图谱，分为项目级产物、feature 目录主干和规范关系。项目级产物包括 templates、scripts、constitution、feature/init JSON；feature 目录包含 spec、requirements checklist、plan、research、data-model、contracts、quickstart、tasks；底部关系链把 User Story、Acceptance Scenario、FR/SC 编号、Technical Decision、Contract/Data Model、Task 和 Implementation 连接起来。

## Source Digest

顶部项目级产物区说明 `.specify/templates/` 提供 spec、plan、tasks、constitution 等模板；`.specify/scripts/` 提供 setup-plan、setup-tasks、check-prerequisites 等命令辅助脚本；`.specify/memory/constitution.md` 记录项目宪法、核心原则、约束、workflow 和 governance；`.specify/feature.json` 加 `init-options.json` 记录当前 feature 目录、integration、script、branch numbering 等初始化/定位信息。规则区强调模板可被 preset/override/extension 替换，脚本负责路径解析、前置检查和 JSON 输出，plan 阶段必须通过 Constitution Check，后续命令定位 feature 不强依赖 git branch。

中部 feature 目录主干列出 `specs/<NNN-feature-name>/` 下的主要文件。`spec.md` 是产品/行为规格，含 feature branch、user scenarios & testing、requirements、success criteria、assumptions，并要求 user story 用 P1/P2/P3 排序、acceptance scenarios 用 Given/When/Then、functional requirements 用 FR-### + MUST，success criteria 用 SC-### 且不写技术栈/API/代码结构。`checklists/requirements.md` 做需求写作质量检查；`plan.md` 是技术计划，含 summary、technical context、constitution check、project structure、complexity tracking；`research.md` 记录 decision、rationale 和 alternatives considered；`data-model.md` 描述 entities、fields、relationships、validation rules、state transitions；`contracts/` 存外部接口契约；`quickstart.md` 写关键验证步骤；`tasks.md` 是执行清单，包含 phase、编号、依赖和执行顺序，完成后标记 `[X]`。

底部规范关系链强调 User Story 提供用户价值，Acceptance Scenario 提供可验收行为，FR/SC 编号提供可度量需求，Technical Decision 记录技术取舍，Contract/Data Model 固化接口与数据，Task 形成可执行任务，Implementation + `[X]` 提供完成证据。

## Key Claims

- explicit: SpecKit 项目级产物包括 `.specify/templates/`、`.specify/scripts/`、`.specify/memory/constitution.md`、`.specify/feature.json` 和 `init-options.json`。
- explicit: `.specify/templates/` 承载 spec、plan、tasks、constitution 等模板；`.specify/scripts/` 承载 setup-plan、setup-tasks、check-prerequisites 等辅助脚本。
- explicit: feature 目录 `specs/<NNN-feature-name>/` 包含 spec、requirements checklist、plan、research、data-model、contracts、quickstart、tasks。
- explicit: `spec.md` 作为产品/行为规格，要求 user story 优先级、acceptance scenarios、requirements、success criteria 和 assumptions 等内容。
- explicit: `plan.md` 作为技术计划，包含 technical context、constitution check、project structure、complexity tracking 等内容。
- explicit: `tasks.md` 作为执行清单，要求任务编号、phase、依赖、执行顺序，并在完成后标记 `[X]`。
- explicit: 规范关系链从 User Story 到 Acceptance Scenario、FR/SC、Technical Decision、Contract/Data Model、Task、Implementation + `[X]`。
- inferred: SpecKit 通过文件结构和编号体系把“用户价值 -> 验收行为 -> 可度量需求 -> 技术取舍 -> 可执行任务 -> 完成证据”串成可追踪实现链。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/SpecKit Artifact 图谱|SpecKit Artifact 图谱]] — 可沉淀项目级和 feature 级产物结构及格式约束。
- compiled-concept candidate: [[concepts/需求到任务的可追踪链|需求到任务的可追踪链]] — 可沉淀 User Story 到 Implementation 的编号与证据关系。
- compiled-synthesis candidate: [[synthesis/OpenSpec 与 SpecKit 对比|OpenSpec 与 SpecKit 对比]] — 可补充 SpecKit 产物结构侧的对比证据。
- map-entry candidate: [[maps/Vibe Spec 工作流学习地图|Vibe Spec 工作流学习地图]] — 可作为 SpecKit artifact 细节节点。

## Maintenance Notes

- 图片为 1672x941 高密度图谱，主体可读；右侧和中部部分格式约束字号较小，已以结构化摘要保留，不做逐字 OCR。
- `feature.json` 与 `init-options.json` 的精确职责来自图片可见文字概括，未联网核验当前 SpecKit 实现。
- 未修改 `index.md`、`log.md` 或编译页；本批 worker 只记录 compile 候选关系。
