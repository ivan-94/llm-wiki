---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# 复合工程（Compound Engineering）

## Definition

复合工程是 Agent 工程成熟度路径中的一级：通过「计划、委派、评估、沉淀」的循环，把每次会话中学到的经验固化进规则文件，让改进在未来每一次会话中复利累积，而不是只改善当前这一次。

## Why It Matters

上下文工程改善的是「本次会话」，复合工程改善的是「未来每次会话」。如果每次都重新踩同样的坑、重新解释同样的约定，Agent 的边际收益是平的；复合工程让收益像复利一样累积，是从「一次性提效」走向「系统性提效」的关键拐点。

## Mental Model

复合工程像给团队写 wiki/runbook：单次任务做完不算完，要把「这次怎么做对的、踩了什么坑」写回规则文件，下次所有 Agent 都站在更高的起点上。

## Key Claims

- `智能体工程的 8 个等级.xmind` 把复合工程定位为第 4 级，核心循环是计划、委派、评估、沉淀。
- 关键动作是把经验教训写入 `CLAUDE.md` 或等效规则文件，使改进进入未来会话。
- 它位于上下文工程（第 3 级）之上、MCP/Skills（第 5 级）之下：先有上下文密度，再有经验沉淀，再有能力扩展。
- 更高阶段（后台 Agent、自主 Agent 团队）依赖复合工程提供的沉淀机制才能持续学习。

## Examples

- 一次 review 发现的反复出现的错误，被写进规则文件/skill，后续 Agent 自动规避。
- `闪极记忆.xmind` 的「记录员」、Hermes 的「从经验中创造技能」都是把经验沉淀为可复用资产的形态。

## Common Confusions

- 复合工程不是「写更多文档」，而是「写能改变 Agent 下一次行为的规则」。
- 它和上下文工程互补而非替代：一个管本次密度，一个管跨次沉淀。
- 沉淀的载体可以是规则文件、skill、test、hook 或 runtime 约束，不限于 `CLAUDE.md`。

## Evidence

- [[sources/Agent/智能体工程的 8 个等级.xmind|智能体工程的 8 个等级]]

## Relations

- part-of: [[concepts/Agentic Engineering|Agentic Engineering]]
- prerequisite: [[concepts/上下文工程|上下文工程]]
- related: [[concepts/Agent Skills|Agent Skills]]
- related: [[concepts/子代理委派模式|子代理委派模式]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: Kieran Klaassen

## My Understanding

当前理解：复合工程的一句话是「把这次学到的写回规则，让下次更省力」；它让 Agent 工程从线性提效变成复利提效。

## Review Questions

- 复合工程的循环四步是什么？
- 复合工程和上下文工程改善的对象有什么不同？
- 经验沉淀可以落在哪些载体上？

## Open Questions

- 该概念来自 partial source（`智能体工程的 8 个等级` 仅部分展开），「复合工程」的提出归因（Kieran Klaassen）和原始定义未联网核验。
