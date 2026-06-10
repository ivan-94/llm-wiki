---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png"
raw_created_at: 2026-06-05T14:56:16.528084+00:00
raw_modified_at: 2026-06-05T14:56:16.528426+00:00
raw_size: 1773388
raw_fingerprint: "size=1773388;birth=2026-06-05T14:56:16.528084+00:00;mtime=2026-06-05T14:56:16.528426+00:00"
raw_snapshot_at: 2026-06-10T13:15:09+00:00
ingested_at: 2026-06-10
status: ingested
---

# adversarial-ui-review-loop.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/adversarial-ui-review-loop.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-06-05T14:56:16.528084+00:00`; modified `2026-06-05T14:56:16.528426+00:00`; size `1773388`; snapshot `2026-06-10T13:15:09+00:00`
- Coverage: opened with Agent vision; full 1536x1024 infographic inspected; visible text is clear.

## Source Cluster

- Directory cluster: Vibe/工具/mattpocock:skills  ⭐
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[sources/Vibe/工具/mattpocock:skills  ⭐/Matt Pocock Skills.xmind|Matt Pocock Skills.xmind]] — 同属 Matt Pocock Skills cluster，提供 skill 方法论总览。
  - contrasts-source: [[sources/Vibe/工具/mattpocock:skills  ⭐/visual-fidelity-loop.png|visual-fidelity-loop.png]] — 本图适用于无目标设计稿的现有 UI 审美审查；visual-fidelity-loop 适用于已有设计稿/截图目标的像素对齐。

## Summary

这张图定义了 Adversarial UI Review Loop：在没有明确设计稿时，用只读批判、P0/P1 优先、截断筛选、批准修复和验证复评形成 UI 审美改进循环。

## Source Digest

图中角色分为组织者、UI 设计师和前端开发者。组织者提供上下文、业务目标、用户场景、边界、组件和 token 参考，并提供多端、多状态、关键流程和交互状态截图证据；UI 设计师只查看截图证据，不修改代码，输出 P0/P1/P2/P3 findings；组织者截断筛选，只保留 P0/P1 并补充信息；前端开发者只修复已批准项，复用组件和 token，提交变更记录与修复说明；最后组织者和设计师验证复评，如果仍有 P0/P1 则继续循环。

该循环的原则是只读批判、证据优先、默认只修 P0/P1、拒绝偏好化、复用组件与 token、防止无限挑刺。适用场景是没有目标设计稿的现有产品界面，需要审美改进；不适用于已有 Figma、截图目标、需要视觉像素对齐或以还原为核心目标的任务。

## Key Claims

- explicit: UI 设计师只读批判，不修改代码；前端开发者只修改已批准项，不做审美裁决。
- explicit: Findings 按 P0/P1/P2/P3 分级，默认只修 P0/P1，避免无限挑刺。
- explicit: 输入需要上下文、范围、截图证据和循环记录；输出需要问题清单、修复示例、验证结果和历史版本。
- explicit: 该 skill 适用于无目标设计稿的现有 UI，不适用于已有 Figma/截图目标时的视觉像素对齐。
- inferred: Adversarial UI Review Loop 是把主观审美争论改造成“证据截图 + 严重级别 + 批准修复 + 复评”的工作流治理。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/对抗式 UI 审美审查|对抗式 UI 审美审查]] — 本图提供无设计稿 UI 审查的角色分工、分级和复评循环。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充 UI 审美审查类 workflow skill 的角色分工和循环条件。
- updates: [[concepts/Agent Skills|Agent Skills]] — 作为 Lightweight/Workflow skill 的视觉质量治理案例。
- compiled-entity: [[entities/Matt Pocock|Matt Pocock]] — 补充 Matt Pocock Skills cluster 中 UI 审查工作流证据。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 纳入 Matt Pocock 扩展 skills。
- contrasts-source: [[sources/Vibe/工具/mattpocock:skills  ⭐/visual-fidelity-loop.png|visual-fidelity-loop.png]] — 两者边界由“无设计稿审美改进”与“有目标设计稿像素对齐”区分。

## Maintenance Notes

- 图片没有可见 URL。
- 图中示例 UI 截图为说明性素材，不应当作真实项目缺陷证据。
