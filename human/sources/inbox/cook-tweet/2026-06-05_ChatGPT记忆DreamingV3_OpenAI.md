---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI.md"
source_relpath: "inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI.md"
raw_created_at: 2026-06-05T09:44:04+08:00
raw_modified_at: 2026-06-11T08:36:53+08:00
raw_size: 9723
raw_fingerprint: "size=9723;birth=2026-06-05T09:44:04+08:00;mtime=2026-06-11T08:36:53+08:00"
raw_snapshot_at: 2026-06-11T09:55:10+08:00
ingested_at: 2026-06-11
status: ingested
---

# ChatGPT 记忆进入 Dreaming V3

## Source

- Human raw: [[human/raw/inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI|ChatGPT 记忆进入 Dreaming V3]]
- Raw ref: `human-raw:inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-05T09:44:04+08:00`; modified `2026-06-11T08:36:53+08:00`; size `9723`; snapshot `2026-06-11T09:55:10+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-tweet`
- Cluster role: supplement
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — 两者都关注长期系统质量：一个从 memory freshness，一个从 eval loop。
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 记忆更新和 skill 优化都要求持续学习不能污染未来上下文。
  - related: [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — Claude Code skill memory 与 ChatGPT Dreaming 都把持久化上下文变成可审阅控制面。

## Summary

这份 X post cook note 解读 OpenAI《Dreaming: Better memory for a more helpful ChatGPT》：ChatGPT memory 正从用户显式保存的条目，推进到后台合成、持续更新、可审阅的上下文状态。

## Source Digest

本 source 对 [[concepts/Agent 记忆|Agent 记忆]] 的关键补充是：长期记忆的核心风险不是缺少事实，而是过期事实仍被信任。Dreaming V3 的重点被 raw note 概括为 freshness、continuity、relevance：系统要在后台合成 memory state，随着时间和后续对话更新用户上下文，并让用户通过 memory summary page 审阅和修正。

它也补强 [[concepts/Agent 全局记忆|Agent 全局记忆]]：AI wiki 的 `human/raw` / `human/sources` / `concepts` 分层类似“证据层 -> 合成记忆层”。可靠的长期知识不能跳过来源层，直接把摘要当事实；它需要 Source Manifest、review/doctor 机制、过期策略和冲突修订。

对产品事实要谨慎：raw note 明确指出 OpenAI 原文是分阶段 rollout，Plus/Pro 美国先行，更多国家和 Free/Go 用户在未来几周扩展；不能从中文 X post 推断所有用户层级已同等可用。

## Key Claims

- explicit: OpenAI 原文把 memory 演进描述为从 Saved Memories 到 Dreaming，再到更可独立、更高效的 Dreaming V3。
- explicit: OpenAI 原文强调 memory 要改善 freshness、continuity 和 relevance，并分阶段 rollout。
- explicit: 原文提到约 5x 计算效率提升，使 dreaming-based memory 更可扩展。
- inferred: 这次更新不是单纯扩大记忆容量，而是把离散 saved memory 推向后台合成的 memory state。
- inferred: 长期记忆必须有来源、可审阅、可修订、会过期，否则会把陈旧上下文包装成个性化能力。
- inferred: AI wiki 的 source note 与 synthesis 分层可以视为个人知识系统里的 Dreaming 控制面：证据可追溯，合成判断可更新。

## External Links

- X status: https://x.com/shao__meng/status/2062690152569614572 — raw note input URL; not verified during this ingest.
- Twitter embed: https://twitter.com/shao__meng/status/2062690152569614572 — embed URL recorded in raw note; not verified during this ingest.
- OpenAI original: https://openai.com/index/chatgpt-memory-dreaming/ — official article URL recorded in raw note; not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent 记忆|Agent 记忆]] — 补充 freshness、staleness、reviewable memory summary 和 memory state。
- compiled-concept: [[concepts/Agent 全局记忆|Agent 全局记忆]] — 补充证据层、合成记忆层和过期/修订机制的类比。
- compiled-entity: [[entities/GPT 与 ChatGPT|GPT 与 ChatGPT]] — 补充 ChatGPT memory / Dreaming V3 作为产品记忆案例。
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]] — 作为长期记忆 freshness / staleness 治理案例进入学习路径。
- same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — memory freshness 与 eval loop 都是长期 agent 系统的质量控制面。
- same-cluster: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 记忆和 skill 文本都需要从失败/新证据中更新，且不能污染未来上下文。

## Maintenance Notes

- 原文信息图位于 `human/raw/inbox/cook-tweet/assets/2026-06-05_ChatGPT记忆DreamingV3_OpenAI/infographic.webp`，本次未复制到 `assets/`。
- OpenAI memory / Dreaming V3 是时间敏感产品事实；如需回答当前可用范围，必须重新核验官方来源。
