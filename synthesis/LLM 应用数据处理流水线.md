---
page_type: synthesis
updated_at: 2026-05-30
status: active
source_count: 7
learning_status: learning
confidence: 3
difficulty: 4
review_after: 2026-06-13
---

# LLM 应用数据处理流水线

## Thesis

LLM 应用的输入质量由资料预处理决定。多格式资料需要先经过格式转换、结构化解析、搜索抓取、正文抽取、音视频转写和来源保留，才能稳定进入 RAG、长上下文或知识库。

## Pipeline

1. **Source discovery**：搜索 API（Google/Bing/Tavily）、网页抓取（Playwright/Crawl4AI）、文件收集。
2. **Format conversion**：
   - PDF → Markdown（Marker）或 HTML（pdf2htmlEX）；或 OCR 服务。
   - **DOCX（Open XML 包）**：三层解析——包结构（`[Content_Types].xml`）→ 关系（`_rels/`）→ 语义（`document.xml`：段落 `<w:p>`、运行 `<w:r>`、表格、图片）；mammoth.js 可转 HTML；LibreOffice 可做多格式转换。
   - 图片 → OCR 服务；Pillow/OpenCV 作为前处理工具候选。
   - 网页 → 正文抽取（Trafilatura/newspaper/Readability.js）。
3. **Structure extraction**：保留布局（LayoutLMv3/PaddleOCR PP-Structure）、表格（Table Transformer）、阅读顺序、公式、图像裁剪和来源定位。
4. **Text normalization**：
   - OCR 后处理：去噪、分段、版面恢复。
   - ASR（Whisper/FunASR/SenseVoice）：音视频转文字；**VAD**（声音活动检测）区分语音/非语音段，前置于 ASR；**PUNC**（标点恢复）用于 ASR 后处理，恢复可读文本。
   - 字幕格式：SRT/WebVTT，可嵌入视频容器或硬编码。
5. **Index preparation**：文档分块（RecursiveCharacterTextSplitter 等）、摘要生成（RAPTOR 递归摘要）、metadata、embedding、分层索引。
6. **Consumption**：RAG、长上下文、写作工作台、Agent memory 或 wiki source note。
7. **Evidence retention**：保留 raw link、metadata、coverage 和解析限制。

## 关键工具矩阵（信息来自 raw，not verified）

| 阶段 | 工具候选 |
| --- | --- |
| 搜索 API | Google（限额）、Tavily（LLM 友好输出）、Exa、Serper |
| 页面抓取 | Playwright Python、Crawl4AI |
| 正文抽取 | Trafilatura、newspaper、Readability.js |
| PDF 转换 | Marker（转 Markdown）、pdf2htmlEX（转 HTML） |
| Office 转换 | mammoth.js（DOCX→HTML）、LibreOffice |
| 文档 AI | LayoutLMv3、PaddleOCR PP-Structure、Table Transformer、RAGFlow DeepDoc |
| 图像预处理 | Pillow、OpenCV（候选，信息量有限） |
| ASR | Whisper/faster-whisper、FunASR/Paraformer、SenseVoice |
| VAD/PUNC | 用于 ASR 流水线预处理和后处理 |

## Open Gaps

- **DOCX 覆盖差距**：当前 `docx.xmind` 只提供格式结构知识，缺少完整 Python 解析库实践（python-docx、lxml）和真实文档验证。
- **图像处理覆盖差距**：`图像处理.xmind` 信息量有限（Pillow/OpenCV 候选），缺少具体图像预处理流程、质量评估和与文档 AI 的衔接方案。
- ASR 模型速度、显存和中文效果数据来自 raw，未联网核验，可能因硬件和版本变化。
- 搜索服务价格、配额和 LLM 友好性易变，需要最新核验。

## Evidence

- [[sources/数据处理/资料预处理.xmind|资料预处理]] — PDF/Word/Excel/图片/网页转换入口和工具候选。
- [[sources/数据处理/结构化文档提取.xmind|结构化文档提取]] — Document AI 流水线、布局、表格和 RAG 文档解析路线。
- [[sources/数据处理/docx.xmind|docx.xmind]] — DOCX Open XML 包结构：包结构层 → 关系层 → 语义层三层解析模型。
- [[sources/数据处理/搜索.xmind|搜索]] — 搜索发现、页面抓取、正文抽取和开源产品参考。
- [[sources/数据处理/音视频.xmind|音视频]] — ASR、VAD、PUNC、字幕格式和 Whisper 系列生态。
- [[sources/数据处理/图像处理.xmind|图像处理]] — Pillow/OpenCV 工具候选（信息量有限）。
- [[sources/RAG/RAG.xmind|RAG.xmind]] — 文档进入 RAG 的 chunk、摘要和分层索引后处理。

## Implications

- 知识库 ingest 应记录 coverage，不应把 preview/OCR/vision 当完整阅读。
- PDF 和图片资料要区分"可见文字"与"结构关系"；仅提取文字会丢失表格和版面语义。
- 音视频资料进入 LLM 前至少要拆出 VAD/ASR、时间戳、字幕格式和 PUNC 后处理。
- 网页搜索结果需要正文抽取；摘要 API 可能不够，很多场景仍要做页面抓取。
- DOCX 解析应建立"部件发现 → 关系解析 → 语义重建"路径，不能只抽取 `document.xml` 文本。

## Related Concepts

- [[concepts/结构化文档解析|结构化文档解析]]
- [[concepts/RAG|RAG]]
- [[concepts/上下文工程|上下文工程]]

## My Take

数据处理不是 LLM 应用的前置杂活，而是上下文质量控制面。解析丢失的结构，会在下游变成检索失败、总结失真和错误证据。尤其是 DOCX 的三层解析和 VAD/PUNC 的音视频后处理，是两个常被低估的质量关卡。

## Open Questions

- 具体工具如 Marker、RAGFlow、PaddleOCR、Whisper、FunASR、Tavily 等当前能力未联网核验。
- 图像处理在文档 AI 流水线中的具体作用（图片 PDF 前处理、表格图像识别）需要更多覆盖。
