---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/Agent 解构.xmind"
source_relpath: "Agent/Agent 解构.xmind"
raw_created_at: 2026-03-22T09:28:42.766453+00:00
raw_modified_at: 2026-04-09T01:50:49.252497+00:00
raw_size: 7342323
raw_fingerprint: "size=7342323;birth=2026-03-22T09:28:42.766453+00:00;mtime=2026-04-09T01:50:49.252497+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.857404+00:00
ingested_at: 2026-05-30
status: ingested
---

# Agent 解构.xmind

## Source

- Raw file: [Agent/Agent 解构.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/Agent%20%E8%A7%A3%E6%9E%84.xmind>)
- Raw ref: `raw:Agent/Agent 解构.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-03-22T09:28:42.766453+00:00`; modified `2026-04-09T01:50:49.252497+00:00`; size `7342323`; snapshot `2026-05-29T22:03:22.857404+00:00`
- Coverage: exported and digested 1 sheet: `画布 1`.

## Summary

这是一份 Agent 系统拆解笔记，围绕 Agent Loop、workflow 与 agent 的控制权差异、五类控制模式、Harness 工程、上下文工程、OpenClaw 架构、多 Agent 组织、自主度、记忆和工具设计展开。它的核心观点是：Agent 的主循环相对稳定，真正的工程化差异主要来自循环外围的 harness、上下文、工具、记忆、安全边界和多 Agent 协作协议。

## Source Digest

这份 source 把 Agent 从“会调用工具的模型”推进到“被工程系统包裹的长期执行体”。它先用 `感知 -> 决策 -> 行动 -> 反馈` 固定主循环定义 Agent，再把新增能力放在主循环外部：工具 handler、MCP、Skills、系统提示结构、外化记忆等。workflow 与 agent 的边界被归结为控制权：路径由代码预写的是 workflow，由 LLM 动态决定下一步的是 agent。

在控制模式上，raw 给出从弱到强的五类模式：Prompt Chaining、Routing、Parallelization、Orchestrator-Workers、Evaluator-Optimizer。它们对应不同的任务形态：线性变换、输入分流、分段或投票、动态拆解委派、带反馈的质量优化。这组分类可直接服务于后续的 Agent 编排地图。

工程化部分的重心是 Harness 与上下文。Harness 被定义为围绕 Agent 的验收基线、执行边界、反馈信号和回退手段；OpenAI Agent 优先开发实践强调“Agent 看不到的内容等于不存在”、把约束编码进 lint/类型/CI，以及让 Agent 能查日志、指标、追踪并端到端完成任务。上下文工程则被拆成常驻层、按需加载、运行时注入、记忆层和系统层，重点不是扩大窗口，而是维持信息密度、缓存稳定性和压缩保真。

OpenClaw 和多 Agent 章节把这些原则具体化：通过 Gateway、Channel 适配器、Pi Agent、工具集、上下文+记忆五层解耦，让渠道、Agent 主循环和工具能力分开；通过 source-sink 安全拆分、白名单、工作空间隔离、审计日志和 fallback 控制风险。多 Agent 价值被定位为异步委派和持久化工件，而不是简单多开模型；因此需要 JSONL inbox、worktree 隔离、任务图、交叉验证、深度限制和最小系统提示。

最后，source 将自主度和记忆落到可操作机制：长任务跨 session 续跑需要 Initializer Agent 先创建 `feature-list.json`、`init.sh`、初始提交和进度文件，Coding Agent 后续按进度循环；单 session 内用唯一 `in_progress` 和校正提醒避免漂移；慢速 I/O 通过后台线程和通知队列接入。记忆被分成工作记忆、Skills、JSONL 会话历史和 MEMORY.md；工具设计则从 API 封装进化到 ACI，再到 Tool Search、Programmatic Tool Calling 和示例驱动的高级工具使用。

## Key Claims

- explicit: Agent 主循环可以抽象为感知、决策、行动、反馈，新增能力通常叠加在循环外部，而不是改动循环内部。
- explicit: workflow 与 agent 的核心差异是控制权，代码预写路径属于 workflow，LLM 动态决定下一步属于 agent。
- explicit: Harness 至少包括验收基线、执行边界、反馈信号和回退手段。
- explicit: 上下文工程的关键问题不是窗口长度，而是信息密度、加载层次和压缩策略。
- explicit: 多 Agent 协作需要协议化、worktree 隔离、任务图和交叉验证，否则幻觉和依赖关系会互相放大。
- explicit: Agent 自主度依赖跨 session 状态、单 session 进度约束和慢速 I/O 后台接入，而不是单纯减少人工确认。
- inferred: 这份 source 可以作为 Agentic Engineering、Agent Harness、上下文工程和 Agent 工具设计多个概念页的核心证据来源。

## External Links

- source-thread: [Agent 解构](https://x.com/HiTw93/status/2034627967926825175) - root topic link; not verified.
- extended-reading: [Components of A Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) - coding agent component reference listed under extension reading; not verified.

## Links

- compiled-concept: [[concepts/AI Agent|AI Agent]] - source 提供 Agent Loop、控制模式、多 Agent 和记忆边界，是本轮 AI Agent 概念页的核心证据。
- compiled-synthesis: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] - source 支撑把 Agent 编译为 loop、harness、context、tools、memory、sandbox 的系统工程视角。
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]] - source 作为 Agent 学习路径的系统总览入口。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] - source 提供 Agent 控制模式、多 Agent 组织、自主度和工程化基础设施的系统框架。
- related: [[concepts/Agent Harness|Agent Harness]] - source 明确定义 harness 的四个组成，并列出 OpenAI Agent 优先开发实践。
- related: [[concepts/Agent Skills|Agent Skills]] - source 将 Skills 作为 Agent Loop 外围能力和程序性记忆的一部分。
- related: [[concepts/上下文工程|上下文工程]] - source 对上下文分层、压缩、缓存和文件系统接口有完整展开。
- related: [[concepts/Vibe Coding|Vibe Coding]] - source 中的长任务续跑、worktree 子 Agent 和端到端自主执行可补充 Vibe Coding 的工程化实践。
- related: [[entities/Agent Client Protocol|Agent Client Protocol]] - source 的 ACI 与工具接口演进可作为协议化工具接口的候选背景。
- entity-candidate: [[entities/OpenClaw|OpenClaw]] — raw 提供了五层架构、安全边界、长任务恢复和记忆机制，后续值得判断是否创建实体页。

## Maintenance Notes

- Export covered one sheet and produced usable structured content.
- Raw includes named examples such as nanobot, learn-claude-code, OpenClaw, ChatGPT memory, MCP and Vector/Victoria observability stack, but many are cited as conceptual examples without full source URLs.
