---
page_type: synthesis
updated_at: 2026-06-05
status: active
source_count: 7
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-19
---

# Agent 工作流可进化闭环

## Thesis

可持续的 Agent 工作流不是“让模型一次做完任务”，而是把入口、边界、结构证据、质量门和失败回写组织成一条可进化闭环。Codex/Claude Code 这类工具只是入口；真正复利来自 harness、spec、eval、HAT、Source Manifest 和 skill 文本持续改进。

## Loop Model

```text
Capture -> Cook -> Ingest -> Plan/Spec -> Execute -> Eval/HAT -> Learn -> Update Skill/Harness
```

这条链路把 7 个 human source 连接成一个系统：

| 阶段 | 核心问题 | 证据来源 |
| --- | --- | --- |
| 入口归一 | 哪个 agent 承接工作和知识系统的调度？ | [[human/sources/inbox/cook-my-mind/2026-06-02_Codex作为个人系统超级入口|Codex 作为个人系统超级入口]] |
| Harness 边界 | 模型如何获得工具、上下文、权限、观察和验证？ | [[human/sources/inbox/cook-podcast/2026-05-31_Agent Harness 工程系统_硬地骇客|Agent Harness 工程系统]] |
| 产品控制面 | 哪些用户已在绕路做的动作应产品化为 plan、verbose、subagent？ | [[human/sources/inbox/cook-podcast/2026-05-31_Y Combinator Startup Podcast_Inside Claude Code With Its Creator Boris Cherny|Inside Claude Code With Its Creator Boris Cherny]] |
| 团队拓扑 | 多 Agent 协作如何从口头分工变成 team/orchestrator/skill contract？ | [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] |
| 实现前证据 | Agent 是否真的理解接口、调用栈、seam 和测试替身？ | [[human/sources/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders|AI Agent 协作提示链]] |
| 输出后质量门 | 输出是否经过 benchmark、metric、threshold 和 approval？ | [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] |
| Skill 演进 | 失败样例是否变成可评分数据集和 `best_skill.md`？ | [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] |

## Key Judgments

- **入口不是终点。** Codex 可以成为个人系统超级入口，但入口归一之后必须继续分层：XMind 保留手动深加工，Obsidian 承接图谱前端，cook skills 负责捕获预处理，`human/raw` / `human/sources` 保持来源边界。
- **Harness 是模型能力的工作环境。** 同一模型在聊天框和 coding agent 中表现不同，关键是是否有文件系统、工具、权限、日志、测试、浏览器、CI 和 review 反馈。
- **规则要短而可删。** `AGENTS.md` / `CLAUDE.md` 不应无限堆历史 workaround；重复出现且跨任务复用的约束才进入长期入口，其余应下沉到 skill、HAT、测试或 source note 维护项。
- **实现前需要结构证据。** 对复杂改造，先让 agent 输出 anchored architecture review、public interface、call stack、seams/adapters 和 production/test 双调用图，比直接让它改代码更稳。
- **输出后必须有质量门。** Prompt、memory、context file 只是在修输入侧；没有 test cases、metrics、threshold 和 gate，质量只能靠主观感觉。
- **失败要回写成资产。** 一次 agent 失败如果没有进入测试、HAT 步骤、review checklist、AGENTS 规则或 skill 样例，下次仍会重复发生。
- **Skill 可以被评估和训练。** SkillOpt 的启发不是某个工具本身，而是把 skill 文本当作可读、可审计、可版本化、可用 held-out examples 改进的工程资产。

## Practical Protocol

### 1. 先判断入口和来源域

如果材料只是临时捕获，留在 `human/inbox`；如果用户明确提升为长期来源，进入 `human/raw`；只有进入 `human/raw` 且允许 ingest 后，才写 `human/sources` 并进入 compile gate。入口归一不能破坏来源边界。

### 2. 实现前要求结构化计划

复杂代码或工作流改造进入执行前，至少要求：

- 目标、非目标和不可交给 agent 静默决定的边界。
- public interface / 数据契约 / 调用栈草图。
- production adapter 与 test/in-memory adapter 的替换点。
- production/test 两套调用图是否同形。
- 需要写回 `AGENTS.md`、spec、HAT 或 skill 的团队 convention。

### 3. 执行中保持 harness 信号

执行环境要能给 agent 返回真实反馈：测试、lint、类型检查、日志、浏览器画面、diff、CI、HAT artifacts。没有反馈信号的 agent 只能继续猜。

### 4. 输出后走质量门

对内容、source note、agent 输出或产品 AI，都要问：

