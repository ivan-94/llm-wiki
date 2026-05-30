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

# Vibe 设计原型开发

## Definition

Vibe 设计原型开发是针对高不确定性项目的设计方式变革：先用 Vibe Coding 快速生成可交互原型来探索需求和设计方案，在设计方向收敛后再走严肃工程化路径——而不是在不确定阶段就投入完整规格和实现资源。

## Why It Matters

传统设计流程要求在开发前"想清楚"；但高不确定性项目（新产品、创新功能、需求模糊的领域）往往无法在白纸阶段想清楚。Vibe Coding 让原型成本足够低，使"先做原型，用运行的东西验证设计"成为可行路径。

## Mental Model

不确定项目的设计 = 探索循环（Vibe 生成原型 → 人工运行/体验 → 发现真实问题 → 精化意图） → 收敛后进入工程化。

## Two-Phase Model

### Phase 1：原型探索
- 目标：发现"真实需要什么"，而不是"以为需要什么"。
- 方法：用 Vibe Coding 快速生成可运行的设计雏形（UI 交互、数据流、关键场景）。
- 原则：**原型不可产品化**——原型代码可以抛弃，不应直接演化为生产代码；否则技术负债从原型期就埋下。
- 验证：通过实际体验、用户测试或团队共识判断方向是否正确。

### Phase 2：工程化
- 触发条件：设计方向已收敛，核心场景已验证，可以写出明确的 PRD/spec。
- 方法：用 Agentic Engineering 路径——规格、任务切片、Harness、测试、HAT 和验收。
- 重要：原型代码不直接迁移；从 spec 出发重新实现。

## Key Claims

- explicit（从 Vibe Coding 到 Agentic Engineering）：Vibe Coding 抬高软件创造下限，让非工程师也能快速做产品和验证 idea。
- explicit（年中总结）：产品或老板可以先 Vibe Coding 验证想法，降低方向风险。
- inferred：设计原型开发是 Vibe Coding 和 Agentic Engineering 的组合使用：Vibe 阶段用于发散和验证，Agentic 阶段用于收敛和交付。
- inferred：原型不可产品化是区分"探索"和"交付"的重要边界约束。

## Examples

- 新 AI 功能原型：用一天时间 Vibe Coding 出核心 AI 交互流，让团队体验后确定哪个场景值得深入——再写完整规格。
- 创新产品 Demo：产品经理 Vibe Coding 出可点击的 Demo，用于团队对齐和 VC 演示，不要求可维护性。

## Common Confusions

- Vibe 设计原型开发不是"原型做完就上线"；原型是方向探针，不是产品。
- 也不是说"先 Vibe 后工程化"是所有项目的标准流程；只适合高不确定性场景。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]] — Vibe Coding 抬高创造下限，原型驱动验证。
- [[sources/Vibe/Vibe Coding 随手记/2026年中总结.xmind|2026年中总结]] — 产品可先 Vibe Coding 验证想法；业务项目可 Vibe Coding；严肃项目走完整流程。

## Relations

- part-of: [[concepts/Vibe Coding|Vibe Coding]] — 是 Vibe Coding 在设计探索场景的具体应用模式
- precedes: [[concepts/Agentic Engineering|Agentic Engineering]] — 原型收敛后进入 Agentic Engineering
- contrasts-with: [[concepts/Spec-Driven Development|Spec-Driven Development]] — 高不确定期先原型后 spec，而非先 spec 后实现
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Vibe 设计原型开发是高不确定项目的"先打样后定型"策略——Vibe Coding 降低了打样成本，使这个策略可行。

## Review Questions

- 为什么原型不应该直接演化为生产代码？
- 从原型阶段进入工程化阶段的触发条件是什么？
- 设计原型开发适合哪类项目？不适合哪类？

## Open Questions

- 原型和产品代码之间的边界判断标准还需要具体案例。
