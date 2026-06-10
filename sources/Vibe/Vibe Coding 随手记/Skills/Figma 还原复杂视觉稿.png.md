---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/Skills/Figma 还原复杂视觉稿.png"
source_relpath: "Vibe/Vibe Coding 随手记/Skills/Figma 还原复杂视觉稿.png"
raw_created_at: 2026-06-10T08:42:40.273647+00:00
raw_modified_at: 2026-06-10T08:42:40.273921+00:00
raw_size: 2002002
raw_fingerprint: "size=2002002;birth=2026-06-10T08:42:40.273647+00:00;mtime=2026-06-10T08:42:40.273921+00:00"
raw_snapshot_at: 2026-06-10T13:15:09+00:00
ingested_at: 2026-06-10
status: ingested
---

# Figma 还原复杂视觉稿.png

## Source

- Raw file: [Vibe/Vibe Coding 随手记/Skills/Figma 还原复杂视觉稿.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/Skills/Figma%20%E8%BF%98%E5%8E%9F%E5%A4%8D%E6%9D%82%E8%A7%86%E8%A7%89%E7%A8%BF.png>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/Skills/Figma 还原复杂视觉稿.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-06-10T08:42:40.273647+00:00`; modified `2026-06-10T08:42:40.273921+00:00`; size `2002002`; snapshot `2026-06-10T13:15:09+00:00`
- Coverage: opened with Agent vision; full 1024x1536 infographic inspected; visible Chinese/English labels are clear.

## Source Cluster

- Directory cluster: Vibe/Vibe Coding 随手记/Skills
- Cluster role: tool
- Neighbor sources:
  - same-cluster: no existing mirrored source notes in this raw directory before this ingest; this image currently acts as the directory entry point.
  - toolchain-neighbor: [[sources/Vibe/工具/mattpocock:skills  ⭐/visual-fidelity-loop.png|visual-fidelity-loop.png]] — 两者都处理视觉稿还原和 diff 验证；本图更偏 Figma template restoration 的工程化步骤。

## Summary

这张图把“Figma 视觉稿还原为可维护 HTML 日记模板”整理成一套证据链优先的工作流。核心不是凭感觉像不像，而是先锁定基准、标注画布、人工确认、制定开发计划，再用截图和 visual diff 循环收敛。

## Source Digest

图中把输入拆成 Figma 节点、截图、参考模板和 `TEMPLATE_DEVELOPMENT.md`，再要求建立不可覆盖的 `reference_image`、用 393px 到 rem 的缩放基准，以及先于 diff 生成的 `sections.json`。主工作流共 10 步：探索上下文、建立基准、标注画布、写 `annotation.md`、人工审核标注、制定开发计划、下载与校验素材、实现模板、准备 preview、视觉 diff 循环。

质量闸门强调“标注未确认不得写代码”“计划未确认不得实现”“素材异常先请求补充”“未经审核不得新增变量模式”。Diff loop 的不变量是每轮修复必须对应具体差异，避免凭感觉接近后破坏动态适配；输出应包含 `annotation.md`、`sections.json`、implemented template、preview artifacts、visual diff report 和 validation evidence。

## Key Claims

- explicit: 复杂视觉稿还原应以证据链为核心，每轮都产出截图、diff、日志或 manifest，而不是凭主观感觉判断相似度。
- explicit: 标注未确认、计划未确认、素材缺失、未知变量模式或质量闸门未通过时，应停止猜测并回到人工确认。
- explicit: 工作流要求先标注画布和动态/静态/section 区域，再写工程参数和开发计划，最后进入 preview 与 visual diff 循环。
- inferred: 这张图把视觉还原从“设计审美任务”转成可审查、可回放、可验证的 Agent 工作流。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: [[concepts/视觉还原证据链|视觉还原证据链]] — 本图提供 Figma 还原的标注、审核、diff loop 和证据产物要求。
- updates: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 补充视觉稿还原类 skill 的输入、证据、质量闸门和停止条件。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]] — 可作为 Figma/视觉还原工作流工具入口。
- toolchain-neighbor: [[sources/Vibe/工具/mattpocock:skills  ⭐/visual-fidelity-loop.png|visual-fidelity-loop.png]] — 两者形成“目标设计稿还原 + visual diff 验证”的工具链。

## Maintenance Notes

- 图片没有可见 URL；工具名和文件名来自图中可读文字。
- 本图没有说明具体实现仓库或脚本路径，后续若要执行还原，需要回到相关 skill 或项目工具链核验。
