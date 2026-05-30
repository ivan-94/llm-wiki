---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 18
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Vibe Coding 与 Agentic Engineering

## Thesis

Vibe Coding 是 AI Coding 的生产力入口，Agentic Engineering 是让这种生产力进入严肃软件交付的工程化层。更深一层看，二者的分界不是“快 vs 慢”，而是“让 Agent 在未定义空间里自动补全”与“把未定义空间压缩为规格、决策边界和证据闭环”。

## Comparison

| 维度 | Vibe Coding | Agentic Engineering |
| --- | --- | --- |
| 核心动作 | 用自然语言驱动 Agent 生成和迭代 | 设计 Agent 的工作系统、边界和反馈闭环 |
| 主要收益 | 快速原型、快速探索、降低创造门槛 | 降低漂移、减少返工、可审计可验收 |
| 主要风险 | 需求补全、短视优化、隐式决策、只看最终 diff | 流程过重、编排成本、工具和状态复杂 |
| 关键资产 | prompt、上下文、任务说明、初步测试 | spec、harness、skills、worktree、HAT、日志、review |
| 人的角色 | 提供意图、审查结果、精修 | 设计系统、分配责任、定义验收、治理风险 |

## Transition Logic

Vibe Coding 在小任务里有效，是因为任务复杂度和上下文规模仍在模型 sweet spot 内：一个 prompt 可以描述目标、约束和主要边界，人工审查也能覆盖风险。任务变大后，问题不再是“模型是否会写代码”，而是自然语言 spec 稀疏、语义空间高维、决策具有分形特征，Agent 会在每个未说明处补全产品/架构/安全判断。

Agentic Engineering 的作用就是把这种自动补全变成可控流程：目标层由人决定，语义层和边界层强治理，设计层按风险过滤，实现层才默认交给 Agent。这个分层把“让 AI 多写”变成“让 AI 在正确的决策分辨率下写”。

## Control Boundary

- Vibe layer: 描述意图、生成草稿、探索方案、快速验证方向。
- Spec layer: 把目标、用户价值、FR/SC、examples、NFR 和非目标写成可追踪工件。
- Decision layer: 标出权限、状态、错误、数据、安全、架构、迁移等不可静默补全的决策。
- Harness layer: 用 worktree、tools、hooks、tests、browser、runtime、logs 和 skills 管理执行。
- Evidence layer: 用 CI、HAT、review、反例、Source Manifest 和运行 artifacts 证明完成。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]] 明确把 Vibe Coding 定位为生产力入口，把 Agentic Engineering 定位为可审计、可验证、可持续交付的工程化层。
- [[sources/Vibe/方法论.xmind|方法论.xmind]] 将意图、规格、上下文工程、测试和 SOP 组织成 Vibe Coding 方法论。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]] 解释大需求失败来自稀疏 spec、未定义空间和决策权泄漏。
- [[sources/Vibe/Vibe Coding 随手记/杂记/软件开发本身的复杂性.png|软件开发本身的复杂性]] 提醒软件复杂性不仅是代码生成问题，还包括协作、领域、数据、演进和责任。
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]] 和 [[sources/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind|Agent Harness Engineering]] 提供从工具能力到控制面设计的证据。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Vibe Coding 的 Sweet Spot：从粗生成到精修.xmind|Vibe Coding 的 Sweet Spot]] 支撑任务粒度、状态外置、会话隔离和强验证循环。
- [[sources/Vibe/软件工程基础/Specification by Example/5 落地和反模式.png|5 落地和反模式]] 支撑示例化验收不能退化成 QA 单独写测试脚本。

## Productize First, Then Engineer (先产品化后工程化)

一个健康的 AI 产品演进路径：

1. **Vibe 探索期**：用 Vibe Coding 快速验证方向和用户价值，容忍高自由度、低治理密度。
2. **MVP 稳定期**：用户验证成功后，开始引入 spec artifact、测试和决策边界，但不需要完整 Agentic Engineering。
3. **工程化期**：产品复杂度超过单人单 session 可控范围后，全面切换到 Agentic Engineering：harness、worktree、CONTEXT.md、SbE、HAT、CI 闭环。
4. **持续对齐期**：L5 Learning 层激活，失败棘轮化为规则和工具，系统能力持续提升。

原则：**不要在探索期引入工程化负担，也不要在交付期停留在 Vibe 模式**。过早工程化阻碍探索；过晚工程化导致技术债以 Agent 可见但不可控的形式累积。

## AI Native Organization Dimension (AI Native 组织维度)

AI Native 组织不只是"用了 AI 工具"，而是在组织层面重新分配了认知劳动：

- 工程师的核心能力迁移：从"写代码"→ "设计可验收的工作系统"（spec、harness、evidence、guardrail）。
- 团队分工重组：传统 BA/Dev/QA 三角 → Three Amigos 的 AI 时代版（产品/工程/AI Agent 协作者）。
- 知识沉淀方式变化：口头传递 + 文档 → AGENTS.md/CONTEXT.md/skill/工程宪法 的机器可读形式。
- 速度瓶颈迁移：代码生成速度不再是瓶颈 → 目标设定、审查、验收和知识回写成为新的限速因素。

## Implications

- 原型期可以偏 Vibe Coding，交付期必须向 Agentic Engineering 收敛。
- 大需求不应只增加 prompt 长度，而应拆出规格、任务边界、测试、验收和状态回写。
- 多 Agent 并行不是目的；如果没有 Source Manifest、工作区隔离和合并策略，编排本身会变成新的风险。
- 工程师能力不会简单消失，会转化为 harness、skills、测试策略、架构边界和验收标准。
- “更详细的 prompt”不是规模化方案；规模化方案是更清楚的决策分辨率、更硬的行为证据和更低摩擦的 harness。

## Related Concepts

- [[concepts/Vibe Coding|Vibe Coding]]
- [[concepts/Agentic Engineering|Agentic Engineering]]
- [[concepts/Agent Harness|Agent Harness]]
- [[concepts/Spec-Driven Development|Spec-Driven Development]]
- [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]

## My Take

当前最实用的分界是：当任务只需要探索和粗生成时，用 Vibe Coding；当任务涉及隐性业务规则、跨入口一致性、权限/状态/数据决策、上线验收或长期维护时，必须切到 Agentic Engineering。否则 Agent 会把你没有说清楚的决策写进代码。

## Open Questions

- Agentic Engineering 的最小可行流程还需要按项目类型拆分。
- 编排税和多 Agent 收益之间的平衡缺少更多量化案例。
