---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind"
raw_created_at: 2026-05-11T01:36:02.940063+00:00
raw_modified_at: 2026-05-11T01:36:02.941113+00:00
raw_size: 2769304
raw_fingerprint: "size=2769304;birth=2026-05-11T01:36:02.940063+00:00;mtime=2026-05-11T01:36:02.941113+00:00"
raw_snapshot_at: 2026-05-29T15:54:31.079021+00:00
ingested_at: 2026-05-29
status: ingested
---

# 为 Agents 构造并发执行环境.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E5%A4%A7%E8%A7%84%E6%A8%A1%20AI%20Coding/%E4%B8%BA%20Agents%20%E6%9E%84%E9%80%A0%E5%B9%B6%E5%8F%91%E6%89%A7%E8%A1%8C%E7%8E%AF%E5%A2%83.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-11T01:36:02.940063+00:00`; modified `2026-05-11T01:36:02.941113+00:00`; size `2769304`; snapshot `2026-05-29T15:54:31.079021+00:00`
- Coverage: exported all sheets with `.codex/skills/ai-wiki-xmind-ingest/scripts/export_xmind_source.py`; 1 sheet read and digested.
- Sheets: `0 为 Agents 构造并发执行环境` (75 topics).

## Summary

这份 source 设计了多 agent 并发执行的工程运行环境：文件系统使用 git worktree，运行环境从人类 dev container 扩展为 agent 专用 Docker Compose sandbox，并通过 `.agent/bin/agent` 与 `.agent-runtime/bin/project` 封装初始化、启动、执行、迁移、状态、日志、等待和清理等操作。

## Source Digest

source 的核心问题是：面向人类开发者的 dev container 不能直接满足多个 agent 并发执行任务。人类环境通常固定 container name、固定端口、单工作区挂载、固定日志和 node_modules volume；并发 agent 则需要避免端口冲突、不能共享已有容器实例，并且需要在共享 cache 与隔离 state 之间做清晰边界。

方案把环境拆成共享 Compose 与 agent Compose：共享层复用 image、build、MySQL、Redis、Maven cache、Node 运行环境和 node modules cache；agent 层通过 `WORKTREE_PATH` 挂载独立 worktree，用动态端口映射 admin/api/ui，注入 `AGENT_ID` 和 HAT 开关，并使用 compose project name 形成隔离命名空间。它建议 Maven/npm/pnpm cache 可共享，MySQL/Redis 数据默认每个 agent 独立。

source 进一步提出外层 `.agent/bin/agent` CLI 管理 sandbox 生命周期，内层 `.agent-runtime/bin/project` 管理业务程序生命周期。关键机制包括：`init/up/exec/start/stop/migrate/status/logs/down/clean` 命令，`.agent/runs/{id}/agent.env` 和 `manifest.json` 持久化端口、URL、worktree、compose files、logs 和 artifacts，不让 agent 靠记忆维护运行状态；端口自动分配、幂等操作、exec 与 start 区分、统一日志、健康检查和 JSON 状态输出都是 agent-friendly runtime 的必要约束。

## Key Claims

- explicit: 多 agent 并发执行需要 git worktree 级文件系统隔离。
- explicit: dev container 面向人类开发者，直接用于并发 agent 会遇到端口冲突和共享实例问题。
- explicit: agent Compose 应通过独立 project namespace、动态端口和独立 worktree 来隔离运行环境。
- explicit: build/image/Maven cache/Node cache 等运行时资源可以共享，但 MySQL/Redis 数据默认应按 agent 隔离。
- explicit: 每个 sandbox 应生成 manifest，让 agent 从文件读取状态、端口、URL、日志位置和 artifacts，而不是依赖上下文记忆。
- explicit: `exec` 应用于一次性 test/lint/compile，`start` 应用于长期服务，服务启动要幂等。
- explicit: CLI 应提供机器可读的 `status --json`、友好 `--help`、错误信息和健康检查。
- inferred: 这份 source 是把 Vibe Coding 从个人会话实践推进到多 agent 工程平台的基础设施设计。
- inferred: `.agent/bin/agent` 与 `.agent-runtime/bin/project` 的双层 CLI 边界，可以降低 HAT、browser acceptance 和并行开发的运行时不确定性。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/Agent Runtime|Agent Runtime]] — 可沉淀 agent sandbox、manifest、动态端口、日志和状态查询契约。
- related: [[concepts/Agent Runtime|Agent Runtime]] — 可总结 worktree、Compose project、cache/state 边界和生命周期命令。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为大规模 AI Coding 基础设施章节入口。

## Maintenance Notes

- 本批 worker 被限制不创建或修改编译层页面；Links 仅记录候选关系。
- Source 中的 YAML、JSON 和 CLI 片段是设计草案；source note 已提炼关键契约，未保存完整示例代码。

- Link cleanup candidate: related: HAT 友好运行环境 — 可连接 HAT/browser 验收所需的服务启动、wait、日志和 artifact 机制。.
