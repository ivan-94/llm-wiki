---
type: cook-github
ingest_policy: on-request
inbox_status: unread
inbox_created_at: 2026-06-13
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: github-repository
github_url: https://github.com/addyosmani/agent-skills
normalized_url: https://github.com/addyosmani/agent-skills
owner: addyosmani
repo: agent-skills
requested_ref: default
resolved_commit: d187883b7d761265309cdcc0f202cc76b4b3fb06
default_branch: main
cloned_at: 2026-06-13T14:37:28+00:00
---

# Agent Skills：Review 质量门禁与去 Slop 工作流

## 速读

`addyosmani/agent-skills` 的 Review 组不是传统代码工具，而是一组给 AI coding agent 调用的工程工作流。它把“代码能不能进主干”拆成 4 个可组合门禁：五轴 review、行为不变简化、安全硬化、性能优化。

这一组最适合学习的是：AI 写完代码后，不能只看“能不能跑”，而要把 merge 前检查变成明确流程、证据和输出格式。

## 仓库定位

仓库自定位是面向 AI coding agents 的 production-grade engineering skills。它用 Markdown `SKILL.md`、TOML slash commands、agent persona、reference checklist 组合出一个软件开发生命周期：

```text
DEFINE -> PLAN -> BUILD -> VERIFY -> REVIEW -> SHIP
```

本次 cook 只聚焦 README 中 `Review - Quality gates before merge` 这一组：

- `code-review-and-quality`
- `code-simplification`
- `security-and-hardening`
- `performance-optimization`

## 解决什么问题

AI 写代码的主要风险不是“不会写”，而是写出看似完整但缺少工程收口的代码：

- happy path 能跑，但 edge case、error path、race condition 没覆盖。
- 实现过度抽象、命名泛化、控制流绕，未来人和 agent 都难读。
- 安全边界被 prompt 约束替代，没有真实代码级校验。
- 性能优化靠猜测，甚至为了“显得高级”加入复杂但无证据的优化。

Review 组的思想是：把这些风险前置成 merge 前质量门禁。

## 项目特性

| Skill | 角色 | 核心原则 | 输出 |
| --- | --- | --- | --- |
| `code-review-and-quality` | 总门禁 | 五轴 review：正确性、可读性、架构、安全、性能 | 分级 findings、file:line、修复建议、approve/request changes |
| `code-simplification` | 去 slop | 行为不变地降低复杂度，先理解再动手 | 小步 refactor、测试验证、干净 diff |
| `security-and-hardening` | 安全门禁 | 所有外部输入都不可信，先 threat model | trust boundary、STRIDE、OWASP、LLM 安全规则 |
| `performance-optimization` | 性能门禁 | 先测量再优化 | baseline、瓶颈、修复、复测、防回归 |

## 典型使用方式

`/review` 触发 `code-review-and-quality`，要求检查当前 staged changes 或 recent commits。它把五轴 review 作为总框架，并显式把 security/performance 拉进来。

`/code-simplify` 触发 `code-simplification`，要求先读项目约定，理解目标代码的用途、调用方、边界和测试覆盖，再逐个简化点处理。每次简化都要验证，失败则回退。

`/ship` 是更强的 fan-out：并行调用 `code-reviewer`、`security-auditor`、`test-engineer` 等 persona，再合并成 go/no-go 判断。这个模式说明仓库并不鼓励一个“万能 reviewer persona”包办一切，而是用命令层做编排。

## 主要架构

```mermaid
flowchart LR
  Intent[用户或 Agent 意图] --> Command[Slash Command]
  Intent --> DirectSkill[直接匹配 Skill]
  Command --> Skill[SKILL.md 工作流]
  Command --> Persona[Agent Persona]
  Skill --> Reference[Reference Checklist]
  Persona --> Report[结构化报告]
  Skill --> Gate[Verification Gate]
  Report --> Decision[Approve / Request Changes / Go-No-Go]
  Gate --> Decision

  Review[/review] --> CRQ[code-review-and-quality]
  Simplify[/code-simplify] --> CS[code-simplification]
  CRQ --> SEC[security-and-hardening]
  CRQ --> PERF[performance-optimization]
```

## 代码地图

| 路径 | 作用 |
| --- | --- |
| `README.md` | 总览生命周期、命令和 24 个 skills |
| `AGENTS.md` | 面向 agent 的 skill 路由规则：匹配任务时必须使用对应 skill |
| `plugin.json` | 插件元信息，名称为 `agent-skills` |
| `commands/review.toml` | `/review` 的入口 prompt |
| `commands/code-simplify.toml` | `/code-simplify` 的入口 prompt |
| `commands/ship.toml` | 多 persona fan-out 的发布前判断 |
| `skills/code-review-and-quality/SKILL.md` | Review 总门禁 |
| `skills/code-simplification/SKILL.md` | 行为不变简化 |
| `skills/security-and-hardening/SKILL.md` | 安全硬化 |
| `skills/performance-optimization/SKILL.md` | 性能优化 |
| `agents/code-reviewer.md` | Staff Engineer 视角 review persona |
| `agents/security-auditor.md` | 安全审计 persona |
| `agents/web-performance-auditor.md` | Web 性能审计 persona |
| `references/security-checklist.md` | 安全检查细则 |
| `references/performance-checklist.md` | 性能检查细则 |

