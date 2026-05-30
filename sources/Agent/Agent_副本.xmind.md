---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/Agent_副本.xmind"
source_relpath: "Agent/Agent_副本.xmind"
raw_created_at: 2024-05-04T03:27:38.105144+00:00
raw_modified_at: 2024-05-04T06:54:54.459102+00:00
raw_size: 3013064
raw_fingerprint: "size=3013064;birth=2024-05-04T03:27:38.105144+00:00;mtime=2024-05-04T06:54:54.459102+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.835883+00:00
ingested_at: 2026-05-30
status: ingested
---

# Agent_副本.xmind

## Source

- Raw file: [Agent/Agent_副本.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/Agent_%E5%89%AF%E6%9C%AC.xmind>)
- Raw ref: `raw:Agent/Agent_副本.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-04T03:27:38.105144+00:00`; modified `2024-05-04T06:54:54.459102+00:00`; size `3013064`; snapshot `2026-05-29T22:03:22.835883+00:00`
- Coverage: exported and digested 1 sheet: `思维导图`.

## Summary

这是一份早期 Agent 设计模式笔记，关注 Agent 的迭代式、由概览到细化、由分散到聚集的特点，并用 Robust 与 Emerging 两类模式组织 Reflection、Tool Use、Planning 和 Multi-agent Collaboration。它还把编码场景作为基准测试方向，并链接了吴恩达关于 AI Agent 工作流未来展望的视频。

## Source Digest

这份 source 的结构像一份未完成的学习草稿，但保留了早期 Agent workflow 的设计模式分组。Robust 类模式包括反思和工具调用：反思可以是同一个 LLM 先产出草稿再自我批判，也可以引入另一个 Agent 做审查，类比代码审查；工具调用则被视为 GPT、Claude 等模型接入外部能力的更可靠机制。

Emerging 类模式包括计划和多 Agent 协作：计划把任务拆成步骤执行，拆解者可以是人，也可以是 Agent；多 Agent 协作则把现实世界的多人协作类比到多个 Agent 共同完成任务。source 虽然没有展开具体架构，但它与后续 `Agent 解构.xmind` 中的 Orchestrator-Workers、多 Agent 任务图和交叉验证可以形成时间上的概念延展。

## Key Claims

- explicit: raw 将 Agent 特点概括为由概览到细化、迭代、由分散到聚集。
- explicit: Robust 设计模式包括 Reflection 和 Tool Use。
- explicit: Reflection 可以是 LLM 对自己草稿进行反思，也可以由另一个 Agent 执行审查，类似 code review。
- explicit: Emerging 设计模式包括 Planning 和 Multi-agent Collaboration。
- explicit: Planning 是把任务拆解成多个步骤执行，拆解可以由人工或 Agent 完成。
- inferred: 这份 source 是早期模式清单，适合补充 Agent 设计模式谱系，但不能单独定义完整 Agent 架构。

## External Links

- extended-reading: [吴恩达：AI 智能体工作流的未来展望](https://www.bilibili.com/video/BV1c1421U7yq/?vd_source=fac2c08a95e50313c2e8d2d59b079b6b) - source 中列为扩展阅读；not verified.

## Links

- related: [[concepts/Agentic Engineering|Agentic Engineering]] - source 提供反思、工具调用、计划、多 Agent 协作等 Agent workflow 模式候选。
- related: [[concepts/Agent Harness|Agent Harness]] - Reflection 与另一个 Agent 审查可作为质量反馈机制的早期形态。
- related: [[entities/Claude Code|Claude Code]] - raw 提到 Claude 支持工具调用，但没有展开 Claude Code 细节。

## Maintenance Notes

- Workbook includes placeholder branches `分支主题 3`, `分支主题 4`, and an empty node under `架构`.
- Reflection examples are named `示例1` and `示例 2` but contain no concrete details in the export.

- Link cleanup candidate: entity-candidate: AutoGPT - raw 将 AutoGPT 作为自动拆解任务步骤的例子，但没有足够上下文创建实体页。.
- Link cleanup candidate: entity-candidate: ChatDev - raw 将 chat dev 作为多 Agent 协作例子，但内容稀疏。.
