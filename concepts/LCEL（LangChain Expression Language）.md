---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# LCEL（LangChain Expression Language）

> **Legacy 警告**：本页内容基于 `Langchain(Legacy)` 资料（2024年），legacy · not verified，API 行为以官方文档为准。

## Definition

LCEL 是 LangChain 的声明式编排语言，以 Runnable 为基础节点，通过管道语法（`|`）把模型、提示语模板、检索器和解析器组合成可调用、可流式、可配置的工作流。

## Why It Matters

LCEL 把"如何组合 LLM 应用"标准化：任何实现 Runnable 接口的组件都可以用一致的方式组合、流式调用、并行化、fallback 和观测，而不需要每次手写组合逻辑。它是理解 LangChain 应用架构的基础抽象。

## Mental Model

把 LCEL 想象成 Unix 管道：`prompt | model | parser` 就像 `cat file | grep pattern | awk '...'`。每个节点是函数，`|` 是连接符，整个链是可组合的管道。区别在于每个节点还支持流式、并行、配置和 fallback。

## Key Claims

- explicit（来自 Langchain 表达式语言.xmind）：Runnable 是 LangChain 的基础节点，大部分组件包括 ChatModel、LLM、Output Parser 都实现 Runnable 接口。
- explicit（来自 Langchain 表达式语言.xmind）：LCEL 的 `|` 管道语法本质上组合 RunnableSequence，适合把 prompt、model、parser、retriever 串成 chain。
- explicit（来自 Langchain 表达式语言.xmind）：RunnableParallel 将同一输入并行送入多个 Runnable 分支，并返回按 key 组织的字典结果。
- explicit（来自 Langchain 表达式语言.xmind）：RunnableLambda 可承载自定义逻辑，但如果内部直接调用其他 Runnable，需要透传 RunnableConfig 才不丢失回调和上下文。
- explicit（来自 Langchain 表达式语言.xmind）：LCEL 存在循环、中断恢复、human-in-the-loop 和包装实例方法可用性方面的局限，这些是 LangGraph 扩展解决的问题。
- explicit（来自 Langchain 表达式语言.xmind）：`bind` 绑定 Runnable 调用参数，`with_config` 绑定 RunnableConfig，两者语义不同。

## Examples

- 基本 RAG 管道：`setup_and_retrieval | prompt | model | output_parser`。
- 并行执行：`RunnableParallel({"answer": chain_a, "context": chain_b})` 对同一输入并发运行两条链。
- Fallback 链：`primary_chain.with_fallbacks([backup_chain])` 在主链失败时切换到备选。
- 会话历史：`RunnableWithMessageHistory` 把消息历史透明地注入 chain，每次调用自动附加历史。

## Common Confusions

- LCEL 的局限是无自然循环：需要循环执行的 Agent 流程应该用 LangGraph 而不是 LCEL。
- `with_config` 和 `bind` 是不同操作：`with_config` 设置运行时配置（如回调、标签），`bind` 设置 Runnable 的固定参数（如模型参数）。
- 流式体验需要上下游所有节点都支持流，中间节点不支持流会阻断整个流式体验。

## Evidence

- explicit: [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言.xmind]] — 主要证据，详细记录 Runnable 接口、组合原语和高级配置。
- related: [[sources/Langchain(Legacy)/Langchain.xmind|Langchain.xmind]] — 说明 LCEL 在 LangChain Core 中的位置。

## Relations

- part-of: [[entities/LangChain|LangChain]] （legacy · not verified）
- contrasts-with: [[entities/LangGraph|LangGraph]] （LangGraph 扩展 LCEL 以支持有状态循环和 checkpoint）
- enables: [[concepts/Runnable 服务化|Runnable 服务化]] （LCEL 的 Runnable 可通过 LangServe 暴露为服务）
- used-in: [[synthesis/LangChain 应用模式目录（Legacy）|LangChain 应用模式目录（Legacy）]]
- related-source: [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

LCEL 的核心心智模型是"LLM 应用编排代数"：Sequence、Parallel、Assign、Branch、Config、Event 六类原语覆盖了大多数编排模式。理解这六类原语后，大部分 LangChain chain 构建都是组合而不是新发明。

## Review Questions

- RunnableSequence 和 RunnableParallel 的区别是什么？
- 什么时候应该用 LangGraph 而不是 LCEL？
- `bind` 和 `with_config` 分别绑定什么？

## Open Questions

- LangChain 的 API 在 2025-2026 有较大演变，具体 Runnable 接口和参数细节需要官方文档核验（legacy · not verified）。
