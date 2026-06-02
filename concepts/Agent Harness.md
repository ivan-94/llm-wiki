---
page_type: concept
updated_at: 2026-06-01
status: active
source_count: 11
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-05
---

# Agent Harness

## Definition

Agent Harness 是围绕 Agent 的执行环境、上下文入口、权限、工具、反馈、验证和观测所构成的工程控制面。

## Why It Matters

Agent 能力越强，越需要 harness 把它限制在可理解、可恢复、可验证的轨道上。没有 harness，Vibe Coding 容易变成一次性生成和人工救火。

## Mental Model

Harness = empower + constrain：给 Agent 足够能力，同时给它边界、仪表盘和验收门。

**OS 类比**：Harness 之于 Agent 就像操作系统之于应用程序——进程调度（任务分配）、内存管理（上下文压缩）、文件系统（状态持久化）、权限（护栏）、系统调用（工具）、错误处理（失败恢复）。模型是 CPU，Harness 是 OS。

## Four Core Elements

Harness 的设计需要覆盖四个要素：
1. **验收基线（Acceptance Baseline）**：事先定义什么算"完成"（测试、HAT、review），而不是事后靠肉眼判断。
2. **执行边界（Execution Boundary）**：Agent 可以做什么、不能做什么（权限、hooks、危险命令禁止）。
3. **反馈信号（Feedback Signal）**：测试结果、lint 输出、HAT 证据、日志、生产异常等能让 Agent 或人类判断执行状态的信号。
4. **回退路径（Rollback Path）**：任务失败时如何回到安全状态（worktree 废弃、git reset、状态快照恢复）。

## Component Taxonomy

- context layer: AGENTS/CLAUDE、Source Manifest、docs、memory、retrieval、compaction 和 progressive disclosure。
- tool layer: shell、git、browser、MCP、test runner、linters、formatters、local servers 和 project scripts。
- state layer: 文件系统、worktree、logs、artifacts、issues、PR、HAT results 和 long-running task checkpoints。
- guardrail layer: permissions、hooks、禁止危险命令、schema checks、type checks、安全边界和 prompt injection 防护。
- feedback layer: unit/integration/e2e tests、Playwright/browser evidence、LLM evaluator、review agent、human HAT 和 production signals。
- learning layer: 把失败沉淀为新 skill、模板、规则、检查清单、ADR 或 lint。

## Harness Loop (Four Steps)

Harness 的持续改进循环：
1. **Collect（收集轨迹）**：收集 Agent 执行的日志、失败记录、测试报告、review 反馈和 HAT 结果。
2. **Identify（识别缺失约束）**：分析哪些失败来自上下文不足、工具缺失、权限不当或验收标准模糊。
3. **Optimize（选择控制点）**：把改进写入 AGENTS/CLAUDE 入口、新 skill、hook、linter、测试、runtime 约束或 checklist。
4. **Embed（写回系统）**：让改进自动生效，下次 Agent 执行不需要人工重新提醒。

**探索-执行 Handoff**：Harness 还需要管理探索阶段和执行阶段的交接，确保探索结论以结构化 handoff 文档传递，不让探索噪声污染执行上下文。详见 [[concepts/探索-执行上下文隔离|探索-执行上下文隔离]]。

**Selenium/验收层**：浏览器自动化测试（Selenium、Playwright）和 HAT 是 harness feedback layer 的高价值组件，能提供接近真实用户路径的验收证据，而不只是单元测试覆盖率。

## Ratcheting Loop

Harness 的核心循环是：观察失败 -> 定位缺失约束 -> 选择可执行控制点 -> 写回系统 -> 下次自动生效。比如 Agent 忽略架构边界时，不只是这次提醒它，而是补 AGENTS 入口、结构测试或 review checklist；Agent 误用危险命令时，不只是口头禁止，而是加 hook 或权限门。

## Key Claims

- Harness 的目标不是让 Agent 少做事，而是让 Agent 做事时更可控、更可观测、更容易复盘。
- Harness 循环包括收集轨迹、识别失败、优化上下文/工具/权限/测试，再把改进写回 workflow。
- Skills、AGENTS/CLAUDE、hooks、MCP、browser/test tools、worktree 和 HAT 都可以是 harness 组件。
- 浏览器兼容性测试和 HAT 证据让 Agent 不只通过单元测试，还能接近用户路径验收。
- 好的 harness 把 Agent 降级为更接近 `f(task_spec) -> result` 的执行器：任务输入清晰、状态外置、输出可验证、失败可回放。
- 工具越多不一定越强；工具范围、权限、安全边界和错误反馈共同决定 Agent 的实际可靠性。

## Examples

- `Harness = EMPOWER + CONSTRAIN` 将 harness 拆成赋能和约束两侧。
- `Harness 循环1/2` 用图示表达持续优化闭环。
- `浏览器兼容性测试.xmind` 将 Selenium、云测试和截图证据纳入 Agent 验收。
- `为 Agents 构造并发执行环境` 把隔离 worktree、运行时和 agent task 分派视为 harness。

## Common Confusions

- Harness 不是单个脚本或工具，而是一组环境、协议和反馈机制。
- 增加工具不一定提高质量；工具需要配合权限、上下文和验收标准。

## Evidence

- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind|Agent Harness Engineering]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness = EMPOWER + CONSTRAIN.xmind|Harness = EMPOWER + CONSTRAIN]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环1.png|Harness 循环1]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/Harness 循环2.png|Harness 循环2]]
- [[sources/Vibe/Vibe Coding 随手记/Harness/浏览器兼容性测试.xmind|浏览器兼容性测试]]
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Vibe Coding 的 Sweet Spot：从粗生成到精修.xmind|Vibe Coding 的 Sweet Spot]]
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind|hat-prepare]] 和 [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind|hat-run]] — 补充 harness acceptance baseline 和 feedback layer 的 HAT 准备/执行证据。

## Relations

- enables: [[concepts/Vibe Coding|Vibe Coding]]
- enables: [[concepts/Agentic Engineering|Agentic Engineering]]
- includes: [[concepts/Agent Skills|Agent Skills]]
- contains: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — HAT 是 harness feedback layer 中接近用户路径的验收协议
- contains: [[concepts/探索-执行上下文隔离|探索-执行上下文隔离]] — 探索-执行 handoff 是 harness context layer 的核心策略
- contains: [[concepts/Agent 并发执行环境|Agent 并发执行环境]] — 并发执行环境是 harness state layer 的基础设施实现
- contains: [[concepts/Agent Coding Guardrails|Agent Coding Guardrails]] — guardrails 是 harness guardrail layer 的行为约束部分
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：Agent Harness 是把 Agent 的“能力”转成“可靠交付”的中间层。

## Review Questions

- Harness 为什么同时要 empower 和 constrain？
- Harness 循环中哪些输入最适合用于改进？
- 浏览器/HAT 证据为什么属于 harness？

## Open Questions

- 还需要对不同工具链的 harness 成本做横向比较。
