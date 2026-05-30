---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/变体/OpenClaw.xmind"
source_relpath: "Agent/变体/OpenClaw.xmind"
raw_created_at: 2026-03-13T07:20:45.237140+00:00
raw_modified_at: 2026-03-22T04:16:33.237751+00:00
raw_size: 15525770
raw_fingerprint: "size=15525770;birth=2026-03-13T07:20:45.237140+00:00;mtime=2026-03-22T04:16:33.237751+00:00"
raw_snapshot_at: 2026-05-29T22:03:28.122548+00:00
ingested_at: 2026-05-30
status: ingested
---

# OpenClaw.xmind

## Source

- Raw file: [Agent/变体/OpenClaw.xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E5%8F%98%E4%BD%93/OpenClaw.xmind)
- Raw ref: `raw:Agent/变体/OpenClaw.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-03-13T07:20:45.237140+00:00`; modified `2026-03-22T04:16:33.237751+00:00`; size `15525770`; snapshot `2026-05-29T22:03:28.122548+00:00`
- Coverage: exported and read 2 sheets: `概览`, `架构`.

## Summary

这份思维导图把 OpenClaw 描述为本地优先、Loopback-first、Unix 哲学导向的个人 Agent 系统。它的核心结构是 Gateway、Node、Channel 三层：Gateway 是控制平面和消息路由，Node 是设备端执行节点，Channel 负责接入 20+ 即时通讯平台。导图同时覆盖记忆系统、工作区、CLI、skills 生态、自动化、媒体设备、工具、子智能体、多 Agent 和插件架构。

## Source Digest

OpenClaw 的设计重心是「把 AI 助手搬到个人设备上」而不是构建云端托管平台。三层架构中，Gateway 维护 WebSocket、Session 和 Agent 调度；Node 在设备端执行本地操作；Channel 接入聊天平台。Loopback-first 设计默认不开放外网端口，需要远程访问时通过 Tailscale Serve/Funnel 或 SSH 端口转发暴露，而不是直接开放服务。工作区是每个 Agent 的独立文件系统作用域，配置、记忆、技能都以纯文本文件形式存在。

记忆层由 Daily Log、长期记忆、自动记忆保存和搜索工具组成。Daily Log 每天 append-only 写入 `memory/YYYY-MM-DD.md`，Session 启动时读取今天和昨天的日志；`MEMORY.md` 存储长期事实，只在 main/private session 中加载；上下文接近上限时触发 Pre-Compaction，后台隐藏 turn 会把重要信息保存到记忆和 Daily Log，再压缩旧上下文。搜索工具包含 `memory_search` 语义搜索和 `memory_get` 精确读取。导图还记录了向量记忆、BM25 和本地文件记忆的组合。

OpenClaw 的哲学偏向极简和自我扩展。导图强调 CLI 是智能体连接世界的主要接口，核心工具只有 Read、Write、Edit、Bash；OpenClaw 不内置 MCP，而是鼓励通过 CLI 或 mcporter skill 桥接。Skill、记忆和扩展可被 Agent 自己重写、修复和重载。自动化层包括 Hook、Gateway 内置定时任务、心跳、Webhooks 和 Gmail PubSub；心跳适合多项周期检查、上下文感知决策和低开销监控。架构 sheet 进一步补充 Gateway、Channel、AI Agent Runtime、插件扩展系统、多 Agent 隔离、会话工具、Docker 沙箱、Canvas/A2UI、语音唤醒和 Talk Mode。

## Key Claims

- explicit: OpenClaw 的核心架构由 Gateway、Node、Channel 三层组成。
- explicit: OpenClaw 采用 Loopback-first 设计，默认不开放外网端口；远程访问通过 Tailscale Serve/Funnel 或 SSH 转发。
- explicit: Daily Log 每日 append-only 写入 `memory/YYYY-MM-DD.md`，Session 开启时会读取今天和昨天的日志。
- explicit: `MEMORY.md` 是长期记忆文件，只在 main/private session 中加载，群组隔离 session 不会看到。
- explicit: OpenClaw 的核心工具被描述为 Read、Write、Edit、Bash，设计哲学偏 Unix 小工具和文本流。
- explicit: OpenClaw 不内置 MCP，导图建议通过 CLI 或 mcporter skill 进行桥接。
- explicit: OpenClaw 支持 Hook、定时任务、心跳、Webhooks、多 Agent、子智能体和会话工具。
- inferred: OpenClaw 是 Agent runtime 设计中的「本地优先、自我扩展、极简工具面」样本，适合与 Hermes、Nano Bot、Coze 形成对比。

## External Links

- local-service: [OpenClaw Web UI](http://localhost:18789) — local Web UI address shown in source; not verified.
- extended-reading: [OpenClaw 系统架构设计与二次开发手册](https://github.com/MindDock/OpenClaw-Dev-Guide) — listed as architecture/development guide; not verified.
- extended-reading: [OpenClaw 架构深度解析：如何把 AI 助手搬到你的个人设备上](https://juejin.cn/post/7611158381474250778) — listed as extended reading; not verified.
- extended-reading: [深度解析：一张图拆解OpenClaw的Agent核心设计](https://zhuanlan.zhihu.com/p/2004505448938767308) — listed as extended reading; not verified.
- extended-reading: [一文彻底搞懂 OpenClaw 的架构设计与运行原理（万字图文）](https://juejin.cn/post/7610830383229124659?searchId=202603171100347BC714816CDFEF435A10) — listed as extended reading; not verified.
- extended-reading: [OpenClaw 完全指南：这可能是全网最新最全的系统化教程了！](https://zhuanlan.zhihu.com/p/2015027745743189513) — listed as extended reading; not verified.
- extended-reading: [OpenClaw 架构深度拆解](https://x.com/0XBrianXYZ/status/2027931510947598598) — listed as extended reading; not verified.
- extended-reading: [你不知道的 Agent：原理、架构与工程实践](https://x.com/HiTw93/status/2034627967926825175) — listed as extended reading; not verified.
- skill-install: [clawdis mcporter skill](https://github.com/steipete/clawdis) — listed in CLI skill install command; not verified.
- skill-ecosystem: [skills.sh](https://skills.sh/) — listed as skills ecosystem resource; not verified.

## Links

No downstream wiki pages were created or updated in this scoped ingest.

## Maintenance Notes

- XMind helper reported `ok: true`; no `sheets_error`.
- Some branches are structural placeholders or sparse, including empty nodes under `三层架构`, `通信流程`, `CLI`, and `生态`; they were not treated as detailed claims.
- External links were extracted from the XMind export and were not browsed or verified.
- This batch intentionally did not update `index.md` or `log.md`.

- Link cleanup candidate: batch-boundary: No wiki concept, entity, synthesis, map, index, or log pages were created or updated for this batch, per task instruction.
- Link cleanup candidate: compile-candidate: OpenClaw; Loopback-first Agent; 本地优先 Agent runtime; Agent 记忆系统; Agent 工作区; Agent 心跳; Skills 生态; 多 Agent 隔离.
