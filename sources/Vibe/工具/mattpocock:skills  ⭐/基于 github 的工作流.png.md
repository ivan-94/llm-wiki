---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png"
raw_created_at: 2026-05-06T03:56:58.984008+00:00
raw_modified_at: 2026-05-06T03:56:58.984253+00:00
raw_size: 1770551
raw_fingerprint: "size=1770551;birth=2026-05-06T03:56:58.984008+00:00;mtime=2026-05-06T03:56:58.984253+00:00"
raw_snapshot_at: 2026-05-29T16:13:05+00:00
ingested_at: 2026-05-29
status: ingested
---

# 基于 github 的工作流.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/%E5%9F%BA%E4%BA%8E%20github%20%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/基于 github 的工作流.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-06T03:56:58.984008+00:00`; modified `2026-05-06T03:56:58.984253+00:00`; size `1770551`; snapshot `2026-05-29T16:13:05+00:00`
- Coverage: vision inspection of full 1536x1024 PNG; layer structure, state machine, runner strategy, feedback loops, and warning banner were read.

## Summary

这张图把 GitHub Issues 定义为 Agent 开发闭环的任务队列、状态机、交接合同和反馈总线，而不是单纯记录工具；流程覆盖需求/规格、Issue 队列、Triage/Grooming、Agent Runner 执行、PR/CI/Review 反馈。

## Source Digest

图按五层组织工作流。需求与规格层先从 conversation、头脑风暴和问题/机会点生成 PRD issue，再用 `/to-issues` 拆成最小可交付、独立、可验证、可迭代的 slice issue。GitHub Issue 队列层把 PRD issue 与 slice issue 放入中央状态机，labels 从 `unlabelled`、`needs-triage` 流向 `needs-info`、`ready-for-agent`、`ready-for-human` 或 `wontfix`。

Triage/Grooming 层通过 `/triage` 做价值评估、范围与影响判断、可行性判断、上下文补充、标签与路由，最终为 ready-for-agent 生成 Agent Brief 作为交接合同。Agent Runner 层通过 gh CLI 领取 ready-for-agent、读取 issue comments、锁定 agent-active 或评论锁、创建工作分支，然后读 Brief 和代码库、执行测试/类型检查/lint/diagnose/tdd，产出 commits、branch、PR 和 run logs。PR/CI/Review 层处理 CI、人工 review、合并、关闭 issue；失败回流会通过评论、标签和下一轮 agent 或人工处理回到 issue 状态机。

## Key Claims

- explicit: GitHub 在该流程中不是只做记录，而是承担任务队列、状态机、交接合同和反馈总线。
- explicit: PRD issue、slice issues、labels、Agent Brief comments、branch 和 commits 是中间产物；PR、CI result、review comments、merged code、closed issue、out-of-scope record 是输出。
- explicit: `ready-for-agent` 对应可交给 Agent 执行，`ready-for-human` 对应需要人类判断/权限/设计，`wontfix` 对应明确不做并沉淀原因。
- explicit: 真正的自动领取、锁定、重试和开 PR 需要额外的 Agent Runner 实现；mattpocock/skills 提供的是任务协议与手动/半自动工作流。
- inferred: Agent Brief 是该流程的关键契约层，用于把当前行为、期望行为、关键接口、验收标准、out of scope 和不依赖弱信号的原则固定下来。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: GitHub Issue 状态机 — 本图提供 labels、状态流转、失败回流与成功闭环。
- compiled-concept: Agent Brief 交接合同 — 本图把 Brief 明确为 Agent 可接手的交付契约。
- compiled-synthesis: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — 候选综合；本图可作为 GitHub Issues 工作流的核心证据。

## Maintenance Notes

- 未修改 index/log 或实际创建 compile 页面；上述 Links 是候选关系。
- 右下角重要提示明确指出 mattpocock/skills 只提供任务协议与手动/半自动工作流，自动领取/锁定/重试/开 PR 需要额外 Runner。
