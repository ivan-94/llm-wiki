---
page_type: map
updated_at: 2026-06-05
status: active
scope: Agent
---

# Agent 学习地图

## Purpose

以 `Agent 解构` 为枢纽，组织 AI Agent 的系统化学习路径：从 Agent Loop、控制模式、工具/MCP/CLI、记忆、沙箱，到多 Agent 协作、运行时变体对比和闪极智能体产品化专题。

## Entry Points

- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]：Agent 系统总枢纽（Loop、控制模式、harness、上下文、多 Agent、记忆、工具演进）。
- [[sources/Agent/Agent.xmind|Agent.xmind]]：认知架构与 Agent/Model 边界入门。
- [[sources/Agent/智能体工程的 8 个等级.xmind|智能体工程的 8 个等级]]：工程成熟度路径（含复合工程）。
- [[sources/Agent/工具调用.xmind|工具调用.xmind]]：工具设计与评估入口。
- [[sources/Agent/记忆.xmind|记忆.xmind]]：记忆系统与 14 方案入口。
- [[sources/Agent/沙箱.xmind|沙箱.xmind]]：执行隔离入口。
- [[sources/Agent/多智能体.xmind|多智能体.xmind]]：多 Agent 协作入口。

## Learning Path

1. 读 [[concepts/AI Agent|AI Agent]]，建立 Agent Loop、认知架构和系统边界。
2. 读 [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]] 与 [[concepts/Agent 控制模式|Agent 控制模式]]，理解控制权谱系。
3. 读 [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]，把各层串成系统视角。
4. 读 [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]]，把入口、harness、结构证据、eval gate 和 skill 演进连成操作闭环。
5. 读 [[concepts/Agent Harness|Agent Harness]]，连接工具、上下文、反馈和验证。
6. 读 [[concepts/Agent 工具调用|Agent 工具调用]]、[[concepts/Agent-friendly CLI（ACI）|Agent-friendly CLI（ACI）]] 和 [[entities/Model Context Protocol|Model Context Protocol]]，理解工具接入与选型。
7. 读 [[concepts/Agent 记忆|Agent 记忆]]、[[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]、[[concepts/会话分层存储与压缩|会话分层存储与压缩]] 和 [[concepts/多渠道记忆协议|多渠道记忆协议]]，理解跨 session 状态与治理。
8. 读 [[concepts/Agent 沙箱|Agent 沙箱]]，理解执行隔离与威胁模型差异。
9. 读 [[concepts/Agent Runtime|Agent Runtime]]、[[concepts/Agent MessageBus|Agent MessageBus]] 与 [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]]，理解运行时与变体分类。
10. 读 [[concepts/多 Agent 协作协议|多 Agent 协作协议]] 与 [[concepts/子代理委派模式|子代理委派模式]]，理解协作与委派。
11. 读 [[concepts/复合工程（Compound Engineering）|复合工程（Compound Engineering）]]，理解经验沉淀的复利。

## 变体对比分支

- 总线型 / 最小架构：[[entities/Nano Bot|Nano Bot]]
- 学习型 / 长期运行：[[entities/Hermes|Hermes]]
- 本地优先 / 极简工具面：[[entities/OpenClaw|OpenClaw]]
- 低代码平台：[[entities/Coze|Coze]]
- 多 Agent 团队运行时：[[entities/ClawTeam|ClawTeam]] vs [[entities/oh-my-claude-code|oh-my-claude-code]]
- 对比依据：[[concepts/Agent Runtime|Agent Runtime]] 的变体分类轴与 [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] 的运行时变体对比表。

## 闪极智能体专题分支

- 产品实体：[[entities/闪极智能体|闪极智能体]]（含 sharge `ai_glass` 同产品线）
- 运行时与消息：[[concepts/Agent MessageBus|Agent MessageBus]]
- 会话治理：[[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- 多渠道记忆：[[concepts/多渠道记忆协议|多渠道记忆协议]]（Loomos Memory）
- 执行隔离：[[concepts/Agent 沙箱|Agent 沙箱]]（nsjail MVP）
- 源：闪极智能体 / 里程碑与计划 / excalidraw / 会话存储与压缩 / 闪极记忆 / 沙箱PRD / ai_glass。

## Core Concepts

- [[concepts/AI Agent|AI Agent]]
- [[concepts/Agent 控制模式|Agent 控制模式]]
- [[concepts/Workflow 与 Agent 的边界|Workflow 与 Agent 的边界]]
- [[concepts/Agentic Engineering|Agentic Engineering]]
- [[concepts/Agent Harness|Agent Harness]]
- [[concepts/Agent Skills|Agent Skills]]
- [[concepts/Agent 工具调用|Agent 工具调用]]
- [[concepts/Agent-friendly CLI（ACI）|Agent-friendly CLI（ACI）]]
- [[concepts/Agent 记忆|Agent 记忆]]
- [[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]
- [[concepts/会话分层存储与压缩|会话分层存储与压缩]]
- [[concepts/多渠道记忆协议|多渠道记忆协议]]
- [[concepts/Agent 沙箱|Agent 沙箱]]
- [[concepts/Agent Runtime|Agent Runtime]]
- [[concepts/Agent MessageBus|Agent MessageBus]]
- [[concepts/低代码 Agent 平台 vs 代码优先 Runtime|低代码 Agent 平台 vs 代码优先 Runtime]]
- [[concepts/多 Agent 协作协议|多 Agent 协作协议]]
- [[concepts/子代理委派模式|子代理委派模式]]
- [[concepts/复合工程（Compound Engineering）|复合工程（Compound Engineering）]]

## Key Entities

- [[entities/Model Context Protocol|Model Context Protocol]]
- [[entities/LangChain|LangChain]]
- [[entities/Claude Code|Claude Code]]
- [[entities/Agent Client Protocol|Agent Client Protocol]]
- [[entities/闪极智能体|闪极智能体]]
- [[entities/Nano Bot|Nano Bot]]
- [[entities/Hermes|Hermes]]
- [[entities/OpenClaw|OpenClaw]]
- [[entities/Coze|Coze]]
- [[entities/ClawTeam|ClawTeam]]
- [[entities/oh-my-claude-code|oh-my-claude-code]]

## Synthesis To Read

- [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]
- [[synthesis/Agent 工作流可进化闭环|Agent 工作流可进化闭环]]
- [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]

## Review Queue

- 2026-06-06: [[concepts/AI Agent|AI Agent]]
- 2026-06-06: [[concepts/Agent 控制模式|Agent 控制模式]]
- 2026-06-06: [[concepts/Agent 工具调用|Agent 工具调用]]
- 2026-06-06: [[concepts/Agent 记忆|Agent 记忆]]
- 2026-06-06: [[concepts/Agent 记忆生命周期|Agent 记忆生命周期]]
- 2026-06-06: [[concepts/Agent 沙箱|Agent 沙箱]]
- 2026-06-06: [[concepts/Agent Runtime|Agent Runtime]]
- 2026-06-06: [[concepts/多 Agent 协作协议|多 Agent 协作协议]]
- 2026-06-06: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]

## Open Gaps

- mem0、Letta、Graphiti、MemOS、OpenViking、OpenSandbox、DeepAgents、Langflow、Dify 等仍为 entity-candidate，未建独立页。
- `智能体工程的 8 个等级`、`闪极智能体.xmind`、`claude skill.pdf` 为 partial/预览源，复合工程、运行时对比、Claude Skills 细节待补足证据。
- 多 Agent 自主协作的收益/成本缺少量化对比。
