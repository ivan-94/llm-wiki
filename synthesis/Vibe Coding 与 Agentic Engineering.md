---
page_type: synthesis
updated_at: 2026-05-29
status: active
source_count: 14
learning_status: learning
confidence: 2
difficulty: 4
review_after: 2026-06-05
---

# Vibe Coding 与 Agentic Engineering

## Thesis

Vibe Coding 是 AI Coding 的生产力入口，Agentic Engineering 是让这种生产力进入严肃软件交付的工程化层。前者强调快速表达和生成，后者强调规格、边界、反馈、观测、验收和责任。

## Comparison

| 维度 | Vibe Coding | Agentic Engineering |
| --- | --- | --- |
| 核心动作 | 用自然语言驱动 Agent 生成和迭代 | 设计 Agent 的工作系统、边界和反馈闭环 |
| 主要收益 | 快速原型、快速探索、降低创造门槛 | 降低漂移、减少返工、可审计可验收 |
| 主要风险 | 需求补全、短视优化、隐式决策、只看最终 diff | 流程过重、编排成本、工具和状态复杂 |
| 关键资产 | prompt、上下文、任务说明、初步测试 | spec、harness、skills、worktree、HAT、日志、review |
| 人的角色 | 提供意图、审查结果、精修 | 设计系统、分配责任、定义验收、治理风险 |

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]] 明确把 Vibe Coding 定位为生产力入口，把 Agentic Engineering 定位为可审计、可验证、可持续交付的工程化层。
- [[sources/Vibe/方法论.xmind|方法论.xmind]] 将意图、规格、上下文工程、测试和 SOP 组织成 Vibe Coding 方法论。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]] 解释大需求失败来自稀疏 spec、未定义空间和决策权泄漏。
- [[sources/Vibe/Vibe Coding 随手记/杂记/软件开发本身的复杂性.png|软件开发本身的复杂性]] 提醒软件复杂性不仅是代码生成问题，还包括协作、领域、数据、演进和责任。
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]] 和 [[sources/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind|Agent Harness Engineering]] 提供从工具能力到控制面设计的证据。

## Implications

- 原型期可以偏 Vibe Coding，交付期必须向 Agentic Engineering 收敛。
- 大需求不应只增加 prompt 长度，而应拆出规格、任务边界、测试、验收和状态回写。
- 多 Agent 并行不是目的；如果没有 Source Manifest、工作区隔离和合并策略，编排本身会变成新的风险。
- 工程师能力不会简单消失，会转化为 harness、skills、测试策略、架构边界和验收标准。

## Related Concepts

- [[concepts/Vibe Coding|Vibe Coding]]
- [[concepts/Agentic Engineering|Agentic Engineering]]
- [[concepts/Agent Harness|Agent Harness]]
- [[concepts/Spec-Driven Development|Spec-Driven Development]]

## My Take

当前最实用的分界是：当任务只需要探索和粗生成时，用 Vibe Coding；当任务需要别人接手、上线、验收或长期维护时，必须切到 Agentic Engineering。

## Open Questions

- Agentic Engineering 的最小可行流程还需要按项目类型拆分。
- 编排税和多 Agent 收益之间的平衡缺少更多量化案例。
