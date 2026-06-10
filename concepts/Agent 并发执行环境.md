---
page_type: concept
updated_at: 2026-06-10
status: active
source_count: 3
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-13
---

# Agent 并发执行环境

## Definition

Agent 并发执行环境是专门为多个 Agent 同时独立工作而设计的隔离运行基础设施，通过 git worktree 文件系统隔离、动态端口映射和 Compose 命名空间，让 Agent 之间不相互干扰，同时共享构建缓存和基础镜像。

## Why It Matters

面向单人工作的 dev container 不能直接用于多 Agent 并发：端口冲突、共享状态、单工作区挂载会造成运行时干扰。只有把"人类开发环境"和"Agent 沙箱环境"清晰分层，才能可靠地同时跑多个 Agent 开发任务、验收测试和 HAT 运行。

## Mental Model

人类开发环境 = 单实例、持久状态、手动管理；Agent 沙箱 = 多实例并发、状态按需隔离、生命周期可控。

## Architecture

### 共享层（所有 Agent 复用）
- 构建缓存（Maven、npm/pnpm cache）
- 基础 Docker 镜像
- 基础 MySQL/Redis 服务（可选复用，视业务隔离需求）

### Agent 层（每个 Agent 独立）
- `git worktree` 文件系统隔离：每个 Agent 在独立分支工作
- 动态端口分配（避免冲突）
- 注入 `AGENT_ID`、`WORKTREE_PATH`
- Compose project 命名空间隔离

### 生命周期 CLI（双层设计）
- `.agent/bin/agent`：管理沙箱生命周期（init / up / exec / start / stop / migrate / status / logs / down / clean）
- `.agent-runtime/bin/project`：管理业务程序生命周期

### State Manifest
- 每个沙箱生成 `.agent/runs/{id}/manifest.json`，记录端口、URL、worktree、Compose files、logs、artifacts。
- Agent 从文件读取状态，不依赖上下文记忆。

## Key Claims

- explicit：多 Agent 并发需要 worktree 级文件系统隔离。
- explicit：dev container 面向人类，直接用于并发 Agent 会遇到端口冲突和共享实例问题。
- explicit：build cache 和镜像可共享；MySQL/Redis 数据默认应按 Agent 隔离。
- explicit：`exec` 用于一次性 test/lint/compile；`start` 用于长期服务，且要幂等。
- explicit：CLI 应提供机器可读 `status --json`、友好 `--help`、错误信息和健康检查。
- inferred：State Manifest 是让 Agent 从文件读状态而非依赖上下文记忆的关键设计决策。
- inferred：Loop Engineering 需要 worktree/沙箱隔离作为并行循环的运行基础，否则多个 Agent 分支会互相污染。

## Examples

- 用 `git worktree add ./agents/feature-1 feature-1-branch` 创建隔离工作区。
- `.agent/bin/agent up --agent-id feat-login` 启动一个新沙箱，自动分配端口并写 manifest。
- `agent exec --agent-id feat-login npm test` 在沙箱内运行一次性测试。

## Common Confusions

- 并发环境不等于多进程运行；关键是文件、状态和端口三重隔离。
- 不是所有 Agent 任务都需要完整沙箱；只读分析或简单 diff 可以更轻量。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/为 Agents 构造并发执行环境.xmind|为 Agents 构造并发执行环境]] — 完整设计方案，包括 CLI、Compose 结构、manifest 和双层生命周期。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/为 Agents 构造并发执行环境.xmind|为 Agents 构造并发执行环境（Matt Pocock cluster）]] — 复核同一设计在工具 cluster 中的工作流位置，并与 `setup-agent-runtime` 占位 source 互证。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind|Loop Engineering.xmind]] — 将 worktrees 列为 loop engineering 的基础组件。

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]] — 并发执行环境是 harness 的 state layer 和 execution layer 的实现
- enables: [[concepts/Agentic Engineering|Agentic Engineering]] — 多 Agent 并行交付的基础设施前提
- enables: [[concepts/Loop Engineering|Loop Engineering]] — worktree/沙箱隔离让循环中的并行 Agent 不互相干扰
- enables: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]] — 隔离 worktree、端口和服务生命周期让多个 HAT 验收任务更容易复现和调度
- used-in: [[entities/Agent Game|Agent Game]] — Agent Game 项目使用文件系统作为状态层的极简形态
- related-source: [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 构建 Agent Runtime.xmind|Ext 构建 Agent Runtime]] — 稀疏 runtime source 指向本页作为实际展开证据
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Understanding

当前理解：Agent 并发执行环境是"让 AI Coding 规模化"的基础设施，解决多个 Agent 同时跑不互相搞砸的问题。

## Review Questions

- 为什么 dev container 不能直接支持多 Agent 并发？
- manifest.json 解决了什么问题？
- exec 和 start 的语义差异是什么？

## Open Questions

- 不同项目类型（纯前端、微服务、单体）的并发环境实施成本还需要对比案例。