## 核心模块

### code-review-and-quality

这是总门禁。它要求所有变更 merge 前都经过五轴检查：正确性、可读性、架构、安全、性能。

它的关键不是“挑毛病”，而是建立 approve 标准：只要变更明确改善代码健康，并遵循项目约定，就可以批准；不追求完美主义。这个尺度很重要，因为 AI reviewer 容易陷入无限建议。

高价值做法：

- 先看测试，因为测试揭示意图和覆盖面。
- 变更粒度有明确尺度：约 100 行容易 review，约 300 行可接受，约 1000 行应该拆。
- refactor 和 feature work 要分开，避免行为变化和结构变化混在一个 diff 里。
- findings 要分级，不让作者把所有建议都当成 blocker。
- review 最后要检查 verification story：跑了什么测试、build 是否通过、UI 是否有截图、是否有 before/after。

### code-simplification

这是最贴近“去 slop”的 skill。它的目标不是减少行数，而是让代码更容易理解、修改和调试，同时保持行为完全不变。

它最值得学的是两个约束：

- Chesterton's Fence：不知道某段代码为什么存在，就不要先拆掉。
- Rule of 500：如果重构会超过 500 行，优先考虑 codemod、sed、AST transform 等自动化，而不是手改。

它把 slop 信号具体化了：

- 3 层以上深嵌套。
- 50 行以上长函数。
- nested ternary。
- `data`、`result`、`temp` 这类泛名。
- 重复逻辑。
- 死代码、无意义 wrapper、只有一个策略的 strategy pattern。

### security-and-hardening

这个 skill 把安全从“最后扫一眼”改成“每个边界的设计约束”。它要求先做 threat model：找 trust boundary、命名资产、用 STRIDE 过一遍、把 abuse case 写成测试。

它对 AI 代码特别有价值，因为它明确把 LLM output 视为不可信输入：

- 不把模型输出直接送进 `eval`、SQL、shell、`innerHTML` 或文件路径。
- 不把 system prompt 当成安全边界。
- 不把 secrets、跨租户数据或完整 system prompt 塞进 context。
- tool/agent 权限要收敛，破坏性动作要确认。
- token、rate、递归深度都要有限制。

### performance-optimization

这个 skill 的中心是 measure-first：不测量就优化，就是猜。

它的流程是：

```text
MEASURE -> IDENTIFY -> FIX -> VERIFY -> GUARD
```

它还把“指标诚实”写进工作流：没有 Lighthouse、CrUX、PageSpeed Insights、DevTools trace 或 live MCP 数据时，静态阅读只能说 potential impact，不能伪造 LCP/INP/CLS 等指标。

这对 AI 很重要，因为 agent 很容易“看代码猜性能”。这个 skill 要求把猜测降级成假设，再用测量确认。

## 数据流 / 控制流

一个理想的 AI 代码变更收口流程可以这样组织：

```text
Agent 实现代码
  -> 测试或验证证据
  -> /review 五轴总审查
  -> code-simplification 去复杂度
  -> security-and-hardening 过安全边界
  -> performance-optimization 只优化被测量证明的问题
  -> 分级 findings + 修复建议
  -> human 或 command 层做最终 merge 判断
```

关键点是：这些 skill 不是四个孤立 checklist，而是一套 gate composition。`code-review-and-quality` 做总入口，`security-and-hardening` 和 `performance-optimization` 是高风险维度的深挖，`code-simplification` 是 review 后最常见的修复动作。

## 依赖与技术栈

仓库本身不是运行时应用，核心资产是：

- Markdown skills。
- TOML slash commands。
- Markdown agent personas。
- Reference checklists。
- 一个 Node.js validation script。

它引用 Lighthouse、Chrome DevTools MCP、CrUX、PageSpeed Insights、`npm audit` 等外部工具，但这些是宿主环境能力，不是仓库自身依赖。

## 设计亮点

第一，skill 都有明确触发条件和反触发条件。比如 `code-simplification` 明确说：如果还没理解代码，不要简化；如果代码已经清楚，不要为了简化而简化。

第二，它把 AI 常见失败模式写成工程约束，而不是只靠“请认真一点”。例如 review 要看 tests first，性能要 metric honesty，安全要 treat model output as untrusted。

第三，它区分了 skill、persona、command 三层：

- Skill 是流程。
- Persona 是视角。
- Command 是编排入口。

这个分层比“写一个超长 system prompt”更可维护。

## 批判性点评

这个仓库强在方法论表达，弱在执行约束。绝大多数 gate 依赖 agent 自觉执行；除了结构验证脚本，仓库本身不会自动阻止 agent 跳过测试、跳过测量或给出空泛 review。

另一个边界是平台差异。Claude Code、Cursor、Gemini CLI、OpenCode、Copilot 对 skill、command、persona 的支持方式不同。同一套 Markdown 能迁移，但执行一致性未必一致。

