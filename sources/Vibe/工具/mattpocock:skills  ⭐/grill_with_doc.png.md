---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/grill_with_doc.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/grill_with_doc.png"
raw_created_at: 2026-05-05T20:41:11+08:00
raw_modified_at: 2026-05-05T20:41:11+08:00
raw_size: 1879235
raw_fingerprint: "size=1879235;birth=2026-05-05T20:41:11+08:00;mtime=2026-05-05T20:41:11+08:00"
raw_snapshot_at: 2026-05-30T00:07:20+08:00
ingested_at: 2026-05-30
status: ingested
---

# grill_with_doc.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/grill_with_doc.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/grill_with_doc.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/grill_with_doc.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T20:41:11+08:00`; modified `2026-05-05T20:41:11+08:00`; size `1879235`; snapshot `2026-05-30T00:07:20+08:00`
- Coverage: Vision read of a 864 x 1821 infographic. Main headings, process boxes, side panels, and visible labels are readable; small explanatory copy is summarized rather than treated as exact OCR.

## Summary

这张图说明 `grill-with-docs` 是一种带文档沉淀的设计拷问流程：围绕术语、概念边界、边界场景、实现与说法矛盾、上下文关系等问题逐个追问，并把对齐后的语言、关系和决策写回 `CONTEXT.md`、`CONTEXT-MAP.md` 或 ADR。

## Source Digest

图的中心是从 Plan、`CONTEXT.md` / `CONTEXT-MAP.md`、`docs/adr/` 读取上下文开始，进入“逐个问题访谈”的循环：一次只问一个问题，聚焦一个决策点；随后用具体场景压测边界，用代码探索验证说法是否被实现支持，再把术语达成一致并立即更新文档。右侧“文档产物”把输出分为 `CONTEXT.md`、`CONTEXT-MAP.md` 和 ADR：前者记录领域语言、术语和关键定义；中者记录多个上下文及关系与边界；ADR 只用于重要且具备权衡的决策。底部给出 ADR 判断门，强调 hard to reverse、surprising later、real trade-off 三个条件都满足才建议 ADR。整体方法不是单纯问答，而是“拷问 -> 验证 -> 记录 -> 对齐 -> 推进”的持续循环。

## Key Claims

- explicit: `grill-with-docs` 的核心约束是“一次只问一个问题”，避免一次性抛出多个未拆分问题。
- explicit: 设计拷问应覆盖模糊术语、同词多义、概念边界、边界场景、实现与说法矛盾、上下文之间的关系。
- explicit: 文档输出包括 `CONTEXT.md`、`CONTEXT-MAP.md` 和 ADR，但 ADR 应谨慎使用。
- explicit: `CONTEXT.md` 格式建议包含 Language、Relationships、Example dialogue、Flagged ambiguities。
- inferred: 该 workflow skill 的价值在于把设计澄清从临时对话升级为可复用的领域词汇和架构记录。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/设计拷问工作流|设计拷问工作流]] — 可沉淀“一次一个问题、场景压测、代码验证、文档回写”的 workflow skill 模式。
- map-entry candidate: [[maps/Vibe 工具与 Agent Skills 学习地图|Vibe 工具与 Agent Skills 学习地图]] — 可作为 mattpocock skills 中“文档化设计澄清”分支。

## Maintenance Notes

- 图片为信息图，整体清晰；小字号说明可能存在视觉读取误差，精确措辞需回看 raw。
- 未联网核验 `CONTEXT.md`、`CONTEXT-MAP.md` 或 ADR 相关实践，只记录图片中可见内容。
