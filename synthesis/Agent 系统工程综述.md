---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 22
learning_status: learning
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# Agent 系统工程综述

## Thesis

Agent 系统工程的主线是把一个会推理的模型放进可执行、可观察、可恢复、可学习的运行系统。模型能力只是内核；真正决定可靠性的，是工具接口、上下文、记忆、沙箱、状态、评估和多 Agent 协议。

## System Layers

| 层 | 核心问题 | 代表资料 |
| --- | --- | --- |
| Agent Loop | 感知、决策、行动、反馈如何闭合 | `Agent 解构.xmind` |
| Context | 什么信息在什么时机进入模型 | `Agent 解构.xmind`, `智能体工程的 8 个等级.xmind` |
| Tools | Agent 如何行动，工具如何低歧义可验证 | `工具调用.xmind`, `MCP.xmind`, `Build CLI For Agent.xmind` |
| Memory | 状态、事实、经历、程序性规则如何跨 session 保留 | `记忆.xmind`, `长记忆.xmind` |
| Sandbox | Agent 行动如何隔离、限权、审计、回收 | `沙箱.xmind`, `沙箱PRD.md` |
| Orchestration | 单 Agent、workflow、多 Agent 如何划分控制权 | `多智能体.xmind`, `LangGraph.xmind` |
| Evaluation | 如何证明工具、prompt、Agent 任务完成质量 | `提示词评估方案设计.xmind`, `LLM 评估.xmind` |

## Key Judgments

- Agent 不是模型功能清单，而是运行系统；系统边界决定可靠性上限。
- 工具设计、上下文工程和记忆系统是 Agent 行为的“隐形 prompt”。
- 沙箱和运行时是让 Agent 从建议者变成执行者的必要边界。
- 多 Agent 编排只有在状态、任务、依赖和交接协议清晰时才有收益。
- Legacy LangChain/LangGraph 资料虽然可能过时，但仍提供有状态运行时、Runnable、checkpoint、stream events 和 observability 的历史抽象。

## Evidence

- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- [[sources/Agent/工具调用.xmind|工具调用.xmind]]
- [[sources/Agent/MCP.xmind|MCP.xmind]]
- [[sources/Agent/Build CLI For Agent.xmind|Build CLI For Agent.xmind]]
- [[sources/Agent/智能体工程的 8 个等级.xmind|智能体工程的 8 个等级]]
- [[sources/Agent/记忆.xmind|记忆.xmind]]
- [[sources/Agent/沙箱.xmind|沙箱.xmind]]
- [[sources/Agent/提示词评估方案设计.xmind|提示词评估方案设计.xmind]]
- [[sources/提示语工程:上下文工程/LLM 评估.xmind|LLM 评估.xmind]]
- [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]]
- [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言]]
- [[sources/Agent/闪极智能体/闪极智能体.xmind|闪极智能体.xmind]]

## Implications

- 建 Agent 项目时，不应先问“用哪个模型”，而应先问任务是否需要工具、记忆、沙箱、评估和运行时持久化。
- 工具/API 暴露给 Agent 前，应做工具评估和返回结构设计。
- 长任务或高风险任务必须有 checkpoint、日志、回滚和可交接 artifacts。
- 如果一个 Agent 失败重复出现，就应沉淀为 rule、hook、skill、test 或 runtime 约束。

## Related Concepts

- [[concepts/AI Agent|AI Agent]]
- [[concepts/Agent 工具调用|Agent 工具调用]]
- [[concepts/Agent 记忆|Agent 记忆]]
- [[concepts/Agent 沙箱|Agent 沙箱]]
- [[concepts/Agent Harness|Agent Harness]]
- [[entities/Model Context Protocol|Model Context Protocol]]

## My Take

这批 Agent 资料的核心价值，是把 Agent 从“模型会不会自主”转成“系统是否让自主行为可控”。这比工具列表更重要，也更适合作为后续 Vibe/Agentic Engineering 学习主线。

## Open Questions

- LangChain legacy 资料中的 API 和产品能力需要核验当前事实。
- OpenClaw、Hermes、Nano Bot、闪极智能体等候选实体需要更多上下文后再决定是否建独立实体页。
