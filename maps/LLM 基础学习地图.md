---
page_type: map
updated_at: 2026-05-30
status: active
scope: LLM
---

# LLM 基础学习地图

## Purpose

组织 Token/Embedding、Transformer、语言模型内部机制、微调、评估和模型工程的学习路径。

## Entry Points

- [[sources/LLM/Token and Embedding.xmind|Token and Embedding.xmind]]：表示学习入口。
- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]：Transformer 演进入口。
- [[sources/LLM/语言模型内部原理.xmind|语言模型内部原理.xmind]]：推理内部机制入口。
- [[sources/LLM/微调生成模型.xmind|微调生成模型.xmind]]：微调和对齐入口。

## Learning Path

1. 读 [[concepts/Token 和 Embedding|Token 和 Embedding]]，理解文本如何变成向量。
2. 读 [[concepts/Transformer|Transformer]]，理解自注意力、多头注意力和 GPT/BERT 分化。
3. 读 [[sources/LLM/语言模型内部原理.xmind|语言模型内部原理]]，补上 LM Head、KV cache、解码策略。
4. 读 [[concepts/LLM 微调|LLM 微调]]，理解 SFT、RLHF、DPO、LoRA/QLoRA。
5. 读 [[concepts/LLM 评估|LLM 评估]] 和 [[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]，连接模型行为与评估。
6. 读 [[concepts/RAG|RAG]]，理解何时用检索代替或补充微调。

## Core Concepts

- [[concepts/Token 和 Embedding|Token 和 Embedding]]
- [[concepts/Transformer|Transformer]]
- [[concepts/LLM 微调|LLM 微调]]
- [[concepts/RAG|RAG]]
- [[concepts/LLM 评估|LLM 评估]]

## Synthesis To Read

- [[synthesis/RAG 与长上下文|RAG 与长上下文]]
- [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]]

## Review Queue

- 2026-06-06: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- 2026-06-06: [[concepts/Transformer|Transformer]]
- 2026-06-06: [[concepts/LLM 微调|LLM 微调]]

## Open Gaps

- `State of GPT`、`claude skill.pdf` 等 PDF 当前只是 preview ingest，不是全文阅读。
- 模型 API、prompt caching 和工具链事实具有时效性，使用前需要核验。
