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

# Runnable 服务化

> **Legacy 警告**：本页内容基于 LangServe.xmind（2024年），legacy · not verified，API 行为以官方文档为准。

## Definition

Runnable 服务化是把 LangChain 的 Runnable（chain、agent、模型组合）通过 REST API 暴露为可远程调用服务的做法。LangServe 是这一做法的典型实现，支持 invoke、stream、batch 等执行形态，并提供 Playground 调试界面。

## Why It Matters

LLM 应用通常在 Python 后端构建，但前端和其他服务需要远程调用。Runnable 服务化让 LLM 应用可以跨语言、跨服务消费，并统一暴露多种执行形态（同步/流式/批量）的标准接口。

## Mental Model

把 Runnable 服务化类比为把函数变成微服务：原本只能在本地 Python 调用的 chain，通过 LangServe 变成任何人都可以调用的 REST endpoint，并且保留了原 Runnable 的流式、批量和事件监听能力。

## Key Claims

- explicit（来自 LangServe.xmind）：LangServe 用于将 LangChain `Runnable` 部署为 REST API，基于 FastAPI 和 Pydantic。
- explicit（来自 LangServe.xmind）：LangServe 暴露 `/invoke`、`/stream`、`/batch`、`/stream_log`、`/stream_events`、`/playground` 等标准端点。
- explicit（来自 LangServe.xmind）：当自动类型推断不足时，可以通过 `with_types` 或 `CustomUserType` 显式定义输入输出类型。
- explicit（来自 LangServe.xmind）：TypeScript 客户端可以通过 `@langchain/core/runnables/remote` 的 `RemoteRunnable` 调用远端 chain。
- inferred：Runnable 服务化需要显式定义输入输出 schema，否则远程消费方无法可靠地调用和处理响应。

## Examples

- FastAPI + LangServe 部署 OpenAI 模型：`add_routes(app, ChatOpenAI(), path="/openai")`。
- 前端通过 TypeScript `RemoteRunnable` 调用后端 chain，接入 CopilotKit 实现 copilot 功能。
- Playground 端点：`http://localhost:8000/joke/playground` 提供在线测试界面，无需写代码就可以测试 chain。

## Common Confusions

- LangServe 不处理鉴权、版本管理、扩缩容和 CI/CD；这些生产级治理需要额外搭建。
- `RemoteRunnable` 客户端和服务端需要保持接口兼容，schema 变更会破坏远程调用方。
- LangServe 和 LangSmith 是不同工具：前者负责暴露服务，后者负责观测和评估。

## Evidence

- explicit: [[sources/Langchain(Legacy)/LangServe.xmind|LangServe.xmind]] — 主要证据，详细记录 LangServe 端点、类型、客户端和部署示例（legacy · not verified）。

## Relations

- part-of: [[entities/LangChain|LangChain]] （legacy · not verified）
- prerequisite: [[concepts/LCEL（LangChain Expression Language）|LCEL]] （Runnable 是 LCEL 的核心组件，服务化的是 Runnable）
- implemented-by: [[entities/LangServe|LangServe]] （legacy · not verified）
- related-source: [[sources/Langchain(Legacy)/LangServe.xmind|LangServe.xmind]]
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]]

## My Understanding

Runnable 服务化解决的是"本地构建好的 chain 如何让其他系统消费"的问题。它的优雅之处在于把原 Runnable 的多种调用形态（invoke/stream/batch）都原封不动地暴露到 REST 接口，远程消费方获得和本地调用几乎相同的能力。

## Review Questions

- LangServe 暴露了哪些端点？它们分别对应什么调用形态？
- 为什么需要显式定义输入输出类型？
- RemoteRunnable 如何在 TypeScript 中调用 Python 构建的 chain？

## Open Questions

- LangServe 在 2025-2026 的维护状态和替代方案（legacy · not verified）。
- 生产级 LLM API 网关的鉴权、限流、版本管理方案，LangServe 本身不覆盖。
