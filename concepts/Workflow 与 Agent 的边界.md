---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 3
difficulty: 3
review_after: 2026-06-06
---

# Workflow 与 Agent 的边界

## Definition

Workflow 与 Agent 的边界指的是用「控制权归属」区分两类系统：执行路径由代码预先写死的是 workflow，下一步由 LLM 在运行时动态决定的是 agent。

## Why It Matters

这条边界决定了成本曲线、可控性和可调试性。把它说清楚，才能回答工程上的核心问题：这个任务到底要不要 Agent Loop，还是一个确定性流程就够了。

## Mental Model

Workflow 是铺好的轨道，火车只能按轨道走；Agent 是给了地图和目的地的司机，自己选路。轨道更可控更便宜，司机更灵活但更贵也更可能开错。

## Key Claims

- `Agent 解构.xmind`：核心差异是控制权——代码预写路径属于 workflow，LLM 动态决定下一步属于 agent。
- `闪极智能体.xmind` 给出成本模型：低复杂度任务用 Workflow 或 one-shot 缓存更省；高复杂度任务里 Workflow 成本随复杂度快速膨胀，而 Agent Loop 更适合按推理步数线性扩展。
- `闪极记忆.xmind`：在记忆检索场景中，Workflow 适合固定流程、效率高但结果一般；Agent Loop 适合复杂查询、多轮检索、试错和按需加载资源。
- `LangChain.xmind`：LangGraph 这类运行时同时支持 workflow 编排（图、持久化、重放）和 agent 动态决策，二者不是非此即彼。

## Examples

- 固定「检索 → 拼 prompt → 生成」是 workflow；让模型自己决定检索几次、读哪些引用、是否换工具是 agent（见 [[concepts/多渠道记忆协议|多渠道记忆协议]]）。
- 闪极智能体对简单问答走缓存/workflow，对跨能力编排走 Agent Loop，是按成本和复杂度分流的混合架构。

## Common Confusions

- 边界不是产品标签，而是控制权位置；同一个系统不同环节可以分别是 workflow 和 agent。
- 「用了 LLM」不等于「是 agent」；只要路径写死，它仍是 workflow。
- Agent 更灵活不等于更优；在可枚举的确定流程上，workflow 更便宜更可验证。

## Evidence

- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]
- [[sources/Agent/LangChain.xmind|LangChain.xmind]]
- [[sources/Agent/闪极智能体/闪极智能体.xmind|闪极智能体.xmind]]
- [[sources/Agent/闪极智能体/闪极记忆.xmind|闪极记忆.xmind]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- contrasts-with: [[concepts/Agent 控制模式|Agent 控制模式]]
- related: [[concepts/Agentic Engineering|Agentic Engineering]]
- implemented-by: [[entities/LangChain|LangChain]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：判断一个环节是 workflow 还是 agent，只要问「下一步是谁定的」——代码定就是 workflow，模型定就是 agent；成本和复杂度决定该用哪个。

## Review Questions

- 区分 workflow 与 agent 的唯一判据是什么？
- 为什么高复杂度任务里 Agent Loop 的成本扩展优于 Workflow？
- 为什么真实系统常常是 workflow 与 agent 的混合？

## Open Questions

- 复杂度到多高时应该从 workflow 切换到 Agent Loop，缺少可操作的量化阈值。
