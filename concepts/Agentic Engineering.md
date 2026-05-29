---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 7
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

## Control Surface

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
- `异常治理.xmind` 将线上异常上下文、可观测性和 agent 可消费报告连接起来。

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

## Relations

- builds-on: [[concepts/Vibe Coding|Vibe Coding]]
- uses: [[concepts/Agent Harness|Agent Harness]]
- uses: [[concepts/Agent Skills|Agent Skills]]
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
