---
page_type: map
updated_at: 2026-05-30
status: active
scope: LLM Application
---

# LLM 应用与数据处理学习地图

## Purpose

组织 RAG、长上下文、结构化文档解析、搜索抓取、资料预处理、音视频处理和 LangChain legacy 应用框架。

## Entry Points

- [[sources/RAG/RAG vs 长文本.xmind|RAG vs 长文本.xmind]]：RAG 与长上下文入口。
- [[sources/数据处理/结构化文档提取.xmind|结构化文档提取.xmind]]：Document AI 入口。
- [[sources/数据处理/资料预处理.xmind|资料预处理.xmind]]：多格式资料转换入口。
- [[sources/数据处理/搜索.xmind|搜索.xmind]]：搜索和网页抽取入口。
- [[sources/Langchain(Legacy)/Langchain  表达式语言.xmind|Langchain 表达式语言.xmind]]：LCEL/Runnable 入口。

## Learning Path

1. 读 [[concepts/RAG|RAG]]，理解检索增强生成的基本控制面。
2. 读 [[synthesis/RAG 与长上下文|RAG 与长上下文]]，判断何时保留索引，何时用长上下文。
3. 读 [[concepts/结构化文档解析|结构化文档解析]]，理解 PDF/表格/图片资料进入 RAG 前的结构化要求。
4. 读 [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]]，把搜索、抓取、OCR/ASR 和转换串起来。
5. 读 [[entities/LangChain|LangChain]]，把 LCEL、LangGraph、LangServe 和 tracing 作为应用框架参考。

## Core Concepts

- [[concepts/RAG|RAG]]
- [[concepts/结构化文档解析|结构化文档解析]]
- [[concepts/上下文工程|上下文工程]]
- [[concepts/Token 和 Embedding|Token 和 Embedding]]

## Key Entities

- [[entities/LangChain|LangChain]]
- [[entities/Langfuse|Langfuse]]

## Synthesis To Read

- [[synthesis/RAG 与长上下文|RAG 与长上下文]]
- [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]]

## Review Queue

- 2026-06-06: [[concepts/RAG|RAG]]
- 2026-06-06: [[concepts/结构化文档解析|结构化文档解析]]
- 2026-06-06: [[synthesis/RAG 与长上下文|RAG 与长上下文]]
- 2026-06-06: [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]]

## Open Gaps

- 搜索服务、文档解析工具和 ASR 工具当前能力未联网核验。
- LangChain legacy 资料应作为历史/学习材料，而非最新 API 说明。
