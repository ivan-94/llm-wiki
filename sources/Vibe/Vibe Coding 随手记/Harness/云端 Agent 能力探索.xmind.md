---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind"
source_relpath: "Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind"
raw_created_at: 2026-05-23T13:14:00.922486+00:00
raw_modified_at: 2026-05-23T14:26:00.355623+00:00
raw_size: 294228
raw_fingerprint: "size=294228;birth=2026-05-23T13:14:00.922486+00:00;mtime=2026-05-23T14:26:00.355623+00:00"
raw_snapshot_at: 2026-05-29T15:54:16.975722+00:00
ingested_at: 2026-05-29
status: ingested
---

# 云端 Agent 能力探索.xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Harness/%E4%BA%91%E7%AB%AF%20Agent%20%E8%83%BD%E5%8A%9B%E6%8E%A2%E7%B4%A2.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Harness/云端 Agent 能力探索.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-23T13:14:00.922486+00:00`; modified `2026-05-23T14:26:00.355623+00:00`; size `294228`; snapshot `2026-05-29T15:54:16.975722+00:00`
- Coverage: helper exported all 3 sheets: `画布 1` with title-only overview, `Codex` with 40 topics, and `claude code` with 54 topics.

## Summary

这份 XMind 对比整理了 Codex 与 Claude Code 的云端执行、自动化、客户端集成、多智能体编排和 GitHub workflow 能力。核心主题是：云端 coding agent 不只是“远程聊天”，而是围绕运行环境、权限边界、事件流、恢复机制、审查/计划模式和 CI/GitHub 集成形成一套可产品化的工程执行层。

## Source Digest

工作簿先用一个标题页标出“云端 Agent 能力探索”，随后把 Codex 和 Claude Code 分成两条能力谱系。

Codex 侧强调 OpenAI 托管容器、Cloud Environments、setup/agent 阶段隔离、`codex exec` 非交互自动化、Codex SDK、App Server、Codex MCP 和 GitHub Action。它的知识贡献在于把 Codex 能力拆成多层接入方式：最轻的是 CLI 脚本化，往上是 SDK 线程管理，再往上是 App Server 级客户端，最后是 MCP/Agents SDK 编排与 GitHub workflow 自动化。

Claude Code 侧强调 Anthropic 托管 VM、Claude Code on the web、cloud session、environment caching、网络访问级别、GitHub proxy/security proxy、Routines、`ultraplan`、`ultrareview`、托管 PR review 和 GitHub Actions。它的知识贡献在于把 Claude Code 的云端能力拆成任务执行、环境初始化、安全出网、可重复 routine、云端规划、深度审查和 GitHub 事件触发。

两条谱系共同指向一个长期判断：云端 agent 能力的关键不在“能不能改代码”，而在环境可复现、权限可控、状态可恢复、结果可审阅、任务可自动触发，以及能否接入组织现有的 CI、PR、review、triage 和 release 流程。

## Key Claims

- explicit: Codex 云端执行依赖托管容器与 Cloud Environments，setup 阶段适合安装依赖和访问 secrets，agent 阶段适合改代码、跑测试与总结，且默认不联网、secrets 被移除。
- explicit: `codex exec` 被定位为非交互 CLI agent，可接收日志、diff、curl 结果等输入，并通过 stdout/stderr、JSONL 事件流和 output schema 服务脚本化流程。
- explicit: Codex SDK、App Server、Codex MCP 和 GitHub Action 分别面向产品化集成、完整客户端、多 agent 编排和 GitHub workflow 自动化。
- explicit: Claude Code 云端会话可从 GitHub clone repo、运行 setup、改代码、跑测试、推分支，并通过网页 diff、inline feedback 和 PR 继续迭代。
- explicit: Claude Code environment 包含 setup script、environment caching、SessionStart hooks、repo 内配置和常用预装工具；网络能力区分 None、Trusted、Full、Custom，并使用 GitHub proxy/security proxy 控制风险。
- explicit: Claude Code Routines、`ultraplan`、`ultrareview`、托管 Code Review 和 GitHub Actions 分别覆盖定时/API/GitHub 触发、复杂计划、深度审查、PR 自动审查和 workflow 自动化。
- inferred: Codex 的能力栈更适合按“CLI 自动化 -> SDK 嵌入 -> App Server 客户端 -> MCP 编排”理解；Claude Code 的能力栈更适合按“云端会话 -> environment/security -> routine -> plan/review -> GitHub workflow”理解。
- inferred: 选择云端 agent 集成方式时，应优先根据任务是否需要产品化线程管理、客户端级事件/审批、复杂多 agent 编排、或 GitHub 事件自动触发来分层，而不是只比较模型或聊天体验。

## External Links

No external links found in extracted content.

## Links

- related: 云端 Coding Agent — 本 source 可支撑云端 coding agent 的环境、权限、执行、恢复和审查能力定义。
- related: Agent 自动化工作流 — 本 source 可补充 CLI、SDK、MCP、GitHub Action、routine 与 CI 触发的分层模型。
- entity-candidate: Codex — 本 source 整理 Codex 的云端、CLI、SDK、App Server、MCP 和 GitHub Action 能力边界。
- compiled-entity: [[entities/Claude Code|Claude Code]] — 本 source 整理 Claude Code 的云端会话、environment、routine、plan/review 和 GitHub Actions 能力边界。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为云端 agent 平台能力与工作流选型章节的证据入口。

## Maintenance Notes

- Sheet `画布 1` 只有根标题，无实质分支；已作为封面/总题处理。
- 未联网核验 Codex、Claude Code、OpenAI 或 Anthropic 的当前产品细节；本 note 仅反映 raw 中的整理内容。
