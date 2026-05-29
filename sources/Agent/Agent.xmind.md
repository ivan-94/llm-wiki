---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/Agent.xmind"
source_relpath: "Agent/Agent.xmind"
raw_created_at: 2025-01-14T10:43:19.051150+00:00
raw_modified_at: 2026-03-18T12:47:28.615195+00:00
raw_size: 472511
raw_fingerprint: "size=472511;birth=2025-01-14T10:43:19.051150+00:00;mtime=2026-03-18T12:47:28.615195+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.818013+00:00
ingested_at: 2026-05-30
status: ingested
---

# Agent.xmind

## Source

- Raw file: [Agent/Agent.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/Agent.xmind>)
- Raw ref: `raw:Agent/Agent.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-01-14T10:43:19.051150+00:00`; modified `2026-03-18T12:47:28.615195+00:00`; size `472511`; snapshot `2026-05-29T22:03:22.818013+00:00`
- Coverage: exported and digested 1 sheet: `画布 1`.

## Summary

这是一份 Agent 基础概念笔记，定义 Agent 是能观察环境、使用工具并为目标行动的生成式 AI 应用。它用认知架构拆分模型、工具和编排层，强调规划、执行、调整循环，并从知识范围、状态记忆、工具和逻辑层四个维度区分 Agent 与 Model。

## Source Digest

这份 source 适合作为“Agent 入门定义”的证据。它把 Agent 的关键能力概括为自治性、工具使用和目标驱动：给定目标后，Agent 能在模糊人类指令下推理下一步行动并推进目标。与纯 Model 相比，Agent 不只回答问题，而是有外部工具、有状态、有会话历史和原生逻辑层。

认知架构部分把 Agent 拆成模型、工具和编排层。模型是核心决策器，可按场景选择；工具扩展可行动能力；编排层负责接收信息、内部推理、指导下一步行动或决策，直到达成目标或触发停止条件。source 用 `Planning -> Executing -> Adjusting` 表达工作循环，并列出 ReAct、CoT、Chain of Tree 作为推理框架。

学习增强部分区分三条路线：上下文学习、基于检索的上下文学习和微调式学习。这说明 Agent 性能提升不只依赖模型替换，还可以通过上下文、RAG 和 fine-tuning 改善。整体内容较基础，但与 `Agent 解构.xmind` 可以互补：本 source 定义 Agent 的最小组成，后者展开工程化外围系统。

## Key Claims

- explicit: 生成式 AI Agent 可以被定义为通过观察周围世界并使用可用工具来实现目标的应用程序。
- explicit: Agent 具有自治性，给定合适目标后可以独立行动并处理模糊指令。
- explicit: Agent 的基础组件包括模型、工具和编排层。
- explicit: 编排层描述 Agent 如何接收信息、推理、指导下一步行动，并持续到目标达成或停止条件触发。
- explicit: Agent 与 Model 的差异包括知识范围、状态和记忆、原生工具、原生逻辑层。
- inferred: 这份 source 更适合支撑 Agent 概念定义和基础心智模型，不足以单独支撑复杂的多 Agent 或 harness 工程结论。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/Agentic Engineering|Agentic Engineering]] - source 提供 Agent 的基础定义、认知架构和 Agent/Model 边界。
- related: [[concepts/上下文工程|上下文工程]] - source 将上下文学习和检索增强上下文学习列为提升模型性能的路线。
- entity-candidate: Google Agent 白皮书 - raw 只列出扩展资料标题，没有 URL 或具体观点，待补充来源。

## Maintenance Notes

- `认知架构` 下有一个空白节点，`ReAct` 下也有空白节点。
- `Fine-turning based learning` 疑似拼写应为 `Fine-tuning based learning`，未修改 raw，仅记录为原文异常。
