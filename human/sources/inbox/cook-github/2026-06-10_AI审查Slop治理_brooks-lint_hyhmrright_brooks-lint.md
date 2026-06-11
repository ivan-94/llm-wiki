---
source_type: human_markdown
source_origin: human
raw_path: "human/raw/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint.md"
source_relpath: "inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint.md"
raw_created_at: 2026-06-10T12:18:50+08:00
raw_modified_at: 2026-06-10T15:49:02+08:00
raw_size: 16764
raw_fingerprint: "size=16764;birth=2026-06-10T12:18:50+08:00;mtime=2026-06-10T15:49:02+08:00"
raw_snapshot_at: 2026-06-11T09:55:10+08:00
ingested_at: 2026-06-11
status: ingested
---

# brooks-lint：AI 审查 Slop 治理

## Source

- Human raw: [[human/raw/inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint|brooks-lint：AI 审查 Slop 治理]]
- Raw ref: `human-raw:inbox/cook-github/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint.md`
- Type: human_markdown
- Status: ingested
- Raw metadata: created `2026-06-10T12:18:50+08:00`; modified `2026-06-10T15:49:02+08:00`; size `16764`; snapshot `2026-06-11T09:55:10+08:00`
- Coverage: full Markdown note read; embedded infographic is recorded as a raw attachment path but not copied or independently ingested.

## Source Cluster

- Directory cluster: `human/raw/inbox/cook-github`
- Cluster role: tool
- Neighbor sources:
  - same-cluster: [[human/sources/inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill|近30天多源研究技能]] — 同为 GitHub skill/tool cook；分别展示研究管线和审查治理管线。
  - same-cluster: [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — 同属 agent skill/plugin 仓库案例；brooks-lint 更聚焦质量门和 eval。
  - related: [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — brooks-lint 是 Anthropic skill 分类里 code quality/review 的具体反 slop 实践。

## Summary

这份 GitHub cook note 消化了 `hyhmrright/brooks-lint`：一组面向 Claude、Codex、Gemini 等 coding agent 的 AI 代码审查 skills。它把审查 slop 从“模型品味问题”转成固定 taxonomy、Iron Law 证据链、false-positive guard、eval 和 validator 问题。

## Source Digest

本 source 对 [[concepts/AI 代码垃圾治理|AI 代码垃圾治理]] 的贡献，是把 DeSlop 从代码库产物治理扩展到“审查输出治理”。brooks-lint 治理的不是 AST 规则，而是 AI review 本身的泛泛建议、漂浮引用、误报和漂移。它要求每个 finding 遵守 `Symptom -> Source -> Consequence -> Remedy`，用 R1-R6 / T1-T6 稳定词表约束风险命名，并为每类风险写 `What Not to Flag`。

它也补强 [[concepts/Agent Skills|Agent Skills]]：skill 可以承载审查协议、书目原则、模式 guide、report template、eval runner 和 repo validator。交互式 skill、CI review 和 live eval 共用同一个 prompt assembly，说明高质量 skill 需要把“给模型看的说明”和“给系统跑的验证”接到同一规则源。

对 [[concepts/Skill 触发契约|Skill 触发契约]] 的启发是：触发正确只是开始，真正防 slop 的是触发后强制扫描步骤、输出字段、严重度阈值、clean case 和 repo 自检。它不是确定性静态分析器；它降低 slop，而不是消灭 slop。

## Key Claims

- explicit: brooks-lint 把 AI code review 的泛泛建议、假引用、误报和漂移作为治理对象。
- explicit: Iron Law 要求每个 finding 必须遵守 `Symptom -> Source -> Consequence -> Remedy`，不得先给 fix 再补诊断。
- explicit: 项目定义 R1-R6 生产代码衰退风险和 T1-T6 测试衰退风险，并为每类风险写 `What Not to Flag`。
- explicit: `assemble-prompt.mjs` 同时供 CI review 和 live eval 使用，避免交互式 skill 与自动评测规则源分叉。
- explicit: evals 包含正例和 clean case，validator 检查 skill、README、manifest、guide 和 eval 是否同步。
- inferred: AI 审查质量门应同时奖励发现问题和“不该说话时闭嘴”，否则会把误报 slop 包装成严肃审查。
- inferred: DeSlop 工具链需要将模型 rubrics、机械验证、clean eval 和 human review 组合，而不是依赖单个 linter。

## External Links

- GitHub repository: https://github.com/hyhmrright/brooks-lint — raw note input repository at commit `0e92503911f28ff091b14c017d4345f7a2dd8817`; not verified during this ingest.

## Links

- compiled-concept: [[concepts/AI 代码垃圾治理|AI 代码垃圾治理]] — 补充 AI review slop、Iron Law、false-positive guard 和 clean eval 治理。
- compiled-concept: [[concepts/Agent Skills|Agent Skills]] — 补充 code quality/review skill 的协议化案例。
- compiled-concept: [[concepts/Skill 触发契约|Skill 触发契约]] — 补充触发后扫描步骤、输出模板和 eval/validator 边界。
- compiled-synthesis: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 补充 L4 Evidence / L5 Learning 中审查质量门的具体工具案例。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 作为 code quality/review skill 案例进入工具索引。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 作为 DeSlop 和 evidence gate 案例进入学习路径。
- same-cluster: [[human/sources/inbox/cook-github/2026-06-09_近30天多源研究技能_mvanhorn_last30days-skill|近30天多源研究技能]] — 同为 GitHub skill/tool 案例，分别服务研究和审查。
- same-cluster: [[human/sources/inbox/cook-github/2026-06-01_Harness团队架构工厂_revfactory_harness|Harness 团队架构工厂]] — 同属 agent skill/plugin 仓库案例。
- related: [[human/sources/inbox/cook-blog/2026-06-05_Claude_Code团队如何使用技能_Anthropic|Claude Code 团队如何使用技能]] — 该 source 可作为 Anthropic code quality/review skill 分类的具体案例。

## Maintenance Notes

- 原文信息图位于 `human/raw/inbox/cook-github/assets/2026-06-10_AI审查Slop治理_brooks-lint_hyhmrright_brooks-lint/infographic.webp`，本次未复制到 `assets/`。
- `brooks-lint` 作为工具/项目实体候选保留；当前只静态阅读一次，先不建独立实体页。
- 未运行 live eval、repo validator、CI review 或仓库测试；当前判断来自静态阅读。
