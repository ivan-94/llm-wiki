---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 14
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Spec-Driven Development

## Definition

Spec-Driven Development 是先把意图、需求、设计、任务和验收标准沉淀为可追踪规格，再让实现围绕规格生成、验证和回写的开发方式。

## Why It Matters

AI 生成代码越快，越需要规格来承载共同语言、边界、决策和验收。规格不是额外文档，而是让 Agent 和人类对齐的控制面。

## Mental Model

Spec 是 AI 时代的新接口：它连接用户意图、工程设计、任务拆解、测试和交付证据。

## Artifact Stack

SDD 的价值来自产物分层，而不是“文档更多”：

- product spec: 用户价值、场景、指标、FR/SC、非功能需求和待澄清项。
- behavior spec: Given/When/Then、examples、acceptance scenarios 和反例。
- design spec: 关键技术决策、约束、数据模型、接口契约、迁移和风险。
- task spec: 按依赖顺序拆成可执行、可验收、可回滚的工作项。
- evidence spec: 明确哪些测试、HAT、review 和运行证据能证明完成。

如果这些层混在一个长 prompt 里，Agent 会倾向于直接实现；如果分层明确，Agent 更容易知道哪些是目标、哪些是约束、哪些是可变实现。

## Key Claims

- SDD 的核心是把模糊想法转成 requirements/design/tasks 或 spec/plan/tasks 等可追踪工件。
- 规格应聚焦用户需要什么和为什么需要，避免过早写死实现细节。
- OpenSpec 更像变更治理和规范流程，SpecKit 更强调从 constitution 到 spec/plan/tasks 的约束链。
- 技术设计方案、规格书和 Mini Spec 是不同粒度的 spec artifact，可以服务不同复杂度任务。
- 对 Agent 来说，spec 的价值在于减少未定义空间和隐式决策。
- SDD 与 SbE 的关系是互补（complements）：SDD 组织规格资产和执行链，SbE 用具体例子把行为边界和验收反例变硬。两者都服务于同一个目标：让 Agent 在明确的行为边界内工作。
- 对存量系统，spec 还承担防止 Agent 偏离当前事实的作用；对新 feature，spec 更像从想法到任务的脚手架。

## Examples

- `规格书.xmind` 用元数据、用户价值、指标、实体、数据流、NFR、FR、Gherkin 场景组织需求。
- `技术设计方案.xmind` 将背景、目标、约束、接口、数据、风险和验收连接起来。
- OpenSpec 图片组展示变更 proposal、spec delta、tasks 和验证流程。
- SpecKit 图片组展示 constitution、spec、plan、tasks 和 artifact 关系。

## Spec Stack Selection Matrix (B4 四格)

不同任务复杂度和治理需求对应不同规格工具：

| 规格工具 | 最适合 | 主要优势 |
| --- | --- | --- |
| Mini Spec | 小功能/bug fix/局部重构，个人开发 | 轻量、快速、明确边界 |
| SpecKit | 新 feature 从想法到任务的完整交付链 | constitution + spec/plan/tasks 约束链 |
| OpenSpec | 存量系统变更治理，规范维护 | change delta + behavior contract + archive |
| SbE | 业务规则澄清，验收行为确定 | 具体例子消灭歧义，反例驱动测试 |

选型原则：
- 探索/快速验证 → Mini Spec
- 新 feature 完整交付 → SpecKit
- 存量系统防漂移 → OpenSpec
- 业务规则有争议或语义复杂 → 引入 SbE examples

## Common Confusions

- SDD 不等于“先写长文档”；规格要能进入实现、测试和验收循环。
- 规格不应替代人类判断；它让判断显性化、可审查、可回写。

## Evidence

- [[sources/Vibe/方法论.xmind|方法论.xmind]]
- [[sources/Vibe/Spec/规格书.xmind|规格书.xmind]]
- [[sources/Vibe/Spec/技术设计方案.xmind|技术设计方案.xmind]]
- [[sources/Vibe/Spec/Mini Spec.xmind|Mini Spec.xmind]]
- [[sources/Vibe/Spec/OpenSpec/概览.png|OpenSpec 概览]]
- [[sources/Vibe/Spec/SpecKit/Spec_kit.png|SpecKit]]
- [[sources/Vibe/Spec/SpecKit/Spec_kit_产物.png|SpecKit 产物]]
- [[sources/Vibe/Spec/SpecKit/对比 OpenSpec.png|对比 OpenSpec]]

## Relations

- enables: [[concepts/Vibe Coding|Vibe Coding]]
- complements: [[concepts/Specification by Example|Specification by Example]] — SDD 组织规格资产，SbE 用具体例子强化行为边界（非对立关系）
- supported-by: [[concepts/共识方法论|共识方法论]] — 共识方法论是 SDD 必要性的宏观理由
- used-in: [[synthesis/OpenSpec 与 SpecKit 对比|OpenSpec 与 SpecKit 对比]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]

## My Understanding

当前理解：SDD 是把 AI Coding 从“提示词驱动”推向“规格资产驱动”的桥。

## Review Questions

- SDD 中 spec、plan、tasks 各承担什么？
- 为什么规格要保留用户价值和验收标准？
- OpenSpec 与 SpecKit 的流程差异在哪里？

## Open Questions

- OpenSpec、SpecKit、Kiro 等工具当前实现细节未联网核验。
