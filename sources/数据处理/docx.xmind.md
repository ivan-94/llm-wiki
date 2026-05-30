---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/数据处理/docx.xmind"
source_relpath: "数据处理/docx.xmind"
raw_created_at: 2024-12-12T03:29:36.222057+00:00
raw_modified_at: 2024-12-16T05:50:02.509615+00:00
raw_size: 480602
raw_fingerprint: "size=480602;birth=2024-12-12T03:29:36.222057+00:00;mtime=2024-12-16T05:50:02.509615+00:00"
raw_snapshot_at: 2026-05-29T22:13:06.955173+00:00
ingested_at: 2026-05-30
status: ingested
---

# docx.xmind

## Source

- Raw file: [数据处理/docx.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86/docx.xmind>)
- Raw ref: `raw:数据处理/docx.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-12-12T03:29:36.222057+00:00`; modified `2024-12-16T05:50:02.509615+00:00`; size `480602`; snapshot `2026-05-29T22:13:06.955173+00:00`
- Coverage: exported and read 1 sheet: `画布 1`.

## Summary

这份 source 解释 `.docx` 作为 Open XML 包的内部结构：内容类型、关系、文档主体、样式、编号、主题、媒体、属性、宏、OLE、签名等组件如何共同构成一个 Word 文档。它适合作为后续“结构化文档解析”和“Office 文档预处理”的底层格式知识。

## Source Digest

`.docx` 不是单个纯文本文件，而是一个由多个 XML 部件和资源目录组成的包。核心内容集中在 `word/document.xml`，其中段落、运行、文本、表格、节、域、书签、超链接等都通过 XML 标签表达；样式、编号、字体、主题、设置和媒体则在独立部件中维护。`_rels` 目录中的关系文件把这些部件连接起来，例如文档主体到样式、图片、主题和超链接的引用。`[Content_Types].xml` 则声明包中各类部件的 MIME 类型，使解析器知道如何处理不同文件。

这份导图的价值在于把 Word 文档解析拆成三层：包结构层负责发现部件，关系层负责追踪引用，语义层负责理解段落、运行、表格、图片、页眉页脚、批注、修订和动态域。对于资料预处理或 RAG 导入来说，不能只抽取 `document.xml` 文本；如果要保留版式、列表层级、图片、链接和变更痕迹，必须同时读取样式、编号、媒体与关系。

## Key Claims

- explicit: `.docx` 的核心正文在 `word/document.xml`，其中包含文本、段落、表格、图片引用等主要内容。
- explicit: `_rels` 目录用于描述文档各部分之间的连接，图片、样式、主题和超链接等都通过关系引用实现。
- explicit: 样式、编号、字体、主题和文档设置分别存放在独立 XML 文件或目录中，并影响文档渲染与结构解释。
- explicit: 段落由 `<w:p>` 表示，运行由 `<w:r>` 表示，文本由 `<w:t>` 表示；运行是段落内具有相同格式的文本块。
- inferred: 面向 LLM/RAG 的 Word 解析应优先建立“部件发现 -> 关系解析 -> 语义重建”的处理路径，而不是只做正文文本抽取。

## External Links

- schema-reference: [Open XML package content types namespace](http://schemas.openxmlformats.org/package/2006/content-types) — source 中 `[Content_Types].xml` 示例使用的 XML namespace；not verified.

## Links

- related: [[concepts/结构化文档解析|结构化文档解析]] — source 补充 DOCX Open XML 包结构、关系解析和语义重建的底层格式证据。
- related: [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]] — 可支撑 Office 文档从包结构解析到 LLM 可消费表示的预处理环节。
- map-entry: [[maps/LLM 应用与数据处理学习地图|LLM 应用与数据处理学习地图]] — 可作为 Office/DOCX 资料预处理的格式入口。
- related: [[sources/数据处理/资料预处理.xmind|资料预处理.xmind]] — 本 source 提供 DOCX 格式底层知识，对方负责 Office 格式的实际转换工具选型。
- related: [[sources/数据处理/结构化文档提取.xmind|结构化文档提取.xmind]] — DOCX Open XML 包结构是文档 AI 结构提取的格式基础，两个 source 在 pipeline 中互补。

## Maintenance Notes

- 导出内容包含一段 `[Content_Types].xml` 示例，source note 已提炼其作用，没有保存完整 XML 作为 raw cache。
- 该 source 是格式结构说明，未覆盖具体解析库、边界案例或真实 `.docx` 样本验证。
- Compile candidates: Office 文档预处理, DOCX Open XML 包结构, 文档关系解析.
