---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 18
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Vibe Coding

## Definition

Vibe Coding 是用自然语言表达意图、让 coding agent 生成和迭代代码，再由人通过规格、测试、审查和运行反馈控制结果的软件开发方式。

## Why It Matters

AI 让“写出可运行代码”的成本大幅下降，但也放大了需求漂移、隐式决策、短视修补和集成风险。Vibe Coding 的学习重点不是放任模型生成，而是学会把意图、上下文、约束、验证和责任组织成可重复的工程流程。

## Mental Model

Vibe Coding 像“驾驶一个很快但会自行补全路线的执行体”：人负责目的地、路线边界、检查点和刹车机制，Agent 负责快速探索和执行。

## Deep Structure

Vibe Coding 的核心不是“把代码写法换成自然语言”，而是把开发者的控制点从实现语句迁移到意图、上下文、规格、验证和回写。代码生成越快，未定义空间越危险；自然语言 spec 提供的是稀疏约束，Agent 会自动补全剩余空间，所以必须用 examples、tests、HAT、review 和 harness 把关键语义固定住。

一个更稳的理解是：Vibe Coding 先把任务推进到 60 分粗稿，再通过 spec、decision control、evidence 和 refactor 把它推进到可交付质量。小任务可以停在快速探索层；大任务必须进入 [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] 中的多层控制系统。

## Key Claims

- Vibe Coding 把人的主要工作从逐行实现转向表达目标、组织上下文、设定约束、审查结果和维护反馈闭环。
- 可控的 Vibe Coding 需要规格、任务切片、测试、日志、审查、HAT 和运行证据，而不是只看最终 diff。
- 小规模任务的 sweet spot 在于让 Agent 快速生成粗稿，再由人精修；大型任务需要分层 spec、worktree、子 agent、状态记录和验收门禁。
- 需求偏移的根因往往不是模型不会写代码，而是自然语言 spec 稀疏、未定义空间过大、决策权泄漏和工程价值函数缺失。
- Vibe Coding 提高软件创造下限，但专业工程师的价值转向系统设计、边界判断、风险控制和工程品味。
- Vibe Coding 的完成标准不能只是“能跑”；更强的完成定义包括语义正确、关键决策受控、所有入口路径收敛、测试抗捷径、维护者能继续演进。
- 当任务跨越多个语义边界、数据状态或权限规则时，应先上浮决策分辨率，再让 Agent 执行；否则 Agent 会把产品/架构选择悄悄编码进实现。

## Examples

- `Vibe Coding 的 Sweet Spot` 把粗生成与精修区分开，提醒不要把经验阈值当作硬规则。
- `大型需求的偏移根因与控制` 将大需求失败拆成稀疏 spec、未定义空间、证据过拟合和短视优化。
- `为 Agents 构造并发执行环境` 用 worktree、运行时和任务清单支持多 agent 并行。
- `Vibe 实践记录` 和 `实战.xmind` 将 SOP、上下文工程和验收反馈落到具体操作。

## Failure Signals

- Agent 能快速生成代码，但解释不清哪些需求被它自行假设。
- 测试只覆盖 happy path，没有反例、边界、跨入口规则复用和错误实现也能通过的审查。
- 上下文越来越长，Agent 仍在执行，但核心约束和旧决策开始被稀释。
- 任务被拆成文件或技术模块，而不是 I/O 闭合、语义闭合、可独立验证的行为切片。

## Common Confusions

- Vibe Coding 不是“凭感觉让 AI 随便写”，而是把感觉转成可验证的规格和反馈。
- 快速生成不等于低质量交付；质量取决于测试、审查、验收和上下文管理是否跟上。
- 非工程师可以更快做原型，但复杂系统仍需要架构、协作、数据、运维和责任判断。

## Evidence

- [[sources/Vibe/方法论.xmind|方法论.xmind]] 提供 Vibe Coding、SDD 和上下文工程的总方法论。
- [[sources/Vibe/Vibe Coding.xmind|Vibe Coding.xmind]] 汇总 Vibe Coding 概念、工具和扩展阅读。
- [[sources/Vibe/Vibe Coding 随手记/Vibe Coding 随手记.xmind|Vibe Coding 随手记.xmind]] 汇总随手记中的核心主题。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Vibe Coding 的 Sweet Spot：从粗生成到精修.xmind|Vibe Coding 的 Sweet Spot]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]]
- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]]
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]

## Relations

- enables: [[concepts/Agentic Engineering|Agentic Engineering]]
- enabled-by: [[concepts/Agent Harness|Agent Harness]]
- enabled-by: [[concepts/Spec-Driven Development|Spec-Driven Development]]
- used-in: [[synthesis/Vibe Coding 与 Agentic Engineering|Vibe Coding 与 Agentic Engineering]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

现在的理解：Vibe Coding 是 AI Coding 的生产力入口，但长期价值来自把“让 AI 写”升级成“让 AI 在规格、工具、反馈和验收约束下持续交付”。

## Review Questions

- Vibe Coding 和传统 pair programming 的控制点有什么不同？
- 为什么大需求会在 Agent 自动补全时发生偏移？
- 哪些证据可以说明一次 Vibe Coding 结果是可验收的？
- Vibe Coding 的 sweet spot 为什么不应被当作固定行数规则？

## Open Questions

- 大规模 Vibe Coding 的成本模型还需要更多真实项目数据。
- 不同工具链中哪些 harness 机制最能减少返工，需要后续对比。
