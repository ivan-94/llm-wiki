---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/ai_coding.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/ai_coding.png"
raw_created_at: 2026-05-05T05:27:12.607547+00:00
raw_modified_at: 2026-05-05T05:28:04.743179+00:00
raw_size: 1883367
raw_fingerprint: "size=1883367;birth=2026-05-05T05:27:12.607547+00:00;mtime=2026-05-05T05:28:04.743179+00:00"
raw_snapshot_at: 2026-05-29T16:15:48+00:00
ingested_at: 2026-05-30
status: ingested
---

# ai_coding.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/ai_coding.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/ai_coding.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/ai_coding.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T05:27:12.607547+00:00`; modified `2026-05-05T05:28:04.743179+00:00`; size `1883367`; snapshot `2026-05-29T16:15:48+00:00`
- Coverage: Vision read of a 1122x1402 infographic about integrating SbE into AI Coding workflows, including phases, gates, and test layering.

## Summary

这张图将 SbE 放进 AI Coding 工作流：AI Coding 负责加速产出，SbE 负责用业务示例持续校准设计、实现和验证，使“先有示例、再有规格、先有共识、再有代码”成为交付链路。

## Source Digest

图中先重新定位 AI Coding 时代的 SbE：Spec 只是流程中的一步，完整链路包含头脑风暴、需求澄清、规格形成、技术设计、任务拆分、实现验证、覆盖检查和活文档维护。SbE 不应等到最后测试才出现，而应从需求澄清阶段开始介入，把业务目标、规则、示例和待确认问题转成可验证输入。

阶段详解把每一步都拆成重点、输入、输出和检查点。需求澄清阶段使用 Example Mapping 形成业务规则、示例和问题；规格形成阶段用 Markdown Spec/Gherkin/示例表沉淀验收标准；技术设计阶段要求解释“如何支持这些示例”；任务拆分要把任务绑定到示例；实现验证阶段先测试后实现，围绕示例收敛；覆盖检查不只问代码是否写完，而是问哪些示例通过、哪些规则未覆盖；活文档维护则在规则变化时先改示例再改代码。底部还建议测试分层：业务规则密集处用单元测试，跨服务规则用 API/集成测试，核心用户路径用 E2E，低风险展示用组件测试或人工验收。

## Key Claims

- explicit: AI Coding 负责加速产出，SbE 负责用业务示例持续校准设计、实现与验证。
- explicit: SbE 从需求澄清阶段就开始介入，不是等到最后测试时才出现。
- explicit: 完整链路包括头脑风暴、需求澄清、规格形成、技术设计、任务拆分、实现验证、覆盖检查和活文档维护。
- explicit: 五个关键 gate 是 Example Gate、Design Gate、Task Gate、Implementation Gate 和 Coverage Gate。
- explicit: 示例驱动实现时应采用测试分层，避免把所有示例都推进 E2E。
- inferred: 这张图可作为 AI Coding 下“需求到代码的验收链路”综合页的主结构来源。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Specification by Example|Specification by Example]] — 候选概念；本图提供 AI Coding 工作流中的 SbE 定位和阶段边界。
- compiled-concept: [[concepts/示例驱动 AI Coding|示例驱动 AI Coding]] — 候选概念；本图将示例、规格、设计、任务、测试串成 AI 编码交付链。
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]] — 候选地图入口；可放入 SbE 与 AI Coding 实践模块。

## Maintenance Notes

- Vision-based ingest; exact stage wording should be rechecked against raw image before verbatim quotation.
- No compiled pages were created in this batch by scope constraint.
