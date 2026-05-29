---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 7
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# LLM 应用数据处理流水线

## Thesis

LLM 应用的输入质量由资料预处理决定。多格式资料需要先经过格式转换、结构化解析、搜索抓取、正文抽取、音视频转写和来源保留，才能稳定进入 RAG、长上下文或知识库。

## Pipeline

1. Source discovery：搜索 API、网页抓取、文件收集、notebook/写作素材入口。
2. Format conversion：PDF/Office/图片/网页/音视频转换为可读中间格式。
3. Structure extraction：保留布局、表格、阅读顺序、公式、图像和元数据。
4. Text normalization：OCR/ASR、标点恢复、正文抽取、去噪和分段。
5. Index preparation：chunk、summary、metadata、embedding、hierarchical index。
6. Consumption：RAG、长上下文、写作工作台、Agent memory 或 wiki source note。
7. Evidence retention：保留 raw link、metadata、coverage 和解析限制。

## Evidence

- [[sources/数据处理/资料预处理.xmind|资料预处理]] 提供 PDF、Word、Excel、图片、网页转换入口。
- [[sources/数据处理/结构化文档提取.xmind|结构化文档提取]] 提供 Document AI、版面、表格和 RAG 文档解析路线。
- [[sources/数据处理/搜索.xmind|搜索]] 提供搜索发现、页面抓取、正文抽取链路。
- [[sources/数据处理/音视频.xmind|音视频]] 提供 ASR、字幕、VAD、ffmpeg 和 Whisper 生态。
- [[sources/notebook 协作.excalidraw|notebook 协作]] 和 [[sources/案例/写作 ai.xmind|写作 ai]] 提供写作/协作型数据入口。

## Implications

- 知识库 ingest 应记录 coverage，不应把 preview/OCR/vision 当完整阅读。
- PDF 和图片资料要区分“可见文字”与“结构关系”。
- 音视频资料进入 LLM 前至少要拆出 ASR、时间戳、字幕格式和后处理。
- 网页搜索结果需要正文抽取，否则摘要可能不足以支撑严肃回答。

## Related Concepts

- [[concepts/结构化文档解析|结构化文档解析]]
- [[concepts/RAG|RAG]]
- [[concepts/上下文工程|上下文工程]]

## My Take

数据处理不是 LLM 应用的前置杂活，而是上下文质量控制面。解析丢失的结构，会在下游变成检索失败、总结失真和错误证据。

## Open Questions

- 具体工具如 Marker、RAGFlow、PaddleOCR、Whisper、FunASR、Tavily 等当前能力未联网核验。
