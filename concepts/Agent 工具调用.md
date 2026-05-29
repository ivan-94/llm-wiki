---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# Agent 工具调用

## Definition

Agent 工具调用是把外部能力包装成模型可理解、可选择、可执行、可评估的接口，并通过工具描述、参数、返回结构和错误反馈影响 Agent 行为的工程实践。

## Why It Matters

工具是 Agent 从“说”走向“做”的接口。工具设计不只是 API 封装，而是 agent-facing interface 设计：名称、边界、上下文成本、返回字段和错误语义都会改变模型的决策。

## Mental Model

工具像 Agent 的手和传感器；设计目标不是暴露所有能力，而是让 Agent 低歧义、低 token 成本、可验证地完成任务。

## Key Claims

- 工具越多不一定越好；功能重叠和接口过细会增加选择噪声。
- 面向 Agent 的工具可以把常串联的多步任务封装为单次调用，降低循环成本。
- 工具返回应提供高价值上下文，避免让模型处理低层技术标识符。
- 工具评估要看准确性、运行时间、调用次数、token 消耗、工具错误和 agent 推理反馈。
- MCP、ACI、CLI 和 programmatic tool calling 是不同层级的工具接入形式。

## Examples

- `工具调用.xmind` 总结工具原型、评估任务、命名空间、返回结构和 token 效率。
- `MCP.xmind` 把 Resources、Tools、Prompts、Sampling 作为协议层能力。
- `Build CLI For Agent.xmind` 和 `build-cli-for-agent-checklist.md` 把 CLI 视为 Agent 可调用协议。
- `Agent 解构.xmind` 讨论工具 handler、MCP、Skills 和 ACI 的演进。

## Common Confusions

- 普通 API 设计关注人类/程序员调用，Agent 工具设计还要关注模型能否选对、用对、继续行动。
- MCP 不是单个工具，而是给工具、资源和提示模板提供标准化接入协议。
- 工具调用成功不代表任务完成；还需要验证工具结果是否满足语义目标。

## Evidence

- [[sources/Agent/工具调用.xmind|工具调用.xmind]]
- [[sources/Agent/MCP.xmind|MCP.xmind]]
- [[sources/Agent/Build CLI For Agent.xmind|Build CLI For Agent.xmind]]
- [[sources/Agent/build-cli-for-agent-checklist|build-cli-for-agent-checklist]]
- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]

## Relations

- part-of: [[concepts/AI Agent|AI Agent]]
- part-of: [[concepts/Agent Harness|Agent Harness]]
- implemented-by: [[entities/Model Context Protocol|Model Context Protocol]]
- related-source: [[sources/Agent/工具调用.xmind|工具调用.xmind]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：工具调用的质量取决于接口是否面向 Agent 的注意力、反馈和验证来设计，而不是功能是否最多。

## Review Questions

- 为什么更多工具可能降低 Agent 表现？
- 工具返回结构为什么会影响后续推理？
- MCP 与普通 tool calling 的抽象层级差异是什么？

## Open Questions

- 不同模型对工具数量、命名空间和长描述的敏感度需要实验比较。
