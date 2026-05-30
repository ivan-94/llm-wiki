---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/变体/Nano Bot .xmind"
source_relpath: "Agent/变体/Nano Bot .xmind"
raw_created_at: 2026-03-20T12:59:44.990660+00:00
raw_modified_at: 2026-03-22T03:57:33.832243+00:00
raw_size: 2900091
raw_fingerprint: "size=2900091;birth=2026-03-20T12:59:44.990660+00:00;mtime=2026-03-22T03:57:33.832243+00:00"
raw_snapshot_at: 2026-05-29T22:03:37.810000+00:00
ingested_at: 2026-05-30
status: ingested
---

# Nano Bot .xmind

## Source

- Raw file: [Agent/变体/Nano Bot .xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E5%8F%98%E4%BD%93/Nano%20Bot%20.xmind)
- Raw ref: `raw:Agent/变体/Nano Bot .xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-03-20T12:59:44.990660+00:00`; modified `2026-03-22T03:57:33.832243+00:00`; size `2900091`; snapshot `2026-05-29T22:03:37.810000+00:00`
- Coverage: exported and read 1 sheet: `画布 1`.

## Summary

这份思维导图从实现模块角度拆解 Nano Bot：它用 MessageBus 解耦 channel 与 agent，用单一 AgentLoop 处理入站消息和控制命令，用配置驱动 Provider/Channel 扩展，并把定时和主动能力建成回调进入同一 Agent，而不是额外脚本引擎。它的重点是一个轻量 Agent runtime 的工程骨架：Context、Memory、Skills、Tools、Session、Sub Agents、Gateway、MessageBus、Channel、Cron 和 Heartbeat。

## Source Digest

Nano Bot 的架构主线是「少层次、强契约、文件系统优先」。底层用 `MessageBus` 作为渠道和 agent 的稳定边界，平台适配器只需要把事件变成入站消息；`AgentLoop.run()` 持续消费 inbound，对 `/stop`、`/restart` 做控制面处理，其余消息进入完整对话链路。Provider 通过注册表扩展，Channel 通过发现机制和 entry points 插件扩展；定时任务和 heartbeat 最终也回到同一个 Agent 处理，避免状态分裂。

上下文构建由 `nanobot/agent/context.py` 承担。`build_system_prompt` 把人设、OS/Python、workspace、Bootstrap 文件、记忆片段和技能信息组合为 system；`build_messages` 把会话历史与当前用户输入组合为模型消息，并把 runtime context 标记为 metadata only 后合并到用户消息，避免部分供应商拒绝连续同 role 消息。技能系统支持 workspace 覆盖内置技能，`always: true` 且依赖满足的技能会强注入 system，其余技能以 XML 摘要形式弱注入，引导模型按需读取。

记忆系统相对简单：`MEMORY.md` 是长期事实，`HISTORY.md` 是可 grep 的追加时间线；HISTORY 不自动进上下文，需要模型通过文件读取或 grep 手工召回。工具系统用统一 `Tool` 抽象和集中注册表，默认工具包括读写改文件、列目录、exec、web search/fetch、message、spawn、cron，并能在运行开始时动态接入 MCP。会话以 JSONL 持久化，含 metadata 与消息；窗口截断会尽量从 user 开始，并避免孤儿 tool result。子代理由 SpawnTool 异步创建，子代理结果通过 MessageBus 回灌为下一条入站消息，进入同一主循环。

## Key Claims

- explicit: Nano Bot 用 `MessageBus` 解耦 channels 与 agent，事件形状由 `nanobot/bus/events.py` 定义。
- explicit: `AgentLoop.run()` 处理 `/stop`、`/restart` 等控制面消息，其余消息进入完整对话链路。
- explicit: Runtime Context 被标记为 metadata only，并与用户正文合并到同一条 user 消息，避免连续同 role 问题。
- explicit: Nano Bot 的记忆以 Markdown 文件为主，`MEMORY.md` 全量进入 system，`HISTORY.md` 不自动进入上下文。
- explicit: Skills 支持 workspace 覆盖同名内置技能，强注入与弱注入由元数据和依赖条件决定。
- explicit: 子代理通过 MessageBus 把结果回灌到主流程，相当于异步结果作为助手侧补充进入同一会话。
- inferred: Nano Bot 适合作为轻量 Agent runtime 的对照样本，用于比较文件记忆、消息总线、技能注入、子代理回灌和定时能力的最小实现。

## External Links

No external links found in extracted content.

## Links

No downstream wiki pages were created or updated in this scoped ingest.

## Maintenance Notes

- XMind helper reported `ok: true`; no `sheets_error`.
- Several branch labels such as `协议` and `Channel` are sparse; they were treated as structure markers, not standalone claims.
- This batch intentionally did not update `index.md` or `log.md`.

- Link cleanup candidate: batch-boundary: No wiki concept, entity, synthesis, map, index, or log pages were created or updated for this batch, per task instruction.
- Link cleanup candidate: compile-candidate: Nano Bot; Agent runtime 最小架构; MessageBus; Agent 文件记忆; Skills 注入; 子代理回灌; Cron 与 Heartbeat.
