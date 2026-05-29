---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: new
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# Agent 记忆

## Definition

Agent 记忆是让 Agent 在 session 内和跨 session 保留状态、事实、经历、程序性规则与学习结果的系统，通常包含抽取、存储、检索、压缩、演化、冲突解决和衰减。

## Why It Matters

长期 Agent 不能只靠聊天历史。没有记忆系统，Agent 会重复探索、丢失用户偏好、无法跨任务学习；记忆做坏了又会造成污染、过时事实、隐私风险和上下文噪声。

## Mental Model

记忆不是仓库，是供应链：从事件中抽取什么，如何存储，何时召回，如何压缩，何时替换或遗忘，决定了 Agent 的长期行为。

## Key Claims

- 记忆系统可分为存储层、处理层、检索层和控制层。
- 记忆类型可按用途分为 semantic、episodic、procedural，也可按时间分为短期和长期。
- 短期记忆应包含 thread/session 状态、工具结果、TODO、checkpoint 和 resume 信息，而不只是聊天记录。
- 长期记忆需要压缩、筛选、更新、冲突解决和衰减，否则会污染上下文。
- 文件系统、向量库、图数据库、Markdown、JSONL 和混合检索分别适合不同记忆路线。

## Examples

- `记忆.xmind` 比较 QMD、Letta、mem0、OpenViking、LanceDB Pro、Graphiti、MemOS、ChatGPT 和 Claude Code memory。
- `长记忆.xmind` 把短期记忆和长期记忆拆成事实、情景、语义和程序记忆。
- `会话存储与会话压缩.xmind` 讨论闪极智能体场景中的会话压缩与存储。
- `闪极记忆.xmind` 提供多渠道设备记忆协议材料。

## Common Confusions

- 向量库不是记忆系统本身，只是可能的存储/检索层。
- 摘要不是压缩的全部；压缩还涉及抽象层级、触发时机和信息保真。
- 记忆越多不一定越好，召回污染会让 Agent 更不稳定。

## Evidence

- [[sources/Agent/记忆.xmind|记忆.xmind]]
- [[sources/RAG/长记忆.xmind|长记忆.xmind]]
- [[sources/Agent/闪极智能体/会话存储与会话压缩.xmind|会话存储与会话压缩]]
- [[sources/Agent/闪极智能体/闪极记忆.xmind|闪极记忆]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- part-of: [[concepts/Agent Harness|Agent Harness]]
- contrasts-with: [[concepts/RAG|RAG]]
- related-source: [[sources/Agent/记忆.xmind|记忆.xmind]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：Agent 记忆的关键问题不是“存下来”，而是“什么值得进入未来上下文，以及如何避免过时信息伤害未来判断”。

## Review Questions

- semantic、episodic、procedural memory 分别保存什么？
- 记忆压缩、演化和衰减解决什么问题？
- 文件系统记忆和图记忆各有什么优势？

## Open Questions

- 记忆衰减和冲突解决的最佳策略需要真实长期 Agent 数据验证。
