---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-13
---

# Agent 编排图（Graph-based Agent Runtime）

> **Legacy 警告**：本页内容基于 LangGraph.xmind（2024年），legacy · not verified，API 行为以官方文档为准。

## Definition

Agent 编排图是以图（Graph）结构表达 Agent 控制流的运行时架构：节点是可执行单元（LLM 调用、工具、条件判断），边是节点间的转移关系（固定边或条件边），图式结构支持有状态、可循环、可恢复的复杂 Agent 执行。

## Why It Matters

线性 chain 和 DAG 无法表达 Agent 的循环重试、动态分支、多参与者协作和长任务中断恢复等需求。图式运行时把控制流变成一等公民，让 Agent 的状态管理、检查点和中断机制可以显式建模。

## Mental Model

把 Agent 编排图想象成有记忆的状态机：节点执行改变状态，边决定下一步去哪，checkpoint 把状态持久化，让任务可以"暂停-恢复"而不是从头再来。

## Key Claims

- explicit（来自 LangGraph.xmind）：LangGraph 扩展 LangChain 表达式语言，用于构建有状态、多参与者、可循环的 LLM 应用。
- explicit（来自 LangGraph.xmind）：`StateGraph` 通过状态和 channel 合并规则在节点之间共享并更新状态，类似 Redux reducer。
- explicit（来自 LangGraph.xmind）：Checkpoint 支持状态持久化、中断恢复、时间旅行、多轮记忆和长时间运行代理的弹性。
- explicit（来自 LangGraph.xmind）：条件边让图在运行时根据状态选择下一个节点，支持动态控制流。
- explicit（来自 LangGraph.xmind）：stream events 可监听中间模型输出和工具执行事件，而不只等待最终结果。
- explicit（来自 Lang Graph 案例学习.xmind）：LangGraph 支持的模式包括代码生成反思、多智能体协作、supervisor 编排、层级团队、RAG 变体和 Web 导航。
- inferred：图式 Agent 运行时的底层逻辑接近 Pregel 迭代图计算模型，每一步是节点输出 + 全局状态更新。

## Examples

- 代码生成反思图：`generate` → `check_code` → `reflect` → 条件边（通过则结束，不通过则回到 `generate`）。
- Supervisor 模式：LLM supervisor 节点根据当前状态选择下一个 worker agent 执行。
- Human-in-the-loop：在特定节点前插入 `interrupt` 机制，等待人工确认后再继续执行。
- 时间旅行：通过 checkpoint 回退到之前某个状态重新执行，用于调试或撤销操作。

## Common Confusions

- 图式运行时不等于多 Agent 协作；单 Agent 的循环重试也可以用图表达。
- LangGraph 的"图"不是可视化 DAG 图，而是带状态的执行图，节点可以循环执行。
- Checkpoint 是运行时机制，不是数据备份；它存储的是 Agent 的执行状态，而不是业务数据。

## Evidence

- explicit: [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]] — 主要证据，详细记录 StateGraph、checkpoint、stream events 和控制流。
- explicit: [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习.xmind]] — 提供多种 Agent 模式在 LangGraph 上的具体实现案例。

## Relations

- implemented-by: [[entities/LangGraph|LangGraph]] （legacy · not verified）
- contrasts-with: [[concepts/LCEL（LangChain Expression Language）|LCEL]] （LCEL 适合简单无环流程，图式运行时适合循环和复杂状态管理）
- enables: [[concepts/Agentic RAG|Agentic RAG]]
- used-in: [[synthesis/LangChain 应用模式目录（Legacy）|LangChain 应用模式目录（Legacy）]]
- related-source: [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

图式 Agent 运行时解决的是"如何让 Agent 控制流变得可维护"。把节点、边、状态和 checkpoint 显式建模后，复杂 Agent 的行为就不再是黑箱，而是可以检查、暂停、恢复和调试的执行图。

## Review Questions

- `StateGraph` 和普通 Graph 的区别是什么？
- Checkpoint 支持哪些能力？
- 条件边如何实现 Agent 的动态路由？

## Open Questions

- LangGraph 的生产稳定性和 API 演变（legacy · not verified，需要官方文档核验）。
- 图式运行时的调试工具和 trace 可视化在 LangGraph 中的实现细节。
