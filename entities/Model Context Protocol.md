---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 2
---

# Model Context Protocol

## What It Is

Model Context Protocol（MCP）是用于标准化应用程序向 LLM/Agent 提供上下文和能力的开放协议。

## Role In This Wiki

MCP 在本 wiki 中属于 Agent Harness 和工具接入层：它不只是单个工具，而是 Host、Client、Server、Resources、Tools、Prompts、Sampling 和传输协议共同组成的能力接入方式。

## Key Facts

- raw 将 MCP 与普通 tool calling 区分为不同抽象层级。
- MCP 架构包含 Host、Client 和 Server。
- 传输层记录了 stdio 与 HTTP with SSE，底层使用 JSON-RPC 2.0。
- 概念层包含 Resources、Tools、Prompts 和 Sampling。
- 取舍：MCP 工具定义每轮注入上下文，token 效率不如 CLI/ACI；`智能体工程的 8 个等级` 记录 LLM 因此越来越多改用 CLI 工具（见 [[concepts/Agent 工具调用|Agent 工具调用]] 选型）。
- 当前页面未联网核验 MCP 最新规范，只记录 raw 中学习材料。

## Related Concepts

- implemented-by: [[concepts/Agent 工具调用|Agent 工具调用]]
- contrasts-with: [[concepts/Agent-friendly CLI（ACI）|Agent-friendly CLI（ACI）]]
- used-in: [[concepts/Agent Harness|Agent Harness]]
- used-in: [[concepts/AI Agent|AI Agent]]

## Evidence

- [[sources/Agent/MCP.xmind|MCP.xmind]]
- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]

## Open Questions

- MCP 当前协议细节、registry 和编辑器集成状态需要后续按官方文档核验。
