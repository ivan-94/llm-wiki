---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-10
---

# 深模块（Deep Module）

## Definition

深模块（Deep Module）是 John Ousterhout 在《A Philosophy of Software Design》中提出的设计原则：好的模块应该有**简单的接口**和**强大的实现**——接口复杂度远低于功能复杂度，隐藏的复杂性越多，模块越"深"。反之，接口复杂但功能薄弱的模块是"浅模块"。

## Why It Matters

Agent 驱动的开发会产生大量"宽接口"代码——大量方法、参数和概念暴露在表面，而背后实现却很薄。深模块原则帮助人类工程师和 Agent 共同维护"越改越简单"的趋势：每次重构的目标是收缩接口、增强实现，而不是添加更多抽象。

## Mental Model

用矩形面积比喻：
- 宽模块：矩形很宽但很扁（接口多，功能少）
- 深模块：矩形很高但很窄（接口少，功能多）

越深的模块，上层使用者需要理解的"表面积"越小。

## Key Claims

- 深模块的判断标准：接口是否比其内部实现简单得多？能否通过接口完成大量工作？
- `/improve-codebase-architecture` skill 寻找的"deepening opportunities"就是把浅模块重构为深模块的机会。
- deletion test：如果一段代码删除后，调用方无需改变，说明它没有真正被需要（YAGNI 反例）。
- Agent 倾向于添加层和抽象，但这往往会制造浅模块；架构改进的方向是减少接口、增强深度。
- CONTEXT.md 中的模型语言设计也遵循深模块原则：术语的定义应该精确而少，覆盖的语义应该宽而深。

## Examples

- 好的文件 I/O 库（如 Unix 文件系统）：open/read/write/close 四个系统调用覆盖所有文件操作——接口极简，实现极深。
- 浅模块反例：一个类有 20 个方法，每个方法只包装一个外部调用——调用方要理解所有 20 个方法，但每个方法功能极薄。

## Common Confusions

- 深模块 ≠ 单一大类：一个大类可以有很多方法和复杂实现，但如果接口暴露的概念很多，它仍然是"浅"的。
- 简单接口 ≠ 少功能：简单接口是指调用方需要理解的概念少，不是说功能少。
- 深模块不适合一切场景：对于快速原型、一次性脚本，过度追求深模块会增加不必要的设计成本。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills]] — 把 deep module、deletion test、interface 作为工程协作中的关键抽象，并作为 `/improve-codebase-architecture` 的判断依据。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/优化架构.png|优化架构]] — 可视化架构改进中寻找 deepening opportunities 的思路。

## Relations

- related: [[concepts/Agentic Engineering|Agentic Engineering]] — 深模块是 Agentic Engineering L3 执行层中架构设计的核心原则。
- enables: [[concepts/CONTEXT.md 领域语言|CONTEXT.md 领域语言]] — 领域语言设计也应遵循深模块原则，用少量精确术语覆盖更多语义。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

深模块是 Agent 时代架构设计的方向指标：当代码量急剧膨胀时，判断质量的标准不是代码量，而是接口是否比实现更简单。

## Review Questions

- 深模块和浅模块最核心的判断依据是什么？
- deletion test 是如何帮助判断模块深度的？
- Agent 为什么倾向于制造浅模块？

## Open Questions

- 深模块原则在 microservices 架构中如何应用——service 接口本身如何保持"深"？
