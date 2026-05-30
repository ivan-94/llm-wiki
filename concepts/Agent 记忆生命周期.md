---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 2
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# Agent 记忆生命周期

## Definition

Agent 记忆生命周期指一条记忆从被抽取、写入、检索、压缩，到演化、冲突解决和衰减遗忘的全过程治理；它关注的不是「存什么」，而是「什么值得进入未来上下文，以及如何避免过时信息伤害未来判断」。

## Why It Matters

长期 Agent 的失败大多不是「没存」，而是「存了乱」：过时事实污染回答、重复信息撑爆上下文、矛盾记忆让模型摇摆。把记忆当作有生命周期的资产治理，是长期 Agent 可靠的关键，也是 [[concepts/Agent 记忆|Agent 记忆]] 中最难、最容易被低估的部分。

## Mental Model

记忆像生鲜库存：进货要挑（抽取），上架要分类（存储），取用要新鲜（检索+衰减），临期要打包（压缩），冲货要对账（冲突解决），过期要下架（遗忘）。只进不管，库房就烂。

## Key Claims

- `记忆.xmind` 把记忆系统难点归纳为四组治理问题：压缩、演化、冲突解决、衰减。
- 压缩不是普通摘要，而是决定抽象层级、触发时机和信息保真——压错层级会丢关键细节或保留噪声。
- 演化要求 append、replace、delete 和多版本时间语义，让记忆能被更新而不是只能堆叠。
- 冲突解决需要优先级规则：时间、置信度、来源，以及用户直接陈述优先。
- 衰减要主动减少检索污染和记忆爆炸，例如 LanceDB Pro 的 Weibull 生命周期衰减。
- `会话存储与会话压缩.xmind` 给出一种压缩落地：用 Git「工作区/暂存区/仓库」类比分层持久化，压缩时只提交 Summary Area、保护头尾、避免重复提交（详见 [[concepts/会话分层存储与压缩|会话分层存储与压缩]]）。

## Examples

- Graphiti 用时序事实、事件溯源管理记忆演化和冲突。
- 触发时机：上下文接近上限时触发 Pre-Compaction，把重要信息先写入长期记忆再压缩旧上下文（OpenClaw / 闪极）。
- 写入时机：对话被移出上下文时触发压缩写入，或用户显式请求「记一下」（`闪极记忆.xmind` 记录员场景）。

## Common Confusions

- 压缩 ≠ 摘要：摘要是手段之一，压缩还要决定抽象层级与触发时机。
- 记忆越多 ≠ 越聪明：召回污染会让 Agent 更不稳定。
- 「存进向量库」只是存储动作，不构成生命周期治理；没有演化和衰减，向量库会越用越脏。

## Evidence

- [[sources/Agent/记忆.xmind|记忆.xmind]]
- [[sources/Agent/闪极智能体/会话存储与会话压缩.xmind|会话存储与会话压缩]]

## Relations

- part-of: [[concepts/Agent 记忆|Agent 记忆]]
- prerequisite: [[concepts/Agent 记忆|Agent 记忆]]
- contains: [[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- related: [[concepts/上下文工程|上下文工程]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: Graphiti
- entity-candidate: LanceDB Pro

## My Understanding

当前理解：记忆系统好不好，看的是它对「演化、冲突、衰减、压缩」这四件麻烦事有没有显式策略；只解决「写入和检索」的记忆系统会随时间退化。

## Review Questions

- 记忆生命周期治理的四组难点是什么？
- 为什么压缩不能等同于摘要？
- 冲突解决一般按哪些维度排优先级？

## Open Questions

- 衰减曲线和冲突优先级的最佳参数需要真实长期 Agent 数据验证。
