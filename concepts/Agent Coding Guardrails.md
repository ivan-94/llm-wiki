---
page_type: concept
updated_at: 2026-06-10
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-13
---

# Agent Coding Guardrails

## Definition

Agent Coding Guardrails 是约束 AI Agent 写代码时行为的一组工作协议：不猜测假设、优先简洁、精准修改，并在执行多步任务时先定义成功标准再循环验证。

## Why It Matters

Agent 在缺少约束时会把不确定性隐藏起来——直接假设、直接执行、不暴露歧义、不呈现权衡；还会把简单实现复杂化、添加未要求的功能和抽象；以及顺手修改与当前任务无关的代码。Guardrails 是把这些行为偏差变成可约束的工程规则。

## Mental Model

Guardrails = 认知纪律（不猜测）+ 简洁纪律（最小实现）+ 修改边界纪律（只改被要求的）。

在大规模 AI Coding 场景中，Guardrails 还要进入准入治理：AI 生成物应说明假设、证据、风险、回滚路径和删除条件。

## Three Disciplines

### 认知纪律
- 不要猜测；遇到歧义时明确说明假设，提供多种解释。
- 困惑时停下来请求澄清，而不是继续执行。
- 发现更简单方案时主动提出，甚至反驳用户或当前方向。

### 简洁纪律
- 不添加未要求的功能、一次性抽象、过度配置或过早错误处理。
- 以"资深工程师是否会认为复杂"为检验标准。
- AGENTS.md 等全局约束应明确列出"禁止添加"项。

### 修改边界纪律
- 只修改能追溯到用户请求的代码行，匹配既有风格。
- 仅清理自己改动造成的孤儿导入、变量和函数。
- 预先存在的死代码可以指出，但未被要求不应擅自删除。
- 不顺手重构、格式化或删除与本次请求无关的代码。

## Key Claims

- explicit（Karpathy）：模型在不受约束时会替用户做假设、隐藏困惑、忽略歧义和权衡。
- explicit（Karpathy）：精准修改要求每一行变更都能直接追溯到用户请求。
- explicit（Karpathy）：因当前改动产生的孤儿导入/变量/函数应清理；预先存在的死代码不应擅自删除。
- inferred：这套工作协议从"提示模型写好代码"转向"约束模型的假设、复杂度和变更边界"。
- inferred：DeSlop 视角把 Guardrails 从单次任务行为约束扩展为代码库生命周期治理。

## Examples

- 约束 AGENTS.md 写明"禁止添加未请求的功能"，Agent 遇到模糊需求时应先停下说明假设。
- PR 描述模板要求 Agent 列出"本次做了哪些假设"，人工审查时对照。
- `反捷径证据` 审查：问"Agent 是否在没有说明假设的情况下修改了与请求无关的代码"。

## Common Confusions

- Guardrails 不是让 Agent 更慢，而是让 Agent 的工作更可解释、可审查和可控。
- 澄清纪律不是让 Agent 每步都停下来确认；是在"真正歧义"和"正常推断"之间做区分。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/Karpathy 的观察.xmind|Karpathy 的观察]] — 列出认知纪律、简洁纪律和修改边界纪律的原始素材。
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]] — AGENTS.md 不是百科全书；约束需要进入可执行规则，不只是口头禁止。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind|垃圾治理(DeSlop).xmind]] — 补充约束、限权、准入、复杂度税和退场治理。

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]] — Guardrails 是 harness guardrail layer 的行为约束部分
- supports: [[concepts/反捷径证据|反捷径证据]] — 精准修改边界是反捷径审查的前提
- supports: [[concepts/AI 代码垃圾治理|AI 代码垃圾治理]] — Guardrails 是 DeSlop 的生成前和生成中控制层
- related-source: [[entities/Andrej Karpathy|Andrej Karpathy]] — 来源于 Karpathy 对 LLM coding 行为的直接观察
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Agent Coding Guardrails 是把"我希望 Agent 不要这样做"变成可写入规则、可审查、可回归的工程约束。

## Review Questions

- Guardrails 的三类纪律分别针对 Agent 的哪种错误行为？
- 为什么"精准修改"需要"能追溯到用户请求"？
- Guardrails 如何配合 AGENTS.md 实现可执行约束？

## Open Questions

- 不同任务类型（new feature vs bug fix vs refactor）需要不同强度的 guardrails，还需要实践案例支撑。
