---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# CONTEXT.md 领域语言

## Definition

CONTEXT.md 领域语言是在 AI Coding 项目中，把领域内核心概念、术语定义、实体关系、状态机、业务规则和词汇约定以结构化文档形式固化下来，使 Agent 和人类共享稳定的领域理解，减少因概念混用导致的实现偏差。

## Why It Matters

AGENTS.md 负责"Agent 怎么工作"，领域语言文档负责"项目里这些词是什么意思"。当 Agent 对"订单""用户""状态"的理解和业务语言不一致时，实现会在语义层漂移，而测试通常无法发现这类问题。

## Mental Model

CONTEXT.md = 项目级领域词典 + 核心概念关系图 + 状态机 + 业务规则白皮书。

## Contents Taxonomy

| 类别 | 说明 |
| --- | --- |
| 核心领域概念 | 关键实体、值对象、聚合根的定义和边界 |
| 统一语言（Ubiquitous Language） | 业务术语到代码术语的对照，避免双语切换 |
| 实体关系 | 主要实体之间的关系（属于、包含、引用） |
| 状态与转换 | 关键实体的状态机（枚举值 + 合法转换路径） |
| 业务规则 | 跨实体的约束和不变量（invariants） |
| 命名约定 | 文件、类、函数、变量的命名规范 |

## Key Claims

- explicit（方法论）：DDD 的 Ubiquitous Language 和 Bounded Context 在 AI 时代升级为 AI Shared Ontology，要求把领域概念版本化管理。
- explicit（共识方法论变革图）：领域建模升级为 AI Shared Ontology：通过领域本体、术语词典、命名、类型、关系、枚举和版本化管理，让 AI 持有稳定世界模型。
- inferred：CONTEXT.md 是 AI Shared Ontology 的轻量实现，不需要引入完整 OWL 本体工具，以 Markdown 格式就能为 Agent 提供可消费的领域知识层。

## Examples

- 电商项目 CONTEXT.md：`Order` 实体定义、`Order.status` 枚举（PENDING/CONFIRMED/SHIPPED/DELIVERED/CANCELLED）、合法状态转换表。
- 内容平台 CONTEXT.md：`Article`/`Draft`/`Published`/`Archived` 的业务含义区分，以及为什么 `Published` 不能直接回到 `Draft`。

## Common Confusions

- CONTEXT.md 不等于系统架构文档；它聚焦"业务语义"，而不是技术实现方式。
- 它不替代 AGENTS.md；两者互补：AGENTS.md 约束行为，CONTEXT.md 约束语义。

## Evidence

- [[sources/Vibe/方法论.xmind|方法论.xmind]] — DDD/Ubiquitous Language 在 AI 协作中从传统实践升级为表达领域意图的核心交互界面。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/共识方法论/共识方法论变革.png|共识方法论变革.png]] — 领域建模升级为 AI Shared Ontology 的六层框架。

## Relations

- part-of: [[concepts/AGENTS.md 设计模式|AGENTS.md 设计模式]] — 是 AGENTS.md 渐进披露体系中的领域层文件
- supports: [[concepts/Spec-Driven Development|Spec-Driven Development]] — 为 spec 提供稳定的领域语言基础
- supports: [[concepts/共识方法论|共识方法论]] — 是领域建模共识的 AI 可消费实现
- reduces-risk: [[concepts/决策权泄漏|决策权泄漏]] — 稳定的领域语言减少 Agent 在语义层的自动补全
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]

## My Understanding

当前理解：CONTEXT.md 是把 DDD 落到 AI 协作的最轻量工具——不需要 UML，不需要形式化本体，一个 Markdown 词典就能大幅减少 Agent 的语义漂移。

## Review Questions

- CONTEXT.md 和 AGENTS.md 分别约束什么？
- 为什么领域状态机对 Agent 特别重要？
- Ubiquitous Language 在 AI Coding 中的价值是什么？

## Open Questions

- CONTEXT.md 的维护成本和更新时机还需要实践案例说明。
