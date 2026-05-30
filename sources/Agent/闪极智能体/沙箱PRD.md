---
source_type: markdown
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/闪极智能体/沙箱PRD.md"
source_relpath: "Agent/闪极智能体/沙箱PRD.md"
raw_created_at: 2026-04-09T08:17:46.597382+00:00
raw_modified_at: 2026-04-09T08:27:42.325945+00:00
raw_size: 13889
raw_fingerprint: "size=13889;birth=2026-04-09T08:17:46.597382+00:00;mtime=2026-04-09T08:27:42.325945+00:00"
raw_snapshot_at: 2026-05-29T22:04:47.907285+00:00
ingested_at: 2026-05-30
status: ingested
---

# 沙箱PRD.md

## Source

- Raw file: [Agent/闪极智能体/沙箱PRD.md](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E9%97%AA%E6%9E%81%E6%99%BA%E8%83%BD%E4%BD%93/%E6%B2%99%E7%AE%B1PRD.md>)
- Raw ref: `raw:Agent/闪极智能体/沙箱PRD.md`
- Type: markdown
- Status: ingested
- Raw metadata: created `2026-04-09T08:17:46.597382+00:00`; modified `2026-04-09T08:27:42.325945+00:00`; size `13889`; snapshot `2026-05-29T22:04:47.907285+00:00`
- Coverage: full raw Markdown file read.

## Summary

这份 PRD 定义了一个基于 `nsjail` 的多用户 Shell 命令执行服务 MVP。服务通过 HTTP API 接收纯文本 Shell 脚本，用 `bash -lc` 在隔离环境中执行，以 SSE 流式返回输出，并用 SQLite 保存命令元数据和最终聚合结果。范围明确限定在单机、基础隔离、资源控制、并发排队、历史查询、取消和清理，不追求强安全沙箱对抗。

## Source Digest

PRD 的产品目标是为上游可信系统提供一个单机命令执行后端：用户提交命令后，Gateway 按 `user_id` 找到或创建用户级 `NsJailService`，服务维护队列、运行中任务、历史状态，并 fork `nsjail` 进程执行命令。每个用户最多 5 条命令并发，超出进入队列；服务空闲 15 分钟后可淘汰；销毁时必须确认没有残留运行任务并做兜底清理。

隔离模型围绕宿主 `/app`、`/app/data/results/<user_id>` 和 `/app/workspace/<user_id>` 展开。用户 workspace 持久化且可读写，单用户磁盘配额 2 GB；结果文件放在系统数据目录，不放入用户 workspace；jail 内不应直接暴露宿主 `/app`、其他用户目录或系统数据目录。运行时白名单包括 `bash`、Node.js 25、Python 3 和 `uv`。单命令资源限制为 1 core、512 MB、默认 30 分钟，API 可传入不超过 1800 秒的自定义超时。

数据模型采用一张 `commands` 表，保存命令 ID、用户、命令内容、超时、状态、退出码、聚合结果、结果路径、大小、截断标记、错误原因和时间戳。结果小于等于 256 KB 时入 SQLite，超过则落文件；最终聚合硬上限 10 MB，超过后标记 `result_truncated=true`。API 包含提交命令、订阅 SSE 输出、查询详情、按状态查询列表和取消命令。SSE 使用 `status`、`stdout`、`stderr`、`end` 四类标准事件。QA 计划覆盖单元、集成、真实 `nsjail` E2E 和非功能冒烟，验收重点是并发、排队、取消、超时、SSE、结果存储、隔离边界、磁盘配额和进程清理。

## Key Claims

- explicit: MVP 基于 Bun、SQLite、TypeScript、Docker Compose 和 `nsjail`，目标是单机多用户 Shell 命令执行服务。
- explicit: 用户提交的是一次性命令或多行脚本，通过 `bash -lc` 执行，不支持交互式 TTY 或长生命周期后台常驻进程。
- explicit: 客户端断开 SSE 后命令继续执行。
- explicit: 每个用户最多 5 个命令同时执行，超过后进入队列，排队和运行中的命令都允许取消。
- explicit: 命令完成、取消、超时后必须回收该任务对应的整个进程组。
- explicit: 用户 workspace 位于 `/app/workspace/<user_id>`，单用户磁盘配额为 2 GB；执行结果文件位于 `/app/data/results/<user_id>`。
- explicit: jail 内应只暴露命令运行所需最小宿主资源，且不应直接看到宿主 `/app` 内容、其他用户目录或系统数据目录。
- explicit: 单命令限制为 1 core、512 MB、默认最大 30 分钟，自定义超时时间不能超过 1800 秒。
- explicit: `commands` 表保存命令元数据和最终聚合结果，状态枚举包括 `queued`、`running`、`succeeded`、`failed`、`cancelled`、`timed_out`。
- explicit: 最终聚合结果小于等于 256 KB 存库，大于 256 KB 落文件，超过 10 MB 后停止聚合并标记截断。
- explicit: SSE 协议使用 `status`、`stdout`、`stderr`、`end` 事件，不使用裸 `[DONE]`。
- inferred: 该 PRD 更像“可信上游 + 基础隔离 + 可观测执行”的工程 MVP，而不是不可信代码执行平台。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Agent 沙箱|Agent 沙箱]] — source 是 nsjail MVP 与威胁模型差异的核心证据：用户级 NsJailService、资源边界、隔离边界、不追求强对抗。
- updates: [[entities/闪极智能体|闪极智能体]] — nsjail 沙箱服务补入闪极运行时实体证据。
- updates: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] — 支撑运行时变体对比表的沙箱列证据。
- related: [[concepts/Agent Harness|Agent Harness]] — 可补充 Agent 命令执行后端的队列、运行、观察和清理边界。

## Maintenance Notes

- Raw Markdown 已完整读取；未发现外部 URL。
- PRD 明确声明“不追求强安全对抗”，后续 compile 时不应把它误写成强隔离安全设计。
- Compile candidates: 闪极智能体沙箱 PRD, 多用户命令执行服务, nsjail MVP, SSE 命令输出协议, Agent 沙箱验收清单.
