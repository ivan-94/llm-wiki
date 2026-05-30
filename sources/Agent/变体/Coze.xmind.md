---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/变体/Coze.xmind"
source_relpath: "Agent/变体/Coze.xmind"
raw_created_at: 2024-08-21T06:38:00.036289+00:00
raw_modified_at: 2024-08-21T09:27:39.601965+00:00
raw_size: 1047728
raw_fingerprint: "size=1047728;birth=2024-08-21T06:38:00.036289+00:00;mtime=2024-08-21T09:27:39.601965+00:00"
raw_snapshot_at: 2026-05-29T22:03:27.893698+00:00
ingested_at: 2026-05-30
status: ingested
---

# Coze.xmind

## Source

- Raw file: [Agent/变体/Coze.xmind](finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/%E5%8F%98%E4%BD%93/Coze.xmind)
- Raw ref: `raw:Agent/变体/Coze.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-08-21T06:38:00.036289+00:00`; modified `2024-08-21T09:27:39.601965+00:00`; size `1047728`; snapshot `2026-05-29T22:03:27.893698+00:00`
- Coverage: exported and read 1 sheet: `画布 1`.

## Summary

这份思维导图把 Coze 作为低代码 Bot 平台来拆解，重点覆盖知识库、卡片、工具、记忆、Bot 编排模式和 API 能力。它的核心价值是帮助比较「低代码 Agent 平台」和「代码优先 Agent 框架」的边界：Coze 适合快速组合 RAG、工作流、多 Agent 分发和渠道交互，但灵活性与全局状态控制弱于代码框架。

## Source Digest

Coze 的平台模型围绕 Bot 展开。Bot 可以以单 Agent、多 Agent 或工作流形式提供服务：单 Agent 更接近一次带工具和上下文的 LLM 调用，多 Agent 用不同提示词拆解复杂任务并动态分发，工作流则把流程编排直接作为 Bot 的主体。工具层包含插件、工作流和图像流，其中插件可以通过自定义 Node.js 或 Python 代码扩展外部能力，工作流则是更面向小白的流程化插件，支持循环和并发，但导图明确指出它不如代码灵活，且全局变量设置能力不足。

记忆能力被分成长期记忆、数据库、变量和文件盒子。长期记忆会自动总结对话并在后续查询时召回；数据库用于动态数据表和复杂长期存储；变量是用户开启 Bot 时设置的上下文；文件盒子则提供非临时的多模态文件存储、管理和交互。知识库支持 RAG，类型覆盖较丰富，但 PDF 还原精度仍是限制。卡片是自定义消息展示形式，需要客户端支持，当前导图提到豆包和飞书支持，并可通过低代码方式创建和绑定变量。

API 部分更像平台边界清单，包含知识库创建、Bot 信息获取、会话/消息管理、文件上传和工作流执行。整体上，Coze 被描绘为一个以低代码编排、渠道体验和托管能力为优势的 Agent 平台，而不是一个强调本地可控、代码可扩展、运行时可深度定制的 Agent 框架。

## Key Claims

- explicit: Coze 的 Bot 可以采用单 Agent、多 Agent、工作流三种编排模式。
- explicit: Coze 工作流支持循环和并发，但远没有代码灵活，且导图记录了全局变量无法设置的问题。
- explicit: Coze 长期记忆会总结对话信息，并在后续回复时召回这些总结以辅助生成。
- explicit: 文件盒子用于合规存储、管理和交互用户发给 Bot 的多模态文件，不只是临时对话附件。
- explicit: Coze 知识库支持 RAG，知识库类型较丰富，但 PDF 还原精准度仍不足。
- inferred: Coze 更适合低代码 Bot、RAG、工作流和渠道交付场景；需要高度自定义运行时、工具协议或状态控制时，应把它与代码优先框架区分评估。

## External Links

No external links found in extracted content.

## Links

- compiled-entity: [[entities/Coze|Coze]] — source 是 Coze 实体页的主要证据：Bot 编排、知识库、记忆、工作流和 API 能力。
- compiled-concept: [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]] — source 提供低代码平台一侧（快速编排、托管、灵活性受限）的核心证据。
- updates: [[concepts/Agent Runtime|Agent Runtime]] — 作为低代码平台取向补入 runtime 变体分类轴。
- updates: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] — 进入运行时变体对比表的低代码平台一行。

## Maintenance Notes

- XMind helper reported `ok: true`; no `sheets_error`.
- The source includes product capability notes but does not include current product verification; external URLs were not browsed.
- This batch intentionally did not update `index.md` or `log.md`.

- Link cleanup candidate: batch-boundary: No wiki concept, entity, synthesis, map, index, or log pages were created or updated for this batch, per task instruction.
- Link cleanup candidate: compile-candidate: Coze; 低代码 Agent 平台; RAG 知识库; Agent 工作流编排; Bot 多 Agent 分发.
