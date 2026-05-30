---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-10
---

# AI 软件工厂

## Definition

AI 软件工厂是把软件交付流程（计划、开发、审查、测试、发布、监控、复盘）全流程封装为 Agent 可执行的标准化 skills 和质量门禁，从而让一个工程师借助 AI Agent 达到原本需要整个团队才能完成的交付能力。

## Why It Matters

传统软件工厂依赖人力流水线：PM 写需求 → 工程师写代码 → QA 测试 → DevOps 发布。当 Agent 能执行编码、测试、审查和发布时，制约因素从"谁能写代码"变成"如何把质量门禁内化到 Agent 可执行的工作流"。AI 软件工厂的价值就是把工程师的经验沉淀成可复用、可审计的 Agent 操作系统。

## Mental Model

```
AI 软件工厂 = Skills（工程经验固化）
              + 质量门禁（多层防御）
              + 工具集（browser/design/test）
              + 可观测性（日志/canary/监控）
```

每个 skill 不是一次性 prompt，而是带有前提条件、执行步骤、验证规则和失败处理的可重复工作流。

## Key Claims

- AI 软件工厂的核心是把"质量判断"而非"代码生成"固化为 skills：`/review` 汇集领域专家视角，`/codex` 提供异构模型交叉验证，`/qa` 和测试层提供多维度验证。
- 多层质量防御覆盖：Plan 阶段多视角评审（CEO/设计/工程） → 开发后领域审查 + 安全审计 + QA → 异构模型交叉 review → 发布后 canary + 监控 → 复盘。
- 浏览器能力是一等公民：让 Agent 真正"看"网页状态，而不只是阅读代码，是测试和验收的关键差异。
- GStack 的 `/ship`/`/review`/`/qa`/`/autoplan`/`/codex`/`/canary` 等命令是 AI 软件工厂的具体实现案例。
- 软件工厂的飞轮是 dogfooding：用 Agent 工厂构建 Agent 工厂本身，失败经验通过 JSONL 日志沉淀为下一版工作流改进。

## Examples

- GStack：围绕 Claude Code 的 slash commands 套件，把计划评审、代码审查、QA、安全审计和发布串成可重复工作流。
- Matt Pocock Skills：把需求澄清（/grill）→ PRD（/to-prd）→ issue（/to-issues）→ triage → TDD → review → HAT → PR 封装成完整工厂流水线。
- Superpowers：以 session-start hook 注入工作流框架，通过子代理完成 code-review，以 TDD 约束实现阶段。

## Common Confusions

- AI 软件工厂 ≠ Copilot 工具：Copilot 是单轮代码补全助手；软件工厂是把整个软件交付生命周期封装成 Agent 可执行的自动化系统。
- 软件工厂 ≠ 全自动化：核心决策（L0 目标、L2 边界、验收判断）仍需人类；软件工厂负责把明确有界的任务自动化。
- 质量门禁 ≠ 测试：测试是质量门禁的一部分；门禁还包括 review、安全审计、性能监控和用户路径验收（HAT）。

## Evidence

- [[sources/Vibe/工具/AI 软件工厂 GStack.xmind|AI 软件工厂 GStack]] — GStack 是 AI 软件工厂的最具体实现案例，覆盖 skill 体系、质量门禁和工具集。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — 完整工厂流水线的方法论来源。
- [[sources/Vibe/工具/superpower.xmind|superpower]] — 另一个 AI 软件工厂框架，侧重 session-start hook 和子代理评审。
- [[sources/Vibe/Vibe Coding 随手记/杂记/软件软件工厂陷阱.xmind|软件工厂陷阱]] — 记录 AI 软件工厂的反模式。

## Relations

- implemented-by: [[entities/GStack|GStack]] — GStack 是 AI 软件工厂概念的最直接实现。
- implemented-by: [[entities/Superpowers|Superpowers]] — Superpowers 是以 skill framework 为形态的软件工厂实现。
- related: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 工作流技能编排是软件工厂的任务分发和执行层。
- related: [[concepts/Agent Harness|Agent Harness]] — Harness 是软件工厂的运行时控制面。
- related: [[concepts/反馈工程（Feedback Engineering）|反馈工程（Feedback Engineering）]] — 质量门禁本质上是反馈工程在交付流程中的体现。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

AI 软件工厂的核心洞察是：工程师的价值不再是"写代码"，而是"设计让代码质量可验证的控制系统"。把经验固化成 skill，比每次从头 prompt 更有复利。

## Review Questions

- AI 软件工厂和普通 AI Coding 工具的核心区别是什么？
- 为什么浏览器能力在软件工厂中是"一等公民"？
- 多层质量防御覆盖哪些阶段？
- dogfooding 对软件工厂飞轮有什么作用？

## Open Questions

- 不同规模团队（1人/5人/50人）的 AI 软件工厂最小可用版本是什么？
- 质量门禁的覆盖成本和收益如何量化？
