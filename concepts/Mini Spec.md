---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# Mini Spec

## Definition

Mini Spec 是面向小功能、bug fix 和局部重构的轻量规格文档，用较低成本写清目标、上下文、范围、验收标准和实现草图。

## Why It Matters

不是所有需求都值得走完整 PRD/设计/任务流程，但局部修改仍需要精确上下文和边界，尤其是交给 LLM 执行时。

## Mental Model

Mini Spec 是小切片任务的规格护栏。

## Key Claims

- Mini Spec 适合小团队或个人开发中的局部迭代。
- 它应明确 affected files、关键函数、out of scope、外部输入和验收标准。
- 它与 AGENTS.md/全局记忆互补：Mini Spec 给局部任务边界，全局记忆给项目规则。
- 验收标准可以用 Given/When/Then，也可以用“触发条件 -> 行为 -> 状态变化”。

## Evidence

- [[sources/Vibe/Spec/Mini Spec.xmind|Mini Spec.xmind]]

## Change Request Handling

Mini Spec 的变更请求（change request）处理流程：当需求发生变更时，应基于原始 Mini Spec 提出差量修改说明，而不是重写整个 spec。这样 Agent 可以清楚看到变更前后的边界差异，避免偏移。详见 [[sources/Vibe/Vibe 实践记录.xmind|Vibe 实践记录]]。

## Relations

- part-of: [[concepts/Spec-Driven Development|Spec-Driven Development]]
- depends-on: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]] — Mini Spec 给局部边界，全局记忆给项目规则，二者互补
- reduces-risk: [[concepts/决策权泄漏|决策权泄漏]]
- related-source: [[sources/Vibe/Vibe 实践记录.xmind|Vibe 实践记录]] — 包含变更请求处理的具体实践案例
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Mini Spec 是不想开大流程时，仍然让 Agent 有足够上下文和验收边界的中间形态。

## Review Questions

- Mini Spec 和完整 PRD 的边界在哪里？
- 为什么 Mini Spec 要写 out of scope？

## Open Questions

- 还缺少真实项目里的 Mini Spec 样例。
