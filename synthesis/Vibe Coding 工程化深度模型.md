---
page_type: synthesis
updated_at: 2026-06-10
status: active
source_count: 24
learning_status: learning
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# Vibe Coding 工程化深度模型

## Thesis

Vibe Coding 的深层变化不是“用自然语言写代码”，而是软件开发的真理源重排：代码从唯一 source of truth 降级为可再生成、可重构、可替换的执行产物；真正需要长期维护的是意图、行为规格、决策边界、反馈证据和 Agent 可执行环境。Agentic Engineering 的任务，就是把这些真理源组织成一个控制系统。

## Layered Model

| 层级 | 核心问题 | 主要产物 | Agent 风险 | 人类责任 |
| --- | --- | --- | --- | --- |
| L0 Intent | 为什么做，成功是什么 | 用户价值、North Star、非目标 | 优化错目标 | 决定价值函数 |
| L1 Behavior | 系统必须表现出什么行为 | PRD、FR/SC、Gherkin、examples | 自行补全语义 | 澄清业务语言和验收行为 |
| L2 Decisions | 哪些判断不能交给 Agent 静默决定 | 决策图、语义图、边界图、工程宪法 | 决策权泄漏 | 标出产品、安全、架构和领域决策 |
| L3 Execution | 如何让 Agent 稳定执行 | worktree、skills、MCP、hooks、tests、runtime | context rot、短视修补 | 设计 harness 和任务粒度 |
| L4 Evidence | 怎么证明没有走捷径 | CI、HAT、browser evidence、review、Source Manifest | 测试过拟合、表面通过 | 定义完成标准和反捷径审查 |
| L5 Learning | 失败如何变成系统改进 | log、ADR、AGENTS、checklist、skill、lint | 同类错误反复发生 | 把失败棘轮化为规则和工具 |

这个模型解释为什么单纯“prompt 更详细”不能解决大需求偏移。自然语言 spec 只能给出稀疏约束，Agent 会在未定义空间里自动补全；如果 L2 决策边界和 L4 证据机制缺失，代码看似完成，实则把隐性产品/架构/安全决策写死在实现里。

## Failure Modes

- 60 分粗生成：模型快速生成结构完整的方案，但边界、异常、组合场景和长期可维护性开始漂移。
- 决策权泄漏：状态含义、权限例外、错误码、校验层级、规则复用路径等本应上浮的问题被 Agent 静默决定。
- 证据过拟合：测试只证明当前实现能通过 happy path，不能证明语义正确、路径收敛或反例失败。
- 上下文腐烂：上下文变长后关键信息权重下降，Agent 继续执行但不再围绕核心约束优化。
- 编排税：多 Agent、工具、worktree、交接、review 和合并会产生额外协调成本；并发只有在切片清晰且合并可验时才增益。
- 人类瓶颈迁移：代码吞吐量上升后，人类不再主要卡在实现，而是卡在目标设定、审查、验收、合并和知识回写。

## Control Levers

- 决策分辨率：L0 目标、L1 语义和 L2 边界必须强治理；普通 L4 实现细节可以交给 Agent。
- 示例化验收：用 SbE / Given-When-Then 把模糊需求压成业务可读、机器可执行、可回归的行为样例。
- Artifact 分层：规格、设计、任务、数据模型、契约、测试和 HAT 各自承担不同责任，避免一个长文档混装所有判断。
- Harness 棘轮：每次 Agent 失败都应转化为更好的 AGENTS 入口、skill、hook、linter、test、checklist 或 runtime 约束。
- 反捷径证据：主动问“什么错误实现也能通过当前测试”，补规则族、组合场景、破坏性验证和维护者审查。
- Source Manifest：交接给其他 Agent 时保留原始来源，使下游能重读 raw/source，而不是只继承二手摘要。

## Tool Roles

| 工具/方法 | 最适合解决的问题 | 不应承担的问题 |
| --- | --- | --- |
| Specification by Example | 需求歧义、业务规则、验收行为和反例 | 项目级变更账本 |
| SpecKit | 从模糊 feature 到 spec/plan/tasks 的交付脚手架 | 长期维护当前系统事实 |
| OpenSpec | 存量系统的 change delta、behavior contract 和 archive | 快速原型的一次性任务拆解 |
| GitHub workflow | issue/PR/CI/review/HAT 的可追踪协作状态机 | 替代需求澄清和领域建模 |
| Agent Harness | 工具、上下文、权限、验证和运行时控制面 | 替代人的目标函数和风险判断 |

## Maturity Model

1. Prompt draft：人给意图，Agent 出粗稿，质量主要靠人肉检查。
2. Spec slice：任务有明确输入、边界、非目标和验收样例，可以小步实现。
3. Harnessed loop：Agent 在隔离运行时中执行，有测试、lint、日志、hooks 和失败反馈。
4. Agentic delivery：PRD、issue、worktree、sub-agent、review、HAT、PR 形成可交接闭环。
5. Continuous alignment：项目把意图、约束、系统模型和反馈循环持续沉淀，失败自动回写为规则和工具。

