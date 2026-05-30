---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/AI  编排引擎调研.xmind"
source_relpath: "Agent/AI  编排引擎调研.xmind"
raw_created_at: 2024-05-21T01:18:40.022951+00:00
raw_modified_at: 2024-05-27T03:18:48.447711+00:00
raw_size: 183208
raw_fingerprint: "size=183208;birth=2024-05-21T01:18:40.022951+00:00;mtime=2024-05-27T03:18:48.447711+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.709669+00:00
ingested_at: 2026-05-30
status: ingested
---

# AI  编排引擎调研.xmind

## Source

- Raw file: [Agent/AI  编排引擎调研.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/AI%20%20%E7%BC%96%E6%8E%92%E5%BC%95%E6%93%8E%E8%B0%83%E7%A0%94.xmind>)
- Raw ref: `raw:Agent/AI  编排引擎调研.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-21T01:18:40.022951+00:00`; modified `2024-05-27T03:18:48.447711+00:00`; size `183208`; snapshot `2026-05-29T22:03:22.709669+00:00`
- Coverage: exported and digested 1 sheet: `思维导图`.

## Summary

这是一张早期 AI workflow / 编排引擎调研图，主要把 Langflow 放在中心，并把 FastGPT、Dify、FlowiseAI、RAGFlow、LangGraph、Coze 等 AI 编排或应用构建产品，与 n8n、Zapier 这类非 AI 自动化产品并列为参照对象。

## Source Digest

这份 source 的价值不是方法论细节，而是保留了一个产品调研入口：作者把 AI 编排引擎看作 workflow 工具谱系的一部分，既关注面向 LLM/RAG/Agent 的产品，也把传统自动化平台纳入比较。它暗示后续 compile 时可以从两个维度展开：一是 AI 原生编排工具如何承接模型、知识库、工具和流程；二是它们与 n8n、Zapier 这类通用自动化产品的边界差异。

内容目前明显偏占位：`Langflow`、`相关产品` 和两个未命名分支构成主体，没有记录具体评估维度、选型结论、架构比较或使用案例。因此它更适合作为编排工具候选清单，而不是独立支撑产品评测结论。

## Key Claims

- explicit: raw 把 `Langflow` 作为 `AI Workflow` 下的一级主题，说明 Langflow 是本次 AI 编排引擎调研的核心参照之一。
- explicit: raw 将 FastGPT、Dify、Langflow、Coze、FlowiseAI、RAGFlow、LangGraph 归入 `相关产品`，将 n8n、Zapier 归入 `类似的非 AI 产品`。
- inferred: 这份清单支持后续建立“AI 编排工具 vs 通用自动化工具”的比较页，但当前 raw 不足以判断各产品优劣。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]] - source 提供 AI 原生编排（FastGPT/Dify/Langflow/Coze/FlowiseAI/RAGFlow/LangGraph）与通用自动化（n8n/Zapier）并列的产品谱系证据。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] - 编排引擎产品清单可作为 Agentic 工程工具层的后续补充证据。
- related: [[concepts/Agent Harness|Agent Harness]] - workflow 产品可能服务于工具编排、流程约束和执行验证，但本 source 尚未展开 harness 细节。

## Maintenance Notes

- Workbook contains sparse placeholder branches `分支主题 2` and `分支主题 4`.
- No evaluation criteria, screenshots, product notes, or conclusions were present in the exported sheet.

- Link cleanup candidate: entity-candidate: Langflow - raw 中被置于核心位置，但当前没有足够信息创建实体页。.
- Link cleanup candidate: entity-candidate: FastGPT, Dify, Coze, FlowiseAI, RAGFlow, LangGraph, n8n, Zapier - raw 仅提供候选产品清单，待更多来源补足角色和比较维度。.
