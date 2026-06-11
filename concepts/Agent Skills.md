---
page_type: concept
updated_at: 2026-06-11
status: active
source_count: 32
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-05
---

# Agent Skills

## Definition

Agent Skills 是把可复用工作流、工具调用规则、交接协议和验证步骤封装成 Agent 可读取、可执行、可组合的知识单元。

## Why It Matters

单次提示会丢失上下文和经验；skill 把重复工程流程固化成可复用资产，让不同 Agent 在相似任务中少走弯路。

## Mental Model

Skill 是给 Agent 的“操作手册 + 进入条件 + 验证门禁”。

## Key Claims

- 好的 skill 不只是说明做什么，还要说明何时使用、读哪些文件、怎么验证、哪些边界不能越过。
- 工作流型 skill 可以串起 TDD、triage、PRD、issue、review、HAT 和 PR 交付。
- Helper skill 更像工程脚手架：设置 pre-commit、git guardrails、迁移测试数据、生成练习目录等。
- 图示类 source 适合做学习地图，具体实现仍要回到 skill 文件或工具文档核验。
- human source 补充：skill 文本本身可以成为可评估资产；当任务有标准答案时，可以用 train/val/test、answer key、baseline 和验证门来优化 `best_skill.md`。
- human source 补充：team-architecture factory 可以生成 agent definitions、skills 和 orchestrator skill，但运行时依赖和验证路径必须写进 Source Manifest 或维护说明。
- Matt Pocock 视觉/DSL 图补充：skill 可以是审美审查、视觉还原或 DSL 契约，不限于后端工程流水线；关键仍是触发边界、输入证据、输出可用性和验证门。
- Anthropic Claude Code source 补充：skill 是可执行上下文包，可以包含 scripts、references、assets、data、hooks 和 memory；高质量 skill 的核心是 failure shaping、gotchas 和 progressive disclosure。
- GitHub tool source 补充：复杂 skill 可以拆成宿主模型契约和 deterministic engine；`last30days-skill` 用 `SKILL.md` 约束 planning/output，用 Python 管线处理多源检索和排序。
- GitHub review source 补充：代码质量 skill 可以把 AI review slop 治理成 taxonomy、Iron Law、false-positive guard、eval 和 validator，而不是只写主观审查提示词。

### 规格层（来自 `Skills.xmind` / `claude skill.pdf`）

- Skill 是包含 `SKILL.md` 的文件夹，至少有 `name` 和 `description` 元数据，可打包 scripts、references、assets；本质是把程序性知识封装成 Agent 可发现、可审计、可复用的包，属于提示词工程和上下文工程。
- `description` 是给模型判断触发条件用的，不是摘要；过宽或摘要式描述会直接降低触发准确性，是 skill 可用性的核心控制面。
- Agent 处理 skill 的三段路径：发现阶段只暴露 name/description；激活阶段加载完整 `SKILL.md`；执行阶段再按需读取引用文件或运行脚本——这是文件系统驱动的渐进式披露。
- references 要聚焦、避免深层链式引用；scripts 应面向 Agent 使用，具备结构化输出、清晰错误、非交互、幂等、安全默认值、dry-run、退出码和可预测输出大小。
- 一次构建可部署到多个 Agent 产品；企业可借 skill 沉淀组织知识，并用 On Demand Hooks 在必要时激活主观或高价值约束。

### 强弱注入（来自 `Nano Bot .xmind` / 闪极）

- skill 可分强注入和弱注入：`always: true` 且依赖满足的技能强注入进 system prompt；其余技能以 XML 摘要形式弱注入，引导模型按需读取，避免一次性塞满上下文。
- workspace 技能可覆盖同名内置技能；闪极智能体用「内置只读 skills + 用户私有 skills + Skills 索引 + Prompt 分层」组织技能上下文。

### Vibe 工作流 Skills 三分法（来自 Matt Pocock / GStack / Superpowers）

Skills 可按职责分为三类，互补而非替代：

| 类型 | 定位 | 典型例子 |
| --- | --- | --- |
| **Engineering Workflow Skills** | 编排完整工程阶段，跨多工具和人工审查节点 | `/to-prd`、`/triage`、`/deliver-issue`、`/hat-prepare`、`/cross-review` |
| **Helper / Mechanical Skills** | 执行单一机械任务，无复杂判断 | `/setup-pre-commit`、`/migrate-to-shoehorn`、`/scaffold-exercises` |
| **Lightweight Workflow Skills** | 轻量模式编排，触发一组子步骤但无重型脚本 | `/grill-me`（追问需求）、`/diagnose`（调试六阶段）、`/prototype`（原型模式） |

Lightweight mode 的特点：有明确触发词、一次性或持续、告知停止条件、输出形态清晰——本质是 prompt 链，而非完整 workflow skill 框架。

**工具对比：**
- **Matt Pocock Skills**：以 GitHub issue 为状态机，可组合的端到端工程链路。
- **GStack**：以 slash commands 为入口的质量门禁套件（`/ship`/`/review`/`/codex`/`/canary`）。
- **Superpowers**：以 session-start hook 强注入 + TDD 约束 + 子代理评审为核心框架。

## Examples

