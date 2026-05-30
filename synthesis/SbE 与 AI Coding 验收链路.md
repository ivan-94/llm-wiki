---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 8
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# SbE 与 AI Coding 验收链路

## Thesis

Specification by Example 不只是需求澄清方法，它是 AI Coding 验收链路的骨干：用具体例子把行为边界变硬，用测试分层让证据可追溯，用活文档让规格和实现保持同步。结合 AI Coding 工具链，SbE 提供了一套从业务语言到 Agent DoD（Definition of Done）的完整可执行路径。

## Five Gate Acceptance Chain

AI Coding 下的 SbE 五质量门：

| Gate | 问题 | 通过标准 |
| --- | --- | --- |
| G1 业务语言一致 | 需求、spec、示例用了同一个领域词吗？ | 所有角色对核心词含义一致（可用 CONTEXT.md 验证） |
| G2 示例无歧义 | 每个 example 只有一种正确解释吗？ | 给 Three Amigos 看，无不同理解 |
| G3 反例覆盖 | 写了哪些不该发生的情况吗？ | 至少一个 unhappy path 有可执行 example |
| G4 测试可追溯 | 每个关键 example 有对应测试吗？ | example → Gherkin → 自动化测试可追溯 |
| G5 活文档更新 | 业务规则改变时 example 和测试同步了吗？ | 修改规则后 CI 里的 spec 文档也更新 |

## Test Layering

SbE 在 AI Coding 测试分层中的定位：

```
业务层（Gherkin/活文档） ← SbE 主战场，驱动行为契约
   ↓ 驱动
集成层（API/DB contract） ← 行为实现证据
   ↓ 约束
单元层（函数/逻辑） ← Agent 自由发挥区域，但受上层行为约束
```

AI Coding 风险从底层向上流动：Agent 最容易在单元层走捷径，但 SbE 的价值在业务层；只覆盖底层测试，等于把行为语义的验证缺口暴露给 Agent。

## Living Documentation in AI Coding

活文档在 AI Coding 语境中的特殊意义：

- 活文档是 SbE 的持续输出，而不是一次性文档。
- 当 Agent 修改实现时，如果活文档（Gherkin feature files）也在 version control 中，Agent 必须同步更新文档，否则 CI 失败。
- 活文档 = Agent 的行为契约检查器：Agent 不能只改代码，必须同时维护行为描述的一致性。

## Agent DoD (Definition of Done)

SbE + 测试分层 + 活文档合并出 Agent 可执行的完成定义：

- [ ] 所有 G1–G5 质量门通过
- [ ] 业务层 Gherkin 场景全部通过（含反例）
- [ ] 集成层关键 contract 测试通过
- [ ] 活文档与实现一致，无偏差
- [ ] 反捷径审查：错误实现不能骗过当前测试
- [ ] 工程宪法未被违背

## Key Claims

- explicit: SbE 的 Example Mapping 流程（Story → Rules → Examples → Questions）可以直接输出 AI Coding spec 的验收样例部分。
- inferred: 没有 G3 反例的测试套件会显著低估 Agent 通过捷径的概率。
- explicit: 活文档作为版本控制约束，强制 Agent 在修改行为时同步更新业务描述。
- inferred: 测试分层中业务层 Gherkin 是最重要的反捷径屏障，因为它测试的是语义而非实现路径。

## Evidence

- [[sources/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png|2 sbE 是如何运作的]] 说明从规则到示例到自动化测试的流程。
- [[sources/Vibe/软件工程基础/Specification by Example/3 团队如何做.png|3 团队如何做]] 展示 Three Amigos 协作发现示例。
- [[sources/Vibe/软件工程基础/Specification by Example/5 落地和反模式.png|5 落地和反模式]] 包含测试分层和活文档维护的反模式。
- [[sources/Vibe/软件工程基础/Specification by Example/ai_coding.png|ai_coding]] 直接映射 SbE 到 AI Coding 验收链路。
- [[sources/Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png|sbE与DDD_BDD_TDD]] 展示 SbE 在更大方法论链路中的位置。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]] 支撑反捷径证据和偏移控制语境。

## Relations

- synthesizes: [[concepts/Specification by Example|Specification by Example]]
- synthesizes: [[concepts/行为契约式规格|行为契约式规格]]
- synthesizes: [[concepts/反捷径证据|反捷径证据]]
- related-to: [[synthesis/DDD–SbE–BDD–TDD 协作链路|DDD–SbE–BDD–TDD 协作链路]] — 本页聚焦验收链路，DDD 链路聚焦方法论协作关系
- related-to: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 提供 L4 Evidence 层的具体方法论支撑
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]

## My Take

SbE 对 AI Coding 的价值不在于"更多测试"，而在于把测试变成业务语义的证明，而不只是代码路径的证明。这是反捷径证据最重要的来源。

## Open Questions

- 活文档工具链（Cucumber/Serenity/SpecFlow）与 AI Coding 工具链的实际集成方式需要案例验证。
- G2 无歧义标准在实践中如何量化？
