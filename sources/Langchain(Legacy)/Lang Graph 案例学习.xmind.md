---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Lang Graph 案例学习.xmind"
source_relpath: "Langchain(Legacy)/Lang Graph 案例学习.xmind"
raw_created_at: 2024-05-10T14:48:45+00:00
raw_modified_at: 2024-05-12T14:39:02+00:00
raw_size: 11819511
raw_fingerprint: "size=11819511;birth=2024-05-10T14:48:45+00:00;mtime=2024-05-12T14:39:02+00:00"
raw_snapshot_at: 2026-05-29T22:11:23.525833+00:00
ingested_at: 2026-05-30
status: ingested
---

# Lang Graph 案例学习.xmind

## Source

- Raw file: [Langchain(Legacy)/Lang Graph 案例学习.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Lang%20Graph%20%E6%A1%88%E4%BE%8B%E5%AD%A6%E4%B9%A0.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Lang Graph 案例学习.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-10T14:48:45+00:00`; modified `2024-05-12T14:39:02+00:00`; size `11819511`; snapshot `2026-05-29T22:11:23.525833+00:00`
- Coverage: exported and read 1 sheet, `画布 1`, with 247 topics via `ai-wiki-xmind-ingest`.

## Summary

这份图是 LangGraph 案例集，重点不是解释 LangGraph 的基本 API，而是通过代码生成、多智能体协作、反思/批判、规划执行、RAG 变体和 Web 导航，展示图结构如何承载循环、路由、状态共享、工具调用和人工/模型决策。

## Source Digest

这份 source 把 LangGraph 当成“可显式建模控制流的 Agent runtime”来学习。入口从聊天机器人和代码生成器开始，强调状态对象、生成节点、代码检查节点和反思节点如何形成一个可重试、可纠错的闭环。随后转向 multi-agent：简单协作通过两个专门代理和工具节点轮转完成任务，supervisor 模式把路由决策交给 LLM，层级团队则用子图隔离不同团队状态，再由顶层图编排。

反思相关分支把 `reflection`、`reflexion` 和 critique 放在质量闭环里：模型先生成或执行，再通过批判、修订、工具执行或终止条件决定是否继续。planning agents 分支进一步把任务拆成 plan、execute、replan，展示 LangGraph 不只是链式调用，而是能表达“计划-执行-重规划”的控制系统。Reasoning without Observation 和 LLM compiler 分支则把计划表示成带依赖的步骤，并通过变量替换、任务调度和执行结果回填来提高复杂任务的吞吐。

RAG 分支把 adaptive RAG、Agentic RAG、Corrective RAG 和 Self RAG 放到同一个决策框架里：先判断是否检索，再评估检索结果是否相关，必要时重写问题或改用 Web search，最后再评价生成答案与问题、证据之间的匹配。Web 导航分支则把 LangGraph 延展到浏览器/网页任务，说明图式控制流适合处理需要观察、行动、再观察的任务。整体上，这份图的价值在于把多个 Agent 设计模式都落到“状态 + 节点 + 条件边 + 工具节点 + 终止条件”的实现框架中。

## Key Claims

- explicit: LangGraph 案例可覆盖代码生成反思、多智能体协作、supervisor 编排、层级团队、reflection/reflexion、planning agents、RAG 和 Web 导航等模式。
- explicit: 多智能体场景中，可以为不同领域创建专门代理，再用路由器、supervisor 或层级团队把任务分配给合适成员。
- explicit: 代码生成案例使用 `generate`、`check_code`、`reflect` 等节点和条件边，形成生成、检查、反思、重试或结束的循环。
- explicit: RAG 案例把检索必要性、文档相关性、问题重写、Web search 和答案评估作为图中的决策点。
- inferred: 这份 source 的核心学习价值是把 Agent 模式从抽象名称还原为可执行控制流，适合后续编译到 Agent Runtime、LangGraph、Agent Harness 和 Agentic RAG 等节点。

## External Links

- paper: [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — multi-agent 简单协作分支引用；not verified.
- paper: [Reflexion](https://arxiv.org/abs/2303.11366) — 反射/反思分支引用；not verified.
- tutorial: [LangGraph Agentic RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) — RAG 案例学习入口；not verified.
- paper: [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) — planning agents 分支引用；not verified.
- paper: [ReAct](https://arxiv.org/abs/2210.03629) — Reasoning without Observation 分支中用于对比；not verified.
- paper: [LLMCompiler](https://arxiv.org/abs/2312.04511) — LLM compiler 分支引用；not verified.
- paper: [Agentic RAG related paper](https://arxiv.org/abs/2403.14403) — RAG/Agentic RAG 相关分支引用，标题需后续核验；not verified.
- paper: [WebVoyage](https://arxiv.org/html/2401.13919v3) — Web 导航分支引用；not verified.

## Links

- related: [[concepts/Agent Harness|Agent Harness]] — source 通过工具节点、状态、反思、路由和终止条件补充 Agent 控制面的案例证据（legacy · not verified）。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] — source 展示把 Agent 行为拆成可验证、可重试、可编排流程的工程化方式（legacy · not verified）。
- compiled-entity: [[entities/LangGraph|LangGraph]] — source 是 LangGraph 实体页的 Agentic RAG 案例和 Graph-based Agent 模式证据（legacy · not verified）。
- compiled-concept: [[concepts/Agentic RAG|Agentic RAG]] — source 的 Adaptive/Corrective/Self RAG 和 Agentic RAG 决策图是 Agentic RAG 概念页的直接来源（legacy · not verified）。
- compiled-synthesis: [[synthesis/LangChain 应用模式目录（Legacy）|LangChain 应用模式目录（Legacy）]] — source 提供 LangGraph 特定的 Agent 模式案例（legacy · not verified）。
- related: [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言.xmind]] — LCEL 是 LangGraph 中节点和边的实现基础，两个 source 形成 Runnable 与 Graph 两层（legacy · not verified）。
- related: [[sources/提示语工程:上下文工程/上下文工程.xmind|上下文工程.xmind]] — LangGraph 的状态、检查点和中断恢复是上下文工程"写入"和"隔离"策略的具体实现（legacy · not verified）。

## Maintenance Notes

- No raw files were modified.
- The workbook contains large code snippets; this note preserves the control-flow and design details rather than copying exported code.
- Compile candidates: LangGraph, Agent Runtime, Multi-Agent 编排模式, Agentic RAG, Reflection/Reflexion, Planning Agents, Web Navigation Agent.
