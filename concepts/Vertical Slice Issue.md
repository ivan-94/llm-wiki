---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-10
---

# Vertical Slice Issue

## Definition

Vertical Slice Issue 是穿透多个系统层（schema / API / UI / test）的最小可独立验证任务切片，每个切片可以独立实现、独立 demo、独立合并，不依赖其他切片同时完成。

## Why It Matters

大型需求拆成水平层（先建 schema、再建 API、再建 UI）会制造长期的未完成状态，每层单独完工都无法演示价值。Vertical Slice 让每个 issue 都能单独交付可见价值，让 Agent 并发执行时不需要等待彼此。

## Mental Model

把功能想象成一个塔楼。水平切片是每层楼（地基、结构、装修），完工前一直是烂尾楼；垂直切片是一套完整的房间（地基→结构→装修→验收），每套可以独立入住。

## Key Claims

- Vertical Slice 应独立可验证：实现完成后能独立 demo，不依赖其他 slice 同时完成。
- `/to-issues` 的核心产出是穿透多层的垂直切片，并分析串行/并发依赖、适合 LLM 和人类 review 的粒度。
- 好的 slice 应能表达 schema、API 契约、UI 行为和测试覆盖的完整增量，而不是某一层的局部实现。
- 切片应控制在适合 Agent 在单次会话中稳定执行的范围：过大会导致上下文腐烂，过小会产生碎片化合并成本。
- Slice 之间的依赖关系应显式建模（GitHub Sub-Issues / Dependencies），让父 Agent 能安排并发执行顺序。

## Examples

- `"用户登录"` 拆成：① schema 加 user_sessions 表；② /login API 及测试；③ 登录表单和 UI 状态（含 E2E 测试）——三个 slice 各自独立可 demo。
- `/to-issues` 产出的 issue 列表中，每条都有明确输入（pre-condition）、输出（产物）、验收条件，可以被 `/triage` 独立分拣和交给 Agent。

## Common Confusions

- Vertical Slice ≠ 任务分解：任务分解可以是水平的（"拆成 DB + API + UI 三个 task"），切片是垂直的（每个 task 都包含 DB + API + UI）。
- 小 issue ≠ Vertical Slice：issue 可以很小，但如果它只覆盖一层而没有端到端的验证，就不是 slice。
- 独立可验证 ≠ 无依赖：slice 之间可以有依赖（如 slice B 需要 slice A 的 schema），但每个 slice 完成后都应该能 demo 其对应的价值增量。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — 明确 `/to-issues` 应拆 tracer-bullet vertical slices，每个穿透多层并独立可验证。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]] — 可视化 PRD → Vertical Slice Issue 的产出结构。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 描述 `/to-issue` 如何分析依赖关系、控制粒度并准备 LLM 执行切片。

## Relations

- part-of: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — Vertical Slice Issue 是工作流编排的任务分发单元。
- enables: [[concepts/Agent Brief|Agent Brief]] — 每个 Slice 是补充 Brief 的原材料。
- related: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — Slice issue 进入 GitHub 后构成 Agent 任务市场。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

Vertical Slice Issue 是把"写完整个功能"分解为"写完一套完整的最小功能"——让每次提交都可以演示价值，而不是等所有层都完工才能验证。

## Review Questions

- Vertical Slice 和水平分解有什么核心区别？
- 为什么 slice 粒度过大会导致上下文腐烂？
- `/to-issues` 如何保证切片的独立可验证性？
- 如何表达 slice 之间的依赖关系？

## Open Questions

- 在实践中如何平衡切片的粒度：太细碎会增加合并成本，太粗会让 Agent 超时或偏移。