此外，Review 组对真实项目的效果高度依赖上下文质量。如果 agent 没拿到 spec、diff、测试输出、性能数据、部署边界，它只能给出过程正确但证据不足的报告。特别是 performance 和 security，仓库自身也承认静态阅读不能替代真实测量或完整安全审计。

## 风险与不确定

- `hooks/` 未深度覆盖；本次 cook 只聚焦 Review 组和相关 command/persona/reference。
- 没有运行仓库代码，也没有执行 validation script。
- 未联网核验 README 外链或平台安装现状。
- 没有对所有 24 个 skills 做完整比较。
- 信息图由 imagegen 基于本次理解生成，适合作为学习图，不是原仓库官方图。

## 对我的启发

最值得迁移到自己 agent workflow 的不是某一条 checklist，而是门禁组合：

1. 所有 AI 代码改动先形成可 review 的小 diff。
2. review 不只看功能，也看可读性、架构、安全、性能。
3. 简化必须行为不变，并且每步可回退。
4. 安全从 trust boundary 开始，不从漏洞清单开始。
5. 性能优化必须有 baseline 和复测。
6. findings 必须带 file:line 和具体修复建议，否则只是评论。

## 可以继续追的问题

- `agent-skills` 和 `obra/superpowers` 的质量门禁有什么根本差别？
- `code-simplification` 能否和 `ast-grep`、`jscodeshift` 这样的 codemod 工具形成自动化去 slop 流程？
- `/ship` 的 multi-persona fan-out 是否比单一 reviewer 更稳定？
- 能不能把这组 Review skills 改造成 Codex 本地可调用的 `.codex/skills`？
- 对真实项目，怎样把 `performance-optimization` 的 metric honesty 接进 Playwright/Lighthouse CI？

## 信息图

### 总览

![[human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/infographic.webp]]

### code-review-and-quality

![[human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/code-review-and-quality.webp]]

### code-simplification

![[human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/code-simplification.webp]]

### security-and-hardening

![[human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/security-and-hardening.webp]]

### performance-optimization

![[human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/performance-optimization.webp]]

## Source Manifest

- input GitHub URL: `https://github.com/addyosmani/agent-skills`
- normalized URL: `https://github.com/addyosmani/agent-skills`
- requested ref: `default`
- resolved commit: `d187883b7d761265309cdcc0f202cc76b4b3fb06`
- default branch: `main`
- clone command: `git clone --depth 1 --no-recurse-submodules "https://github.com/addyosmani/agent-skills" ".codex/cache/cook-github/addyosmani-agent-skills-main/repo"`
- cloned at: `2026-06-13T14:37:28+00:00`
- cache path: `.codex/cache/cook-github/addyosmani-agent-skills-main`
- repo path: `.codex/cache/cook-github/addyosmani-agent-skills-main/repo`
- repo metadata: `.codex/cache/cook-github/addyosmani-agent-skills-main/repo-metadata.json`
- file inventory: `.codex/cache/cook-github/addyosmani-agent-skills-main/file-inventory.txt`
- exploration report: `.codex/cache/cook-github/addyosmani-agent-skills-main/exploration-report.md`
- 子 Agent: created and completed; agent id `019ec16a-e5f1-7be2-95a0-b80d3bf8545c`; 子 Agent 只返回报告正文，父 Agent 已落盘。
- 父 Agent 补读关键文件:
  - `README.md`
  - `AGENTS.md`
  - `plugin.json`
  - `commands/review.toml`
  - `commands/code-simplify.toml`
  - `skills/code-review-and-quality/SKILL.md`
  - `skills/code-simplification/SKILL.md`
  - `skills/security-and-hardening/SKILL.md`
  - `skills/performance-optimization/SKILL.md`
  - `agents/code-reviewer.md`
  - `agents/security-auditor.md`
  - `agents/web-performance-auditor.md`
- imagegen status: success; built-in imagegen generated 5 PNG images.
- imagegen originals:
  - `.codex/cache/cook-github/addyosmani-agent-skills-main/imagegen-original-overview.png`
  - `.codex/cache/cook-github/addyosmani-agent-skills-main/imagegen-original-code-review-and-quality.png`
  - `.codex/cache/cook-github/addyosmani-agent-skills-main/imagegen-original-code-simplification.png`
  - `.codex/cache/cook-github/addyosmani-agent-skills-main/imagegen-original-security-and-hardening.png`
  - `.codex/cache/cook-github/addyosmani-agent-skills-main/imagegen-original-performance-optimization.png`
- infographic paths:
  - `human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/infographic.webp`
  - `human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/code-review-and-quality.webp`
  - `human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/code-simplification.webp`
  - `human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/security-and-hardening.webp`
  - `human/inbox/cook-github/assets/2026-06-13_Agent-Skills-Review-质量门禁_addyosmani_agent-skills/performance-optimization.webp`
- read-only boundary: 未运行仓库代码，未安装依赖，未执行测试、构建、Docker、未知二进制，未初始化 submodules。
- coverage limitations: 本次 cook 聚焦 Review 质量门禁 4 个 skills；未完整覆盖所有 24 个 skills、hooks 深层行为、docs 全量内容和安装平台运行差异。
