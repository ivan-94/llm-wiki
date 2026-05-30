---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: null
---

# LangChain 应用模式目录（Legacy）

> **全程 Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（2024年），legacy · not verified，API 行为以官方文档为准。

## Thesis

LangChain 提供了一套跨场景的 LLM 应用模式，覆盖 RAG 问答、结构化信息提取、工具调用 Agent、SQL 问答、文本总结、聊天机器人、请求分析和代码理解。这些模式不是孤立的 demo，而是可以按场景组合的可重用控制流模板。

## 模式目录

### 1. RAG 问答
- **基础 RAG**：文档加载 → 分块 → embedding → 向量库 → 检索 → LCEL 生成。
- **带引用 RAG**：返回 source documents，要求模型引用原文 citation，或用工具调用约束引用格式。
- **History-aware RAG**：先用 `create_history_aware_retriever` 改写追问为独立问题，再检索回答。
- **代码理解 RAG**：按语言语义切分、保留文件元数据、MMR 检索和历史感知问答。

### 2. 结构化信息提取
- **Structured Output**：使用工具调用绑定 JSON schema，要求模型输出结构化数据；使用可选字段避免幻觉。
- **打标签（Tagging）**：对文本分类、提取元数据标签，强调清晰 schema 和 few-shot 示例。
- **长文本提取**：三种策略——长上下文模型/分块逐块/RAG 选相关块，各有跨 chunk 事实和幻觉取舍。
- **合成数据生成**：用 few-shot + schema 约束让模型生成结构化样本，用于构建评估数据集。

### 3. 工具调用与 Agent
- **Chain**（固定流程）：绑定工具、解析 tool_calls、路由工具、并行工具调用、try/catch fallback、自纠正重试。
- **Agent**（LLM 决策）：`AgentExecutor` 控制循环，由 LLM 决定工具和调用次数，适合动态不确定任务。

### 4. SQL / CSV 问答
- 自然语言 → SQL 生成 → 执行 → 基于结果回答。
- 关键实践：只读权限、SQL 方言声明、表结构和示例行、few-shot、输出格式约束。
- 大数据库：用 LLM 选相关表，用向量检索候选高基数列值，避免超长 schema prompt。

### 5. 文本总结
- **Stuff**：所有内容塞进一次生成。
- **Map-Reduce**：先对每段独立总结，再合并总结。
- **Refine**：逐段生成，每次在上一个总结基础上细化。

### 6. 聊天机器人
- 使用 `ChatHistory`、`RunnableWithMessageHistory` 维护多轮对话状态。
- 结合历史摘要压缩和 RAG，控制上下文长度并引入知识库支撑。

### 7. 请求分析（Query Analysis）
- Query decomposition、query expansion、HyDE（假设文档嵌入）、路由、step-back 问题、结构化过滤器构造。
- 见 [[concepts/查询分析|查询分析]] 概念页。

### 8. LangGraph Agent 模式（Legacy）
- **代码生成反思**：generate → check_code → reflect → 条件循环。
- **多 Agent 协作**：轮转（round-robin）、supervisor LLM 路由、层级团队子图。
- **Planning Agent**：plan → execute → replan 控制系统。
- **Agentic RAG**：Adaptive RAG、Corrective RAG、Self RAG，见 [[concepts/Agentic RAG|Agentic RAG]]。
- **Web 导航**：observe → act → observe 的浏览器任务。

## Evidence

- [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习.xmind]] — 模式 1-7 的主要证据（legacy · not verified）。
- [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习.xmind]] — 模式 8（LangGraph Agent 模式）的主要证据（legacy · not verified）。

## Implications

- 结构化提取的质量控制（schema 设计、可选字段、few-shot、基准测试）是可以迁移到任何 LLM 框架的通用工程原则。
- History-aware RAG 和聊天机器人结合 RAG 是多轮对话产品的标配，逻辑在框架层面是通用的。
- SQL/CSV 问答的难点在大数据库场景：不在于 SQL 生成，而在于把足够信息放进 prompt 又不超过上下文预算。
- LangGraph 的 Agent 模式展示了"状态 + 节点 + 条件边 + 终止条件"这套语言可以表达大多数 Agent 决策逻辑。

## Related Concepts

- [[concepts/RAG|RAG]]
- [[concepts/查询分析|查询分析]]
- [[concepts/History-aware RAG|History-aware RAG]]
- [[concepts/Agentic RAG|Agentic RAG]]
- [[concepts/LCEL（LangChain Expression Language）|LCEL]]
- [[concepts/Agent 编排图（Graph-based Agent Runtime）|Agent 编排图]]
- [[entities/LangChain|LangChain]]
- [[entities/LangGraph|LangGraph]]

## My Take

LangChain 案例学习的最大价值不是 API 记忆，而是从中抽取"场景 → 控制流 → 质量控制"的模式思维。这些模式大部分可以用其他框架复现；真正持久的是对各场景的工程设计决策的理解。

## Open Questions

- 所有 API 细节均为 legacy · not verified，需要官方文档核验。
- 各应用模式的性能基准（质量、成本、延迟）在当前 wiki 中尚无实测数据。
