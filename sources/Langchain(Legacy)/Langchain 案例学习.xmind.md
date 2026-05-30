---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Langchain 案例学习.xmind"
source_relpath: "Langchain(Legacy)/Langchain 案例学习.xmind"
raw_created_at: 2024-05-01T08:20:35+00:00
raw_modified_at: 2024-05-03T11:43:44+00:00
raw_size: 1823244
raw_fingerprint: "size=1823244;birth=2024-05-01T08:20:35+00:00;mtime=2024-05-03T11:43:44+00:00"
raw_snapshot_at: 2026-05-29T22:11:26.440079+00:00
ingested_at: 2026-05-30
status: ingested
---

# Langchain 案例学习.xmind

## Source

- Raw file: [Langchain(Legacy)/Langchain 案例学习.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Langchain%20%E6%A1%88%E4%BE%8B%E5%AD%A6%E4%B9%A0.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Langchain 案例学习.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-01T08:20:35+00:00`; modified `2024-05-03T11:43:44+00:00`; size `1823244`; snapshot `2026-05-29T22:11:26.440079+00:00`
- Coverage: exported and digested 1 sheet: `括号图` (407 topics).

## Summary

这份图用一组 LangChain 场景把组件落到实践：RAG 问答、带引用回答、结构化信息提取、工具调用与 Agent、SQL/CSV 问答、总结、聊天机器人、请求分析/优化、打标签、合成数据生成、代码理解。它更像一份“应用模式目录”，重点在场景、链路、质量控制和错误处理。

## Source Digest

RAG 分支给出最完整的端到端路径：WebBaseLoader 加载网页，RecursiveCharacterTextSplitter 分块，Chroma + OpenAIEmbeddings 存储，retriever 检索，hub prompt + LCEL 生成答案。它进一步扩展到带历史消息的 RAG：先用 create_history_aware_retriever 将用户追问改写成独立问题，再用 create_retrieval_chain 和 create_stuff_documents_chain 把检索上下文与聊天历史送入回答链。source 还强调返回 source documents、引用 citation、工具调用约束引用、XML 输出解析和后处理压缩等证据回传方式。

结构化提取和打标签分支强调质量控制：工具调用通常效果最好；JSON mode 仍需提示语约束；schema 和字段文档要清晰；可选字段避免强迫模型编造；few-shot 可包含正例和反例；大 schema 可拆分；需要基准测试、验证或纠错步骤。长文本提取则有三种策略：长上下文模型、分块逐块提取、RAG 检索相关块，每种都在跨 chunk 事实、重复提取和幻觉方面有取舍。

工具调用和 Agent 分支区分 chain 与 agent：chain 适合固定流程，可以绑定工具、解析 tool_calls、路由工具、并行工具调用、try/catch、fallback 和自纠正重试；agent 适合由 LLM 决定工具和调用次数，并由 AgentExecutor 控制循环。SQL & CSV 分支把数据库问答拆成自然语言转 SQL、执行 SQL、基于结果回答三步，并强调只读权限、表结构/示例行、few-shot、请求验证、大数据库表筛选和高基数列检索。

后半部分覆盖文本总结、聊天机器人、请求分析和代码理解。总结模式包括 stuff、map-reduce、refine；聊天机器人用 ChatHistory、RunnableWithMessageHistory、历史压缩和 RAG 保持会话连续；请求分析把用户问题转换成结构化查询、多个子查询、路由、过滤器、HyDE、query expansion 和 step-back 问题；代码理解强调按语言语义切分、保留文件元数据、MMR 检索和历史感知问答。

## Key Claims

- explicit: RAG 的核心流程包括 indexing、retrieval and generation，两阶段分别负责数据索引和把相关上下文送入模型回答。
- explicit: 带历史消息的 RAG 需要先把依赖聊天上下文的追问改写成独立问题，再执行检索和回答。
- explicit: 结构化信息提取中，清晰 schema、可选字段、示例、基准测试、拆分大型 schema、验证或纠正步骤都能提升质量。
- explicit: Chain 适合预定义工具流程，Agent 适合让 LLM 决定调用哪些工具和调用次数。
- explicit: SQL 问答需要限制权限、提供 SQL 方言、表结构、必要示例行、输出格式，并避免查询不必要字段。
- explicit: 大数据库问答的难点是把相关表、相关高基数列值和必要 schema 放入 prompt，可用 LLM 选表和向量检索候选值。
- explicit: 请求分析可用于 query decomposition、query expansion、HyDE、路由、step-back 问题和结构化过滤器构造。
- inferred: 这份 source 适合沉淀为 LangChain 应用模式综合页，而不是只编译为单个 LangChain 实体页。

## External Links

- article-source: [Lilian Weng agent article](https://lilianweng.github.io/posts/2023-06-23-agent/) — RAG 示例中用作网页加载和问答的数据源；not verified.
- prompt-hub: [OpenAI tools agent prompt](https://smith.langchain.com/hub/hwchase17/openai-tools-agent) — 聊天机器人工具使用分支引用的 LangChain Hub prompt；not verified.

## Links

- related: [[sources/Agent/LangChain.xmind|Agent/LangChain.xmind]] — 现有 source 提供 LangChain 总览背景，本 source 提供案例层证据（legacy · not verified）。
- related: [[concepts/提示语工程|提示语工程]] — 结构化提取、few-shot、SQL prompt 和请求分析都可补充提示语工程实践（legacy · not verified）。
- related: [[concepts/上下文工程|上下文工程]] — RAG、聊天历史、请求重写、长文本提取、代码理解均是上下文构造策略（legacy · not verified）。
- compiled-synthesis: [[synthesis/LangChain 应用模式目录（Legacy）|LangChain 应用模式目录（Legacy）]] — source 是 RAG/Agent/SQL/提取/请求分析模式目录的核心证据（legacy · not verified）。
- related: [[sources/Langchain(Legacy)/Langchain  组件.xmind|Langchain 组件.xmind]] — 案例 source 与组件 source 形成"设计模式 ↔ 实现组件"对照关系（legacy · not verified）.

## Maintenance Notes

- No raw files were modified.
- External links were extracted from the XMind export and were not browsed or verified.
- Batch instruction prohibited index/log/concepts/maps/synthesis updates; this note records source-only ingest.
- Compile candidates: LangChain 应用模式, RAG, History-aware RAG, citation RAG, structured extraction, tool calling, AgentExecutor, SQL agent, query analysis, HyDE, step-back prompting, code understanding.
