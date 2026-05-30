---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# AI Coding 偏移控制

## Definition

AI Coding 偏移控制是防止 Agent 在大型需求中偏离真实目标、语义边界、决策归属、执行路径和长期工程质量的一组治理方法。

## Why It Matters

大型需求失败常常不是代码不能跑，而是 Agent 在 spec 未覆盖的空间中静默做了产品、架构、安全或领域决策。

## Mental Model

偏移控制 = 决策分辨率 + 语义图 + 执行图 + 证据图 + 反捷径审查 + 维护者视角。

## Key Claims

- 稀疏 spec 会留下高维未定义空间，Agent 会自动补全。
- 决策权泄漏是大型 AI Coding 偏移的核心根因。
- 测试通过只是代理信号，不能等同于语义完成。
- 完成定义应同时覆盖行为、语义、决策归属、路径收敛、抗捷径和可维护性。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移控制审计方向.xmind|大型需求的偏移控制审计方向]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Vibe Coding 的 Sweet Spot：从粗生成到精修.xmind|Vibe Coding 的 Sweet Spot]]

## Relations

- part-of: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- contains: [[concepts/决策权泄漏|决策权泄漏]]
- contains: [[concepts/反捷径证据|反捷径证据]]
- contains: [[concepts/工程宪法|工程宪法]]

## My Understanding

当前理解：偏移控制的重点不是把 spec 写无限长，而是识别哪些判断必须上浮、哪些证据能证明没有投机。

## Review Questions

- 为什么大型需求会出现决策权泄漏？
- 反捷径审查和普通测试有什么差异？

## Open Questions

- 六张治理图还需要整理成可复用模板。
