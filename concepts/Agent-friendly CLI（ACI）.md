---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 3
review_after: 2026-06-06
---

# Agent-friendly CLI（ACI）

## Definition

Agent-friendly CLI（也称 Agent-Computer Interface，ACI）是把命令行工具当作面向 Agent 的协议来设计：输出可解析、失败可恢复、动作可预演、重试不危险、文档可被运行时发现，而不是只服务于人类终端体验。

## Why It Matters

Agent 是「机器用户」，不是更聪明的人类用户。它不会读懂彩色 spinner、不会在交互提示前停下、会盲目重试。把 CLI 设计成确定性协议，是让 Agent 稳定调用真实开发工具的前提，也是 MCP 之外更省 token 的能力接入方式。

## Mental Model

把 CLI 想成一个 REST API：stdout 是响应体（只放结果），stderr 是日志通道，退出码是状态码，`--help` 是 OpenAPI 文档，`--dry-run` 是预检。Agent 靠这些稳定契约决定下一步。

## Key Claims

- 结构化输出是第一层契约：支持 `--json`/`--output json`，JSON 只写 stdout，进度/警告/动画写 stderr；增量结果用 JSON Lines。
- 退出码是 Agent 的控制流分支信号：区分成功、通用失败、参数错误、资源不存在、权限拒绝、冲突等情况。
- 命令应幂等，因为 Agent 会重试；破坏性操作需 `--dry-run`，并提供 `--yes`/`--force` 跳过确认，非 TTY 时自动处理或给清晰错误。
- 大响应会消耗上下文，需默认 `--limit`、字段裁剪、分页或缩小查询路径。
- `--help` 是 Agent 首先读取的工具描述，应含必填/选填、真实示例、JSON 标志和子命令发现路径。
- agent-facing 文档可用 `AGENTS.md`、`CONTEXT.md`、`SKILL.md` 描述 invariants 和推荐调用方式。
- `Agent 解构.xmind` 把这一方向放在工具接口演进里：从 API 封装 → ACI → Tool Search / Programmatic Tool Calling。

## Examples

- `build-cli-for-agent-checklist.md` 给出最小可落地七件事：JSON 输出、stdout/stderr 分离、非交互/确认/dry-run、exit code 与结构化错误、list/get 限流裁剪、幂等或冲突检测、短 AGENTS/SKILL 调用规则。
- 结构化错误输出包含可解析错误码、失败输入、建议下一步，并区分临时错误与永久错误，让 Agent 决定重试、换路径还是停止。

## Common Confusions

- ACI 不只是「加个 `--json`」；它是一整套输入校验、错误语义、恢复和发现机制。
- ACI 与 [[entities/Model Context Protocol|Model Context Protocol]] 不冲突：CLI 更省 token（工具定义不必每轮注入），MCP 提供统一协议接入，二者是工具接入的不同形态。
- 「人类用着顺手」不等于「Agent 用着稳」；交互式确认、彩色输出、模糊错误对 Agent 都是坑。

## Evidence

- [[sources/Agent/Build CLI For Agent.xmind|Build CLI For Agent.xmind]]
- [[sources/Agent/build-cli-for-agent-checklist|build-cli-for-agent-checklist]]
- [[sources/Agent/Agent 解构.xmind|Agent 解构.xmind]]

## Relations

- part-of: [[concepts/Agent 工具调用|Agent 工具调用]]
- related: [[concepts/Agent Harness|Agent Harness]]
- contrasts-with: [[entities/Model Context Protocol|Model Context Protocol]]
- related: [[entities/Agent Client Protocol|Agent Client Protocol]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: CLI-Anything
- entity-candidate: opencli

## My Understanding

当前理解：给 Agent 用的 CLI，本质是一个小协议——稳定可解析的输出、有语义的退出码、幂等和 dry-run、可被运行时发现的 help，缺一个 Agent 就会卡住或闯祸。

## Review Questions

- 为什么 stdout 只能放结果，其他信息要进 stderr？
- 退出码对 Agent 起什么作用？
- ACI 相比 MCP 在 token 成本上的优势是什么？

## Open Questions

- 标准化的 agent-facing CLI schema（如版本化输出契约）还缺少业界统一规范。
