---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/变体/Hermes.xmind"
source_relpath: "Agent/变体/Hermes.xmind"
raw_created_at: 2026-04-07T14:57:39.713634+00:00
raw_modified_at: 2026-04-30T10:00:44.068284+00:00
raw_size: 708588
raw_fingerprint: "size=708588;birth=2026-04-07T14:57:39.713634+00:00;mtime=2026-04-30T10:00:44.068284+00:00"
raw_snapshot_at: 2026-05-29T22:03:44.454983+00:00
ingested_at: 2026-05-30
status: ingested
---

# Hermes.xmind

## Source

- Raw file: [Agent/变体/Hermes.xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E5%8F%98%E4%BD%93/Hermes.xmind)
- Raw ref: `raw:Agent/变体/Hermes.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-04-07T14:57:39.713634+00:00`; modified `2026-04-30T10:00:44.068284+00:00`; size `708588`; snapshot `2026-05-29T22:03:44.454983+00:00`
- Coverage: exported and read 2 sheets: `Hermes`, `实战`.

## Summary

这份思维导图把 Hermes 描述为一个重视学习循环、跨会话记忆、平台网关、自动化和研究轨迹生成的 Agent 系统。导图不仅列出功能，也拆到代码结构和运行时链路：AIAgent 负责对话循环、提示构建、供应商解析和工具调度；CLI、Gateway、ACP、Batch Runner、API Server 是多入口；SQLite/FTS5、记忆提供商、技能管理、cron、委派和批量轨迹构成长期运行与训练数据能力。

## Source Digest

Hermes 的核心定位是「会学习的代理」。导图强调它会从经验中创造技能，在使用过程中改进技能，维护记忆，检索过往对话，并逐步建立用户画像。入口层包括 CLI、Gateway、ACP、Batch Runner、API Server 和 Python Library；核心层是 `AIAgent`，它将提示构建、模型供应商解析、工具分发、压缩、缓存和持久化组合为一个对话循环。工具系统由注册表和工具集驱动，覆盖网页、浏览器、终端、文件、MCP、消息、委派、强化学习环境等。

运行时设计重视长对话可持续性。Agent Loop 在 API 调用前做上下文压力检查，超过阈值会压缩旧消息；工具调用和结果保持成对，尾部消息受保护；Anthropic prompt caching 用稳定 system prompt 和最近消息作为缓存断点以降低输入成本。会话存储基于 SQLite 与 FTS5，支持会话血缘、平台隔离、搜索去重、原子写入和压缩后的续篇恢复。记忆层同时有 `MEMORY.md`、`USER.md` 这类常驻文件，`session_search` 这种长期会话搜索，以及 Honcho、Mem0、ByteRover 等外部记忆提供商插件。

自动化和并行是另一个重点。Cron 由网关守护进程每 60 秒调度，到期任务会在全新 Agent 会话中运行，可以注入技能并把结果发回聊天、本地文件或平台目标。`delegate_task` 会创建隔离上下文、受限工具集和独立终端会话的子 Agent，只把最终摘要带回父上下文。批量任务用于并行生成带工具统计的 ShareGPT 轨迹，服务训练和评估。整体看，Hermes 的差异点不是单个工具，而是把记忆、技能、压缩、缓存、网关、委派、cron、轨迹生成放到同一套可长期运行的代理基础设施中。

## Key Claims

- explicit: Hermes 被描述为内置学习循环的代理，会从经验中创建技能并在使用中持续改进。
- explicit: Hermes 支持本地、Docker、SSH、Daytona、Singularity、Modal 六种终端后端。
- explicit: AIAgent 是核心对话循环，负责提示构建、供应商解析、工具调度、压缩、缓存、持久化、回调、中断和回退。
- explicit: Hermes 的 API 模式包含 chat completions、OpenAI Responses API 和 Anthropic Messages API。
- explicit: Hermes 使用 SQLite 会话存储和 FTS5 搜索，支持压缩前后的会话血缘追踪。
- explicit: Cron 由 Gateway 守护进程调度，并在全新 Agent 会话中运行到期任务。
- explicit: `delegate_task` 生成隔离上下文和受限工具集的子 AIAgent，只有最终摘要进入父上下文。
- inferred: Hermes 适合沉淀为「长期运行 Agent runtime」案例，特别是学习循环、会话血缘、记忆插件、自动化调度和研究轨迹生成的组合设计。

## External Links

- source-repository: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — source title references Hermes Agent repository; not verified.
- reference-article: [深度拆解 Hermes Agent 的记忆系统：它如何修正 OpenClaw 的误区](https://baoyu.io/blog/2026-04-29/manthanguptaa-2034849672985288957) — listed as extended reading for memory-system comparison; not verified.

## Links

No downstream wiki pages were created or updated in this scoped ingest.

## Maintenance Notes

- XMind helper reported `ok: true`; no `sheets_error`.
- Sheet `实战` ends with placeholder nodes `中心主题` and `分支主题 1-4`; substantive sections before that were digested, and placeholder nodes should not be treated as knowledge claims.
- External links were extracted from the XMind export and were not browsed or verified.
- This batch intentionally did not update `index.md` or `log.md`.

- Link cleanup candidate: batch-boundary: No wiki concept, entity, synthesis, map, index, or log pages were created or updated for this batch, per task instruction.
- Link cleanup candidate: compile-candidate: Hermes; Agent 学习循环; Agent 会话血缘; Agent 记忆系统; Agent cron 自动化; 子代理委派; Agent 轨迹生成.
