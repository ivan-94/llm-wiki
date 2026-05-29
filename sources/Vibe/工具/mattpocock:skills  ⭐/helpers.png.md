---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/helpers.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/helpers.png"
raw_created_at: 2026-05-05T12:53:19.522886+00:00
raw_modified_at: 2026-05-05T12:53:19.523438+00:00
raw_size: 1883374
raw_fingerprint: "size=1883374;birth=2026-05-05T12:53:19.522886+00:00;mtime=2026-05-05T12:53:19.523438+00:00"
raw_snapshot_at: 2026-05-30T00:07:20+08:00
ingested_at: 2026-05-30
status: ingested
---

# helpers.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/helpers.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/helpers.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/helpers.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:53:19.522886+00:00`; modified `2026-05-05T12:53:19.523438+00:00`; size `1883374`; snapshot `2026-05-30T00:07:20+08:00`
- Coverage: Vision read of a 1024 x 1536 infographic. Four helper skill panels and the bottom principle row are readable; package names and command names are recorded only where visually clear.

## Summary

这张图汇总 repo helper skills：`git-guardrails-claude-code`、`setup-pre-commit`、`migrate-to-shoehorn`、`scaffold-exercises`。它把这些 skill 归类为安全、钩子、测试数据和课程脚手架，并强调自动化流程必须可重复、可审计、带验证，不覆盖已有配置，倾向小步提交和及时验证。

## Source Digest

图以四宫格呈现工程仓库辅助 skill。`git-guardrails-claude-code` 通过 Claude Code `PreToolUse` hook 阻止危险 git 操作，示例包括 `git push`、`git reset --hard`、`git clean -f/-fd`、`git branch -D`、`git checkout .`、`git restore .`，流程包含选择 project/global 作用域、复制脚本、合并 `settings.json`、赋执行权限、用 JSON 输入验证拦截。`setup-pre-commit` 使用 Husky、lint-staged、Prettier、typecheck 和 tests 构建提交前链路。`migrate-to-shoehorn` 只在测试代码中把类型断言替换为 `fromPartial()`、`fromAny()`、`fromExact()`，用来减少假通过并提升测试数据表达。`scaffold-exercises` 生成课程练习目录，强调命名、禁止空占位文件、禁止坏链接、必要时 `main.ts` 通过运行。底部总原则把 helper skill 定位为脚本化、验证不可省、尊重已有配置、小步提交。

## Key Claims

- explicit: `git-guardrails-claude-code` 的目标是通过 Claude Code PreToolUse hook 阻止危险 git 操作。
- explicit: `setup-pre-commit` 的目标是用 Husky、lint-staged、Prettier、typecheck 和 tests 让提交更干净。
- explicit: `migrate-to-shoehorn` 的迁移范围是 tests only，生产代码禁用 `fromPartial()` / `fromAny()` 等测试数据 helper。
- explicit: `scaffold-exercises` 要生成规范练习目录与基础文件，并运行 lint 作为最终验证。
- inferred: 这组 helper skills 共同服务于“降低 agent 误操作和重复劳动”的仓库治理目标。

## External Links

No external links found in extracted content.

## Links

- related: Agent 仓库治理 Skills — 可整合安全护栏、提交钩子、测试数据迁移和脚手架生成的仓库级辅助模式。
- related: Vibe 工具与 Agent Skills 学习地图 — 可作为 mattpocock skills 中“repo helper”分支。

## Maintenance Notes

- 图片整体可读；部分小字如包名和文件名只在高置信可见时纳入，未逐字 OCR。
- 图中提到的工具行为未实际运行验证，当前 note 仅反映图片表达。
