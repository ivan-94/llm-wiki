---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 10
---

# LangChain

## What It Is

LangChain 是一组用于构建 LLM 应用、RAG、Agent、Runnable 编排、服务化和观测的框架/生态。当前资料位于 `Langchain(Legacy)`，因此本页把它作为历史学习材料和工具谱系记录，不当作最新产品说明。

## Role In This Wiki

LangChain 在本 wiki 中主要用于理解 LLM 应用工程的早期抽象：LCEL/Runnable、LangGraph 状态图、LangServe 服务化、LangSmith/观测、RAG 案例和 tracing。

## Key Facts

- LCEL 以 Runnable、Sequence、Parallel、Lambda、Config、Fallback、Events 等原语组织 LLM 应用。
- LangGraph 将 LLM 应用扩展为有状态、可循环、多参与者、可 checkpoint 的图式运行时。
- LangServe 把 Runnable 服务化并支持 RemoteRunnable。
- LangSmith、Phoenix、Langfuse 在 raw 中作为 tracing/observability 选项出现，但能力细节未核验。

## Related Concepts

- implemented-by: [[concepts/RAG|RAG]]
- related-source: [[sources/Langchain(Legacy)/Langchain.xmind|Langchain.xmind]]
- related-source: [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]]
- related-source: [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言]]
- used-in: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## Evidence

- [[sources/Langchain(Legacy)/Langchain.xmind|Langchain.xmind]]
- [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言]]
- [[sources/Langchain(Legacy)/LangGraph.xmind|LangGraph.xmind]]
- [[sources/Langchain(Legacy)/LangServe.xmind|LangServe.xmind]]
- [[sources/Langchain(Legacy)/跟踪和监控.xmind|跟踪和监控]]

## Open Questions

- `Langchain(Legacy)` 资料的版本状态和当前 LangChain/LangGraph API 需要后续联网核验。