## Consensus Six-Layer Upgrade (共识六层升级)

传统软件团队的共识方法论在 AI 时代需要系统性升级，对应到 Vibe Coding 工程化：

| 层 | 传统方式 | AI 时代升级 | 工程化工具 |
| --- | --- | --- | --- |
| 语言共识 | 文档、口头沟通 | CONTEXT.md 领域语言，供 Agent 直接读入 | [[concepts/CONTEXT.md 领域语言|CONTEXT.md 领域语言]] |
| 需求共识 | PRD + Review 会议 | SbE Examples + Three Amigos 快速对齐 | [[concepts/Specification by Example|SbE]] |
| 执行共识 | 任务分配 + 进度追踪 | Issue + worktree + Source Manifest | Agent 并发执行 |
| 验收共识 | UAT + 人工检查 | HAT + 活文档 + 反捷径清单 | [[concepts/反捷径证据|反捷径证据]] |
| 异常共识 | Bug 报告 + 修复 | Sentry → Agent 可消费上下文 → 自动 PR | [[concepts/异常治理闭环|异常治理闭环]] |
| 知识共识 | 口头传递 + Wiki | AGENTS.md + skill + 工程宪法棘轮化 | [[concepts/工程宪法|工程宪法]] |

## Anomaly Governance & Software Factory Trap

**异常治理闭环**是深度模型中 L5 Learning 层的具体实现路径之一：生产异常 → Sentry 结构化上下文 → Agent 可消费 → 自动 PR → 人工验收。这条链路要求 L2 决策边界清晰，否则 Agent 会静默补全修复边界。

**软件工厂陷阱**是 L3/L4 层的系统性风险：当代码生成速度远超验证和治理能力时，技术债以新的形式累积——不再是"没时间重构"，而是"没有 spec 和证据的高速生成"。防范要素：严格 L2 决策分辨率 + L4 反捷径证据。

**Loop Engineering**补强 L3/L5 的执行循环：automation 发现任务，worktree 隔离并行执行，skills 提供项目知识，connectors 接入工具，sub-agents 生成与验证，memory 保存完成状态和下一步计划。它要求把“下一步该做什么”从聊天临场判断迁移到可中断、可恢复、可审计的循环系统。

**AI 代码垃圾治理（DeSlop）**补强软件工厂陷阱的代码库健康层：垃圾来自高通量生成、低约束输入、弱验证机制和持久化代码库；治理要覆盖生成前约束、生成中限权、生成后准入、合并后观测和演化中删除。

**Vibe 设计原型**不可产品化规则：原型探索适合 Vibe Coding，但原型代码本身不应直接进入产品交付，必须经历重新 spec + 工程化实现的双阶段。见 [[concepts/Vibe 设计原型开发|Vibe 设计原型开发]]。

## Practical Heuristics

- 如果任务说明不能列出“哪些决策不能让 Agent 自己做”，它还不是适合大规模执行的 spec。
- 如果验收只包含 happy path，它会鼓励 Agent 找捷径；至少要补边界、反例和跨入口规则复用。
- 如果多 Agent 并发需要父 Agent 人工解释大量背景，说明切片和 Source Manifest 还不够硬。
- 如果失败只能靠人记住，下次还会失败；失败必须变成 rule、test、hook、skill 或 template。
- 如果一个工具的产物不能进入实现、验证或回写链路，它只是文档装饰，不是工程控制面。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/杂记/从 Vibe Coding 到 Agentic Engineering.xmind|从 Vibe Coding 到 Agentic Engineering]] 支撑 Software 3.0、Vibe Coding、Agentic Engineering 和人类责任迁移。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/大型需求的偏移根因与控制.xmind|大型需求的偏移根因与控制]] 支撑稀疏 spec、决策权泄漏、决策分辨率、六张治理图和反捷径证据。
- [[sources/Vibe/Harness Engineering.xmind|Harness Engineering.xmind]] 支撑 harness 作为控制论反馈闭合和未来软件控制系统的判断。
- [[sources/Vibe/Vibe Coding 随手记/Harness/Agent Harness Engineering.xmind|Agent Harness Engineering]] 支撑 `Agent = Model + Harness`、组件 taxonomy、失败棘轮和安全边界。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Vibe Coding 的 Sweet Spot：从粗生成到精修.xmind|Vibe Coding 的 Sweet Spot]] 支撑 60 分粗生成、任务粒度、状态外置和 `f(task_spec) -> result` 模型。
- [[sources/Vibe/方法论.xmind|方法论.xmind]] 支撑 SDD、SOP、context loop、plan loop、scaffold loop 和 AI 友好工程环境。
- [[sources/Vibe/Spec/SpecKit/对比 OpenSpec.png|对比 OpenSpec]] 支撑 OpenSpec/SpecKit 的账本与脚手架分工。
- [[sources/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png|2 sbE 是如何运作的]] 和 [[sources/Vibe/软件工程基础/Specification by Example/5 落地和反模式.png|5 落地和反模式]] 支撑示例化验收和 SbE 反模式。
- [[sources/Vibe/工具/Github 原住民.xmind|Github 原住民]] 和 [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] 支撑 GitHub/skill/worktree/HAT 组成的 Agent 交付闭环。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind|hat-prepare]]、[[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind|hat-run]]、[[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind|hat-frontend-friendly]] 和 [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 后端项目如何 Agents HAT Friendly.xmind|hat-backend-friendly]] 支撑 L4 Evidence 的 HAT 证据机制和项目侧可验收性要求。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 上下文检查agent-context-audit.xmind|agent-context-audit]] 支撑 L5 Learning 中主动审计入口上下文是否被新 Agent 正确理解的治理方法。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/Loop Engineering.xmind|Loop Engineering.xmind]] 支撑 L3/L5 的系统循环模型。
- [[sources/Vibe/工具/Claude Code/动态工作流.xmind|动态工作流.xmind]] 支撑 Claude Code 侧的脚本化 loop、扇出合成和对抗性验证。
- [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind|垃圾治理(DeSlop).xmind]] 支撑 AI 代码垃圾成因、准入治理和删除机制。

