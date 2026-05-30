---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/diagnose.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/diagnose.png"
raw_created_at: 2026-05-05T12:32:06.753685+00:00
raw_modified_at: 2026-05-05T12:32:06.754339+00:00
raw_size: 1834863
raw_fingerprint: "size=1834863;birth=2026-05-05T12:32:06.753685+00:00;mtime=2026-05-05T12:32:06.754339+00:00"
raw_snapshot_at: 2026-05-29T16:07:00+00:00
ingested_at: 2026-05-30
status: ingested
---

# diagnose.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/diagnose.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/diagnose.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/diagnose.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:32:06.753685+00:00`; modified `2026-05-05T12:32:06.754339+00:00`; size `1834863`; snapshot `2026-05-29T16:07:00+00:00`
- Coverage: opened with Agent vision; full infographic inspected; dimensions `1024x1536`; visible text is clear enough for source note.

## Summary

这张图把 `/diagnose` 描述为困难 bug 的诊断闭环：没有快速、确定、可重复的失败信号时，不要凭感觉修。流程以建立反馈环为最高优先级，然后复现用户问题、提出 3-5 个可证伪假设、一次只改一个变量插桩验证、修复根因，并通过回归测试确认闭环变绿。

## Source Digest

图的中心是一个从红到绿的 6 步循环：先发现症状，再建立可重复失败信号；然后最小步骤复现用户描述的问题；接着提出 3-5 个可验证假设并写出预测；随后一次只改变一个变量，通过插桩、日志或观察结果验证假设；找到根因后做最小修复；最后回归测试，确保失败信号消失、通过信号稳定、覆盖关键路径并重复多次通过。

左侧把反馈环按优先级排序：失败测试最好，其次是 HTTP/curl 脚本、CLI 调用、浏览器脚本、trace replay、最小 harness、fuzz/property、bisect、差分对比和 HITL 脚本。选择原则是越快越好、越确定越好、脱离人工越好、成本越低越好。右侧强调每一步都要确认：症状匹配用户问题、复现率足够高、假设有预测、探针对应假设、修复后旧循环变绿。底部给出无法建立循环时的应急策略：说明卡点、向用户索要 HAR/抓包/完整日志/报错栈/上下文、请求复现环境和权限，或临时 instrumentation；但仍坚持先验证、后修复、小步快跑和勤验证。

## Key Claims

- explicit: 困难 bug 诊断的前提是建立快速、确定、可重复的失败信号；否则不要凭感觉修。
- explicit: `/diagnose` 的核心流程包括建立反馈环、复现用户问题、提出 3-5 个可证伪假设、一次只改一个变量插桩验证、修复根因、回归测试防复发。
- explicit: 反馈环优先级从失败测试、HTTP/curl 脚本、CLI 调用、浏览器脚本，到 trace replay、最小 harness、fuzz/property、bisect、差分对比和 HITL 脚本。
- explicit: 每一步都需要确认症状匹配、复现率足够高、假设有预测、探针对应假设、修复后旧循环变绿。
- explicit: 无法建立循环时，应说明卡点并索要证据、访问、临时 instrumentation 或复现环境。
- inferred: 这张图适合支撑“反馈环优先”的调试方法论，也可作为 Agent HAT/CI/浏览器验收中构造可重复失败信号的依据。

## External Links

No external links found in extracted content.

## Links

- related: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 可提炼困难 bug 诊断的六阶段纪律和红绿反馈标准。
- related: [[concepts/Agent 反馈回路|Agent 反馈回路]] — 可补充失败信号、复现率、确定性和成本排序。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 可作为 bug 诊断和调试 skill 主题入口。

## Maintenance Notes

- 图片视觉清晰；没有明显 URL。
- 图中是方法论流程，不等同于某个仓库的具体诊断脚本；后续 compile 时应把它作为调试策略证据，而不是操作命令清单。