- 有无 test cases 或真实样例？
- metric/rubric 是否具体到可评分？
- threshold/gate 是否能阻止低质量输出进入下游？
- 失败样本是否会回写为 regression example？

### 5. 把失败沉淀到最合适层

失败不总是写进 `AGENTS.md`。更合适的承载层可能是：

- `AGENTS.md`：跨任务、跨 agent 的硬边界。
- skill：可触发的任务流程、工具规则和验证步骤。
- HAT：用户路径验收和人工验收准备。
- test/eval：可重复评分的失败样例。
- source note Maintenance Notes：当前 source 的限制、不确定和需人工核验点。
- synthesis：跨来源形成的新判断、对比或路线图。

## Relations

- synthesizes: [[concepts/Agent Harness|Agent Harness]] — harness 提供环境、权限、工具、观察和验证。
- synthesizes: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — workflow skills 组织 plan/spec/execute/review/HAT 的产物链。
- synthesizes: [[concepts/Agent Skills|Agent Skills]] — skill 是可触发、可验证、可演进的工程资产。
- synthesizes: [[concepts/LLM 评估|LLM 评估]] — eval gate 把输出质量从感觉变成可重复实验。
- synthesizes: [[concepts/LLMOps|LLMOps]] — 数据集、评估器、版本化和线上反馈形成持续质量循环。
- relates-to: [[entities/Codex|Codex]] — Codex 是个人系统入口和执行层候选。
- relates-to: [[entities/Claude Code|Claude Code]] — Claude Code 提供 plan mode、verbose output、subagent 等产品控制面参照。
- relates-to: [[entities/Hermes|Hermes]] — Hermes 在 human source 中作为 eval loop runtime 原语集合出现，当前事实未核验。
- extends: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] — 本页把系统工程综述中的工具/上下文/评估/学习层压成可执行闭环。
- extends: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 本页是 L3 Execution、L4 Evidence、L5 Learning 的具体工作流化。
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## Evidence

- [[human/sources/inbox/cook-my-mind/2026-06-02_Codex作为个人系统超级入口|Codex 作为个人系统超级入口]] — 入口归一与个人知识工作闭环。
- [[human/sources/inbox/cook-podcast/2026-05-31_Agent Harness 工程系统_硬地骇客|Agent Harness 工程系统]] — harness 的环境、权限、上下文、观察和验证定义。
- [[human/sources/inbox/cook-podcast/2026-05-31_Y Combinator Startup Podcast_Inside Claude Code With Its Creator Boris Cherny|Inside Claude Code With Its Creator Boris Cherny]] — 短规则、latent demand、plan mode、subagent lane 和可删脚手架。
- [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — team architecture factory 和 orchestrator skill 案例。
- [[human/sources/inbox/cook-tweet/2026-06-01_AI_Agent协作提示链_MrSanders|AI Agent 协作提示链]] — 实现前结构证据和 TDD 交接协议。
- [[human/sources/inbox/cook-tweet/2026-06-01_AI输出质量控制与Hermes评估循环_EXM7777|AI 输出质量控制与 Hermes 评估循环]] — 输出质量门、benchmark 三要素和失败回写。
- [[human/sources/inbox/cook-tweet/2026-06-03_用SkillOpt训练可进化Agent技能_SkillOpt|用 SkillOpt 训练可进化 Agent 技能]] — skill 文本可评估、可训练、可审计。

## My Take

这批 human source 的共同价值，是把“Agent 能干活”拆成一套可改进系统：人类负责定义价值、边界和质量门；Agent 负责在 harness 内执行；系统负责把失败记录、测试、HAT 和 skill 修订变成下一次执行的初始条件。真正的进步不是某次输出更好，而是下一次同类任务的起点更高。

## Open Questions

- 哪些 AI wiki source-note 质量标准可以变成可评分 eval，而哪些必须保留人工 judgment？
- `AGENTS.md`、skill、HAT、test 和 synthesis 之间的失败回写边界还需要更明确的路由规则。
- SkillOpt、Hermes、Claude Code Agent Teams 等当前事实都需要官方来源核验后才能升级为稳定实体判断。

## Review Questions

- 为什么说 prompt/memory/context file 只是在修输入侧？
- 实现前的 production/test 双调用图解决了什么风险？
- 一次 agent 失败应该如何选择写回 `AGENTS.md`、skill、HAT 还是测试？
- Codex 作为超级入口为什么仍然需要保持 `human/inbox`、`human/raw` 和 `human/sources` 边界？
