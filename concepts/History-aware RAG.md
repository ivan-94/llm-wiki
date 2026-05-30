---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# History-aware RAG

## Definition

History-aware RAG 是在多轮对话场景中，把依赖聊天历史的追问先改写为独立可检索的问题，再执行标准 RAG 流程的扩展架构。它解决了"追问语境缺失导致检索失败"的问题。

## Why It Matters

用户在多轮对话中的追问往往省略了上下文，例如"那它的价格呢"依赖前一轮的主题才能理解。直接向量化这类追问无法找到相关文档；History-aware RAG 先用 LLM 还原完整问题，再检索，从而保证多轮 RAG 的连贯性。

## Mental Model

把多轮对话中的追问想象成速记符号：阅读者（检索系统）看不懂，需要一个上下文翻译器（History-aware 改写步骤）先把速记还原成完整句子，再交给检索系统。

## Key Claims

- explicit（来自 Langchain 案例学习.xmind）：带历史消息的 RAG 需要先把依赖聊天上下文的追问改写成独立问题，再执行检索和回答。
- explicit（来自 Langchain 案例学习.xmind）：LangChain 提供 `create_history_aware_retriever` 把聊天历史和当前问题合并后改写，`create_retrieval_chain` 和 `create_stuff_documents_chain` 负责后续检索和回答。
- inferred：History-aware RAG 在改写步骤会引入一次额外的 LLM 调用，增加延迟，但对多轮对话的检索质量提升显著。

## Examples

- 对话历史：用户问"介绍一下 LangGraph"→ 助手回答 → 用户追问"那它和 LCEL 的区别是什么"
  - 无 History-aware：直接检索"那它和 LCEL 的区别是什么"，可能无法命中。
  - History-aware：先改写为"LangGraph 和 LCEL 的区别是什么"，再检索，召回显著改善。
- LangChain 实现：`create_history_aware_retriever(llm, retriever, contextualize_q_prompt)` 接收 messages 和 input，输出独立问题后检索。

## Common Confusions

- History-aware RAG 是对查询改写，不是对检索结果重排。
- 它不等于把整个对话历史塞进检索查询；而是用 LLM 生成一个"不依赖上下文也能理解"的问题。
- 改写质量取决于 LLM 的理解能力，改写提示语也需要迭代优化。

## Evidence

- explicit: [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习.xmind]] — 详细描述 History-aware RAG 流程和 LangChain 实现（legacy · not verified，API 行为以官方文档为准）。

## Relations

- part-of: [[concepts/RAG|RAG]]
- prerequisite: [[concepts/查询分析|查询分析]]
- related-source: [[sources/Langchain(Legacy)/Langchain 案例学习.xmind|Langchain 案例学习.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

History-aware RAG 是多轮对话系统的 RAG 标配：追问语境丢失会让检索系统失去方向，改写步骤是最简单的修复手段。

## Review Questions

- History-aware RAG 和普通 RAG 在流程上有什么区别？
- 为什么把追问直接发给检索系统会失败？
- `create_history_aware_retriever` 接收什么输入，输出什么？

## Open Questions

- 改写步骤的 prompt 设计对多语言追问的鲁棒性需要测试。
- LangChain 的相关 API 在新版本中可能有变化（legacy · not verified）。
