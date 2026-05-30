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

偏移控制 = 决策分辨率 + 六张治理图 + 完整工作流 + 七维完成定义。

## Six Governance Diagrams

源于 `大型需求的偏移根因与控制`，每张图对应一个治理面：

| 图 | 目的 | 主要问题 |
| --- | --- | --- |
| 决策图 | 标出哪些判断不能交给 Agent 静默决定 | 哪些判断属于产品/架构/安全决策？ |
| 语义图 | 固定实体、状态、规则和不变量 | 系统里的核心词各自是什么意思？ |
| 执行图 | 确保规则落到所有入口的必经路径 | 每个调用入口都强制走了这条规则吗？ |
| 证据图 | 为关键语义匹配测试和 contract | 哪些测试能证明语义，而不只是代码路径？ |
| 反捷径图 | 审查哪些错误实现也能通过当前测试 | 什么错误实现能骗过当前测试？ |
| 维护者图 | 检查实现未来改起来是否痛 | 这段代码两个月后能维护吗？ |

## Nine-Step Workflow

完整工作流（源于 `大型需求的偏移根因与控制`）：
1. 读取原始需求
2. 设定决策分辨率（L0–L4 分层）
3. 生成决策图
4. 生成语义图、执行图、证据图
5. 读取工程宪法
6. 测试先行（基于证据图）
7. 实现
8. 反捷径审查（基于反捷径图）
9. 维护者审查（基于维护者图），必要重构

## Seven Dimensions of Done

完成定义需覆盖七个维度：
1. **行为实现**：用户可见行为符合 spec 和 examples。
2. **语义证明**：关键实体状态和业务规则有可追溯证据。
3. **决策受控**：L0–L2 层的关键判断已记录，不是 Agent 自行补全。
4. **粒度正确**：没有把应该统一的规则分散在多处实现。
5. **路径收敛**：所有入口都经过了必要规则路径。
6. **测试抗投机**：反捷径审查通过，错误实现不容易混过测试。
7. **代码可维护**：维护者审查通过，未来可以修改和演进。

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
- enables: [[concepts/Implementation Notes 审计|Implementation Notes 审计]] — 九步工作流产出的 Implementation Notes 记录偏移决策轨迹
- requires: [[concepts/CONTEXT.md 领域语言|CONTEXT.md 领域语言]] — 语义图的基础来源

## My Understanding

当前理解：偏移控制的重点不是把 spec 写无限长，而是识别哪些判断必须上浮、哪些证据能证明没有投机。

## Review Questions

- 为什么大型需求会出现决策权泄漏？
- 反捷径审查和普通测试有什么差异？

## Open Questions

- 六张治理图还需要整理成可复用模板。
