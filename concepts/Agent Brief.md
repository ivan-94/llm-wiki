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

# Agent Brief

## Definition

Agent Brief 是交给 Agent 的任务上下文包：包含任务目标、输入边界、非目标、决策约束、验收标准和执行提示，目的是让 Agent 能够在没有持续人工陪同的情况下独立完成一个有界任务。

## Why It Matters

聊天式上下文是一次性的，Agent Brief 是持久性的任务协议。没有 Brief，Agent 需要反复询问或自行推断范围——在异步/并发场景下这会放大偏移；有了 Brief，Agent 可以作为可交接任务单元被 triage、分配、执行、验收。

## Mental Model

把 Agent Brief 想象成"工作说明书 + 验收标准"的最小合集：

```
Brief = 目标 + 输入/边界 + 非目标 + 决策约束 + 验收条件 + 提示（hints）
```

## Key Claims

- Agent Brief 是 `/triage` 的输出产物之一：分诊阶段决定哪些 issue 可交给 Agent，并为其补充足够的上下文变成 Brief。
- 好的 Brief 要把"哪些决策不交给 Agent"写出来，而不只是说明做什么——决策边界比任务描述更难写也更关键。
- Agent Brief 不等于 PRD；PRD 描述完整产品意图，Brief 是针对单个可执行切片的执行协议。
- 在多 Agent 并发场景下，Brief 是子 Agent 隔离执行的启动文档；Source Manifest 是其证据对应物。

## Examples

- GitHub Issue 加上 Agent-specific 标签、完整复现步骤、边界、验收条件，可以视为 Brief 的最小实现。
- `/triage` skill 把一个半成品 issue 转化为可交给 Agent 的 Brief，方法是补标签、补上下文、补验收标准。
- `/deliver-issue` 接受的 issue 如果已经包含足够的 Brief 信息，则子 Agent 可以直接进入 TDD 阶段。

## Common Confusions

- Agent Brief ≠ Prompt：Prompt 是提示模型生成输出的指令，Brief 是任务的持久描述，可以在 Agent 重新启动后重新读取。
- Agent Brief ≠ 详细规格：过度详细的 Brief 会约束 Agent 的实现路径；Brief 应该约束目标和边界，而不是实现步骤。
- 没有验收标准的 Brief 是不完整的：缺少验收标准意味着 Agent 无法判断何时完成，等同于没有停止条件的反馈回路。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — 把 triage 定义为补充 Agent 上下文、写 Agent Brief 和推进状态的阶段。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]] — 展示 triage 状态机，Agent Brief 是 Ready For Agent 泳道的前提。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 描述从 `/to-issue` 到 triage 到 Brief 的完整任务预处理链。

## Relations

- part-of: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — Brief 是工作流编排中任务分发的核心产物。
- prerequisite: [[concepts/Vertical Slice Issue|Vertical Slice Issue]] — Brief 通常是对已拆好的 Vertical Slice Issue 的执行上下文补充。
- enables: [[concepts/反馈工程（Feedback Engineering）|反馈工程（Feedback Engineering）]] — Brief 的验收标准定义了反馈的判断基准。
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — Brief 作为 triage 产物进入 GitHub issue 流转。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

Agent Brief 是把"对话式任务交办"变成"文档式任务合同"的关键升级——让任务可以在没有创建者在场的情况下被任意 Agent 拾取和执行。

## Review Questions

- Agent Brief 和 PRD 的核心区别是什么？
- 好的 Brief 为什么要写出"哪些决策不交给 Agent"？
- 验收标准在 Brief 中的地位是什么？
- triage 阶段如何把半成品 issue 转化为 Brief？

## Open Questions

- Brief 的颗粒度如何权衡：太细会约束实现，太粗会导致偏移。
- 跨 Agent / 跨 session 场景下，Brief 如何版本化管理？
