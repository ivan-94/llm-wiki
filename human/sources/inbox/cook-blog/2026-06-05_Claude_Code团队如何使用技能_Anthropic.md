---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic.md"
source_relpath: "inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic.md"
raw_created_at: 2026-06-05T17:28:18+08:00
raw_modified_at: 2026-06-11T09:19:02+08:00
raw_size: 14155
raw_fingerprint: "size=14155;birth=2026-06-05T17:28:18+08:00;mtime=2026-06-11T09:19:02+08:00"
raw_snapshot_at: 2026-06-11T09:55:10+08:00
ingested_at: 2026-06-11
status: ingested
---

# Claude Code 团队如何使用技能

## Source

- Human raw: [[human/raw/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]]
- Raw ref: `human-raw:inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-05T17:28:18+08:00`; modified `2026-06-11T09:19:02+08:00`; size `14155`; snapshot `2026-06-11T09:55:10+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-blog`
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-blog/2026-06-05_当 AI 开始构建自己_Anthropic|当 AI 开始构建自己]] — 同为 Anthropic blog cook；本 source 聚焦 Claude Code skills 操作机制，邻居 source 聚焦 AI 研发自动化与治理窗口。
  - related: [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — 两者都把 skill 当作可持续优化的工程资产，一个强调团队实践和 gotchas，一个强调数据集驱动优化。
  - related: [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — brooks-lint 是“code quality/review skill”类别的具体案例。

## Summary

这份 Anthropic blog cook note 总结 Claude Code 团队如何规模化使用 skills：skill 不是单个 Markdown，而是包含 instructions、scripts、references、assets、data、hooks 和持久化记忆的可执行上下文包。

## Source Digest

本 source 对 [[concepts/Agent Skills|Agent Skills]] 的主要贡献，是把 skill 从“提示词说明”推进到“操作可靠性基础设施”。Anthropic 内部把 skills 归成九类：API/库参考、产品验证、数据分析、业务自动化、代码脚手架、代码质量、CI/CD、runbooks 和基础设施运维。这个分类可以直接用来审查一个 skill library 是否只堆流程，还是覆盖了真实 Agent 失败面。

它也补强 [[concepts/Skill 触发契约|Skill 触发契约]]：description 是模型路由接口，不是给人看的漂亮简介；gotchas、progressive disclosure、setup、scripts、hooks 和 memory 都服务于 failure shaping。好的 skill 应让 Agent 在正确时刻加载正确上下文，用脚本吸收机械步骤，用 hooks 只在必要时强化安全边界。

对 [[entities/Claude Code|Claude Code]] 和 [[entities/Anthropic|Anthropic]] 来说，这份 source 提供了 Anthropic 内部使用 Claude Code skills 的实践证据：数百个 active skills、Product verification 类技能的影响、sandbox -> traction -> marketplace 的晋升路径，以及用 PreToolUse hook 记录 skill 使用情况。上述内部指标只作为作者披露记录，未外部核验。

## Key Claims

- explicit: Anthropic 内部有数百个 Claude Code skills 活跃使用，skills 是 Claude Code 最常用扩展点之一。
- explicit: skill 是文件夹式上下文包，可包含 instructions、scripts、assets、data、references、configuration、hooks 和持久化记忆。
- explicit: description 应写给模型做触发判断，不是人类摘要；gotchas section 是高信号内容，应来自真实失败。
- explicit: Product verification 类 skills 被作者称为对 Claude 输出质量有最大内部可测影响的类别。
- explicit: Anthropic 的 marketplace 晋升路径是先在 sandbox/Slack 等渠道试用，有 traction 后再由 owner 提 PR。
- inferred: skill library 的质量不取决于文档量，而取决于能否把高频失败转成可发现、可验证、可组合的执行环境。
- inferred: Codex 侧的 `ai-wiki-*` skills 应优先沉淀 gotchas、验证脚本和边界错误，而不是扩写背景知识。

## External Links

- Blog article: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills — raw note input URL; not verified during this ingest.

## Links

- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 补充 Anthropic 内部 skill 分类、folder package 形态、gotchas 和 team marketplace 路径。
- compiled-concept: [[concepts/Skill 触发契约|Skill 触发契约]] — 补充 description 作为模型路由接口、progressive disclosure 和 on-demand hooks。
- compiled-entity: [[entities/Claude Code|Claude Code]] — 补充 Claude Code skills 作为核心扩展点和团队分发机制。
- compiled-entity: [[entities/Anthropic|Anthropic]] — 补充 Anthropic 内部 Claude Code skill 实践来源。
- compiled-synthesis: [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]] — 将 gotchas、measurement 和 marketplace 晋升编译为 workflow 学习回写阶段。
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]] — 作为 Agent Skills 团队化和 marketplace 化案例进入学习路径。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 作为 Anthropic Skills 工具案例进入 Vibe 工具索引。
- same-cluster: [[human/sources/inbox/cook-blog/2026-06-05_当 AI 开始构建自己_Anthropic|当 AI 开始构建自己]] — 同为 Anthropic blog cook，分别关注 agent 操作包和 AI 研发自动化。
- related: [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — brooks-lint 可视为代码质量/review skill 的协议化案例。

## Maintenance Notes

- 原文信息图位于 `human/raw/inbox/cook-blog/assets/2026-06-05_Claude_Code团队如何使用技能_Anthropic/infographic.webp`，本次未复制到 `assets/`。
- Anthropic 内部活跃技能数量、verification impact 和 PreToolUse 度量口径未外部核验；当前只作为作者披露的 explicit claim 使用。
