---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill.md"
source_relpath: "inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill.md"
raw_created_at: 2026-06-09T17:01:19+08:00
raw_modified_at: 2026-06-10T20:51:48+08:00
raw_size: 16250
raw_fingerprint: "size=16250;birth=2026-06-09T17:01:19+08:00;mtime=2026-06-10T20:51:48+08:00"
raw_snapshot_at: 2026-06-11T09:55:10+08:00
ingested_at: 2026-06-11
status: ingested
---

# 近30天多源研究技能

## Source

- Human raw: [[human/raw/inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill|近30天多源研究技能]]
- Raw ref: `human-raw:inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-09T17:01:19+08:00`; modified `2026-06-10T20:51:48+08:00`; size `16250`; snapshot `2026-06-11T09:55:10+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-github`
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — 同为 GitHub skill/tool cook；一个关注多源研究管线，一个关注 AI code review 质量协议。
  - same-cluster: [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — 同为 agent skill/plugin 仓库案例，分别展示研究技能、团队架构工厂和审查治理。
  - related: [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — last30days-skill 是“data acquisition and analysis”类 skill 的具体产品化案例。

## Summary

这份 GitHub cook note 消化了 `mvanhorn/last30days-skill`：一个通过 `/last30days <topic>` 触发的 Agent Skill，结合长 `SKILL.md` 契约和 Python engine，把 Reddit、X、YouTube、HN、Polymarket、GitHub、Web 等近 30 天社会信号融合成可引用简报。

## Source Digest

本 source 对 [[concepts/Agent Skills|Agent Skills]] 的价值在于展示“skill contract + deterministic engine”的混合形态。`SKILL.md` 约束宿主 Agent 做 preflight、query planning、输出 voice law 和 footer pass-through；Python engine 负责 source availability、并发检索、normalize、weighted RRF、rerank、cluster、HTML/SQLite 输出。

它也补强 [[concepts/Skill 触发契约|Skill 触发契约]]：当 skill 变成跨平台研究管线，触发契约不只决定是否读取说明，还决定宿主模型是否生成 `--plan`、是否遵守输出格式、是否保留 degraded warning 和 citation footer。超长 contract 可以承载复杂行为，但也带来宿主 Agent 跳读、漏遵循和维护成本。

对 AI wiki 的启发是：面向近实时社会信号的研究不能只依赖普通网页搜索；真正有价值的是跨平台 engagement、freshness、source quality、cluster 和可复用 store/watchlist。当前 source 只是静态阅读仓库，未运行代码、未验证 API/source 可用性。

## Key Claims

- explicit: `last30days-skill` 通过 Agent Skill 契约和 Python engine 提供近 30 天多源研究能力。
- explicit: 项目覆盖 Reddit、X、YouTube、TikTok、HN、Polymarket、GitHub、Web、Bluesky、Truth Social、Perplexity 等来源，部分来源需要 API key、CLI、cookies 或环境变量。
- explicit: 对命名实体、人物、产品、比较类主题，`SKILL.md` 要求宿主 Agent 生成 `--plan` JSON。
- explicit: pipeline 包含并发检索、normalize、signals、dedupe、weighted RRF、rerank、fun scoring、cluster 和可选 SQLite store。
- inferred: 这类 skill 的稳定性取决于“宿主模型契约遵循度 + 外部平台可用性 + deterministic ranking pipeline”三者同时成立。
- inferred: 多源研究 skill 适合进入 AI wiki 的 source discovery / trend monitoring 工具候选，但需要单独运行验证和 credential boundary 设计。

## External Links

- GitHub repository: https://github.com/mvanhorn/last30days-skill — raw note input repository at commit `122158415ae421da83e739f2668032f6bc78d39c`; not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 补充 data acquisition/analysis skill 的 contract + engine 结构。
- compiled-concept: [[concepts/Skill 触发契约|Skill 触发契约]] — 补充超长 skill contract、query planning 和输出契约的复杂触发案例。
- compiled-concept: [[concepts/JIT 检索（Just-in-Time Retrieval）|JIT 检索（Just-in-Time Retrieval）]] — 补充按需获取近实时多源信号的工具候选。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 作为 research/data acquisition skill 案例进入工具索引。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 作为 JIT 检索和外部信号证据输入案例进入学习路径。
- same-cluster: [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — 同为 GitHub skill/tool 案例，分别处理研究证据和审查质量。
- same-cluster: [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — 同属 agent skill/plugin 仓库案例。
- related: [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — Anthropic skill 分类中的数据获取与分析类别可容纳该项目。

## Maintenance Notes

- 原文信息图位于 `human/raw/inbox/cook-github/assets/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill/infographic.webp`，本次未复制到 `assets/`。
- `mvanhorn/last30days-skill` 作为工具/项目实体候选保留；当前只静态阅读一次，先不建独立实体页。
- 未运行仓库代码、未安装依赖、未核验 GitHub 当前状态或外部平台 API 可用性。
