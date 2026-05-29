---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/ACP.xmind"
source_relpath: "Vibe/工具/ACP.xmind"
raw_created_at: 2026-05-14T02:18:16.988721+00:00
raw_modified_at: 2026-05-14T02:37:18.867828+00:00
raw_size: 1626589
raw_fingerprint: "size=1626589;birth=2026-05-14T02:18:16.988721+00:00;mtime=2026-05-14T02:37:18.867828+00:00"
raw_snapshot_at: 2026-05-29T16:02:52.342371+00:00
ingested_at: 2026-05-30
status: ingested
---

# ACP.xmind

## Source

- Raw file: [Vibe/工具/ACP.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/ACP.xmind>)
- Raw ref: `raw:Vibe/工具/ACP.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-14T02:18:16.988721+00:00`; modified `2026-05-14T02:37:18.867828+00:00`; size `1626589`; snapshot `2026-05-29T16:02:52.342371+00:00`
- Coverage: helper exported all sheets. Sheet count: 1. Sheets: `画布 1` (index 0, 250 topics).

## Summary

这份 XMind 系统介绍 Agent Client Protocol（ACP）：它是面向 agentic coding 的客户端/编辑器与 AI 编程 agent 通信协议，基于 JSON-RPC 2.0，目标是解耦编辑器与 agent、降低重复集成成本、减少锁定，并标准化会话、提示回合、工具调用、权限、文件系统、终端、计划、配置和扩展机制。

## Source Digest

source 把 ACP 定位为 AI 编程 agent 与代码编辑器、IDE、CLI、Web UI 等 client 之间的标准协议，类比 LSP 对编辑器与语言服务器关系的标准化。它不是通用聊天协议，而是聚焦 agentic coding：client 管理用户界面、文件、终端、权限和上下文，agent 分析代码、修改文件、执行命令，并通过 ACP 回传进度、工具调用、结果和 stop reason。

能力模型覆盖 session 管理、prompt turn、多模态内容块、工具调用展示与状态更新、权限请求、文件读写、未保存内容暴露、终端创建/输出/等待/杀死、计划展示、模型/模式/推理等级配置、slash commands 和扩展元数据。架构上，stdio 是当前主要本地传输，HTTP/WebSocket 面向远程 agent 但仍在演进；ACP 与 MCP 互补，ACP 管 client-agent 通信，MCP 管 agent 与外部工具/上下文服务器通信。

source 也列出治理、生态和限制：ACP 当前由 Zed 与 JetBrains 共同治理，目标是开放互操作生态；适用场景包括 IDE、编辑器、CLI/TUI、桌面/Web、Notebook/数据分析环境、消息平台、本地 agent 和远程 agent。限制包括远程支持仍不成熟、协议机制持续演进、capability 协商复杂、安全边界依赖实现，以及协议主要服务编程任务而非所有 agent 场景。

## Key Claims

- explicit: ACP 标准化 client/IDE/editor 与 AI 编程 agent 之间的通信，面向 agentic coding 而非通用聊天。
- explicit: ACP 基于 JSON-RPC 2.0，支持 request-response、notification，并默认使用 Markdown 作为用户可读文本格式。
- explicit: ACP 的核心价值是解耦编辑器与 agent、降低重复集成成本、减少开发者锁定，并让 client 与 agent 生态独立演进。
- explicit: ACP 覆盖 session、prompt、content、tool calls、permissions、file system、terminals、agent plan、session config、slash commands、extensibility 和 transports 等模块。
- explicit: ACP 与 MCP 互补；ACP 负责 client-agent 通信，MCP 负责 agent 与外部工具/上下文服务器通信。
- inferred: ACP 可作为 Vibe 工具生态中的“agent-client 互操作层”实体或概念，连接 IDE、CLI、权限、安全和工具调用 UX。

## External Links

No external links found in extracted content.

## Links

- compiled-entity: [[entities/Agent Client Protocol|Agent Client Protocol]] — 可沉淀 ACP 的治理、定位、协议模块、生态角色和限制。
- related: Agent Client 协议层 — 可描述 IDE/client 与 agent 的标准交互边界。
- related: Vibe Coding 工具体系 — 可作为 agentic coding client/agent 协议工具入口。

## Maintenance Notes

- Exported content names Zed、JetBrains、Ben Brandt、Sergey Ignatov and protocol evolution details, but no URLs were present; no external verification was performed.
- Protocol details may change over time; future compile should re-check official ACP documentation if current-state accuracy is required.
