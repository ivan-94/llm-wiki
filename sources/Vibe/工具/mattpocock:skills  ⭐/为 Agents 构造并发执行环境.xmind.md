---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind"
raw_created_at: 2026-06-01T10:42:26.453483+00:00
raw_modified_at: 2026-06-01T10:42:26.542267+00:00
raw_size: 2728350
raw_fingerprint: "size=2728350;birth=2026-06-01T10:42:26.453483+00:00;mtime=2026-06-01T10:42:26.542267+00:00"
raw_snapshot_at: 2026-06-01T13:47:46.128658+00:00
ingested_at: 2026-06-01
status: ingested
---

# 为 Agents 构造并发执行环境.xmind

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/%E4%B8%BA%20Agents%20%E6%9E%84%E9%80%A0%E5%B9%B6%E5%8F%91%E6%89%A7%E8%A1%8C%E7%8E%AF%E5%A2%83.xmind>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-01T10:42:26.453483+00:00`; modified `2026-06-01T10:42:26.542267+00:00`; size `2728350`; snapshot `2026-06-01T13:47:46.128658+00:00`
- Coverage: XMind helper exported all sheets; `sheet_count=1`; `0` titled `为 Agents 构造并发执行环境` with 75 topics.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供工作流技能总体方法论。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind]] — 同属个人 Agent 工作流 cluster，提供端到端流程位置。

## Summary

这份 XMind 设计面向并发 Agent 的隔离执行环境：用 git worktree 分离文件系统，用独立 Compose 分离运行时和状态，并用 `.agent/bin/agent` 脚本统一沙箱生命周期。

## Source Digest

source 先指出 dev container 面向人类开发者，默认带有固定 container、固定端口和单工作区假设；并发 Agent 任务还需要处理端口冲突、不能共享现有实例、状态隔离和日志定位问题。因此它提出 `docker-compose.agent.yml` 继承共享 compose：镜像、build、MySQL/Redis、Maven/Node cache 可以共享，但 MySQL/Redis 数据和 compose project 默认隔离。

source 的关键设计是把 Agent sandbox 变成可管理对象：`.agent/runs/{id}` 保存 manifest、端口和日志；`.agent/bin/agent init/up/exec/start/stop/migrate/status/logs/destroy` 管理生命周期；业务脚本在容器内用 `.agent-runtime/bin/project start/stop/migrate/status/wait` 保持幂等、健康检查和机器可读输出。

## Key Claims

- explicit: dev container 面向人类开发者，并发 Agent 任务需要额外处理端口冲突和实例隔离。
- explicit: Agent compose sandbox 应使用独立 compose project，端口动态分配，cache 可共享，state 默认隔离。
- explicit: 每个 sandbox 应生成 manifest，避免 Agent 靠记忆保存状态。
- explicit: Agent CLI 应提供 init、up、exec、start、stop、migrate、status、logs、destroy 等生命周期命令。
- explicit: `status --json` 和友好的 `--help`/错误信息是 Agent 可操作性的关键。
- inferred: Agent Runtime 的核心不是 Docker 本身，而是把运行环境状态、端口、日志、健康检查和幂等操作产品化。

## External Links

No external links found in extracted content.

## Links

- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 Matt Pocock 扩展 skill 在工作流链路中的位置。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 workflow/helper/lightweight skills 的具体节点。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 提供 Matt Pocock Skills 扩展集证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock Skills 工具 cluster。

## Maintenance Notes

- XMind helper 成功导出全部 1 个 sheet；每个 sheet 已在本次批量 ingest 中读取并消化。
- 本 source note 是批量 ingest 生成的消化层，不保存完整 raw 导出；需要细节时应回 raw XMind。