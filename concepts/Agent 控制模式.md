---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 3
difficulty: 3
review_after: 2026-06-06
---

# Agent 控制模式

## Definition

Agent 控制模式是指在 LLM 应用中如何安排「谁决定下一步」的一组结构化模式，从代码预写的固定路径，到由模型动态拆解、委派和自我优化的强自主结构，按控制权强弱排成谱系。

## Why It Matters

大多数「Agent 项目」的复杂度和成本，不来自模型本身，而来自选错了控制结构：简单线性任务套上动态 Agent Loop 会浪费 token 和稳定性，复杂开放任务硬塞进固定 workflow 又会脆。控制模式提供一张选型谱系，帮助按任务形态决定该给模型多少决策权。

## Mental Model

把控制权想成一根滑杆：左端是代码写死每一步（workflow），右端是模型自己决定每一步（autonomous agent）。五类模式是滑杆上的刻度，越往右越灵活也越贵越难验证。

## Key Claims

- `Agent 解构.xmind` 给出从弱到强的五类控制模式：Prompt Chaining（线性变换）、Routing（输入分流）、Parallelization（分段或投票）、Orchestrator-Workers（动态拆解委派）、Evaluator-Optimizer（带反馈的质量优化）。
- 这五类模式对应不同任务形态，选型应先看任务是线性、分流、可并行、需动态拆解还是需迭代优化，而不是默认上最强模式。
- `Agent_副本.xmind` 的早期设计模式（Reflection、Tool Use、Planning、Multi-agent Collaboration）是同一谱系的早期表达：Reflection 对应 Evaluator-Optimizer，Planning 对应 Orchestrator-Workers。
- 控制模式可以组合嵌套：一个 Orchestrator 内部的 worker 仍可以是 Routing 或 Prompt Chaining。

## Examples

- Prompt Chaining：把「抽取要点 → 翻译 → 校对」串成固定三步链。
- Routing：根据查询意图把请求分流到不同知识库或模型规模（参见闪极 `sys1_command` 按难度分发模型）。
- Orchestrator-Workers：主 Agent 把复杂功能拆成子任务并委派子代理（见 [[concepts/子代理委派模式|子代理委派模式]]）。
- Evaluator-Optimizer：模型先产草稿，再由自身或另一个 Agent 评分并迭代（即 Reflection / code review 类比）。

## Common Confusions

- 控制模式不等于「Agent vs workflow」二选一；它是连续谱系，多数真实系统是混合结构（见 [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]]）。
- 更强的控制模式不等于更好结果；Evaluator-Optimizer 在简单任务上只会增加成本。
- Parallelization 既可以是「分段并行」也可以是「多次投票取共识」，两者目的不同。

## Evidence

- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- [[sources/Agent/Agent_副本.xmind|Agent_副本.xmind]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- contrasts-with: [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]]
- enables: [[concepts/多 Agent 协作协议|多 Agent 协作协议]]
- enables: [[concepts/子代理委派模式|子代理委派模式]]
- related-source: [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：先判断任务形态，再决定给模型多少决策权；五类模式是从「代码控制」到「模型控制」之间的刻度，可以嵌套组合。

## Review Questions

- 五类控制模式按控制权强弱排序是怎样的？
- Orchestrator-Workers 和 Routing 的关键差异是什么？
- 为什么不应该对所有任务都用最强的 Evaluator-Optimizer？

## Open Questions

- 各模式在真实任务上的成本/质量权衡缺少量化对比数据。
