---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/LangChain.xmind"
source_relpath: "Agent/LangChain.xmind"
raw_created_at: 2026-04-01T06:59:51.375932+00:00
raw_modified_at: 2026-04-01T10:45:49.836763+00:00
raw_size: 1617939
raw_fingerprint: "size=1617939;birth=2026-04-01T06:59:51.375932+00:00;mtime=2026-04-01T10:45:49.836763+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.896394+00:00
ingested_at: 2026-05-30
status: ingested
---

# LangChain.xmind

## Source

- Raw file: [Agent/LangChain.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/LangChain.xmind>)
- Raw ref: `raw:Agent/LangChain.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-04-01T06:59:51.375932+00:00`; modified `2026-04-01T10:45:49.836763+00:00`; size `1617939`; snapshot `2026-05-29T22:03:22.896394+00:00`
- Coverage: all XMind sheets exported and digested; sheet count `1`; sheets: `0: 画布 1` with `33` topics.

## Summary

这份 mind map 用 LangChain 生态拆分 Agent 框架的层次：LangChain 提供应用抽象，LangGraph 提供图执行与运行时能力，DeepAgents 在其上包装成更开箱即用的 Agent runtime。

## Source Digest

source 的核心价值在于把 LangChain 生态从“一个库”拆成三个层级。LangChain 是上层应用构建工具箱，覆盖 model、message、tool、agent、memory、I/O、流式输出、结构化输出和 middleware；LangGraph 是更底层的执行运行时，强调图编排、持久化、重放、流、中断、human-in-the-loop 和子图；DeepAgents 则站在二者之上，把现代 Agent 需要的循环、规划分解、短期/长期记忆，以及 Tool、MCP、Skill、SubAgent 等外围能力组合成开箱即用形态。

这份材料适合后续编译到 Agent 框架分层、Agent runtime 与 harness 的概念模型中。它没有展开具体 API 或代码示例，更多是用于建立 LangChain / LangGraph / DeepAgents 的职责边界。

## Key Claims

- explicit: LangChain 包含构建 Agent 应用的多类抽象，包括 Models、Messages、Tools、Agents、Memory、I/O、流式输出、结构化输出和中间件。
- explicit: LangGraph 被定位为底层运行时，核心能力包括基于图的逻辑编排、持久化执行、流式传输、中断、human-in-the-loop 和子图支持。
- explicit: DeepAgents 基于 LangChain 与 LangGraph，目标是提供开箱即用的 Agent runtime。
- inferred: 这份资料把 Agent 框架理解成“应用抽象层、执行运行时层、成品 Agent runtime 层”三个层次，而不是把 LangChain 生态当作单一工具。

## External Links

- framework-layering: [不同的层次](https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/) — 用于区分 agent framework、runtime 与 harness 等层级；not verified.
- langgraph-docs: [对比 Workflow 与智能体](https://docs.langchain.com/oss/python/langgraph/workflows-agents) — 用于理解 LangGraph 中 workflow 与 agent 的边界；not verified.

## Links

- related: [[concepts/Agentic Engineering|Agentic Engineering]] — 可作为 Agent 工具链和运行时分层的补充证据。
- related: [[concepts/Agent Harness|Agent Harness]] — LangGraph/DeepAgents 的运行时能力可进入 harness 能力边界对比。
- related: [[concepts/Agent Skills|Agent Skills]] — source 把 Skill 列为现代 Agent 外围能力之一，但未展开技能设计细节。

## Maintenance Notes

- No issues. One sheet was discovered, exported, read, and digested.
- Compile candidates: Agent 框架分层, LangChain, LangGraph, DeepAgents, Agent Runtime.
