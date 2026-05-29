---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/Skills.xmind"
source_relpath: "Agent/Skills.xmind"
raw_created_at: 2026-03-16T00:15:54.678756+00:00
raw_modified_at: 2026-04-27T07:47:28.017880+00:00
raw_size: 1356199
raw_fingerprint: "size=1356199;birth=2026-03-16T00:15:54.678756+00:00;mtime=2026-04-27T07:47:28.017880+00:00"
raw_snapshot_at: 2026-05-29T22:03:23.001735+00:00
ingested_at: 2026-05-30
status: ingested
---

# Skills.xmind

## Source

- Raw file: [Agent/Skills.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/Skills.xmind>)
- Raw ref: `raw:Agent/Skills.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-03-16T00:15:54.678756+00:00`; modified `2026-04-27T07:47:28.017880+00:00`; size `1356199`; snapshot `2026-05-29T22:03:23.001735+00:00`
- Coverage: all XMind sheets exported and digested; sheet count `2`; sheets: `0: Skills` with `179` topics, `1: 开发` with `8` topics.

## Summary

这份 mind map 系统整理 Agent Skills：它们是由指令、脚本和资源组成的可迁移操作手册，通过渐进式加载向 Agent 按需提供程序性知识、组织上下文和工作流能力。

## Source Digest

source 把 Skill 定义为包含 `SKILL.md` 的文件夹，至少有 `name` 与 `description` 元数据，也可以打包 scripts、references 和 assets。它的本质被归为提示词工程和上下文工程：把团队、公司或用户的程序性知识封装成 Agent 可发现、可审计、可复用的包。对作者来说，一次构建可部署到多个 Agent 产品；对工具和企业来说，Skill 是扩展能力和沉淀组织知识的标准载体。

材料重点不只是目录结构，而是 Agent 如何处理 Skill。发现阶段只暴露 name/description；激活阶段加载完整 `SKILL.md`；执行阶段再按需读取引用文件或运行脚本。source 进一步强调 description 是给模型判断触发条件用的，不是摘要；references 要聚焦且避免深层链式引用；scripts 应面向 Agent 使用，具备结构化输出、非交互、幂等、清晰错误、dry-run、退出码和可预测输出大小等特征。

最佳实践部分把 Skill 视为文件系统驱动的渐进式披露机制，建议建立踩坑点章节、利用代码资源减少 Agent 重造样板、避免过度限制 Claude、考虑初始配置与记忆存储，并用 On Demand Hooks 在必要时激活主观或高价值约束。第二张 sheet 额外记录了 skills.sh 发现规则和 `/skills` 目录放置约定，但内容较薄，主要作为实现入口线索。

## Key Claims

- explicit: Agent Skills 是由指令、脚本和资源组成的文件夹，Agent 可以发现并使用它们以更准确、高效地完成任务。
- explicit: 一个技能至少包含 `SKILL.md`，其中有 `name`、`description` 和执行任务所需的指令；也可包含 scripts、references、assets。
- explicit: Skill 通过按需加载程序性知识、组织上下文和用户特定上下文来发挥作用。
- explicit: Agent 对 Skill 的典型处理路径是发现、激活、执行，先加载轻量元数据，再读完整指令，再按需使用资源。
- explicit: scripts 应该有结构化输出、清晰错误、非交互行为、幂等性、安全默认值和可预测输出大小。
- inferred: 高质量 Skill 是一种 agent-facing workflow artifact，既是知识包，也是轻量运行协议。
- inferred: `description` 字段是 Skill 触发准确性的核心控制面，过宽或摘要式描述会降低可用性。

## External Links

- spec: [Agent Skills specification](https://agentskills.io/specification) — source 根节点链接；not verified.
- scripting: [Using scripts in skills](https://agentskills.io/skill-creation/using-scripts#use-structured-output) — 结构化输出和脚本设计参考；not verified.
- validation: [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) — 技能验证参考库；not verified.
- description: [Agent Skills description guidance](https://agentskills.io/skill-creation/optimizing-descriptions) — description 触发设计参考；not verified.
- reference: [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — Claude Code 参考资料；not verified.
- article: [构建 Claude Code 的经验教训：我们如何使用 Skills](https://x.com/trq212/status/2033949937936085378) — Claude Code Skills 经验文章；not verified.
- docs: [Claude Code Skills 最佳实践](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Claude Skills 最佳实践；not verified.
- article: [写好 Skills 的 7 个原则](https://x.com/yibie/status/2024423864068178308) — Skills 写作经验文章；not verified.
- market: [ClawHub](https://clawhub.ai/skills?sort=downloads) — Skills 市场入口；not verified.
- repository: [anthropics/skills](https://github.com/anthropics/skills) — Skills 仓库；not verified.
- repository: [openai/skills](https://github.com/openai/skills) — Skills 仓库；not verified.
- repository: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Skills 仓库；not verified.
- repository: [baoyu-skills](https://github.com/JimLiu/baoyu-skills) — Skills 示例仓库；not verified.
- repository: [antfu/skills](https://github.com/antfu/skills) — Skills 示例仓库；not verified.
- repository: [superpowers](https://github.com/obra/superpowers/tree/main/skills) — Skills 示例仓库；not verified.
- repository: [mattpocock/skills](https://github.com/mattpocock/skills) — Skills 示例仓库；not verified.
- tool: [agent-skills](https://github.com/vercel-labs/skills) — skill 管理/发现工具线索；not verified.
- docs: [Claude Skills best-practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — 第二张 sheet 的 Claude Skills 最佳实践链接；not verified.

## Links

- related: [[concepts/Agent Skills|Agent Skills]] — source 是现有 Agent Skills 概念页的直接补强材料。
- related: [[concepts/上下文工程|上下文工程]] — source 明确把 Skills 归入上下文工程和渐进式披露。
- related: [[concepts/Agent Harness|Agent Harness]] — scripts、hooks、资源加载和 skill discovery 可补充 harness 控制面。
- related: [[entities/Anthropic|Anthropic]] — source 多处引用 Claude/Anthropic Skills 文档和实践，但未核验当前产品状态。

## Maintenance Notes

- No issues. Two sheets were discovered, exported, read, and digested.
- Sheet `开发` 信息量较薄，只提供 skills.sh 发现规则和 `/skills` 目录约定线索。
- Compile candidates: Agent Skills, 渐进式披露, Skill description 触发设计, Skill scripts 设计, On Demand Hooks, Skills 市场.
