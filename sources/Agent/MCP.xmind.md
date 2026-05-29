---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/MCP.xmind"
source_relpath: "Agent/MCP.xmind"
raw_created_at: 2024-12-16T05:50:28.594616+00:00
raw_modified_at: 2025-09-28T10:36:32.240442+00:00
raw_size: 773937
raw_fingerprint: "size=773937;birth=2024-12-16T05:50:28.594616+00:00;mtime=2025-09-28T10:36:32.240442+00:00"
raw_snapshot_at: 2026-05-29T22:03:23.002013+00:00
ingested_at: 2026-05-30
status: ingested
---

# MCP.xmind

## Source

- Raw file: [Agent/MCP.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/MCP.xmind>)
- Raw ref: `raw:Agent/MCP.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-12-16T05:50:28.594616+00:00`; modified `2025-09-28T10:36:32.240442+00:00`; size `773937`; snapshot `2026-05-29T22:03:23.002013+00:00`
- Coverage: all XMind sheets exported and digested; sheet count `1`; sheets: `0: 画布 1` with `58` topics.

## Summary

这份 mind map 把 MCP 定义为模型上下文协议，说明它与普通工具调用的层次差异，并概览 Host、Client、Server 架构、JSON-RPC 传输、Resources、Tools、Prompts、Sampling 以及常见 MCP 市场入口。

## Source Digest

source 的主线是把 MCP 解释为一种让应用向 LLM 标准化提供上下文和能力的开放协议。它强调 MCP 不等同于单个工具：工具是 LLM 可调用的函数层概念，而 MCP 是与具体 LLM 供应商无关的接口协议，可以被不同 LLM、Agent 框架和服务提供商复用实现。架构上，Host 是 Claude、Cursor 等面向用户的应用，Client 负责与 MCP Server 通信，Server 提供实际业务能力。

协议层关注 request、notification、result、error 等消息表达；传输层包括本地 stdio 和 HTTP with SSE，两者底层都使用 JSON-RPC 2.0。概念层包含 Resources、Tools、Prompts 和 Sampling：Resources 面向读取类上下文，Tools 面向经用户批准后的函数调用，Prompts 是预设任务模板，Sampling 允许服务端请求客户端执行 LLM。source 还记录了一组 MCP registry、market 和编辑器集成入口，并把 Figma、Chrome DevTools 作为自用 MCP 方向。

## Key Claims

- explicit: MCP 是开放协议，用于标准化应用程序如何为 LLM 提供上下文。
- explicit: MCP 与工具不在同一抽象层级；MCP 是通用接口协议，最终可作为工具能力被 LLM 使用。
- explicit: MCP 架构包含 Host、Client 和 Server，Host 面向用户，Client 与 server 通信，Server 提供实际业务。
- explicit: MCP 传输层覆盖 stdio 和 HTTP with SSE，底层使用 JSON-RPC 2.0。
- explicit: MCP 基本概念包括 Resources、Tools、Prompts 和 Sampling。
- inferred: MCP 更适合编译为 Agent 能力集成协议，而不是单个工具或单一产品实体。

## External Links

- protocol-docs: [MCP quickstart](https://modelcontextprotocol.io/quickstart) — source 根节点链接；not verified.
- registry: [Github MCP Registry](https://github.com/mcp) — MCP 市场/registry 入口；not verified.
- market: [MCP.so](https://mcp.so/) — MCP 市场入口；not verified.
- claude-docs: [Claude Code Popular MCP Server](https://docs.claude.com/en/docs/claude-code/mcp#popular-mcp-servers) — Claude Code 常见 MCP server 参考；not verified.
- editor-integration: [Vscode 扩展菜单已内置 MCP](https://code.visualstudio.com/mcp) — 编辑器集成参考；not verified.
- market: [阿里百炼](https://bailian.console.aliyun.com/?utm_content=se_1021228187&gclid=Cj0KCQjw58PGBhCkARIsADbDilw3btiSdKkg_gmDiUUalW5l1ospvpV34YY0-pmImUUbIEqOx7kEfywaAsp6EALw_wcB&tab=mcp#/mcp-market) — MCP 市场入口；not verified.
- list: [Awesome MCP servers](https://github.com/punkpeye/awesome-mcp-servers) — MCP server 列表；not verified.

## Links

- related: [[concepts/Agentic Engineering|Agentic Engineering]] — MCP 可作为 Agent 能力集成和上下文供给协议的证据。
- related: [[concepts/Agent Harness|Agent Harness]] — MCP 的 Host/Client/Server 与传输层可补充 harness 外部工具接入模型。
- related: [[entities/Claude Code|Claude Code]] — source 把 Claude Code 作为 MCP 应用和 server 生态入口之一。

## Maintenance Notes

- No issues. One sheet was discovered, exported, read, and digested.
- Compile candidates: Model Context Protocol, MCP, Agent 工具协议, Host/Client/Server, Resources/Tools/Prompts/Sampling.
