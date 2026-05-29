---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/LangServe.xmind"
source_relpath: "Langchain(Legacy)/LangServe.xmind"
raw_created_at: 2024-06-06T07:42:33.139487+00:00
raw_modified_at: 2024-08-08T07:58:41.870398+00:00
raw_size: 327362
raw_fingerprint: "size=327362;birth=2024-06-06T07:42:33.139487+00:00;mtime=2024-08-08T07:58:41.870398+00:00"
raw_snapshot_at: 2026-05-29T22:11:27.790686+00:00
ingested_at: 2026-05-30
status: ingested
---

# LangServe.xmind

## Source

- Raw file: [Langchain(Legacy)/LangServe.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/LangServe.xmind>)
- Raw ref: `raw:Langchain(Legacy)/LangServe.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-06-06T07:42:33.139487+00:00`; modified `2024-08-08T07:58:41.870398+00:00`; size `327362`; snapshot `2026-05-29T22:11:27.790686+00:00`
- Coverage: exported and read 1 sheet, `画布 1`, with 29 topics via `ai-wiki-xmind-ingest`.

## Summary

这份图介绍 LangServe：把 LangChain `Runnable` 部署成 REST API 的服务层。它强调 FastAPI/Pydantic 基础、标准调用端点、playground、Python 服务端示例、自定义输入输出类型，以及 TypeScript `RemoteRunnable` 客户端接入方式。

## Source Digest

这份 source 把 LangServe 放在 LangChain 生态的部署边界：开发者在本地或应用内构造 `Runnable`，再通过 LangServe 暴露成可远程调用、流式调用、批量调用和事件流监听的 REST API。它列出的端点包括 `/invoke`、`/stream`、`/batch`、`/stream_log`、`/stream_events`、`/playground` 和 `/astream_events`，说明 LangServe 不只是简单 HTTP 包装，而是尽量保留 Runnable 的多种执行形态。

示例部分展示 FastAPI 应用中用 `add_routes` 暴露 OpenAI、Anthropic 模型，以及 prompt + model 组合后的 chain。类型分支强调自动推断并不总可靠，因此需要 `with_types` 或继承 `CustomUserType` 来显式定义输入输出 schema。这一点对于把 LLM 应用交给前端、CopilotKit 或其他服务消费很关键：远程 API 必须有可理解、可验证的输入输出契约。

客户端分支给出 TypeScript 侧 `RemoteRunnable` 的使用方式，并把远程 chain 接到 CopilotKit backend 的 adapter 中。整体上，这份图的价值是把 LangChain 的“应用构建”延伸到“服务化部署和跨语言调用”，但没有展开生产级鉴权、版本、监控、扩缩容或 CI/CD。

## Key Claims

- explicit: LangServe 用于将 LangChain `Runnable` 部署为 REST API。
- explicit: LangServe 基于 FastAPI 和 Pydantic，并暴露 invoke、stream、batch、stream log/events、playground 等调用方式。
- explicit: 服务端可以通过 `add_routes` 暴露模型或 prompt/model 组合后的 chain。
- explicit: 当自动类型推断不足时，可以通过 `with_types` 或 `CustomUserType` 显式定义输入输出类型。
- explicit: TypeScript 客户端可以通过 `@langchain/core/runnables/remote` 的 `RemoteRunnable` 调用远端 chain。
- inferred: LangServe 适合沉淀为 LangChain 生态中的“部署/服务化”节点，和 LangGraph 的运行时编排、LangSmith 的评估监控形成互补。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/Agent Harness|Agent Harness]] — LangServe 的远程 Runnable、流式端点和类型契约可补充 Agent 工具/服务接入边界。

## Maintenance Notes

- No raw files were modified.
- Source focuses on API exposure and client usage; production治理 such as auth, deployment topology, observability, cost and rollback are not covered.
- Compile candidates: LangServe, Runnable 服务化, RemoteRunnable, LangChain Deployment, LLM API Gateway.
