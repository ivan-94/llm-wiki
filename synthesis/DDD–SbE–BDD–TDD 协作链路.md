---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# DDD–SbE–BDD–TDD 协作链路

## Thesis

DDD、SbE、BDD 和 TDD 是四种解决不同层次问题的方法论，它们不是竞争关系，而是可以组成一条从"领域理解"到"可信实现"的协作链路。在 AI Coding 语境中，这条链路能帮助 Agent 在正确的领域模型下执行，并以可验证的行为证据为完成依据。

## Collaboration Chain

```
DDD（领域驱动设计）
  → 建立通用语言，识别边界上下文，对齐业务和技术模型
      ↓ 产出：领域术语、限界上下文、聚合根
SbE（Specification by Example）
  → 把领域规则转化为具体可执行的示例，消灭歧义
      ↓ 产出：rules + examples + questions（三色卡）
BDD（行为驱动开发）
  → 把 SbE examples 表达为 Gherkin（Given/When/Then）
      ↓ 产出：feature files、活文档、可自动化的场景
TDD（测试驱动开发）
  → 把 BDD 场景驱动为最小可通过的实现，循环验证
      ↓ 产出：red-green-refactor 循环，实现+测试
```

## Layered Responsibilities

| 方法论 | 主要问题 | 主要参与者 | AI Coding 中的角色 |
| --- | --- | --- | --- |
| DDD | 我们在解决什么领域问题？ | 产品 + 工程师 + 领域专家 | 产出 CONTEXT.md 领域语言，供 Agent 读入 |
| SbE | 这个规则具体是什么意思？ | 产品 + 开发 + QA（Three Amigos） | 产出 Agent spec 的 examples 和反例 |
| BDD | 我们如何用统一语言描述行为？ | 开发 + QA | 产出 Gherkin feature files（活文档） |
| TDD | 什么代码实现了这个行为？ | 开发 | Agent 在 BDD 边界内执行 red-green-refactor |

## Key Insights

- DDD 的通用语言（Ubiquitous Language）是 SbE examples 的语义基础：没有领域共识，examples 里的词会被不同人和 Agent 理解成不同含义。
- SbE 是 BDD 的"上游"：先用 Example Mapping 找到规则和问题，再用 Gherkin 把 examples 标准化为可执行场景。
- BDD 不等于 SbE：BDD 是表达形式，SbE 是发现过程。只用 Gherkin 写测试而跳过 Three Amigos 讨论，会丢失 SbE 的核心价值。
- TDD 在 BDD 约束下防止 Agent 自由发挥：Agent 必须先让 Gherkin 场景通过，再优化内部实现，而不是反过来。

## AI Coding Integration

在 AI Coding 工作流中激活这条链路：

1. **领域对齐**（DDD）：写 CONTEXT.md，固定核心概念、状态机和边界上下文。
2. **需求澄清**（SbE + Example Mapping）：Three Amigos 快速对齐 rules/examples/questions。
3. **行为规格**（BDD/Gherkin）：把 examples 转化为 feature files，作为 Agent 的验收约束。
4. **实现驱动**（TDD）：Agent 在 feature files 约束下做 red-green-refactor，不能先写实现后补测试。
5. **活文档维护**：Agent 每次修改行为，必须同步更新 feature files，否则 CI 失败。

## Key Claims

- inferred: 没有 DDD 的 SbE 容易出现示例里的词被不同角色理解成不同含义。
- inferred: 没有 SbE 的 BDD 容易退化成 QA 单独写 Gherkin，而不是三方共识驱动。
- explicit: BDD 场景（Gherkin）来自 SbE examples，不是直接映射测试用例。
- inferred: TDD 在 BDD 约束下才能对 Agent 产生足够约束力；单独 TDD 容易被 Agent 走捷径。

## Evidence

- [[sources/Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png|sbE与DDD_BDD_TDD]] 直接展示了 SbE 与 DDD/BDD/TDD 的关系图。
- [[sources/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png|2 sbE 是如何运作的]] 提供从规则到示例到自动化测试的流程证据。
- [[sources/Vibe/软件工程基础/Specification by Example/3 团队如何做.png|3 团队如何做]] 展示 Three Amigos 协作与 Example Mapping。
- [[sources/Vibe/方法论.xmind|方法论.xmind]] 将 SbE/BDD/TDD 放在 AI Coding 方法论体系中。

## Relations

- synthesizes: [[concepts/Specification by Example|Specification by Example]]
- synthesizes: [[concepts/Example Mapping|Example Mapping]]
- synthesizes: [[concepts/CONTEXT.md 领域语言|CONTEXT.md 领域语言]]
- related-to: [[synthesis/SbE 与 AI Coding 验收链路|SbE 与 AI Coding 验收链路]] — 本页聚焦方法论协作关系，验收链路聚焦 Gate 和 DoD
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]

## My Take

这条链路的价值不在于必须完整执行每个步骤，而在于理解每个方法解决哪一层的歧义问题。在 AI Coding 中，最常被跳过的是 DDD（领域对齐）和 SbE（examples 发现），而这两步缺失会直接导致 Agent 的行为边界模糊。

## Open Questions

- 在小团队快速迭代场景下，DDD–SbE–BDD–TDD 的最小可行组合是什么？
- Example Mapping 的时间成本在 AI Coding 工作流中如何量化？
