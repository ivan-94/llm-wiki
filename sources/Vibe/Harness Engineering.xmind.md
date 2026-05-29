---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Harness Engineering.xmind"
source_relpath: "Vibe/Harness Engineering.xmind"
raw_created_at: 2026-03-22T04:17:40.531108+00:00
raw_modified_at: 2026-04-19T14:08:33.011895+00:00
raw_size: 12651638
raw_fingerprint: "size=12651638;birth=2026-03-22T04:17:40.531108+00:00;mtime=2026-04-19T14:08:33.011895+00:00"
raw_snapshot_at: 2026-05-29T15:53:32.197140+00:00
ingested_at: 2026-05-29
status: ingested
---

# Harness Engineering.xmind

## Source

- Raw file: [Vibe/Harness Engineering.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Harness%20Engineering.xmind>)
- Raw ref: `raw:Vibe/Harness Engineering.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-03-22T04:17:40.531108+00:00`; modified `2026-04-19T14:08:33.011895+00:00`; size `12651638`; snapshot `2026-05-29T15:53:32.197140+00:00`
- Coverage: helper exported and read all `7` sheets: `Harness 工程`, `控制论`, `道与术`, `智能体 = 模型 + 套具`, `软件工程新瓶子装旧酒`, `未来的技术框架畅想`, `Harness 剖析`.

## Summary

这份多 sheet XMind 是一组关于 Harness Engineering 的综合资料，核心是把工程师角色从“亲自写代码”迁移到“设计 Agent 可工作的环境、约束、反馈闭环和知识系统”。它从 OpenAI/Anthropic/LangChain 等资料出发，把 Harness 解释为控制论式反馈系统、模型外部的套具/桁架、Agentic 开发的工程优先级重排，以及未来类似 Rails/Kubernetes 的 agent-native 软件控制框架。

## Source Digest

该 workbook 的主线是：当 Agent 的代码吞吐量超过人类注意力后，真正稀缺的不再是写代码能力，而是可观测环境、可验证闭环、结构化知识、边界约束和人类判断。Harness Engineering 因此不是提示词技巧，而是围绕 Agent 构造一套能“感知、行动、验证、修复、沉淀”的工程系统。

资料反复强调上下文是昂贵内存。AGENTS.md 不应成为百科全书，而应作为目录，把仓库知识拆进可索引、可验证、可更新的 docs、架构图、质量评分、计划和债务记录；同时通过自定义 linter、结构测试、CI、错误信息和文档园艺 Agent 把团队品味提升为可执行不变量。工程师的工作从实现细节转向定义意图、验收标准、回滚路径、质量边界和 trade-off。

第二条主线是控制论。蒸汽机调速器、Kubernetes 控制器和 Harness Engineering 都被描述为“声明目标状态、观察真实状态、修复偏差”的反馈闭合。传统代码库有编译器、测试、lint 等底层反馈，但缺少能在架构、抽象和系统质量层面闭环的传感器/执行器；LLM 让高层感知和执行开始可自动化，但仍依赖人类把系统知识外化成机器可读规范。

第三条主线是 Agent Harness 的组件模型：模型只是推理核心，外部套具包括系统提示、工具、MCP、skills、文件系统、沙盒、浏览器、日志、测试、状态管理、hooks、中间件、记忆、搜索、压缩、子代理委派、验证循环和权限护栏。资料把 Prompt Engineering、Context Engineering、Harness Engineering 分为递进层级，其中 Harness 覆盖工具编排、状态持久化、错误恢复、验证循环、安全强制和生命周期管理。

第四条主线是未来框架想象：AI 时代可能需要一个类似 Rails 的“软件控制系统标准模型”。在这个模型中，代码更像缓存，真正的 source of truth 是 Intent、Constraints 和 Feedback；仓库可能围绕 `/intent`、`/constraints`、`/system_model`、`/feedback_loops` 组织，传统 CI/CD 演进为 Continuous Alignment Pipeline，由 Agent 持续 build、test、fix、refactor，人类负责目标函数、约束和取舍。

## Key Claims

