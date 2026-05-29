---
page_type: entity
updated_at: 2026-05-29
status: active
source_count: 1
---

# Agent Client Protocol

## What It Is

Agent Client Protocol（ACP）是面向 agentic coding 的 client/IDE/editor 与 AI 编程 agent 的通信协议，本 wiki 的 raw 将其描述为基于 JSON-RPC 2.0 的互操作层。

## Role In This Wiki

ACP 是 Vibe 工具生态中的协议层参照：它说明 Agentic Engineering 不只需要模型和工具，还需要 client-agent 之间的会话、权限、文件、终端、计划和配置协议。

## Key Facts

- Source 将 ACP 类比为 agentic coding 场景下的 LSP：解耦编辑器/client 与 agent。
- 能力模型覆盖 session、prompt turn、content blocks、tool calls、permissions、filesystem、terminal、plan、session config、slash commands、extensibility 和 transports。
- Source 认为 ACP 与 MCP 互补：ACP 管 client-agent 通信，MCP 管 agent 与外部工具/上下文服务器通信。
- 协议当前状态可能变化，未来使用前需要核验官方文档。

## Related Concepts

- [[concepts/Agent Harness|Agent Harness]]
- [[concepts/Agentic Engineering|Agentic Engineering]]

## Evidence

- [[sources/Vibe/工具/ACP.xmind|ACP.xmind]]

## Open Questions

- 远程 transport、capability negotiation 和安全边界的当前实现状态需要后续官方核验。
