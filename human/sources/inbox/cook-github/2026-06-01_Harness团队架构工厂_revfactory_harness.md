---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness.md"
source_relpath: "inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness.md"
raw_created_at: 2026-06-01T15:55:50+08:00
raw_modified_at: 2026-06-05T09:25:54+08:00
raw_size: 13837
raw_fingerprint: "size=13837;birth=2026-06-01T15:55:50+08:00;mtime=2026-06-05T09:25:54+08:00"
raw_snapshot_at: 2026-06-05T10:30:50+08:00
ingested_at: 2026-06-05
status: ingested
---

# Harness 团队架构工厂

## Source

- Human raw: [[human/raw/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]]
- Raw ref: `human-raw:inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-01T15:55:50+08:00`; modified `2026-06-05T09:25:54+08:00`; size `13837`; snapshot `2026-06-05T10:30:50+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-github`
- Cluster role: case
- Neighbor sources:
  - related: [[human/sources/inbox/cook-podcast/2026-05-31_Agent Harness 工程系统_硬地骇客|Agent Harness 工程系统]] — 同样围绕 Agent Harness，但本 source 是具体 GitHub 仓库案例，播客 source 是概念与工程系统解释。
  - related: [[human/sources/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders|AI Agent 协作提示链]] — 两者都把 agent 协作从提示词转成可复用的结构化协议。

## Summary

这份 promoted inbox note 消化了 `revfactory/harness` 仓库。它把 Harness 定位为 Claude Code 生态里的 team-architecture factory：根据领域描述生成 agent team、skills 和 orchestrator，而不是直接完成某个业务任务。

## Source Digest

本 source 的核心价值是提供一个“生成团队架构”的具体案例。仓库资产主要是 `skills/harness/SKILL.md` 和 `references/` 下的团队模式、orchestrator 模板、skill 写法、测试和 QA 指南。其流程先审计目标项目已有 harness，再做领域分析、选择 Agent Teams / Subagents / Hybrid 模式，生成 `.claude/agents/`、`.claude/skills/` 和 orchestrator skill，最后做结构、触发、dry-run 和对照验证。

它补强了 [[concepts/Agent Harness|Agent Harness]] 中“harness 是长期演进系统”的视角：好的 harness 不只是工具集合，还要包含团队拓扑选择、角色边界、验证和持续维护。它也补强 [[concepts/Agent Skills|Agent Skills]]：skill 是可生成、可审计、可测试、可交接的工程资产，而不是单段 prompt。

需要保留的限制是：raw note 明确没有联网核验 GitHub platform 状态、stars、issues、PR、Actions 或网页渲染；Agent Teams 依赖 experimental flag 这一事实来自仓库文档，不应直接当作当前产品状态。

## Key Claims

- explicit: `revfactory/harness` 被 raw note 定位为 L3 Meta-Factory / Team-Architecture Factory，目标是生成其他 harness，而非作为业务 harness 运行。
- explicit: 仓库支持 Pipeline、Fan-out/Fan-in、Expert Pool、Producer-Reviewer、Supervisor、Hierarchical Delegation 六类团队架构模式。
- explicit: 运行路径依赖 Claude Code v2.x、plugin system 和 Agent Teams API，并要求 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。
- inferred: Harness 的长期价值在于把 agent/skill/orchestrator 的职责边界写成可重读 contract，并用验证机制持续修正。
- inferred: 如果工作流依赖实验运行时接口，Source Manifest 和维护说明必须显式记录该依赖，避免下游 agent 把漂移风险误当成稳定能力。

## External Links

- GitHub repository: https://github.com/revfactory/harness — raw note 的输入仓库；not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent Harness|Agent Harness]] — 补充 team-architecture factory 作为 harness 设计和演进案例。
- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 补充 skill 生成、触发验证、QA 与 Progressive Disclosure 的案例。
- compiled-concept: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 agent team、subagent 和 orchestrator 的交接模式。
- compiled-synthesis: [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]] — 将 team-architecture factory 编译为可进化工作流中的团队拓扑与 orchestrator 层。
- same-cluster: [[human/sources/inbox/cook-podcast/2026-05-31_Agent Harness 工程系统_硬地骇客|Agent Harness 工程系统]] — 同主题，概念解释与仓库案例互证。
- related: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 两者都把 skill 当成可评估、可版本化的工程资产。

## Maintenance Notes

- 原文信息图位于 `human/raw/inbox/cook-github/assets/2026-06-01_Harness团队架构工厂_revfactory_harness/infographic.webp`，本次未复制到 `assets/`，因为 source note 可通过 raw link 回到原文。
- raw note 的外部 GitHub 状态没有联网核验；当前事实如版本、接口依赖和生态状态需要单独查官方来源。
