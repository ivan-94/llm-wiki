---
page_type: concept
updated_at: 2026-06-11
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-24
---

# AI 代码垃圾治理

## Definition

AI 代码垃圾治理是针对高通量 AI 生成代码带来的死代码、重复、复杂度、边界漂移、测试缺口、命名混乱、职责混杂和临时代码沉积，建立约束、限权、准入、观测和删除机制的工程治理方法。

## Why It Matters

AI 让生成变便宜，但维护、理解、验证和删除仍然昂贵。如果生成速度长期大于验证速度，代码库会自然膨胀，并把未声明假设和局部最优固化成长期技术债。

## Mental Model

垃圾 = 高通量生成 x 低约束输入 x 弱验证机制 x 持久化代码库。

治理 = 生成前约束 + 生成中限权 + 生成后准入 + 合并后观测 + 演化中删除。

## Key Claims

- LLM 会补全未声明假设；未声明假设是垃圾的原材料。
- Agent 容易追求局部最优，让当前文件、当前报错、当前组件成立，但破坏系统全局一致。
- “可见进展”会奖励模型和用户继续生成，但进展感不等于工程质量。
- AI 生成物准入时应携带假设、证据、风险和回滚路径。
- 复杂度治理需要让新增代码支付复杂度税；退场治理需要让临时代码有删除条件。
- DeSlop 工具链应结合机械扫描、主观审查、分诊和修复循环，而不是只依赖单个 linter。
- brooks-lint 补充：AI review slop 本身也要治理；每条 finding 必须有 `Symptom -> Source -> Consequence -> Remedy` 证据链，并用 clean eval 抑制误报。

## Examples

- 机械扫描：unused declarations、dead exports、cycles、orphaned files、large files、God components、props 膨胀、cross-tool imports、test coverage gaps。
- 主观审查：naming quality、logic clarity、type safety、contract coherence、error consistency、abstraction fitness、ai-generated debt、design coherence。
- 修复循环：scan -> triage -> next -> fix -> resolve -> next。

## Common Confusions

- DeSlop 不是“反对 AI 生成代码”，而是承认生成廉价后，治理必须覆盖复杂度、上下文、角色和删除。
- 代码垃圾不只是不美观；它会污染未来 Agent 的上下文，使模型继续模仿坏结构。
- 只做生成后 lint 不够；垃圾治理还要前置约束和权限，并在合并后观察真实运行。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind|垃圾治理(DeSlop).xmind]] — 提供成因公式、生命周期治理方向和工具维度清单。
- [[human/sources/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]] — human source，补充 AI review slop、Iron Law、false-positive guard、eval 和 validator。

## Relations

- part-of: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 对应 L3 Execution、L4 Evidence 和 L5 Learning 的治理工具箱。
- addresses: [[concepts/软件工厂陷阱|软件工厂陷阱]] — 防止把生成速度误认为交付能力。
- supports: [[concepts/Agent Coding Guardrails|Agent Coding Guardrails]] — guardrails 是生成前约束和生成中限权的一部分。
- related: [[concepts/反捷径证据|反捷径证据]] — 准入治理要求证据匹配 claim。
- related: [[concepts/异常治理闭环|异常治理闭环]] — 合并后观测和异常反馈是 DeSlop 的运行时侧。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

AI 代码垃圾治理的关键不是“扫出更多坏味道”，而是让 AI 生成物在进入代码库前后都必须解释假设、付出复杂度成本，并保留删除与回滚路径。

## Review Questions

- 为什么“生成便宜、维护昂贵”会改变代码治理重点？
- DeSlop 的五个治理阶段分别是什么？
- 机械扫描和主观审查为什么要配合使用？

## Open Questions

- `desloppify`、`taste-skill`、`brooks-lint` 的当前实现能力和适用语言范围需要后续联网或仓库级核验。
