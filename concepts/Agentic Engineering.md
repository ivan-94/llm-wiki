---
page_type: concept
updated_at: 2026-06-11
status: active
source_count: 8
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Agentic Engineering

## Definition

Agentic Engineering 是把 coding agent 当作强执行体来设计、约束、观察和验收的软件工程实践。

## Why It Matters

当 Agent 能连续写、跑、改、再试时，工程质量不再只取决于单次提示，而取决于规格、任务边界、工具权限、反馈信号、异常治理、审查和回滚机制。

## Mental Model

Vibe Coding 是加速器，Agentic Engineering 是刹车、仪表盘、护栏和维修手册。

## Three Governance Types

根据年中总结的实践归纳，Agentic Engineering 的治理可分为三类：

- **静态治理**：定期扫描和重构 Agent 快速产出的低质量代码；不能靠 AI 自己清理自己制造的混乱。
- **动态治理**：通过生产异常监控（Sentry/异常治理闭环）、GitHub Issue、修复 PR 和审核上线等链路支持严肃生产系统。
- **上下文治理（Harness 工程）**：避免 AGENTS.md、Skills 和协作上下文膨胀导致生成效果下降；目标是让 Agent 以更精准的上下文工作，而不是更多上下文。

## Software 3.0 Control Surface

Agentic Engineering 的控制面可以分成五类：

- intent control: 人类定义目标、非目标、成功指标和风险边界。
- semantic control: spec、examples、领域语言、状态机和业务规则固定系统含义。
- decision control: 标出哪些产品、安全、架构、数据和错误处理决策不能交给 Agent 静默补全。
- execution control: 用 worktree、runtime、tools、MCP、skills、hooks、tests 和 logs 让 Agent 可运行、可观察、可回滚。
- evidence control: 用 CI、HAT、browser evidence、review、Source Manifest 和反捷径测试证明完成质量。

## Key Claims

- Agentic Engineering 不否定 Vibe Coding，而是给它补上责任边界、反馈闭环和长期可维护性。
- 人的工程化能力不会完全消失，而是被部分内化到工具、规则、skills、测试和流程中。
- Agentic Engineering 的关键资产包括 spec、AGENTS/CLAUDE 入口、可执行测试、HAT、日志、review、handoff 和运行时隔离。
- 对复杂系统，工程师的价值更集中在目标设定、系统建模、风险判断和验收标准，而不是逐行键入代码。
- Agentic Engineering 的关键不是“多 Agent”，而是让 Agent 的每个动作有来源、边界、反馈和可交接证据。
- 失败不应只被修掉；高频失败应该被回写成规则、skill、hook、测试、模板或文档入口，使系统下限持续抬升。
- Anthropic AI 研发自动化 source 补充：AI 执行成本下降后，工程师价值进一步迁移到任务 steering、实验设计、结果可信度判断、审查和治理协调。

## Eight Maturity Levels Alignment

与 Vibe Coding 工程化深度模型的成熟度层级对应：

1. Prompt draft → 粗稿生成（纯 Vibe）
2. Spec slice → 有边界的任务切片
3. Harnessed loop → 测试/lint/日志/hooks 反馈闭环
4. Agentic delivery → PRD/issue/worktree/HAT 可交接闭环
5. Continuous alignment → 失败自动回写为规则和工具（L5 Learning）

静态/动态/上下文三类治理分别对应成熟度 3-5 层的不同治理面。

## Definition Of Done

严肃 Agentic Engineering 的完成定义至少包含：

- behavior done: 用户可见行为符合 spec 和 examples。
- decision done: 关键产品/架构/安全决策已上浮并记录。
- evidence done: 测试、HAT、review 或运行证据能覆盖正例、反例和关键边界。
- handoff done: Source Manifest、log、PR/HAT 产物足以让下游 Agent 或人类重读和复核。
- learning done: 本次失败、约束或新经验已回写到长期知识入口。

## Examples

- Claude Code 的 SubAgent、Agent Teams 和 dynamic workflow 是 Agentic Engineering 的编排工具例子。
- `Agent Game` 和 `Karpathy LLM Wiki` 把文件系统当作 Agent 可读写状态层。
- `异常治理闭环`：Sentry Issue → Agent 生成修复 PR → 验证上线 → 关闭 Issue（动态治理典型案例）。
- 静态治理：定期跑架构扫描脚本，找出 Agent 快速生成但结构不佳的模块并重构。

## Common Confusions

- Agentic Engineering 不是“多开几个 Agent”，而是让 Agent 的工作能被解释、复现、审查和验收。
- 自动化越多，越需要明确权限、状态和停止条件。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]]
- [[sources/Vibe/Vibe Coding 随手记/杂记/人的工程化能力都会被内化掉.xmind|人的工程化能力都会被内化掉]]
- [[sources/Vibe/Vibe Coding 随手记/杂记/AI 时代工程师的修炼和跃升.xmind|AI 时代工程师的修炼和跃升]]
- [[sources/Vibe/Vibe Coding 随手记/文件系统/Agent Game.xmind|Agent Game]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/异常治理.xmind|异常治理]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]]
- [[human/sources/inbox/cook-blog/2026-06-05_当 AI 开始构建自己_Anthropic|当 AI 开始构建自己]] — human source，补充 AI 研发自动化和人类瓶颈迁移证据。

## Relations

- builds-on: [[concepts/Vibe Coding|Vibe Coding]]
- uses: [[concepts/Agent Harness|Agent Harness]]
- uses: [[concepts/Agent Skills|Agent Skills]]
- contains: [[concepts/异常治理闭环|异常治理闭环]] — 动态治理的核心实现
- contains: [[concepts/Agent Coding Guardrails|Agent Coding Guardrails]] — 上下文治理的行为约束
- enables: [[concepts/软件工厂陷阱|软件工厂陷阱]] — 走出陷阱的工程化路径
- used-in: [[synthesis/Vibe Coding 与 Agentic Engineering|Vibe Coding 与 Agentic Engineering]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Agentic Engineering 是把 Agent 从“能帮忙写代码的工具”提升为“需要工程系统承载的协作者”。

## Review Questions

- Agentic Engineering 要补齐 Vibe Coding 的哪些短板？
- 为什么文件系统可以成为 Agent 状态层？
- 多 Agent 协作最需要哪些交接合同？

## Open Questions

- Agentic Engineering 和传统平台工程、DevOps 的边界还需要更多案例拆分。
