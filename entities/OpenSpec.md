---
page_type: entity
updated_at: 2026-05-30
status: active
source_count: 4
---

# OpenSpec

## What It Is

OpenSpec 在本 wiki 中被整理为一种 change-driven / delta-driven 的规格账本工作流，用 `openspec/specs` 维护当前事实，用 `openspec/changes` 管理未来变更。

## Role In This Wiki

它用于理解存量系统中的行为规范治理：如何把 proposal、spec delta、design、tasks、archive 串成可归档、可审计的变更链。

## Key Facts

- 工作流包括 init/update、propose/new、artifacts、apply、sync/archive 和当前 specs。
- OpenSpec 强调 behavior contract、brownfield-first 和迭代式规格演进。
- 它更适合维护已有系统的当前事实、变更审计和规格历史。
- 当前命令、目录和语法未联网核验；本页只依据 raw/source 中的图片材料。

## Related Concepts

- implemented-by: [[concepts/Spec-Driven Development|Spec-Driven Development]]
- uses: [[concepts/行为契约式规格|行为契约式规格]]
- contrasts-with: [[entities/SpecKit|SpecKit]]
- used-in: [[synthesis/OpenSpec 与 SpecKit 对比|OpenSpec 与 SpecKit 对比]]

## Evidence

- [[sources/Vibe/Spec/OpenSpec/概览.png|OpenSpec 概览]]
- [[sources/Vibe/Spec/OpenSpec/产出规范.png|OpenSpec 产出规范]]
- [[sources/Vibe/Spec/OpenSpec/软件工程映射.png|OpenSpec 软件工程映射]]
- [[sources/Vibe/Spec/SpecKit/对比 OpenSpec.png|对比 OpenSpec]]

## Open Questions

- OpenSpec 当前项目状态、命令和目录规范需要后续联网核验。
