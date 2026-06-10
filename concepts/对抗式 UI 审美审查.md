---
page_type: concept
updated_at: 2026-06-10
status: active
source_count: 1
learning_status: new
confidence: 2
difficulty: 3
review_after: 2026-06-24
---

# 对抗式 UI 审美审查

## Definition

对抗式 UI 审美审查是在没有明确设计稿时，用只读设计批判、严重级别分级、批准修复和复评循环来改善现有 UI 的工作流。

## Why It Matters

没有设计稿时，UI 改进很容易变成偏好争论或无限挑刺。对抗式审查把主观审美压成可执行流程：截图证据、P0/P1 findings、组织者筛选、前端只修批准项、复评后继续或停止。

## Mental Model

```
截图证据 -> 只读批判 -> P0/P1 筛选 -> 批准修复 -> 验证复评 -> 继续/停止
```

## Key Claims

- UI 设计师只读批判，不修改代码；前端开发者只修已批准项，不做审美裁决。
- 默认只修 P0/P1，避免把“可以更好”变成无限工作。
- 组织者负责提供上下文、截图、范围、组件/token 参考，并筛选裁决。
- 适用场景是没有目标设计稿的现有 UI；已有 Figma 或截图目标时应改用 [[concepts/视觉还原证据链|视觉还原证据链]]。
- 复用组件和 token 是修复约束，防止每次审美改进都制造新的视觉系统分叉。

## Examples

- 现有后台表格界面没有设计稿，但按钮层级、间距、文本对比度和图标含义存在明显问题，可以先让设计角色只读截图输出 P0/P1 findings。
- 多端截图中发现移动端主要操作不可见，这是 P0/P1；“次要文案亲和度不足”通常不应阻塞修复。

## Common Confusions

- 对抗式 UI 审美审查不是视觉还原；它没有 target design，不能用像素差异作为唯一目标。
- 设计师的职责是发现问题和说明理由，不是直接改代码。
- P2/P3 可以记录，但默认不进入修复范围，除非组织者明确批准。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/adversarial-ui-review-loop.png|adversarial-ui-review-loop.png]] — 提供角色分工、P0/P1/P2/P3 分级、截断筛选、批准修复和复评循环。

## Relations

- part-of: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — 它是 UI 质量改进类 workflow skill。
- contrasts-with: [[concepts/视觉还原证据链|视觉还原证据链]] — 有明确目标时走 fidelity；无目标设计稿时走审美审查。
- related: [[concepts/Agent Skills|Agent Skills]] — 这是 skill 能承载非代码生成审查流程的例子。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

对抗式 UI 审美审查的价值是把“你觉得不好看”变成“哪个截图、哪个位置、什么严重级别、谁批准修”的闭环。

## Review Questions

- 为什么设计师只读批判、前端只修批准项？
- P0/P1/P2/P3 分级如何防止无限挑刺？
- 什么时候不应该使用这个流程？

## Open Questions

- P0/P1 的具体判定标准还需要按产品类型沉淀更多案例。
