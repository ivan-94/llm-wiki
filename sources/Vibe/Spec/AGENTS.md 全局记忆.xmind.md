---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Spec/AGENTS.md 全局记忆.xmind"
source_relpath: "Vibe/Spec/AGENTS.md 全局记忆.xmind"
raw_created_at: 2025-09-29T08:03:08.924959+00:00
raw_modified_at: 2025-10-27T01:39:56.298444+00:00
raw_size: 577078
raw_fingerprint: "size=577078;birth=2025-09-29T08:03:08.924959+00:00;mtime=2025-10-27T01:39:56.298444+00:00"
raw_snapshot_at: 2026-05-29T15:53:29.538642+00:00
ingested_at: 2026-05-29
status: ingested
---

# AGENTS.md 全局记忆.xmind

## Source

- Raw file: [Vibe/Spec/AGENTS.md 全局记忆.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Spec/AGENTS.md%20%E5%85%A8%E5%B1%80%E8%AE%B0%E5%BF%86.xmind>)
- Raw ref: `raw:Vibe/Spec/AGENTS.md 全局记忆.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2025-09-29T08:03:08.924959+00:00`; modified `2025-10-27T01:39:56.298444+00:00`; size `577078`; snapshot `2026-05-29T15:53:29.538642+00:00`
- Coverage: helper exported and read all `1` sheet: `AGENTS.md 全局记忆`.

## Summary

这份 XMind 是一张 AGENTS.md/全局 Prompt 设计清单，覆盖启动环境、项目架构、验证链路、约定模式、安全围栏、构建部署、行为引导、变更范围、工作流程、异常处理、Checklist、外部案例与迭代建议。核心观点是把 AGENTS.md 当作给 LLM 的项目级提示语和记忆入口，但要保持聚焦、结构清晰、可拆分、可演进。

## Source Digest

该 source 将 AGENTS.md 视为 Agent 协作中的“全局记忆”和项目入口。它要求把依赖安装、系统依赖、环境变量、虚拟环境、数据库迁移、服务启动、目录结构、monorepo 局部规则、技术栈、测试/lint/format/集成测试命令、文件级验证、API/日志/git/命名规范、安全边界、构建部署和回滚流程等项目事实显式化，从而减少 Agent 的猜测和工具调用。

资料同时强调 AGENTS.md 的提示语属性：应规定响应语言、变更范围、禁止编辑区域、工作流、异常处理和提交前 checklist。好的规则要像 Prompt 一样写，聚焦、无歧义、结构清晰，不宜过长；可以给 few-shot 示例、反例和链接。对于大型项目，应通过拆分文件和局部 AGENTS.md 实现渐进式披露，让全局文件提供入口而不是承载所有百科知识。

这份资料适合编译“Agent 全局记忆”“AGENTS.md 设计模式”“Agent 项目入口文档”等概念，也能和 Harness Engineering 中“AGENTS.md 作为目录而非百科全书”的观点互相支撑。

## Key Claims

- explicit: AGENTS.md 应记录启动和环境信息，包括依赖安装、准备工作、系统依赖、环境变量、虚拟环境、数据库迁移和服务启动方式。
- explicit: AGENTS.md 应提供目录结构、模块架构、技术栈和 monorepo 局部规则，帮助 Agent 减少猜测和无效工具调用。
- explicit: 验证链路应包含单元测试、lint、format、集成测试、文件级命令、mock、TDD 和测试组织方式。
- explicit: 项目约定应覆盖命名、git、REST/API、版本策略、错误格式、鉴权、日志、异常处理和前端组件风格。
- explicit: 全局 Prompt 可以规定响应语言、变更范围、禁止编辑文件、具体工作流和异常处理策略。
- explicit: AGENTS.md 应像 Prompt 一样编写：聚焦、无歧义、结构清晰、避免过长、提供示例和反例。
- explicit: 当规则过长时，应拆分文件或使用目录级 AGENTS.md 做级联规则。
- inferred: AGENTS.md 的高价值不在于“规则越多越好”，而在于把最常用、最容易出错、最影响验证的项目知识变成 Agent 可直接消费的入口。

## External Links

- reference: [Golden Testing Rules for AI](https://github.com/goldbergyoni/golden-testing-rules-for-ai) — source 中作为 AI 单元测试和端到端测试最佳实践参考；not verified.
- reference: [codex AGENTS.md](https://github.com/openai/codex/blob/main/AGENTS.md) — source 案例；not verified.
- reference: [Dify AGENTS.md](https://github.com/langgenius/dify/blob/main/AGENTS.md) — source 案例；not verified.
- reference: [LangChain AGENTS.md](https://github.com/langchain-ai/langchain/blob/master/AGENTS.md) — source 案例与 checklist 参考；not verified.
- reference: [CPython AGENTS.md](https://github.com/python/cpython/blob/e8a8f39971493fc6f7009e188eeb9921cc74b115/AGENTS.md) — source 案例；not verified.
- reference: [Kiro Steering](https://kiro.dev/docs/steering/) — source 参考；not verified.
- reference: [Cursor Rules](https://cursor.com/docs/context/rules) — source 参考；not verified.
- reference: [AGENTS.md](https://agents.md/) — source 参考；not verified.
- reference: [Improve your AI code output with AGENTS.md](https://www.builder.io/blog/agents-md?utm_source=x&utm_campaign=agents-md&utm_content=ss) — source 参考；not verified.

## Links

- compiled-concept: AGENTS.md — 本 source 提供项目入口、全局记忆、验证链路和规则拆分的设计清单。
- compiled-concept: Agent 全局记忆 — 资料强调把项目事实和协作偏好外化为 Agent 可读记忆。
- compiled-concept: Agent 项目验证链路 — 资料列出测试、lint、format、集成测试和文件级命令。
- map-entry: Vibe Spec 学习地图 — 适合作为 Spec/规则类资料的基础节点。

## Maintenance Notes

- helper `export_xmind_source.py` 返回 `ok: true`、`sheets_error: ""`，无 sheet 缺失。
- 外部案例链接未联网核验；已按 raw 可见 URL 记录并标注 `not verified`。
- 该 source 是设计清单型材料，部分节点是占位提示而非完整操作规范。