推荐学习顺序（参考 `地图.png`）：

1. `地图.png` — 整体 skill 体系全景，理解 workflow/helper/lightweight 三区。
2. `tdd.png`、`to_prd__to_issue.png`、`triage 分诊.png` — 垂直切片 TDD、PRD 到 issue 和分诊状态机。
3. `diagnose.png` — 复现、最小化、假设、仪器化、修复和回归测试闭环（lightweight mode 典型案例）。
4. `superpower.xmind` — session-start hook 注入 + 子代理评审（Superpowers 框架）。
5. `AI 软件工厂 GStack.xmind` — slash commands 质量门禁套件（GStack 框架）。

## Common Confusions

- Skill 不是普通知识摘要；它应该改变 Agent 下一步行动。
- Skill 越多不一定越好，关键是触发边界清晰、验证成本可承受、与项目上下文匹配。
- `description` 不是摘要而是触发器：写成「这个 skill 讲了什么」会让模型不知道何时该用它。
- 强注入和弱注入是两种成本/收益取舍：强注入保证一定出现但占上下文，弱注入省上下文但依赖模型主动读取。

## Evidence

### 2026-06-01 扩展技能刷新

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext Skills 审查.png|Vibe/工具/mattpocock:skills  ⭐/Ext Skills 审查.png]] — 补充 skill 审查、交付封装和 HAT-friendly 改造证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 实现一条龙deliver-issue.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 实现一条龙deliver-issue.xmind]] — 补充 skill 审查、交付封装和 HAT-friendly 改造证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind]] — 补充 skill 审查、交付封装和 HAT-friendly 改造证据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 后端项目如何 Agents HAT Friendly.xmind|Vibe/工具/mattpocock:skills  ⭐/Ext 后端项目如何 Agents HAT Friendly.xmind]] — 补充 skill 审查、交付封装和 HAT-friendly 改造证据。

- [[sources/Agent/Skills.xmind|Skills.xmind]]
- [[sources/Agent/claude skill.pdf|claude skill.pdf]]
- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot .xmind]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/地图.png|地图.png]] — skill 体系推荐学习顺序全景图
- [[sources/Vibe/工具/mattpocock:skills  ⭐/diagnose.png|diagnose]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/tdd.png|tdd]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/to_prd__to_issue.png|to_prd__to_issue]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/triage 分诊.png|triage 分诊]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]]
- [[sources/Vibe/工具/superpower.xmind|superpower]] — Superpowers 框架（partial）
- [[sources/Vibe/工具/AI 软件工厂 GStack.xmind|AI 软件工厂 GStack]] — GStack slash commands 质量门禁套件
- [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — human source，补充 skill 文本可训练、可验证、可审计的资产视角。
- [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — human source，补充 skill/orchestrator 生成和触发验证案例。
- [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — human source，补充 Anthropic 内部 skill 分类、gotchas、progressive disclosure、hooks、memory 和 marketplace 路径。
- [[human/sources/inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill|近30天多源研究技能]] — human source，补充 data acquisition/analysis skill 的 contract + engine 案例。
- [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — human source，补充 code quality/review skill 的反 slop 协议案例。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png|adversarial-ui-review-loop.png]] — UI 审美审查 skill，补充只读批判、P0/P1 筛选和批准修复循环。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/visual-fidelity-loop.png|visual-fidelity-loop.png]] — 视觉还原 skill，补充 target/diff/patch/verify 证据链。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png|create-dsl-skills.png]] — DSL-backed skill，补充 contract.pyi、examples 和机械验证路线。

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- related: [[concepts/上下文工程|上下文工程]]
- enabled-by: [[concepts/Agent 工具调用|Agent 工具调用]]
- contains: [[concepts/Skill 触发契约|Skill 触发契约]] — 触发契约是 skill 可用性的核心控制面
- contains: [[concepts/Skill Contract DSL|Skill Contract DSL]] — DSL-backed skill 把触发、输入、输出和控制流契约化
- contains: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — HAT skills 是 workflow skill 在验收阶段的协议化组合
- related: [[concepts/Agent 上下文审计|Agent 上下文审计]] — 上下文审计可检查 skill 触发与入口文档是否让新 Agent 误判
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- implemented-by: [[entities/Superpowers|Superpowers]] — session-hook 注入型框架实现
- implemented-by: [[entities/GStack|GStack]] — slash commands 质量门禁套件实现
- related: [[entities/Matt Pocock|Matt Pocock]] — 可组合 GitHub 闭环 skills 方法论
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: ClawHub

## My Understanding

当前理解：Agent Skills 是把“我希望 Agent 以后这样做”从聊天偏好变成可复读的工程资产。

## Review Questions

- 一个 workflow skill 和 helper skill 的差别是什么？
- 为什么 skill 需要验证命令和触发边界？
- 哪些 skill 适合放在项目级，哪些适合放在用户级？
- Agent 处理 skill 的「发现/激活/执行」三段分别加载什么？
- 为什么 `description` 应写成触发条件而不是摘要？
- 强注入和弱注入的取舍是什么？

## Open Questions

- 多 skill 冲突时的优先级和可观测性还需要进一步设计。
