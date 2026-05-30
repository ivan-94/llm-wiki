---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 1
---

# GStack

## What It Is

GStack（由 Garry Tan 创建，GitHub: `garrytan/gstack`）是一个围绕 Claude Code 构建的 AI 软件工厂工具集：通过 slash commands、Markdown skills、浏览器/设计/测试工具和 JSONL 可观测性，把软件交付流程（计划、开发、审查、测试、发布、监控、复盘）封装成 Agent 可执行的质量门禁工作流。

## Role In This Wiki

GStack 是 `concepts/AI 软件工厂` 的最具体实现案例，也是 slash commands 作为 Agent 协作入口的代表性工具。它与 Matt Pocock Skills 和 Superpowers 构成 Claude Code 增强路线的三种不同风格。

## Key Facts

**核心 Slash Commands：**
- `/ship`：完整发布流程命令，集成计划评审、开发、测试、审查和部署。
- `/review`：多领域专家视角代码审查，集成领域、安全、架构等不同 reviewer。
- `/qa`：QA 验证流程，配合测试体系执行验收。
- `/autoplan`：从 CEO/设计/工程多视角自动生成计划评审。
- `/codex`：触发 Codex 模型对代码/产物做异构交叉验证（不同模型互审以提高置信度）。
- `/canary`：发布后的渐进式验证和线上 canary 监控。

**测试体系三层：**
1. 静态验证 + 生成质量检查（免费）
2. 端到端技能实际运行（付费）
3. LLM-as-judge 质量评估

**浏览器能力：** 基于 Playwright 的无头浏览器 CLI（`browse/`），用于 QA、设计评审、安全审计、性能监控和部署验证——让 Agent 真正"看"网页状态。

**杠杆模型：** 高质量 prompt 复用 + 交叉验证置信度 + 即时反馈速度 + 失败经验累积 = 压缩认知成本飞轮。

## Related Concepts

- implements: [[concepts/AI 软件工厂|AI 软件工厂]] — GStack 是 AI 软件工厂的标准实现案例。
- implemented-by: [[entities/Claude Code|Claude Code]] — GStack 围绕 Claude Code 构建，以 Claude Code 作为核心执行引擎。
- contrasts-with: [[entities/Matt Pocock|Matt Pocock]] — Matt Pocock 侧重 skill 可组合性和 GitHub 闭环，GStack 侧重质量门禁 slash commands 和工具集集成。
- contrasts-with: [[entities/Superpowers|Superpowers]] — Superpowers 通过 session-start hook 注入框架，GStack 通过命令套件封装流程。
- related: [[concepts/Agent Skills|Agent Skills]] — GStack 的 skills 是 AI 软件工厂中工程经验固化的具体产物。

## Evidence

- [[sources/Vibe/工具/AI 软件工厂 GStack.xmind|AI 软件工厂 GStack]] — 系统描述 GStack 的工作流、命令体系、工具层和杠杆模型。

## Open Questions

- GStack 仓库 `garrytan/gstack` 的当前状态、实际安装方式和 skill 完整列表未联网核验。
- 部分工具分类节点（设计与视觉、部署与运维、安全与质量、文档与复盘）在 XMind 中只有标题无展开，功能细节待后续补充。
