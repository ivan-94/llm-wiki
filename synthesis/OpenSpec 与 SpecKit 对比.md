---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 9
learning_status: learning
confidence: 3
difficulty: 3
review_after: 2026-06-05
---

# OpenSpec 与 SpecKit 对比

## Thesis

OpenSpec 和 SpecKit 都试图把 AI Coding 从 prompt 驱动推向 spec artifact 驱动，但侧重点不同：OpenSpec 更像变更治理和 spec delta 工作流，SpecKit 更强调 constitution、spec、plan、tasks 之间的约束链。

更深的差异是：OpenSpec 维护“当前事实和未来变更”的边界，适合存量系统防漂移；SpecKit 维护“想法到实现”的交付链，适合新 feature 从模糊意图走到可执行任务。两者都需要 SbE 或等价 examples 补足行为证据，否则 spec 仍可能停留在抽象文档层。

## Comparison

| 维度 | OpenSpec | SpecKit |
| --- | --- | --- |
| 主要关注 | change/proposal/spec/tasks 的治理链路 | constitution/spec/plan/tasks 的产物链 |
| 适用场景 | 管理变更、维护规范、让需求变更可审查 | 从模糊想法生成可执行计划和任务 |
| 核心产物 | proposal、spec delta、task list、validation | constitution、feature spec、plan、tasks、feature metadata |
| 对 Agent 的价值 | 给 Agent 明确变更范围和约束 | 给 Agent 明确目标、计划、任务和实现边界 |
| 风险 | 当前命令/目录状态需核验 | artifact 精确语义需回官方实现确认 |

## Selection Rules

- 如果问题是“现有系统现在承诺什么，下一次变更如何不破坏当前事实”，优先 OpenSpec。
- 如果问题是“一个新 feature 如何从想法变成 research、data model、contracts、tasks 和 implementation”，优先 SpecKit。
- 如果问题是“业务规则是否真的被理解”，无论 OpenSpec 还是 SpecKit，都要引入 SbE examples。
- 如果问题是“Agent 是否能长期执行不漂移”，spec artifact 还必须进入 GitHub/CI/HAT/harness 闭环。

## Evidence

- [[sources/Vibe/Spec/OpenSpec/概览.png|OpenSpec 概览]] 展示 OpenSpec 的角色和流程。
- [[sources/Vibe/Spec/OpenSpec/产出规范.png|OpenSpec 产出规范]] 展示 proposal/spec/tasks 等产物。
- [[sources/Vibe/Spec/OpenSpec/软件工程映射.png|OpenSpec 软件工程映射]] 将 OpenSpec 映射到软件工程活动。
- [[sources/Vibe/Spec/SpecKit/Spec_kit.png|SpecKit]] 展示 SpecKit 工作流。
- [[sources/Vibe/Spec/SpecKit/Spec_kit_产物.png|SpecKit 产物]] 展示 SpecKit artifact 图谱。
- [[sources/Vibe/Spec/SpecKit/对比 OpenSpec.png|对比 OpenSpec]] 直接给出两者对比。
- [[sources/Vibe/方法论.xmind|方法论.xmind]] 将 OpenSpec 与 Spec Kit 放在 SDD 工具谱系中。

## Implications

- 选择工具前先判断问题是“变更治理”还是“从想法到任务”。
- 两者都不能替代验收和运行反馈；spec artifact 需要进入测试、HAT 和 PR 流程。
- 当前产品/命令细节未联网核验，wiki 中的结论应理解为 raw 的学习整理，而非最新产品说明。
- 深度 compile 的重点不是二选一，而是把 OpenSpec、SpecKit、SbE 和 HAT 放到同一条“当前事实 -> 变更意图 -> 行为证据 -> 执行任务 -> 完成证据”的链路中。

## Related Concepts

- [[concepts/Spec-Driven Development|Spec-Driven Development]]
- [[concepts/Vibe Coding|Vibe Coding]]
- [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]

## My Take

OpenSpec 更像工程治理语言，SpecKit 更像 agent-friendly 规格生产线。二者可以互补：前者管理变更，后者生成执行链。

## Open Questions

- 需要后续用真实项目跑一次 OpenSpec/SpecKit，比较产物质量和 Agent 可执行性。
