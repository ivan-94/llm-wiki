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

- Source 将 ACP 类比为 agentic coding 场景下的 LSP：解耦编辑器/client 与 agent，降低重复集成成本，减少开发者锁定。
- 能力模型覆盖 session、prompt turn、content blocks、tool calls、permissions、filesystem、terminal、plan、session config、slash commands、extensibility 和 transports。

**Transport 演进：**
- `stdio`：当前主要本地传输方式，agent 与 client 在同一机器上通过标准输入输出通信。
- `HTTP/WebSocket`：面向远程 agent 场景，但官方标注仍在演进中，当前不成熟。
- 远程 transport 的成熟意味着 Agent 可以完全在云端执行，client 只负责 UI——这是 ACP 的长期方向。

**ACP 与 MCP 分工图：**
```
用户/IDE Client ──[ACP]──> AI Agent ──[MCP]──> 外部工具/上下文服务器
                (会话/权限/终端/计划)      (工具调用/数据获取)
```

**当前已知 used-in：**
- Zed（共同治理方）
- JetBrains（共同治理方）
- 生态目标覆盖：IDE、编辑器、CLI/TUI、桌面/Web、Notebook、消息平台、本地和远程 agent。

- 协议当前状态可能变化，未来使用前需要核验官方文档。

## Related Concepts

- related: [[concepts/Agent Harness|Agent Harness]]
- related: [[concepts/Agentic Engineering|Agentic Engineering]]
- contrasts-with: [[entities/Model Context Protocol|Model Context Protocol]] — MCP 管 agent↔工具通信，ACP 管 client↔agent 通信，两者互补而非竞争
- used-in: [[entities/Cursor|Cursor]] — Cursor 作为 AI Coding IDE，是 ACP 典型 client 场景
- used-in: [[entities/Claude Code|Claude Code]] — Claude Code CLI 是 ACP 的 agent 侧实现
- used-in: [[entities/Codex|Codex]] — Codex CLI 是 ACP 的 agent 侧实现

## Evidence

- [[sources/Vibe/工具/ACP.xmind|ACP.xmind]]

## Open Questions

- 远程 transport、capability negotiation 和安全边界的当前实现状态需要后续官方核验。