## Relations

- synthesizes: [[concepts/Vibe Coding|Vibe Coding]]
- synthesizes: [[concepts/Agentic Engineering|Agentic Engineering]]
- synthesizes: [[concepts/Agent Harness|Agent Harness]]
- synthesizes: [[concepts/Spec-Driven Development|Spec-Driven Development]]
- uses: [[concepts/Specification by Example|Specification by Example]]
- uses: [[concepts/HAT（Hand Acceptance Test）|HAT（Hand Acceptance Test）]]
- uses: [[concepts/Agent 上下文审计|Agent 上下文审计]]
- uses: [[concepts/Loop Engineering|Loop Engineering]]
- uses: [[concepts/AI 代码垃圾治理|AI 代码垃圾治理]]
- extends: [[synthesis/Vibe Coding 与 Agentic Engineering|Vibe Coding 与 Agentic Engineering]]
- informs: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]]
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]]

## My Take

这批 Vibe 资料真正有价值的不是“AI 能写更多代码”，而是已经隐约形成了一套 Agentic 软件工程控制论：把目标、语义、决策、执行、证据和学习分层治理。浅 compile 只会得到“Vibe Coding 需要 spec 和 harness”；深 compile 应该得到“什么时候交给 Agent、哪些必须上浮给人、哪些证据才算完成、失败如何变成系统能力”。

## Wave 4b 补充：工具生态层定位

### L4 证据机制的核心工具角色

L4 Evidence（证据层）的具体工具已在 Wave 4b 资料中得到更明确的支撑：

- **GStack 核心洞察**（`AI 软件工厂 GStack.xmind` 中的 `核心洞察` 节点）：解释为什么高质量 prompt 复用 + 交叉验证置信度 + 即时反馈速度压缩认知成本——这正是 L4 证据机制的工程实现。
- **GStack 交叉评审**（`/codex` 命令）：用 Claude 与 Codex 的二次评审说明异构模型验证，是"主动问什么错误实现也能通过当前测试"的工具化实现。
- **L4 核心验证逻辑**：[[concepts/HAT（Hand Acceptance Test）|HAT]]（`/hat-prepare`/`/hat-run`）从用户路径验收；`/cross-review` 提供 diff evidence；browser 能力让 Agent 真正"看"状态而不是读代码——三者共同构成 L4 反捷径证据体系。新增 HAT-friendly 前后端 source 说明，L4 证据质量还依赖项目是否暴露稳定选择器、URL 状态、日志、Request Id 和可观测性。

### L3 执行层的工具支撑

L3 Execution（执行层）在 Wave 4b 中有更完整的工具覆盖：

- **Agent Board / 看板管理**（`看板管理.xmind`）：把 worktree 并发、issue triage、runner 选择和 HAT 状态机产品化为可视控制面——是 L3 执行层的编排 UI 候选。
- **Agent 沙箱**：Codex 云端容器和 worktree 隔离是 L3 Agent 并发执行的运行时隔离机制，链接 [[concepts/Agent 沙箱|Agent 沙箱]]。
- **远程 Agent 控制栈**：tmux/Happy Engineering/Tailscale 让 L3 执行不受本地 laptop 约束，链接 [[concepts/远程 Agent 控制栈|远程 Agent 控制栈]]。

### L5 学习层的上下文审计

[[concepts/Agent 上下文审计|Agent 上下文审计]] 把“新 Agent 会不会读错入口”变成可采样反馈：sub-agent 独立答题，主 Agent 建立 ground truth，再从正确性、推理路径、探索成本和上下文污染定位入口文档、skill 描述或 handoff 的缺陷。这让 L5 Learning 不只是失败后补规则，也能主动检查规则是否真的被 Agent 理解。

## Open Questions

- 编排税目前只有占位 source 和外部链接，需要补充真实案例才能形成强概念页。
- Agentic Engineering 的 L5 Continuous alignment 还缺少真实项目长期运行证据。
- OpenSpec、SpecKit、GitHub 产品细节未联网核验；本页只依赖 raw/source 中记录的学习材料。
