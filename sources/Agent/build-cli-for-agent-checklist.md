---
source_type: markdown
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/build-cli-for-agent-checklist.md"
source_relpath: "Agent/build-cli-for-agent-checklist.md"
raw_created_at: 2026-04-18T07:22:15.688263+00:00
raw_modified_at: 2026-04-18T07:22:15.689050+00:00
raw_size: 10957
raw_fingerprint: "size=10957;birth=2026-04-18T07:22:15.688263+00:00;mtime=2026-04-18T07:22:15.689050+00:00"
raw_snapshot_at: 2026-05-29T22:03:59+00:00
ingested_at: 2026-05-30
status: ingested
---

# build-cli-for-agent-checklist.md

## Source

- Raw file: [Agent/build-cli-for-agent-checklist.md](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/build-cli-for-agent-checklist.md>)
- Raw ref: `raw:Agent/build-cli-for-agent-checklist.md`
- Type: markdown
- Status: ingested
- Raw metadata: created `2026-04-18T07:22:15.688263+00:00`; modified `2026-04-18T07:22:15.689050+00:00`; size `10957`; snapshot `2026-05-29T22:03:59+00:00`
- Coverage: full raw Markdown file read.

## Summary

这份 Markdown 是 agent-friendly CLI 设计清单，核心判断是 Agent 更像依赖确定性、结构化、可恢复、可自动化协议的机器用户，因此 CLI 需要把输出、错误、交互、重试、分页、认证和文档都设计成 Agent 可稳定调用的接口。

## Source Digest

document 从“Agent 不是更聪明的人类用户”出发，把 CLI 设计目标从人类终端体验转为 agent-facing protocol。P0 要求集中在可解析、不会挂住、可恢复和安全：所有数据命令应支持稳定 JSON/NDJSON；stdout 只承载结果，stderr 放诊断；非交互默认可运行；危险确认有显式绕过；退出码有语义；错误可行动；写操作幂等；破坏性动作有 dry-run；输入要防 hallucination；大输出要有边界。

P1/P2 把这些原则扩展成更完整的 Agent 操作面：字段裁剪、quiet/bare output、stdin/stdout pipeline、一致命令语法、渐进 help、机器可读 schema、raw JSON payload、成功输出可验证状态、conflict/transient/permanent error 分类、headless 认证、AGENTS/SKILL 文档、多 surface 共享核心、prompt injection 防护、agent readiness eval、CI 测 hang，以及版本化输出 schema。最小可落地版本把优先级收束到七件事：JSON 输出、stdout/stderr 分离、非交互/确认/dry-run、exit code 与结构化错误、list/get 限流裁剪、幂等或 conflict 检测、短 AGENTS/SKILL 调用规则。

## Key Claims

- explicit: Agent-friendly CLI 应该像小型协议，输入可验证、输出可解析、失败可恢复、动作可预演、重试不危险、响应不浪费 context、文档可被运行时发现。
- explicit: stdout 应作为 API contract，只放结果；stderr 用于日志、进度、warning、spinner 和人类消息。
- explicit: Agent/脚本/subagent 不能可靠处理交互式 prompt，因此 CLI 应支持非交互模式并在非 TTY 下禁用 prompt。
- explicit: 写操作应尽量幂等，破坏性操作应支持 `--dry-run`，避免 Agent retry/resume/replay 造成重复或破坏。
- explicit: 大响应会消耗 Agent context，因此默认输出应有 `--limit`、字段选择、分页或明确缩小查询路径。
- explicit: agent-facing 文档可以用 `AGENTS.md`、`CONTEXT.md`、`SKILL.md` 描述 invariants 和推荐调用方式。
- inferred: 这份 checklist 可以作为评估开发工具是否适合 Agent 自动化的验收标准，而不只是 CLI UX 建议。

## External Links

- source: [Writing CLI Tools That AI Agents Actually Want to Use](https://dev.to/uenyioha/writing-cli-tools-that-ai-agents-actually-want-to-use-39no) — checklist 整理来源之一；not verified.
- source: [Making your CLI agent-friendly](https://www.speakeasy.com/blog/engineering-agent-friendly-cli) — checklist 整理来源之一；not verified.
- source: [You Need to Rewrite Your CLI for AI Agents](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/) — checklist 整理来源之一；not verified.
- source: [7 Principles for Agent-Friendly CLIs](https://trevinsays.com/p/7-principles-for-agent-friendly-clis) — checklist 整理来源之一；not verified.

## Links

- compiled-concept: [[concepts/Agent-friendly CLI（ACI）|Agent-friendly CLI（ACI）]] — checklist 给出 ACI 的 P0/P1/P2 和最小可落地七件事，是该概念页核心证据。
- related: [[concepts/Agent 工具调用|Agent 工具调用]] — CLI 作为 agent-facing 工具接入协议的检查标准。
- related: [[concepts/Agent Harness|Agent Harness]] — CLI contract、非交互、安全默认值和可观测性可补充 harness 的工具面约束。
- related: [[concepts/Agent Skills|Agent Skills]] — source 明确建议用 `SKILL.md`/agent 文档描述调用准则。

## Maintenance Notes

- No issues. Full raw Markdown was read and digested.
- Compile candidates: Agent-friendly CLI, CLI as protocol, 结构化错误, 非交互 CLI, agent readiness eval, tool schema versioning.
