---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png"
raw_created_at: 2026-06-04T13:32:27.735373+00:00
raw_modified_at: 2026-06-04T13:32:27.735597+00:00
raw_size: 1705150
raw_fingerprint: "size=1705150;birth=2026-06-04T13:32:27.735373+00:00;mtime=2026-06-04T13:32:27.735597+00:00"
raw_snapshot_at: 2026-06-10T13:15:09+00:00
ingested_at: 2026-06-10
status: ingested
---

# create-dsl-skills.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/create-dsl-skills.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/create-dsl-skills.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-06-04T13:32:27.735373+00:00`; modified `2026-06-04T13:32:27.735597+00:00`; size `1705150`; snapshot `2026-06-10T13:15:09+00:00`
- Coverage: opened with Agent vision; full 1536x1024 infographic inspected; visible text is clear.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供 skill 方法论总览。
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext Skills 审查.png|Ext Skills 审查.png]] — 两者都把 skill 从散文提示提升为可审查契约。

## Summary

这张图把 `create-dsl-skills` 定义为用于 Agent Skills 的 Python-shaped Skill Contract DSL：目标是把自然语言的不确定性降低到可控、可验证的范围内。

## Source Digest

图中 WHY 部分强调 skill 不是散文，而是 Agent 行为契约；DSL 要减少猜测、跳读和隐式约定，把触发、输入、输出、安全边界前置，并让 skill 从“看起来对”变成可审查、可验证。

WHAT 部分把组成拆成 `contract.pyi` 规范本体、`SKILL.md` Agent Guide、`examples/*.md` 复杂语法按需加载、`validate_contract.py` 机械验证。DSL 是 Python-shaped，但不是通用编程语言；它的价值是“一份规范定义形状，一份指南告诉 Agent 如何使用形状”。

HOW 部分给出写法：先写最小契约，包括 skill、activate_when、inputs、outputs；再按真实控制流选择 workflow、modes、graph、state、loop；`call_*` 只嵌入自然语言 f-string；用户输入、授权和审批用结构化参数表达；语义审查之后再执行机械检查。工作流闭环是读来源、草拟 contract、声明行为、语义审查、压缩、机械验证、维护 skill。

## Key Claims

- explicit: Skill 不是散文，而是 Agent 行为契约。
- explicit: DSL 的目标是把自然语言的不确定性降到可控、可验证范围。
- explicit: 组成包括 `contract.pyi`、`SKILL.md`、`examples/*.md` 和 `validate_contract.py`。
- explicit: 写法应从最小契约开始，再根据真实控制流增加 workflow/modes/graph/state/loop。
- explicit: 最佳原则是 hard error 管机械错误，warning 保留语义缺口。
- inferred: `create-dsl-skills` 把 skill 作者的设计判断拆成“形式契约 + 自然语言语义 + 机械验证”三层，降低下游 Agent 误用概率。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/Skill Contract DSL|Skill Contract DSL]] — 本图提供 DSL-backed skill 的 contract.pyi、SKILL.md、examples 和验证闭环。
- updates: [[concepts/Agent Skills|Agent Skills]] — 补充 skill 作为行为契约和可验证资产的设计路线。
- updates: [[concepts/Skill 触发契约|Skill 触发契约]] — 补充 activate_when、inputs、outputs 和安全边界前置。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — DSL 可表达 workflow/modes/graph/state/loop 等编排结构。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 补充 Matt Pocock Skills cluster 中 DSL-backed skill 证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock 扩展 skills。

## Maintenance Notes

- 图片没有可见 URL。
- 图中的 `contract.pyi`/`validate_contract.py` 是 DSL 结构说明，不代表本 wiki 已实际接入该验证器。
