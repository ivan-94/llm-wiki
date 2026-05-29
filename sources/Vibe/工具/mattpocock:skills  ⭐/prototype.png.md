---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/prototype.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/prototype.png"
raw_created_at: 2026-05-11T08:32:16.967093+00:00
raw_modified_at: 2026-05-11T08:32:16.967383+00:00
raw_size: 1679636
raw_fingerprint: "size=1679636;birth=2026-05-11T08:32:16.967093+00:00;mtime=2026-05-11T08:32:16.967383+00:00"
raw_snapshot_at: 2026-05-30T00:07:20+08:00
ingested_at: 2026-05-30
status: ingested
---

# prototype.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/prototype.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/prototype.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/prototype.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-11T08:32:16.967093+00:00`; modified `2026-05-11T08:32:16.967383+00:00`; size `1679636`; snapshot `2026-05-30T00:07:20+08:00`
- Coverage: Vision read of a 1024 x 1536 infographic. Main sections and flow steps are readable; terminal and UI mockup details are interpreted visually, not extracted as exact code.

## Summary

这张图说明 Prototype Skill 用“可丢弃原型”回答设计问题：在正式实现前快速摸清状态模型、业务边界、API/数据结构或页面布局方向的不确定性。它区分 Logic Prototype 和 UI Prototype，并给出从明确问题到清理原型的八步流程。

## Source Digest

图的核心主张是“先快速摸清不确定性，再决定正式实现”。使用场景包括状态模型说不清、业务规则有边界情况、API / 数据结构需要手感、页面布局方向不确定，以及想在投入生产代码前快速试错。原型被定义为临时学习工具，分成两条分支：Logic Prototype 更像终端交互小程序，通过按键触发 action、每步展示完整 state，适合状态机、Reducer 和数据模型；UI Prototype 支持同一路由多方案、通过 `?variant=` 切换、底部浮动切换条，适合页面、组件和流程设计。流程从明确问题开始，选择 Logic 或 UI 分支，把原型放在靠近真实代码的位置，做到一条命令可运行，然后暴露完整状态或方案，让用户试玩、比较、反馈，记录结论，最后删除原型或吸收到正式代码。

## Key Claims

- explicit: Prototype Skill 的目标是用可丢弃原型回答设计问题。
- explicit: 适用场景包括状态模型、业务边界、API/数据结构、页面布局方向和生产前试错。
- explicit: Logic Prototype 适合状态机、Reducer、数据模型，强调 action 触发和完整 state 展示。
- explicit: UI Prototype 适合页面、组件、流程设计，支持多方案切换。
- explicit: 原型流程最终要记录结论，并删除原型或吸收到正式代码。
- inferred: 该 skill 把“不确定性探索”从生产实现中分离出来，降低过早固化错误设计的成本。

## External Links

No external links found in extracted content.

## Links

- related: 可丢弃原型工作流 — 可沉淀 Logic/UI prototype 分支和“学到答案后清理”的原则。
- related: Vibe 工具与 Agent Skills 学习地图 — 可作为 mattpocock skills 中“设计不确定性探索”分支。

## Maintenance Notes

- 图片清晰；终端示例和 UI mockup 只作为视觉示意，不作为可运行命令或真实 API 记录。
- 未创建实际 prototype 或验证图中流程，只完成 source note ingest。
