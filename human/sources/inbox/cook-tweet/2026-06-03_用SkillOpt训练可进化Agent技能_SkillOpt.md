---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt.md"
source_relpath: "inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt.md"
raw_created_at: 2026-06-03T20:41:39+08:00
raw_modified_at: 2026-06-05T09:27:30+08:00
raw_size: 9852
raw_fingerprint: "size=9852;birth=2026-06-03T20:41:39+08:00;mtime=2026-06-05T09:27:30+08:00"
raw_snapshot_at: 2026-06-05T10:30:50+08:00
ingested_at: 2026-06-05
status: ingested
---

# 用 SkillOpt 训练可进化 Agent 技能

## Source

- Human raw: [[human/raw/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]]
- Raw ref: `human-raw:inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-03T20:41:39+08:00`; modified `2026-06-05T09:27:30+08:00`; size `9852`; snapshot `2026-06-05T10:30:50+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-tweet`
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — eval loop 和 SkillOpt 都依赖可评分样例与失败回写。
  - same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders|AI Agent 协作提示链]] — 一个是人工设计提示链，一个是用验证集优化 skill 文本。

## Summary

这份 X article cook note 把 Microsoft SkillOpt 解释为“训练 skill 文本”的方法：不改模型权重，而是让目标模型带当前 skill 跑样例，优化器模型提出小幅文本编辑，再用验证集决定是否接受，最终部署 `best_skill.md`。

## Source Digest

本 source 对 [[concepts/Agent Skills|Agent Skills]] 的关键补充是：skill 可以从手写 prompt 变成可评估资产。SkillOpt 的前置条件不是“写更好提示词”，而是准备 train/val/test 样例、answer key、scorer 和 no-skill baseline，让每次编辑都经过 held-out data 检查。

它也补强 [[concepts/LLM 评估|LLM 评估]] 与 [[concepts/LLMOps|LLMOps]]：评估不只用于模型或应用输出，也可以用于长期加载的 skill 文本。可审计的 `best_skill.md` 比不可读的模型权重更适合作为团队资产，尤其适合 extraction、classification、QA、可运行代码和其他有标准答案的任务。

对 AI wiki 来说，这提示 cook/ingest/HAT 类 skill 的自进化要从窄任务开始：frontmatter 完整性、Source Manifest 是否包含 cache path、是否越过 human/raw 边界、Links 是否有关系类型等，都比“观点质量”更适合先做样例评分。

## Key Claims

- explicit: SkillOpt 优化的是 skill 文本，不是模型权重；部署产物仍是普通 `best_skill.md`。
- explicit: SkillOpt 适合 extraction、classification、QA、可运行代码等有标准答案的任务，不适合无法定义正确性的任务。
- explicit: answer key 是流程关键输入，脏样例会把验证门优化到错误目标。
- explicit: 务实路径是借用现有 benchmark 形状，小样本低成本试跑，再决定是否扩大训练成本。
- inferred: agent skills 要可自进化，前提是把成功标准转成可批量评分的样例集。
- inferred: AI wiki 应优先把边界、结构和格式要求转成 regression examples，而不是直接优化主观内容质量。

## External Links

- X status: https://x.com/hooeem/status/2061528919786791154 — raw input URL; not verified during this ingest.
- Twitter embed: https://twitter.com/hooeem/status/2061528919786791154 — embed URL recorded in raw note; not verified during this ingest.
- X article: https://x.com/hooeem/article/2061528919786791154 — article URL recorded in raw note; not verified during this ingest.
- GitHub repository: https://github.com/microsoft/SkillOpt — external link observed in raw note; not verified during this ingest.
- Project site: https://microsoft.github.io/SkillOpt/ — external link observed in raw note; not verified during this ingest.
- Paper PDF: https://arxiv.org/pdf/2605.23904 — external link observed in raw note; not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 补充 skill 文本可训练、可验证、可审计的资产视角。
- compiled-concept: [[concepts/LLM 评估|LLM 评估]] — 补充用 train/val/test、answer key 和 baseline 评估 skill 文本。
- compiled-concept: [[concepts/LLMOps|LLMOps]] — 将 prompt/skill 版本化、数据集和评估标准纳入同一持续改进闭环。
- compiled-synthesis: [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]] — 将 SkillOpt 编译为 skill 文本从失败样例中演进的学习阶段。
- same-cluster: [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — SkillOpt 可以看作 eval loop 在 skill 文本层面的应用。
- related: [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — 两者都把 skill 当成可版本化、可验证、可维护的工程资产。

## Maintenance Notes

- Microsoft SkillOpt 作为候选实体保留在本节；目前只在本 source 中出现，先不建独立实体页。
- 原文没有打开或联网核验 GitHub、项目站点、arXiv 链接；SkillOpt 当前状态需要官方来源核验。
- 原文信息图位于 `human/raw/inbox/cook-tweet/assets/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt/infographic.webp`，本次未复制到 `assets/`。
