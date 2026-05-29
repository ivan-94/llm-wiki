---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/sharge/ai_glass.xmind"
source_relpath: "sharge/ai_glass.xmind"
raw_created_at: 2025-05-06T07:58:58+00:00
raw_modified_at: 2025-05-06T10:37:33+00:00
raw_size: 225094
raw_fingerprint: "size=225094;birth=2025-05-06T07:58:58+00:00;mtime=2025-05-06T10:37:33+00:00"
raw_snapshot_at: 2026-05-29T22:18:10.987536+00:00
ingested_at: 2026-05-30
status: ingested
---

# ai_glass.xmind

## Source

- Raw file: [sharge/ai_glass.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/sharge/ai_glass.xmind>)
- Raw ref: `raw:sharge/ai_glass.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-05-06T07:58:58+00:00`; modified `2025-05-06T10:37:33+00:00`; size `225094`; snapshot `2026-05-29T22:18:10.987536+00:00`
- Coverage: sheet-aware export completed for 1 sheet: `ai_glass`; all exported branches were read and digested.

## Summary

这份脑图记录 `ai_glass` 的几个系统思路：`gpt_stream` 流程中的意图路由、专家匹配、模型规模分发、音频流，以及“记忆管家”的快速回忆和检索分析。它是项目架构草图，包含若干占位分支。

## Source Digest

`gpt_stream` 流程下的 `handover sys1?` 分支描述了多种路由：`sys1_command` 判断用户意图、识别 AI 眼镜设备操作，并根据问题难度分发不同规模的模型；`match_expert_name` 根据用户输入路由到具体智能体；`match_expert_expertise` 则结合用户输入和历史，匹配擅长完成当前任务的智能体。`ExpertClient` 被设定为每个智能体的父类，说明系统以专家/智能体客户端为扩展单元。

“记忆管家”分支强调两条路径：一是利用最近聊天记录做快速回忆，快速判断是否满足用户要求；二是做查询分析，包括先分析需要查询的时间范围、暴力检索该时段聊天记录，再生成查询关键词，用向量检索找相关内容。这体现了一个混合检索思路：时间范围过滤、关键词生成和向量检索共同服务于个人记忆查询。

脑图还列出音频流和录音专家，但没有展开。整体更像 `ai_glass` 早期架构备忘，适合后续和真实代码实现互相校验。

## Key Claims

- explicit: `sys1_command` 用于判断用户意图、设备操作和问题难度，并按难度分发不同规模模型。
- explicit: `match_expert_name` 根据用户输入路由具体智能体。
- explicit: `match_expert_expertise` 根据用户输入和历史匹配擅长任务的智能体。
- explicit: 每个智能体都是 `ExpertClient` 的子类。
- explicit: 记忆管家结合最近聊天快速判断、时间范围分析、聊天记录检索、关键词生成和向量检索。
- inferred: 该架构把 AI 眼镜交互拆成设备命令、专家路由、音频流和个人记忆检索四类能力。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/上下文工程|上下文工程]] — 记忆管家和专家路由涉及历史上下文筛选与检索。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] — 专家客户端和路由可作为 agent 系统架构案例。

## Maintenance Notes

- `handover sys1?` 标题带问号，可能表示未定架构命名。
- `分支主题 3`、`分支主题 4`、`录音专家`、`音频流` 分支未展开。
- Compile candidate: ai_glass 可作为 project/entity-candidate；sys1_command、记忆管家、ExpertClient 可作为后续项目架构术语候选。
