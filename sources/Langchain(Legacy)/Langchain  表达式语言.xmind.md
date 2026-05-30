---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Langchain  表达式语言.xmind"
source_relpath: "Langchain(Legacy)/Langchain  表达式语言.xmind"
raw_created_at: 2024-05-08T10:39:33.156320+00:00
raw_modified_at: 2024-12-11T07:14:38.621629+00:00
raw_size: 663697
raw_fingerprint: "size=663697;birth=2024-05-08T10:39:33.156320+00:00;mtime=2024-12-11T07:14:38.621629+00:00"
raw_snapshot_at: 2026-05-29T22:11:26.662719+00:00
ingested_at: 2026-05-30
status: ingested
---

# Langchain  表达式语言.xmind

## Source

- Raw file: [Langchain(Legacy)/Langchain  表达式语言.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Langchain%20%20%E8%A1%A8%E8%BE%BE%E5%BC%8F%E8%AF%AD%E8%A8%80.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Langchain  表达式语言.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-08T10:39:33.156320+00:00`; modified `2024-12-11T07:14:38.621629+00:00`; size `663697`; snapshot `2026-05-29T22:11:26.662719+00:00`
- Coverage: exported and digested 2 sheets: `核心概念` (198 topics), `继承体系` (60 topics).

## Summary

这份图解释 LangChain Expression Language 的核心抽象：Runnable 是基础节点，`|`、Sequence、Parallel、Binding、Lambda、Passthrough、Assign、Map、stream、batch、with_config、with_fallbacks 等机制把模型、提示语、检索器和解析器组合成可调用、可流式、可配置、可观测的工作流。

## Source Digest

LCEL 的中心是 Runnable。source 先用 `setup_and_retrieval | prompt | model | output_parser` 建立管道心智模型，再展开 Runnable 的标准接口：`invoke`、`stream`、`batch` 以及异步变体，并强调每个 Runnable 都有 input/output schema。这让 LangChain 组件可以像函数、Unix 管道和类型化节点一样组合。

基本原语部分保留了关键组合模式：RunnableSequence 串联步骤；RunnableParallel 用字典把同一输入并行送给多个分支；Binding 固定调用参数；RunnableLambda 承接条件逻辑、自定义解析和动态返回 Runnable；RunnablePassthrough、assign、pick 支持保留原输入并扩展字段；`map()` 把单输入 chain 批量化。source 特别指出流处理需要上下游都支持，否则流式体验会被中间节点阻断。

高级部分把 LCEL 放到工程运行时语境里：fallback 处理失败回退，RunnableWithMessageHistory 管理会话历史，RunnableLambda/RunnableBranch 实现路由，RemoteRunnable 包装 LangServe 远程服务，with_listeners/Callbacks/LangSmith/verbose 支撑调试和观测，with_types 支撑类型声明。配置分支区分 configurable_fields/configurable_alternatives、RunnableConfig、with_config 和 bind，指出配置可以沿调用链传给子 Runnable，但在 Lambda 中直接 invoke 下游时需要手动透传 config。

第二张 sheet 从继承体系补足抽象边界：Runnable 定义类型、schema、操作符、调用、stream、events、retry、fallback、map 等接口；RunnableSerializable 借助 BaseModel 支撑序列化和可配置字段/备选项。source 也记录了 LCEL 的局限：缺乏自然循环机制、中断恢复和 human-in-the-loop 较难、包装方法可能返回新实例导致原对象专有方法不可用。

## Key Claims

- explicit: Runnable 是 LangChain 的基础节点，大部分组件包括 ChatModel、LLM、Output Parser 都实现 Runnable 接口。
- explicit: LCEL 的 `|` 管道语法本质上组合 RunnableSequence，适合把 prompt、model、parser、retriever 串成 chain。
- explicit: RunnableParallel 将同一输入并行送入多个 Runnable 分支，并返回按 key 组织的字典结果。
- explicit: RunnableLambda 可承载自定义逻辑，但如果内部直接调用其他 Runnable，需要透传 RunnableConfig 才不丢失回调和上下文。
- explicit: RunnableWithMessageHistory 是把消息历史接入 Runnable 的标准方式之一。
- explicit: `bind` 绑定的是 Runnable 调用参数，`with_config` 绑定的是 RunnableConfig，两者语义不同。
- explicit: LCEL 存在循环、中断恢复、human-in-the-loop 和包装实例方法可用性方面的局限。
- inferred: LCEL 可被编译为“LLM 应用编排代数”：Sequence/Parallel/Assign/Branch/Config/Event 是理解 LangChain 工作流的最小原语集合。

## External Links

- documentation: [Runnable custom runnable concepts](https://python.langchain.com/docs/concepts/runnables/#custom-runnables) — source 中 Runnable 分支引用的 LangChain 概念页；not verified.
- documentation: [Runnable API reference](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable) — source 的 API 文档扩展阅读；not verified.
- documentation: [LCEL cheatsheet](https://python.langchain.com/v0.2/docs/how_to/lcel_cheatsheet/#declaratively-make-a-batched-version-of-a-runnable) — source 的 CheatSheet 扩展阅读；not verified.
- documentation: [Streaming concepts](https://python.langchain.com/docs/concepts/streaming/) — `astream_events` 分支引用；not verified.
- documentation: [Custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/#astream-events-api) — 自定义事件示例引用；not verified.
- example-endpoint: [LangServe local joke endpoint](http://localhost:8000/joke/) — RemoteRunnable 示例中的本地服务地址；not verified.

## Links

- compiled-entity: [[entities/LangChain|LangChain]] — source 提供 LCEL 的 Runnable、Sequence、Parallel、Config、history、events 和 RemoteRunnable 证据（legacy · not verified）。
- compiled-concept: [[concepts/LCEL（LangChain Expression Language）|LCEL（LangChain Expression Language）]] — source 是 LCEL 概念页的直接知识来源（legacy · not verified）。
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]] — source 是 LLM 应用编排与 LangChain 运行抽象的学习材料。
- related: [[sources/Agent/LangChain.xmind|Agent/LangChain.xmind]] — 现有 LangChain source 可作为 LCEL 所在框架的背景证据。
- related: [[concepts/上下文工程|上下文工程]] — LCEL 的 RunnableConfig、历史消息、路由、stream 和 callbacks 都与上下文传递相关。
- related: [[concepts/Agent Harness|Agent Harness]] — LCEL 的观测、fallback、配置和事件机制可作为 Agent 运行控制面的实现候选。
- related: [[sources/Langchain(Legacy)/Lang Graph 案例学习.xmind|Lang Graph 案例学习.xmind]] — LCEL 是 LangGraph 中节点和边的实现基础，两个 source 在同一 legacy 体系里形成 Runnable 与 Graph 两层（legacy · not verified）。

## Maintenance Notes

- No raw files were modified.
- External links were extracted from the XMind export and were not browsed or verified.
- Batch instruction prohibited index/log/concepts/maps/synthesis updates; this note records source-only ingest.
- Compile candidates: LangChain Expression Language, Runnable, RunnableSequence, RunnableParallel, RunnableLambda, RunnableConfig, RunnableWithMessageHistory, LangServe RemoteRunnable.
