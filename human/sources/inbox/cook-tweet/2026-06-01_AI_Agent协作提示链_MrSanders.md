---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders.md"
source_relpath: "inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders.md"
raw_created_at: 2026-06-01T15:12:01+08:00
raw_modified_at: 2026-06-05T09:22:56+08:00
raw_size: 7474
raw_fingerprint: "size=7474;birth=2026-06-01T15:12:01+08:00;mtime=2026-06-05T09:22:56+08:00"
raw_snapshot_at: 2026-06-05T10:30:50+08:00
ingested_at: 2026-06-05
status: ingested
---

# AI Agent 协作提示链

## Source

- Human raw: [[human/raw/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders|AI Agent 协作提示链]]
- Raw ref: `human-raw:inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-01T15:12:01+08:00`; modified `2026-06-05T09:22:56+08:00`; size `7474`; snapshot `2026-06-05T10:30:50+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-tweet`
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — 同为 X article/post 消化，分别关注实现前结构协议和输出后质量门。
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 同为 agent 工作流改进材料，分别关注提示链协议和 skill 文本优化。

## Summary

这份 X post cook note 把 agent 协作拆成一条提示链：先做 anchored architecture review，再迭代分析文本，画类型接口、调用栈、seams、adapters 和 production/test 双调用图，最后沉淀为 tech spec 并交给 TDD 实现。

## Source Digest

本 source 对 [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] 的贡献是提供一个设计到实现的微型协议。它强调 agent 不应直接改代码，而应先证明自己理解边界：能否锚定模块、解释 locality/cohesion 问题、展示 production/test 调用图同形、明确注入层和 adapter。

它也补强 [[concepts/Agent Brief|Agent Brief]] 和 [[concepts/Spec-Driven Development|Spec-Driven Development]]：下游执行 agent 需要的不是泛泛结论，而是接口、调用栈、约束、命名共识、团队 convention 和少量剩余 todo。把反复出现的设计约束写进 `AGENTS.md` 或 spec，可以把一次对话变成后续可复用规则。

该 source 的重要边界是：它来自未登录可见 X 页面，quote 图片和引用 post 未完整消费，适合作为工作流启发，不适合作为外部事实来源。

## Key Claims

- explicit: agent 应先做 anchored architecture review，锚定文件/模块、协作者和参考代码库来审查 locality/cohesion。
- explicit: 设计讨论应先在对话文本里逐行校准，不急于生成报告或文件。
- explicit: 候选方案应包含 public interface、调用栈、seams、production adapter 和 test/in-memory adapter。
- inferred: Production 和 Tests 调用图同形是判断抽象是否利于测试替身和依赖注入的关键检查。
- inferred: spec / `AGENTS.md` 中持久化命名、反模式和团队约定，可以减少下游 agent 重新犯同类设计错误。

## External Links

- X status: https://x.com/MrSanders/status/2060487209375990205 — raw input URL; not verified during this ingest.
- Twitter embed: https://twitter.com/MrSanders/status/2060487209375990205 — embed URL recorded in raw note; not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充“架构审查 -> 结构草图 -> spec -> TDD”的可交接链路。
- compiled-concept: [[concepts/Agent Brief|Agent Brief]] — 补充 brief 应包含结构证据、约束和实现前提。
- compiled-concept: [[concepts/Spec-Driven Development|Spec-Driven Development]] — 将设计共识转成可执行 spec 后再进入实现。
- compiled-concept: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]] — 反复出现的团队 convention 可以写回入口规则。
- compiled-synthesis: [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]] — 将架构审查、双调用图和 TDD 交接编译为实现前结构证据阶段。
- same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — 实现前结构协议与输出后质量门互补。
- same-cluster: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 手写协议与可训练 skill 都把 agent 操作变成可审查资产。

## Maintenance Notes

- 原文只基于 browser-use 可见页面，不使用 X API、搜索缓存或登录态；quoted media 未识别。
- 原文信息图位于 `human/raw/inbox/cook-tweet/assets/2026-06-01_AI_Agent协作提示链_MrSanders/infographic.webp`，本次未复制到 `assets/`。
