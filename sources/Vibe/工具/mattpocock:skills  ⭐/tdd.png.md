---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/工具/mattpocock:skills  ⭐/tdd.png"
source_relpath: "Vibe/工具/mattpocock:skills  ⭐/tdd.png"
raw_created_at: 2026-05-05T12:33:36.742206+00:00
raw_modified_at: 2026-05-05T12:33:36.742876+00:00
raw_size: 1872058
raw_fingerprint: "size=1872058;birth=2026-05-05T12:33:36.742206+00:00;mtime=2026-05-05T12:33:36.742876+00:00"
raw_snapshot_at: 2026-05-29T16:07:40+00:00
ingested_at: 2026-05-30
status: ingested
---

# tdd.png

## Source

- Raw file: [Vibe/工具/mattpocock:skills  ⭐/tdd.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E5%B7%A5%E5%85%B7/mattpocock%3Askills%20%20%E2%AD%90/tdd.png>)
- Raw ref: `raw:Vibe/工具/mattpocock:skills  ⭐/tdd.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T12:33:36.742206+00:00`; modified `2026-05-05T12:33:36.742876+00:00`; size `1872058`; snapshot `2026-05-29T16:07:40+00:00`
- Coverage: Vision ingest of the full 864x1821 vertical infographic; readable headings, workflow blocks, warning panels, and bottom principle strip were inspected.

## Summary

这张图把 TDD 表达为“按用户可见行为垂直切片”的循环：先选一个可观察行为，写失败测试，再用最小实现通过测试，随后在绿灯保护下重构并进入下一个行为。它强调测试应像规格说明，验证公开接口和可观察结果，而不是绑定内部结构。

## Source Digest

图中核心不是泛化的“先测后写”，而是把 TDD 约束到可交付行为的开发节奏。左侧对比了错误方式和正确方式：错误方式是先横向写满测试再写实现；正确方式是一个行为完整跑通后再推进下一个行为，因此每一步都能看到面向用户的价值。中间环路将 Red-Green-Refactor 串成可重复闭环，要求红灯阶段只写一个失败断言，绿灯阶段只写必要代码，重构阶段只改善设计且不改变行为。

右侧和下方把测试质量边界讲清楚：好测试通过公开接口、可观察行为和一个逻辑断言来表达规格；坏信号包括 mock 内部协作者、测试 private 方法、断言调用次数或顺序、绕过接口查数据库，以及把测试名写成 HOW 而不是 WHAT。图中还提出 “Deep module” 模型：测试应依赖小而清晰的公开接口，允许内部策略、缓存、算法、校验等复杂实现自由重构。Mock 只适合系统边界，例如外部 API、数据库、文件系统、时间和随机性；内部协作用真实实现。

## Key Claims

- explicit: TDD 的垂直切片应从一个用户可见行为出发，而不是先按内部结构横向铺测试。
- explicit: 好测试验证公开接口、可观察行为，像规格说明，并能承受重构。
- explicit: mock 应放在系统边界；内部协作者优先使用真实实现。
- explicit: 环测试信号包括测试 private 方法、mock 内部协作者、断言调用次数或顺序、绕过接口查数据库、测试名描述 HOW 而不是 WHAT。
- explicit: Red-Green-Refactor 循环要求一次只做一件事：让测试失败、最快通过、持续重构、保持简洁接口。
- inferred: 该图把 TDD 的主要价值定义为设计反馈和行为安全网，而不是覆盖率或测试数量。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/垂直切片 TDD|垂直切片 TDD]] — 可沉淀 Red-Green-Refactor、公开接口测试、mock 边界和 deep module 测试面。
- map-entry candidate: [[maps/Vibe Coding 工作流学习地图|Vibe Coding 工作流学习地图]] — 可作为实现阶段的测试驱动开发节点。

## Maintenance Notes

- Vision-based ingest; exact icon labels and small captions should be rechecked against the raw image if used verbatim.
- No index/log updates were made because this batch worker was restricted to the five source notes only.
