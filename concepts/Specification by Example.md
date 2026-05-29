---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 11
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Specification by Example

## Definition

Specification by Example 是通过业务人员、开发和测试共同讨论具体例子，把需求澄清成可验证规格和自动化验收测试的协作方法。

## Why It Matters

SbE 解决的是“大家以为理解一致，但其实没有”的问题。对 AI Coding 来说，示例能把抽象需求转成 Agent 更容易执行和验证的具体行为边界。

## Mental Model

需求先变成例子，例子再变成规格，规格最后变成测试。

## AI Coding Role

在 AI Coding 里，SbE 的作用是把“人类以为说清楚了”的需求，改写成 Agent 不能轻易误读的行为样例。示例既是沟通材料，也是反捷径证据：它让 Agent 必须同时满足 happy path、异常路径、边界值和业务反例，而不是只生成看似合理的主流程。

## Key Claims

- SbE 的价值在于在开发前发现歧义，而不是等实现完成后返工。
- Three Amigos、Example Mapping、Gherkin 和 Cucumber 是 SbE 常见协作与自动化工具链。
- SbE 与 DDD/BDD/TDD 可以形成链路：领域语言对齐、行为示例澄清、测试驱动实现。
- 用于 AI Coding 时，示例可以作为 prompt/spec 的验收样例和反例，降低 Agent 自行补全需求的风险。
- 示例数量不是越多越好；高价值路径、常见风险和少量关键异常比机械枚举 UI 场景更能约束 Agent。
- SbE 的反模式包括示例过于技术化、只让 QA 写示例、过早自动化，以及把示例当测试脚本而不是共同语言。

## Examples

- `1为什么需要 sbE.png` 说明需求缺陷和返工成本是 SbE 的动机。
- `2 sbE 是如何运作的.png` 描述从业务规则到示例、规格和自动化测试的流程。
- `3 团队如何做.png` 展示团队协作、例子发现和工具链。
- `cucumber-1/2.png` 将 Gherkin 场景和测试分层联系起来。
- `ai_coding.png` 把 SbE 映射到示例驱动的 AI Coding。

## Common Confusions

- SbE 不是只写测试脚本；重点是跨角色共同澄清例子。
- Gherkin 是表达形式，不等于 SbE 全部。
- SbE 和 SDD 不冲突：SDD 组织规格资产，SbE 提供具体行为样例。

## Evidence

- [[sources/Vibe/软件工程基础/Specification by Example/1为什么需要 sbE.png|1为什么需要 sbE]]
- [[sources/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png|2 sbE 是如何运作的]]
- [[sources/Vibe/软件工程基础/Specification by Example/3 团队如何做.png|3 团队如何做]]
- [[sources/Vibe/软件工程基础/Specification by Example/4 组织和协作.png|4 组织和协作]]
- [[sources/Vibe/软件工程基础/Specification by Example/5 落地和反模式.png|5 落地和反模式]]
- [[sources/Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png|sbE与DDD_BDD_TDD]]
- [[sources/Vibe/软件工程基础/Specification by Example/ai_coding.png|ai_coding]]

## Relations

- complements: [[concepts/Spec-Driven Development|Spec-Driven Development]]
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- used-in: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]
- related-source: [[sources/Vibe/软件工程基础/Specification by Example/SbE.xmind|SbE.xmind]]

## My Understanding

当前理解：SbE 是把需求讨论变成“可执行例子”的协作技术，特别适合给 Agent 提供不会随意发挥的行为边界。

## Review Questions

- SbE 如何减少需求歧义？
- Three Amigos 在 SbE 中分别贡献什么？
- Gherkin 场景和自动化测试之间是什么关系？
- SbE 如何帮助 AI Coding 降低漂移？

## Open Questions

- 图片中的收益百分比和工具细节未联网核验，只应作为 raw 观点记录。
