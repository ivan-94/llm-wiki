---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/Github 原住民.xmind"
source_relpath: "Vibe/工具/Github 原住民.xmind"
raw_created_at: 2026-05-07T03:37:51.775275+00:00
raw_modified_at: 2026-05-07T05:38:13.282212+00:00
raw_size: 4119767
raw_fingerprint: "size=4119767;birth=2026-05-07T03:37:51.775275+00:00;mtime=2026-05-07T05:38:13.282212+00:00"
raw_snapshot_at: 2026-05-29T16:03:40.320897+00:00
ingested_at: 2026-05-29
status: ingested
---

# Github 原住民.xmind

## Source

- Raw file: [Vibe/工具/Github 原住民.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/Github%20%E5%8E%9F%E4%BD%8F%E6%B0%91.xmind>)
- Raw ref: `raw:Vibe/工具/Github 原住民.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-05-07T03:37:51.775275+00:00`; modified `2026-05-07T05:38:13.282212+00:00`; size `4119767`; snapshot `2026-05-29T16:03:40.320897+00:00`
- Coverage: all sheets discovered and exported with `export_xmind_source.py`; sheet count `1`; sheets: `画布 1` (105 topics).

## Summary

这份 XMind 把 GitHub 原生工作流归纳为从 Issue 到 Label、Projects、PR、Actions、Milestones、Releases 和 Discussions 的闭环，强调任务源、流转自动化、PR 质量门禁和社区噪音隔离。

## Source Digest

source 的核心公式是 `Issue -> Label -> Projects -> PR -> Actions -> 自动闭环`。它认为 GitHub 原住民工作方式的关键不是工具数量，而是让任务从提出、分类、执行、审查、合并、发布到关闭的流转足够顺滑。五个原则分别是：Issue 是唯一任务源，一个 PR 只做一件事，PR 必须关闭 issue，自动化优先于人工拖拽，Discussion 承接用法咨询和闲聊以保持 issue 池纯净。

落地层面，source 给出一人公司最小可用版本：bug/feature issue 模板，type/priority/status 标签，Backlog -> In Progress -> Review -> Done 看板，强制 `Closes #xxx` 的 PR 模板，以及 CI 测试、PR 自动打标签和 stale 提醒 Actions。更完整版本分为六层武器：Issue 模板和 labels 作为入口与分类器；Sub-Issues 与 dependencies 拆任务和表达阻塞；Projects 作为跨阶段、跨仓库的可视化作战地图；PR 作为质量闸门，带 checklist、issue 关联、分级 review 和 CI；Milestones/Releases 控制版本节奏；Discussions 分离社区流量和真正待办。

实战案例用 Next.js 风格流转说明 Discussion 可能转化为 bug issue，经过 triage 和优先级判断后拆分子 issue，贡献者认领并开 PR，CI 跑测试，合并后子 issue 自动关闭，主 issue 进度更新，所有子 issue 完成后主 issue 关闭并推动 milestone 前进。

## Key Claims

- explicit: GitHub 原生工作流的核心闭环是 Issue、Label、Projects、PR、Actions 之间的自动流转。
- explicit: Issue 应作为唯一任务源，Discussion 应承接用法问题和闲聊，以保持 issue 池纯净。
- explicit: 一个 PR 应只做一件事，并通过 `Closes #xxx`、`Fixes #xxx` 或相关链接与 issue 强关联。
- explicit: 最小可用 GitHub 工作流包括 issue 模板、精简 labels、Projects 看板、PR 模板和基础 Actions 自动化。
- explicit: 完整治理可分为 Issue、Sub-Issues/Dependencies、Projects、PR、Milestones/Releases、Discussions 六层。
- inferred: 这份 source 可作为 Agent 项目协作和 PRD/issue/HAT 工作流的 GitHub 原生底座。
- inferred: 对个人或小团队来说，先建立最小闭环比一次性引入复杂项目管理系统更有价值。

## External Links

No external links found in extracted content.

## Links

- compiled-synthesis: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — 六层 GitHub 治理体系的核心来源，包括最小可用版本和六层武器。
- compiled-synthesis: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 支撑 GitHub 作为 Agentic delivery 的状态机与证据流转层。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — GitHub-HAT 工作流簇的核心来源。
- prerequisite: [[sources/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png|基于 github 的工作流]] — Github 原住民是理解 GitHub 工作流图的前提知识。
- used-in: [[entities/GStack|GStack]] — GStack 的发布和质量门禁流程以 GitHub 为基础平台。

## Maintenance Notes

- source 中的 Next.js 流转是示例化案例，未绑定真实 issue 编号或官方流程；后续引用时应标注为流程例子。
- source 没有外部 URL；GitHub Projects、Sub-Issues、Dependencies、Actions、Milestones 等当前产品行为未联网核验。

- Link cleanup candidate: related: GitHub 原生工作流 — 可沉淀 Issue 到 PR、Actions、Release 的闭环模型。.
- Link cleanup candidate: related: Issue 驱动开发 — source 强调 Issue 是唯一任务源和 triage 入口。.
- Link cleanup candidate: related: PR 质量门禁 — source 汇总 PR 模板、review 分级、CI 与 issue 关联。.
