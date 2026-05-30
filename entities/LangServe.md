---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# LangServe

> **Legacy 警告**：本页内容基于 `LangServe.xmind`（截至 2024年8月），legacy · not verified，API 行为以官方文档为准。信息量有限，如 LangServe 已被弃用或替代，请以官方文档为准。

## What It Is

LangServe 是 LangChain 生态中用于把 `Runnable` 暴露为 REST API 的服务化框架。它基于 FastAPI 和 Pydantic，自动为 chain 生成多种调用端点，支持跨语言（TypeScript）客户端通过 `RemoteRunnable` 访问。

## Role In This Wiki

LangServe 作为 Runnable 服务化概念的具体实现参照，展示如何把本地 LangChain chain 变成可远程调用的 API 服务。详细概念见 [[concepts/Runnable 服务化|Runnable 服务化]]。

## Key Facts

- **端点**：自动生成 `/invoke`、`/stream`、`/batch`、`/stream_log`、`/stream_events`、`/astream_events`、`/playground`。
- **部署方式**：通过 `add_routes(app, runnable, path="/endpoint")` 把 chain 接入 FastAPI 应用。
- **类型声明**：自动类型推断不总可靠，可通过 `with_types` 或继承 `CustomUserType` 显式定义输入输出 schema。
- **TypeScript 客户端**：通过 `@langchain/core/runnables/remote` 的 `RemoteRunnable` 访问远端 chain。
- **局限**：不处理生产级鉴权、版本管理、扩缩容或 CI/CD。

## Related Concepts

- implements: [[concepts/Runnable 服务化|Runnable 服务化]]
- part-of: [[entities/LangChain|LangChain]] （legacy · not verified）
- prerequisite: [[concepts/LCEL（LangChain Expression Language）|LCEL]]

## Evidence

- [[sources/Langchain(Legacy)/LangServe.xmind|LangServe.xmind]] — 唯一证据，记录 LangServe 端点、类型声明和客户端调用方式（legacy · not verified）。

## Open Questions

- LangServe 的当前维护状态和官方推荐替代方案（legacy · not verified）。
- 生产场景下如何在 LangServe 基础上添加鉴权、版本和监控，尚无 wiki 证据。
