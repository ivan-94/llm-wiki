---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 8
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-06
---

# Agent 工作流技能编排

## Definition

Agent 工作流技能编排是把 PRD、issue、triage、TDD、review、HAT、PR、merge 等工程阶段封装为可触发、可组合、可交接的 Agent skills。

## Why It Matters

单个 skill 只能解决局部问题；工作流编排决定多个 skill 如何传递产物、状态和验证证据，避免下一位 Agent 只继承摘要。

## Mental Model

Workflow skills 是 Agent 的工程流水线，每个节点有输入、输出、触发条件和停止条件。

## Key Claims

- 轻量 workflow skill 应明确触发词、持续性、输出形态和停止条件。
- setup/triage/to-prd/to-issue/tdd/review/hat/pr 等 skill 形成从想法到交付的链路。
- Source Manifest 是跨 Agent 交接中的关键产物，防止下游只依赖摘要。
- GitHub issue/PR 可以作为 Agent 工作流状态机和证据流转层。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/地图.png|地图]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/地图2.png|地图2]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png|基于 github 的工作流]]

## Relations

- contains: [[concepts/Agent Skills|Agent Skills]]
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：Agent 工作流技能编排的目标是把“怎么协作交付”从口头流程变成可被 Agent 反复执行的状态机。

## Review Questions

- workflow skill 和 helper skill 的边界是什么？
- Source Manifest 为什么是交接产物而不是装饰模板？

## Open Questions

- 还需要区分个人 workflow 和团队 workflow 的最小技能集。
