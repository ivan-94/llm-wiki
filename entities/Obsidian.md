---
page_type: entity
updated_at: 2026-06-01
status: active
source_count: 1
---

# Obsidian

## What It Is

Obsidian 是一个基于本地 Markdown 文件夹的个人知识管理工具，本 wiki 将其用作知识库载体。它以链接为中心：双向链接、反向链接和关系图谱把分散笔记连接成可浏览的知识网络，Canvas 和 MOC（Map of Content）用于可视化梳理和学习路径组织。

## Role In This Wiki

Obsidian 是本 AI Wiki 的技术基础。wiki 的 source note / concept / entity / synthesis / maps 文件夹契约、frontmatter 元数据、`[[wikilink]]` 内部链接、`raw:` 协议引用和 iCloud 同步，都直接对应 Obsidian 的 Vault / note / link / attachment / sync 模型。vault-sync skill 负责把本 wiki repo 发布到 Obsidian iCloud 容器供 iOS 阅读。

## Key Facts

- Vault 对应一个本地文件夹，note 是 `.md` 文件，可被普通文本编辑器打开。
- 链接体系：`[[wikilink]]` 内部链接、`![[embed]]` 内嵌、Backlinks 面板、Graph 关系图、Unlinked Mentions（尚未链接但出现文字的笔记）。
- Canvas 提供可视化梳理能力，适合知识地图和学习路径设计。
- Frontmatter 支持 YAML 元数据，配合插件可用于过滤、排序、状态管理。
- Obsidian 本身是工具箱，真正价值来自如何设计"收集 → 整理 → 连接 → 复用"的 workflow。
- 类比：Obsidian 之于 Markdown 知识管理，类似 VSCode 之于代码编辑——可扩展的工作台，而非封闭产品。
- 在 AI wiki 工作流里，Obsidian 还承担 Inbox、XMind/图片输入、ChatGPT 生成 Markdown、Codex 日报/周报、recap/insight/knowledge gap 回顾的第二大脑文件系统底座。

## Related Concepts

- enables: [[concepts/Agent Skills|Agent Skills]] — wiki 作为 Agent 可读的文件系统，Agent skills 通过读取 wiki 页面来获取上下文。
- used-in: wiki 目录契约 — wiki 的 `sources/`/`concepts/`/`entities/`/`synthesis/`/`maps/` 目录结构依赖 Obsidian 的 Vault 文件组织。
- related: [[concepts/上下文工程|上下文工程]] — wiki 作为 Agent 上下文来源，Obsidian 的 wikilink 和 MOC 结构直接影响上下文可检索性。

## Evidence

- [[sources/Vibe/Vibe Coding 随手记/文件系统/Obsidian.xmind|Obsidian.xmind]] — 描述 Vault、note、frontmatter、link、backlinks、Canvas、Graph、MOC，并补充 Obsidian 作为 AI 第二大脑文件系统底座的工作流。

## Open Questions

- Obsidian 插件生态（如 Dataview、Templater）在 wiki 工作流中的最佳使用方式还未系统化。
- iOS 版 Obsidian 的 iCloud 同步延迟对 wiki 查阅体验的影响需要实测。
