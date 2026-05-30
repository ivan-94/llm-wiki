---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Agent/Build CLI For Agent.xmind"
source_relpath: "Agent/Build CLI For Agent.xmind"
raw_created_at: 2026-04-10T08:22:56.089419+00:00
raw_modified_at: 2026-04-18T07:19:14.259382+00:00
raw_size: 452545
raw_fingerprint: "size=452545;birth=2026-04-10T08:22:56.089419+00:00;mtime=2026-04-18T07:19:14.259382+00:00"
raw_snapshot_at: 2026-05-29T22:03:22.815154+00:00
ingested_at: 2026-05-30
status: ingested
---

# Build CLI For Agent.xmind

## Source

- Raw file: [Agent/Build CLI For Agent.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Agent/Build%20CLI%20For%20Agent.xmind>)
- Raw ref: `raw:Agent/Build CLI For Agent.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-04-10T08:22:56.089419+00:00`; modified `2026-04-18T07:19:14.259382+00:00`; size `452545`; snapshot `2026-05-29T22:03:22.815154+00:00`
- Coverage: exported and digested 2 sheets: `画布 1`, `checklist`.

## Summary

这是一份面向 Agent 的 CLI 设计清单，主张 CLI 应把 stdout/stderr、结构化输出、退出码、幂等性、帮助文本、可组合性、非交互执行、错误语义和命令语法都设计成 Agent 可解析、可重试、可发现的接口。第二个 sheet `checklist` 只包含占位分支，没有提供实质检查项。

## Source Digest

这份 source 把 CLI 视为 Agent-Computer Interface，而不是只给人类看的命令行。核心要求是让 Agent 能稳定解析结果、判断下一步、组合命令、重试失败并发现能力。结构化输出是第一层契约：支持 `--json` 或 `--output json`，JSON 只写 stdout，进度、警告、加载动画都写 stderr；输出尽量扁平、类型稳定，增量结果用 JSON Lines。

控制流层面，退出码被设计成 Agent 的分支信号：0 表示成功，1 是通用失败，2 是参数错误，3 是资源不存在，4 是权限拒绝，5 是冲突。它还要求结构化错误输出包含可解析错误代码、失败输入、建议下一步，并区分临时错误与永久错误，这样 Agent 才能决定重试、换路径还是停止。

操作语义上，source 强调幂等、可组合和非交互。因为 Agent 会重试，`create` 类命令不能因资源已存在而迫使 Agent 写特殊异常逻辑；批量操作、stdin 输入、`--quiet` 裸值输出和 selector 删除能减少循环调用；`--dry-run` 必须输出结构化结果，`--yes`、`--no-confirm`、`--force` 用于跳过确认，非 TTY 时要自动处理或给出清晰错误。

发现与学习层面，`--help` 被视为工具描述、参数规范和使用指南，必须清晰标注必填/选填、提供真实示例、记录 JSON 标志，并通过子命令 help 支持能力发现。命令形态应使用一致的名词-动词语法，让 Agent 可以从模式中推断功能。

## Key Claims

- explicit: Agent 友好的 CLI 应支持结构化输出，并保持 stdout 只承载 API 契约，其他信息进入 stderr。
- explicit: JSON 输出应尽量扁平、类型稳定，增量输出适合使用 JSON Lines。
- explicit: 退出码是 Agent 的控制流，应该把成功、参数错误、资源不存在、权限拒绝、冲突等情况区分开。
- explicit: CLI 命令应该幂等，因为 Agent 会重试，网络和进程也可能中断。
- explicit: `--help` 是 Agent 首先读取的工具描述，应包含必填/选填、示例、JSON 标志和子命令发现路径。
- explicit: `--dry-run`、确认跳过选项和非交互终端检测是 Agent 自动化执行的必要边界。
- inferred: 这份 source 可直接支撑“Agent 友好 CLI”或“Agent-Computer Interface”概念页，并可转成工程检查清单。

## External Links

- extended-reading: [Writing CLI Tools That AI Agents Actually Want to Use](https://dev.to/uenyioha/writing-cli-tools-that-ai-agents-actually-want-to-use-39no) - source 中列为扩展阅读；not verified.
- extended-reading: [Making your CLI agent-friendly](https://www.speakeasy.com/blog/engineering-agent-friendly-cli) - source 中列为扩展阅读；not verified.
- extended-reading: [You Need to Rewrite Your CLI for AI Agents](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/) - source 中列为扩展阅读；not verified.
- extended-reading: [7 Principles for Agent-Friendly CLIs](https://x.com/trevin/status/2037250000821059933) - source 中列为扩展阅读；not verified.
- library: [CLI-Anything](https://github.com/HKUDS/CLI-Anything) - source 中列为相关库；not verified.
- library: [opencli](https://github.com/jackwener/opencli) - source 中列为相关库；not verified.

## Links

- compiled-concept: [[concepts/Agent-friendly CLI（ACI）|Agent-friendly CLI（ACI）]] - source 把结构化输出、退出码、幂等、dry-run 和 help 文档编译为 ACI 设计原则，是该概念页核心证据。
- compiled-concept: [[concepts/Agent 工具调用|Agent 工具调用]] - source 补充 CLI 作为 Agent 工具接入形态。
- compiled-synthesis: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]] - source 支撑 Agent 系统工程中的工具契约与执行反馈。
- related: [[concepts/Agentic Engineering|Agentic Engineering]] - source 给出 Agent 可操作工具接口的工程约束。
- related: [[concepts/Agent Harness|Agent Harness]] - CLI 退出码、结构化错误、dry-run 和非交互控制可作为执行边界与反馈信号。
- related: [[entities/Agent Client Protocol|Agent Client Protocol]] - source 与 Agent 工具协议和 ACI 方向高度相关，但讨论对象是 CLI 而不是具体协议。

## Maintenance Notes

- Sheet `checklist` only contains placeholder branches `分支主题 1` through `分支主题 4`; no actionable checklist content was available there.
- No external links were browsed or verified during ingest.

- Link cleanup candidate: entity-candidate: CLI-Anything - raw 仅列为库链接，待后续补充用途和成熟度。.
- Link cleanup candidate: entity-candidate: opencli - raw 仅列为库链接，待后续补充用途和成熟度。.
