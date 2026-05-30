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

# Example Mapping

## Definition

Example Mapping 是 Three Amigos 会议中用于结构化澄清需求的协作技术：把一个 User Story 拆成规则（Rules）和具体例子（Examples），并标记仍有疑问的问题（Questions），在 30 分钟内快速达成跨角色的共同理解。

## Why It Matters

需求讨论往往陷入"大家说的是同一件事，但各自有不同的理解"。Example Mapping 通过强制输出具体例子，把抽象规则转化为可验证的边界，在实现前就消灭歧义。对 AI Coding，这些例子可以直接作为 Agent 的 spec 输入和验收测试。

## Mental Model

黄色卡：Story；蓝色卡：规则；绿色卡：每条规则的具体例子；红色卡：尚未解答的问题。

## Session Structure

典型 Example Mapping 会议：
1. 写下 Story（黄色卡）。
2. 列出已知规则（蓝色卡），每条规则一张。
3. 为每条规则写具体例子（绿色卡）：GIVEN/WHEN/THEN 格式。
4. 遇到无法立即回答的问题，写红色卡，不卡讨论节奏。
5. 约 25-30 分钟后看地图：规则多/例子少 = 还需要澄清；红色多 = 需要调研。

## AI Coding Role

在 AI Coding 场景，Example Mapping 的产出可以直接：
- 作为 Mini Spec 的验收标准区块（GIVEN/WHEN/THEN 例子）
- 作为 Agent 任务的行为边界约束
- 作为反捷径证据的来源（反例和边界例子）
- 进入 Cucumber/Gherkin 自动化测试

## Key Claims

- explicit（SbE 图）：Three Amigos（业务/开发/测试）协作产出的例子能在开发前就发现需求歧义。
- explicit（SbE 图）：SbE 的核心模式是把规则变成例子，把例子变成可执行规格。
- inferred：Example Mapping 是 SbE "Example Discovery"阶段的标准工具，适合快速对齐新 feature 的边界和反例。

## Examples

- 电商促销规则："满 100 减 20"的 Example Mapping 会产生：正常满足、刚好 100、99.99 不满足、叠加优惠券的例子。
- AI Coding 场景：把"用户注册"的 Story 用 Example Mapping 展开，得到密码强度规则的4个具体例子，直接写入 Mini Spec。

## Common Confusions

- Example Mapping 不是流程设计，而是需求澄清工具；它的产出是例子和问题，不是代码或流程图。
- 例子越多不一定越好；目标是覆盖关键规则族和边界，而不是机械枚举所有场景。

## Evidence

- [[sources/Vibe/软件工程基础/Specification by Example/3 团队如何做.png|3 团队如何做]] — 展示 Three Amigos 协作和例子发现过程。
- [[sources/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png|2 sbE 是如何运作的]] — 从规则到例子到可执行规格的流程。

## Relations

- part-of: [[concepts/Specification by Example|Specification by Example]] — Example Mapping 是 SbE 需求澄清阶段的核心工具
- enables: [[concepts/行为契约式规格|行为契约式规格]] — 例子是行为契约的基础材料
- produces: [[concepts/Mini Spec|Mini Spec]] — Example Mapping 的例子可以直接进入 Mini Spec 的验收标准
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]]

## My Understanding

当前理解：Example Mapping 是把"大家说清楚了"变成"大家写下了具体例子"的最快工具。有了例子，AI Coding 场景下 Agent 的漂移就少了一个藏身之处。

## Review Questions

- Example Mapping 中四类卡片各自代表什么？
- 什么情况说明 Example Mapping 还没有做充分？
- Example Mapping 的产出如何转化为 AI Coding 的 spec 输入？

## Open Questions

- Three Amigos 在 AI Coding 团队中，当"产品/开发/测试"都是 Agent 时的角色还需要探索。
