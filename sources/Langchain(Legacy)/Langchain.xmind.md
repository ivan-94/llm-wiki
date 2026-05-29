---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Langchain.xmind"
source_relpath: "Langchain(Legacy)/Langchain.xmind"
raw_created_at: 2024-04-23T07:07:05.746190+00:00
raw_modified_at: 2024-05-08T10:39:45.243842+00:00
raw_size: 588530
raw_fingerprint: "size=588530;birth=2024-04-23T07:07:05.746190+00:00;mtime=2024-05-08T10:39:45.243842+00:00"
raw_snapshot_at: 2026-05-29T22:11:27.063880+00:00
ingested_at: 2026-05-30
status: ingested
---

# Langchain.xmind

## Source

- Raw file: [Langchain(Legacy)/Langchain.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Langchain.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Langchain.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-04-23T07:07:05.746190+00:00`; modified `2024-05-08T10:39:45.243842+00:00`; size `588530`; snapshot `2026-05-29T22:11:27.063880+00:00`
- Coverage: exported and digested 1 sheet: `思维导图` (37 topics).

## Summary

这份图是 LangChain 架构速览：LangChain core 提供基础协议与表达式语言，community 提供社区组件，Model I/O、Retrieval、Agent 工具和高级编排策略构成应用层；LangServe 把 chain 暴露成 REST API；LangSmith 用于开发、调试和监控。

## Source Digest

本 source 的信息密度较低，但它提供了 LangChain 生态的上层分层：core 是抽象协议和 LCEL 所在位置，支持流式、异步、并行、跟踪、并发和组合；community 承载模型输入输出、检索、文档加载、文本分割、向量数据库、embedding、retriever 和工具等集成；LangChain 包提供更高级编排策略，包括 chain、agent 和 retrieval strategy。

生态边界也清晰：LangServe 负责将 chain 变成 REST API，LangSmith 负责开发、调试和监控。它适合作为 LangChain 相关 sources 的入口，而不是承载细节的唯一证据。

## Key Claims

- explicit: LangChain core 包含基础抽象协议和 LangChain 表达式语言，是编排的核心。
- explicit: core 支持流、异步、并行执行、跟踪、并发和组合。
- explicit: community 层包含模型输入输出、检索、文档读取、文本分割、向量数据库、Embedding、Retriever 和 Agent 工具等组件。
- explicit: LangChain 上层提供 chain、agent 和 retrieval 策略等更高级编排能力。
- explicit: LangServe 用于将 chain 暴露为 REST API，LangSmith 用于开发、调试和监控。
- inferred: 这份 source 应作为 LangChain 生态总览入口，细节应回到组件、LCEL、案例、监控等 source。

## External Links

No external links found in extracted content.

## Links

- related: [[sources/Agent/LangChain.xmind|Agent/LangChain.xmind]] — 现有 source 与本 source 同属 LangChain 生态总览。
- related: [[concepts/上下文工程|上下文工程]] — source 提到的流、异步、检索、工具、监控和组合都是上下文工程实现面的一部分。

## Maintenance Notes

- No raw files were modified.
- Batch instruction prohibited index/log/concepts/maps/synthesis updates; this note records source-only ingest.
- Compile candidates: LangChain, LangChain Core, LangChain Community, LangServe, LangSmith.