- explicit: 软件工程团队的首要任务会从写代码转向设计环境、明确意图，并构建让 Codex/Agent 可靠工作的反馈闭环。
- explicit: 人类时间与注意力是稀缺资源；没有 Harness Engineering，人会成为 Agent 代码吞吐量之后的 QA 和决策瓶颈。
- explicit: AGENTS.md 不应作为巨型百科全书，而应作为小而稳定的入口和目录，仓库知识应结构化沉淀在 docs、架构文档、质量文档和计划记录中。
- explicit: 仅靠文档不足以维持一致性，需要 linter、CI、结构测试、错误信息和文档园艺等自动化手段强制不变量。
- explicit: Harness Engineering 可被类比为控制论反馈闭合：声明目标、观察状态、比较偏差并执行修正。
- explicit: Agent Harness 包括编排循环、工具、记忆、上下文管理、提示词构建、输出解析、状态管理、错误处理、护栏、安全、验证循环和子智能体编排。
- explicit: 上下文管理策略包括压缩、观察遮蔽、即时检索和子代理委派；工具范围应最小化，过多工具会损害性能。
- explicit: 验证循环是生产级 Agent 与玩具演示的关键差异，可包括测试/lint/typecheck、Playwright 视觉反馈和独立 LLM 评判。
- explicit: Anthropic 长任务应用构建案例采用生成者-评估者循环，Planner 扩展规格，Generator sprint 开发，Evaluator 用 Playwright 和阈值评估后退回不合格结果。
- explicit: 未来 Harness 框架可能把软件系统建模为意图声明、约束、反馈循环、系统认知层和持续重构引擎。
- inferred: Harness Engineering 的核心学习对象不是单个 Agent 产品，而是“如何把高层工程判断编码成可执行反馈系统”。
- inferred: 对 Agentic 开发而言，DRY、阻塞式门禁、审美式代码规范等传统优先级可能下降；可观测性、TDD、BDD、benchmark 和可验证循环的重要性会上升。
- inferred: 未来工程师的差异化能力会更多体现在定义 objective、约束和验收，而不是手写实现量。

## External Links

- source-reference: [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — source 中用于生成者-评估者循环、长任务应用构建和 Playwright 评估案例；not verified.
- source-reference: [OpenAI: Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) — source 中列为 Harness 概念和 Codex agent-first 工程实践来源；not verified.
- source-reference: [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/#:~:text=But%20this%20co,the%20loop%20creates%20this%20overfitting) — source 用于“模型 + 桁架/套具”、harness 组件和模型/桁架共进化讨论；not verified.
- source-reference: [The Anatomy of an Agent Harness tweet](https://x.com/akshay_pachaar/status/2041146899319971922) — source 的 `Harness 剖析` sheet 标题引用；not verified.
- source-reference: [控制论相关 tweet](https://x.com/odysseus0z/status/2030416758138634583) — source 的 `控制论` sheet 标题引用；not verified.
- source-reference: [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) — source 扩展阅读；not verified.
- source-reference: [AI Agent 时代下，工程师如何重构工作方式](https://github.com/onevcat/2026-let-s-vision) — source 扩展阅读；not verified.
- source-reference: [从上下文工程到 Harness Engineering](https://mp.weixin.qq.com/s/ERSjcq9YURHvlsdTUv_Paw) — source 扩展阅读；not verified.
- source-reference: [为什么你的 AI 优先战略可能大错特错](https://x.com/dotey/status/2043953753921847582) — source 扩展阅读；not verified.
- source-reference: [软件工程新瓶子装旧酒引用 tweet](https://x.com/GenAI_is_real/status/2036266930290696599) — source 的占位 sheet 中出现；not verified.

## Links

- compiled-concept: Harness Engineering — 本 source 提供定义、动机、反馈闭环、工程实践和未来框架想象。
- compiled-concept: [[concepts/Agent Harness|Agent Harness]] — 资料系统列出 harness 组件、循环步骤和设计决策。
- compiled-concept: [[concepts/上下文工程|上下文工程]] — 候选更新；资料把 context 视为昂贵内存，并给出压缩、检索、子代理委派等治理策略。
- compiled-concept: Agent 可观测性 — 资料强调 UI、日志、指标、浏览器、测试和错误信息对 Agent 可读。
- compiled-concept: Agentic 软件控制系统 — 未来框架 sheet 将软件系统建模为 Intent、Constraints、Feedback 和系统认知层。
- compiled-synthesis: Harness Engineering 与控制论 — 候选综合；控制论 sheet 可与 Kubernetes、蒸汽机调速器和 Agentic 开发形成对比。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 适合作为 Vibe 主题中的核心工程方法论。

## Maintenance Notes

- helper `export_xmind_source.py` 返回 `ok: true`、`sheets_error: ""`，7 个 sheet 均已导出并阅读。
- `软件工程新瓶子装旧酒` sheet 仍是占位结构，只有“中心主题/分支主题”与一个 tweet 链接；后续需要补写或标记为低信息量。
- 多处外部资料标题和 URL 未联网核验；External Links 已标注 `not verified`。
- 原导出中存在项目符号、缩进和引用痕迹不完全规范的问题；本 source note 已消化为摘要，不保留完整机械 outline。
