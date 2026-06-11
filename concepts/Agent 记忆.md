---
page_type: concept
updated_at: 2026-06-11
status: active
source_count: 6
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

- 记忆系统可分为存储层、处理层、检索层和控制层；控制层负责生命周期、冲突解决、资源预算和安全治理。
- 记忆类型可按用途分为 semantic、episodic、procedural，也可按时间分为短期和长期。
- 短期记忆应包含 thread/session 状态、工具结果、TODO、checkpoint 和 resume 信息，而不只是聊天记录。
- 长期记忆需要压缩、筛选、更新、冲突解决和衰减，否则会污染上下文（生命周期治理详见 [[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]）。
- 文件系统、向量库、图数据库、Markdown、JSONL 和混合检索分别适合不同记忆路线；混合检索常组合向量+BM25，并用 RRF 融合、Rerank 重排。
- 跨方案共通机制：混合检索、RRF/MMR/重排、衰减和分层摘要。
- ChatGPT Dreaming source 补充：长期记忆的核心风险是过期后仍被信任；好的 memory state 需要 freshness、continuity、relevance、可审阅摘要和用户修订入口。

### 14 方案比较（来自 `记忆.xmind`，按取向归四类）

| 取向 | 方案 | 要点 |
| --- | --- | --- |
| 状态管理优先 | Letta | 常驻上下文的白盒记忆块 |
| 状态管理优先 | ChatGPT Memory | 产品级会话/摘要记忆 |
| 结构化知识优先 | Graphiti | 时序图、事件溯源、预设/习得本体、增量图构建 |
| 结构化知识优先 | mem0 | 同时处理向量记忆、程序性记忆和图记忆 |
| 结构化知识优先 | LanceDB Pro | LLM 驱动六类抽取、向量+BM25 混合、重排、Weibull 衰减 |
| 学习闭环优先 | Hindsight | retain/recall/reflect 学习闭环 |
| 学习闭环优先 | MemOS | 长期知识、工具轨迹、任务总结、技能进化统一为记忆 OS |
| 学习闭环优先 | Hermes | 从经验创造技能、会话血缘、记忆 provider 插件 |
| 人机协作优先 | QMD | 本地 Markdown 检索引擎 |
| 人机协作优先 | OpenViking | `viking://` 虚拟文件系统、L0/L1/L2 分层、目录递归检索 |
| 人机协作优先 | memU | 类文件系统/层级目录的常驻代理记忆 |
| 人机协作优先 | Claude Code | 文件系统纯文本（CLAUDE.md、skills、自动记忆目录） |

（DeerFlow 作为 mem0 相关案例、Hermes 单列为 runtime 学习型方案；以上为 `记忆.xmind` 14 个 sheet 的归类提炼，具体实现回 raw 核验。）

### Loomos / 会话分层

- 闪极 Loomos Memory 把记忆扩展为多渠道检索协议（search/readMore/installTools），详见 [[concepts/多渠道记忆协议|多渠道记忆协议]]。
- 会话历史本身用分层存储（messages/messages_staged + 保护头尾）管理压缩与恢复，详见 [[concepts/会话分层存储与压缩|会话分层存储与压缩]]。

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
- [[human/sources/inbox/cook-tweet/2026-06-05_ChatGPT记忆DreamingV3_OpenAI|ChatGPT 记忆进入 Dreaming V3]] — human source，补充 memory freshness、staleness、reviewable summary 和后台合成 memory state。

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- part-of: [[concepts/Agent Harness|Agent Harness]]
- contains: [[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]
- contains: [[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- contains: [[concepts/多渠道记忆协议|多渠道记忆协议]]
- contrasts-with: [[concepts/RAG|RAG]]
- related-source: [[sources/Agent/记忆.xmind|记忆.xmind]]
- related: [[entities/GPT 与 ChatGPT|GPT 与 ChatGPT]] — ChatGPT memory / Dreaming V3 是产品级记忆系统案例。
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: mem0
- entity-candidate: Letta
- entity-candidate: Graphiti
- entity-candidate: MemOS
- entity-candidate: OpenViking

## My Understanding

当前理解：Agent 记忆的关键问题不是“存下来”，而是“什么值得进入未来上下文，以及如何避免过时信息伤害未来判断”。

## Review Questions

- semantic、episodic、procedural memory 分别保存什么？
- 记忆压缩、演化和衰减解决什么问题？
- 文件系统记忆和图记忆各有什么优势？
- 14 方案的四类取向（状态/结构化/学习闭环/人机协作）各举一个代表？
- Loomos 多渠道记忆和会话分层存储分别解决什么？

## Open Questions

- 记忆衰减和冲突解决的最佳策略需要真实长期 Agent 数据验证。
