---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 4
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-06
---

# 低代码 Agent 平台 vs 代码优先 Runtime

## Definition

这是一条 Agent 构建路线的选型轴：低代码 Agent 平台用可视化编排、托管知识库和渠道交付换取上手速度；代码优先 Runtime 用代码可控的循环、工具、记忆和运行时换取深度定制和全局状态控制。

## Why It Matters

很多团队在「用 Coze/Dify 拖一个」和「写一套 runtime」之间反复横跳。这条轴帮助先想清楚：你要的是快速交付一个 RAG/渠道 Bot，还是要可深度定制运行时、工具协议和状态控制的长期系统——选错会么早期被平台锁死，要么过度工程。

## Mental Model

低代码平台像「带模板的网站搭建器」：快，但能改的地方平台说了算。代码优先 Runtime 像「自己写后端」：慢，但每一层都能改。

## Key Claims

- `Coze.xmind`：低代码平台擅长快速组合 RAG、工作流、多 Agent 分发和渠道交互，但工作流不如代码灵活、全局变量控制弱、PDF 还原精度受限。
- `LangChain.xmind`：代码优先生态分层为应用抽象（LangChain）、执行运行时（LangGraph：图编排、持久化、重放、中断、human-in-the-loop）、成品 runtime（DeepAgents）。
- `AI 编排引擎调研.xmind` 把这一谱系并列：AI 原生编排（FastGPT、Dify、Langflow、Coze、FlowiseAI、RAGFlow、LangGraph）与通用自动化（n8n、Zapier）。
- 选型轴可归纳为：上手速度、定制深度、全局状态控制、托管与渠道、运行时可观测性、迁移与锁定风险。
- 真实产品常混合：闪极智能体用代码优先 runtime，但通过 OpenAI 兼容接口和 Skills 反向开放，兼顾控制与生态。

## Examples

- 想快速给客服接一个带知识库的 Bot 并发到飞书/豆包 → 低代码平台（Coze）更划算。
- 想自定义 Agent Loop、会话压缩、沙箱、模型路由和设备 Channel → 代码优先 Runtime（见 [[concepts/Agent Runtime|Agent Runtime]]，闪极智能体）。

## Common Confusions

- 低代码不等于「能力弱」，而是「可控点少」；它在标准场景反而更快更稳。
- 代码优先不等于「不用框架」；LangGraph/DeepAgents 仍是框架，只是控制权在代码侧。
- n8n/Zapier 这类通用自动化不是 Agent 平台，但常被并列比较，要区分「流程自动化」与「模型驱动决策」。

## Evidence

- [[sources/Agent/变体/Coze.xmind|Coze.xmind]]
- [[sources/Agent/LangChain.xmind|LangChain.xmind]]
- [[sources/Agent/AI  编排引擎调研.xmind|AI 编排引擎调研.xmind]]
- [[sources/Agent/闪极智能体/闪极智能体-里程碑与计划.xmind|闪极智能体-里程碑与计划]]

## Relations

- contrasts-with: [[concepts/Agent Runtime|Agent Runtime]]
- part-of: [[concepts/AI Agent|AI Agent]]
- implemented-by: [[entities/Coze|Coze]]
- implemented-by: [[entities/LangChain|LangChain]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: Dify
- entity-candidate: Langflow
- entity-candidate: FastGPT
- entity-candidate: DeepAgents

## My Understanding

当前理解：先问「我要交付一个标准 Bot，还是要长期可控的系统」；前者选低代码平台，后者选代码优先 Runtime，混合架构则用 runtime 内核 + 平台式开放。

## Review Questions

- 低代码平台和代码优先 Runtime 的核心权衡是什么？
- LangChain / LangGraph / DeepAgents 三层分别负责什么？
- 为什么 n8n/Zapier 要和 AI 编排工具区分？

## Open Questions

- 各低代码平台当前的能力边界和锁定风险未联网核验。
