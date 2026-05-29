---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind"
raw_created_at: 2026-05-11T01:36:02.940063+00:00
raw_modified_at: 2026-05-11T01:36:02.941113+00:00
raw_size: 2769304
raw_fingerprint: "size=2769304;birth=2026-05-11T01:36:02.940063+00:00;mtime=2026-05-11T01:36:02.941113+00:00"
raw_snapshot_at: 2026-05-29T16:07:40+00:00
ingested_at: 2026-05-30
status: ingested
---

# 为 Agents 构造并发执行环境.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/%E4%B8%BA%20Agents%20%E6%9E%84%E9%80%A0%E5%B9%B6%E5%8F%91%E6%89%A7%E8%A1%8C%E7%8E%AF%E5%A2%83.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-11T01:36:02.940063+00:00`; modified `2026-05-11T01:36:02.941113+00:00`; size `2769304`; snapshot `2026-05-29T16:07:40+00:00`
- Coverage: XMind helper exported all discovered sheets; sheet count `1`; sheet titles: `为 Agents 构造并发执行环境`; topic count `75`.

## Summary

这份 XMind 规划了面向并发 agent 的项目运行环境：用 git worktree 隔离文件系统，用独立 Compose project 隔离运行时命名空间和端口，用共享 cache 降低构建成本，用 manifest、CLI 和容器内脚本让 agent 可复现地启动、测试、迁移、查看状态和清理环境。

## Source Digest

资料从人类 dev container 的限制切入：dev container 适合固定工作区和固定端口的人类开发体验，但并发 agent 不能直接共享同一个实例，否则会遇到端口冲突、容器命名冲突、共享状态污染和日志位置不确定等问题。方案保留 dev container 的基础构建能力，同时拆出面向 agent 的 Compose 覆盖文件：共享 image/build、MySQL/Redis 基础服务、Maven cache、Node 运行环境和 Node module cache；agent 侧通过 `${WORKTREE_PATH}` 挂载独立 worktree，通过 `${ADMIN_HOST_PORT:-0}` 等动态端口避免冲突，并用 Compose project 名作为隔离命名空间。

运行管理层被设计成两类脚本。容器内脚本负责业务程序生命周期，例如 start、stop、migrate、status、wait，并要求启动幂等，比如自动终止已有进程再启动。容器外 `.agent/bin/agent` 管理 sandbox，包括 init、up、exec、start、stop、migrate、status、logs、down、clean 等命令。关键设计是每个 sandbox 生成 `.agent/runs/{id}/manifest.json` 和 `agent.env`，记录 project、worktree、composeFiles、ports、urls、logs 和 artifacts，避免 agent 依靠记忆推断环境状态。

资料还强调命令语义边界：`exec` 用于 compile/test/lint 等一次性任务，`start` 用于长期服务以供 HAT/browser 使用；`down` 只停止 sandbox，`clean` 还删除独立数据卷；cache 可以共享，但 MySQL/Redis 数据默认按 agent 隔离。最后建议把通用流程写入 AGENTS.md，把详细教程和 CLI reference 放入 docs，让后续 agent 能按同一运行契约工作。

## Key Claims

- explicit: dev container 面向人类开发者，并发 agent 需要额外处理端口冲突和实例共享问题。
- explicit: agent 运行环境应通过独立 Compose project、动态端口和独立 worktree 隔离并发任务。
- explicit: image/build、Maven/npm/pnpm cache、Node 运行环境等可共享；MySQL/Redis 数据默认每个 agent 独立。
- explicit: `.agent/bin/agent` 应提供 init、up、exec、start、stop、migrate、status、logs、down、clean 等管理命令。
- explicit: 每个 sandbox 应生成 manifest，不让 agent 依靠记忆保存端口、URL、worktree 和日志位置。
- explicit: `exec` 用于一次性命令，`start` 用于启动长期服务供 HAT/browser 使用。
- inferred: 这份方案的核心目标是把 agent 并发执行从“临时命令习惯”提升为可发现、可清理、可复用的运行时契约。

## External Links

No external links found in extracted content.

## Links

- related: Agent 并发执行环境 — 可沉淀 worktree、Compose sandbox、动态端口、manifest 和 CLI 生命周期契约。
- related: Vibe Coding 工作流学习地图 — 可作为多 agent 执行和 HAT 验收基础设施节点。

## Maintenance Notes

- XMind helper succeeded with `ok: true` and empty `sheets_error`; all 1 discovered sheet was exported and digested.
- The exported workbook includes project-specific example names such as `sharge-agent-pr17`, `eye-dev`, and `glasses`; treat them as illustrative examples unless compiling into a project-specific runtime guide.
- No index/log updates were made because this batch worker was restricted to the five source notes only.
