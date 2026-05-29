---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png"
raw_created_at: 2026-05-04T13:50:33+00:00
raw_modified_at: 2026-05-04T13:51:10+00:00
raw_size: 1834758
raw_fingerprint: "size=1834758;birth=2026-05-04T13:50:33+00:00;mtime=2026-05-04T13:51:10+00:00"
raw_snapshot_at: 2026-05-29T16:20:35+00:00
ingested_at: 2026-05-30
status: ingested
---

# sbE与DDD_BDD_TDD.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/sbE%E4%B8%8EDDD_BDD_TDD.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/sbE与DDD_BDD_TDD.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-04T13:50:33+00:00`; modified `2026-05-04T13:51:10+00:00`; size `1834758`; snapshot `2026-05-29T16:20:35+00:00`
- Coverage: Vision inspection of a 1122x1402 infographic. Reliable visible text and layout were read at the diagram/table/summary level; exact small-print wording should be rechecked against the raw image if quoted.

## Summary

这张图把 DDD、SbE、BDD、TDD 放在同一条从业务理解到代码实现的协作链路里：DDD 负责理解领域，SbE 对齐需求和示例，BDD 把行为表达成可执行场景，TDD 用测试驱动底层实现。

## Source Digest

图片的核心不是把四种方法并列比较，而是强调它们在交付链路中的分工和衔接。上半部分用业务问题到高质量软件的流程图说明：领域建模先澄清业务语言和边界，Specification by Example 用示例和规则建立共享理解，BDD 将示例落成 Given-When-Then 等可执行行为场景，TDD 则把这些行为压力传导到设计、单元测试和重构。

中部表格把四者的关注层次拆开：SbE 关注需求/验收层，典型产物是示例、规则和可执行规格；BDD 关注行为/验收表达层，典型产物是场景；DDD 关注业务建模层，典型产物是领域模型、通用语言和限界上下文；TDD 关注设计/实现层，典型产物是单元测试和重构后的代码。下半部分用电商“下单支付”串联四种视角，说明从订单、支付、余额、账户等领域概念，到余额 100/50/未登录等示例，再到行为场景，最后进入测试、实现、通过、重构的循环。

图中还列出常见误解：BDD 不等于只写 Gherkin，SbE 不等于自动化测试，DDD 不只适合大项目，TDD 不能替代验收测试。这些误解共同指向一个边界：SbE/BDD/TDD 是不同层次的协作机制，自动化只是结果之一，业务共识和反馈链路才是主线。

## Key Claims

- explicit: 图中主张 `DDD 帮你理解业务；SbE 帮你对齐需求；BDD 帮你表达行为；TDD 帮你驱动实现`。
- explicit: SbE 常作为业务与技术之间的桥梁，BDD 常是 SbE 的落地表达方式之一，TDD 支撑底层实现质量。
- explicit: 四者不是并列替代关系，而是互相配合；推荐组合是 DDD 定义语言与模型，SbE 对齐示例与规则，BDD 形成可执行场景，TDD 驱动内部实现。
- explicit: 电商“下单支付”示例把 DDD 的领域概念、SbE 的余额/支付示例、BDD 的 Given-When-Then 场景和 TDD 的测试实现串成一条链路。
- inferred: 这张图适合支撑 `Specification by Example`、`BDD`、`DDD`、`TDD` 四者关系的综合页，而不是单独替代每个方法的完整教程。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/Specification by Example|Specification by Example]] — 候选概念；图片提供 SbE 在需求对齐和验收层的定位。
- related: [[synthesis/DDD SbE BDD TDD 协作链路|DDD SbE BDD TDD 协作链路]] — 候选综合；图片适合与同目录 SbE 流程图一起编译四种工程方法的关系。
- related: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]] — 候选地图入口；可作为软件工程基础中“从业务到测试实现”的学习节点。

## Maintenance Notes

- Image source note created from vision inspection; no OCR file or derived asset was written.
- This batch scope only permits source notes, so no concept, synthesis, map, index, or log page was modified.
- Exact visible text should be rechecked against the raw image before quotation because the infographic contains dense small labels.
