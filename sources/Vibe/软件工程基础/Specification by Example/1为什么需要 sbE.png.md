---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/1为什么需要 sbE.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/1为什么需要 sbE.png"
raw_created_at: 2026-05-04T21:43:05+08:00
raw_modified_at: 2026-05-04T21:43:31+08:00
raw_size: 1671937
raw_fingerprint: "size=1671937;birth=2026-05-04T21:43:05+08:00;mtime=2026-05-04T21:43:31+08:00"
raw_snapshot_at: 2026-05-30T00:14:12+08:00
ingested_at: 2026-05-30
status: ingested
---

# 1为什么需要 sbE.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/1为什么需要 sbE.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/1%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20sbE.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/1为什么需要 sbE.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-04T21:43:05+08:00`; modified `2026-05-04T21:43:31+08:00`; size `1671937`; snapshot `2026-05-30T00:14:12+08:00`
- Coverage: Agent vision inspected the full 1149x1369 course infographic. Main headings, examples, process diagram, comparison panels, and takeaway are readable.

## Summary

这张图解释为什么需要 Specification by Example：软件失败的核心问题常常不是技术不足，而是业务、文档、开发理解和最终实现之间持续失真。SbE 通过具体例子建立共同语言，把模糊、不可验证、不可执行的需求变成可讨论、可判断、可自动化验证的行为规格。

## Source Digest

图像以“问题不在技术，在沟通方式”为中心，说明需求从业务想法到需求文档、开发理解、最终实现的每次传递都可能产生偏差。左侧引用 Standish Group 研究中的 31% 失败项目归因于“不清楚的需求”；右侧流程图则把偏差定位在需求递交链路，而不是单个开发环节。

中部把文档驱动开发的需求问题分成三类：模糊，用“大量、友好、方便”等词导致不同理解；不可验证，缺少客观验收标准，例如“保证数据准确性”无法判断误差范围和“准确”的含义；不可执行，文档本身无法被机器运行或自动化检查，例如通知相关人员仍依赖人工解释。下方订单取消例子对比传统描述与 SbE：传统文档容易漏掉“已支付订单不能取消”“超时未支付订单”等边界，导致线上投诉、返工和延期；SbE 用 Given/When/Then 示例表达“未支付可取消”和“已支付不可取消”，让需求清晰、可验证、可执行，并形成活文档。

## Key Claims

- explicit: 图中主张需求误解是软件失败的核心原因之一，技术和架构无法建立在错误需求之上。
- explicit: Standish Group 调研在图中被用来说明 31% 的项目因为“不清楚的需求”失败。
- explicit: 文档驱动开发的典型问题包括模糊、不可验证和不可执行。
- explicit: 订单取消示例中，传统描述容易让开发错误实现“已支付订单也可以取消”，并漏掉超时未支付等测试场景。
- explicit: SbE 用具体示例表达需求，可以让每个示例都能判断通过或失败，并可自动化为验收测试。
- inferred: SbE 的首要价值不是替换需求沟通，而是把沟通结果压缩成业务人员、开发和测试都能复核的行为样例。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/Specification by Example|Specification by Example]] — 可沉淀 SbE 解决需求误解、模糊需求和验收不可执行的问题背景。
- compiled-concept candidate: [[concepts/可执行规格|可执行规格]] — 可补充从自然语言文档到 Given/When/Then 验收示例的转换价值。
- map-entry candidate: [[maps/软件工程基础学习地图|软件工程基础学习地图]] — 可作为需求沟通与验收测试主题的入口。

## Maintenance Notes

- 图片主要文字清晰；小号示意图文字已按可见内容概括，精确引用时应回看 raw。
- Standish Group 的 31% 数据未联网核验来源和上下文。
- 未修改 `index.md`、`log.md` 或编译页；本批 worker 只记录 compile 候选关系。
