---
page_type: concept
updated_at: 2026-06-10
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-24
---

# Skill Contract DSL

## Definition

Skill Contract DSL 是用 Python-shaped contract 描述 Agent Skill 的触发、输入、输出、控制流、安全边界和验证规则，让 skill 从散文提示变成可审查、可机械验证的行为契约。

## Why It Matters

自然语言 skill 容易隐藏触发歧义、输入缺口、输出不清和安全边界不明。DSL-backed skill 的价值不是替代 `SKILL.md`，而是把关键形状前置，让 Agent 和审查者都能看见这个 skill 应该如何被触发、执行和验证。

## Mental Model

```
contract.pyi = 形状契约
SKILL.md = Agent 使用指南
examples/*.md = 复杂语法按需样例
validate_contract.py = 机械验证
```

## Key Claims

- Skill 不是散文，而是 Agent 行为契约。
- DSL 的目标是把自然语言的不确定性降到可控、可验证范围。
- 最小契约应覆盖 skill、activate_when、inputs、outputs。
- 复杂控制流可进一步表达 workflow、modes、graph、state、loop。
- `call_*` 只应嵌入自然语言 f-string，避免把 DSL 发展成另一门复杂通用语言。
- 最佳原则是 hard error 管机械错误，warning 保留语义缺口。

## Examples

- 一个 HAT skill 的 contract 可以声明：只有当存在 `hat-prepare` 产物时才能运行；输入是 guide/prepare.sh 路径；输出是 summary/results/logs/artifacts。
- 一个 UI review skill 的 contract 可以声明：输入必须包含截图证据和范围；输出必须是 P0/P1 findings 和批准修复项，而不是泛泛建议。

## Common Confusions

- Skill Contract DSL 不是要把 skill 全部程序化；自然语言仍负责“怎么做”和“为什么”。
- DSL 不是越完整越好；轻量到足以约束 Agent，避免变成另一门沉重语言。
- 机械验证只能管形状错误，不能替代语义审查。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png|create-dsl-skills.png]] — 提供 WHY/WHAT/HOW、工作流闭环和风险判断。

## Relations

- part-of: [[concepts/Agent Skills|Agent Skills]] — Skill Contract DSL 是 skill 契约化的一种实现路线。
- strengthens: [[concepts/Skill 触发契约|Skill 触发契约]] — `activate_when`、inputs 和 outputs 让触发契约更可检查。
- supports: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — workflow/modes/graph/state/loop 可表达复杂 skill 控制流。
- related: [[concepts/Agent 上下文审计|Agent 上下文审计]] — 审计可检查新 Agent 是否按 contract 形成正确行动模型。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

Skill Contract DSL 的价值是给自然语言 skill 加一层骨架：自然语言保留语义弹性，contract 约束触发、输入、输出和控制流。

## Review Questions

- `contract.pyi` 和 `SKILL.md` 的分工是什么？
- 为什么 hard error 和 warning 要区分？
- DSL 过度设计会带来什么风险？

## Open Questions

- 还需要真实 skill 文件案例验证 DSL contract 的维护成本和收益。
