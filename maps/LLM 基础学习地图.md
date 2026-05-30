---
page_type: map
updated_at: 2026-05-30
status: active
scope: LLM
---

# LLM 基础学习地图

## Purpose

按“通识 → 表示 → 架构 → 内部机制 → 训练管线 → 微调实战 → 评估 → 选型”组织 LLM 基础的学习路径，从文本如何变成向量一路走到该用微调还是 RAG 的工程判断。

## Entry Points

- 可选前置：[[sources/机器学习/python 深度学习入门.xmind|python 深度学习入门.xmind]]：深度学习/神经网络/梯度下降通识底座，零基础者先读。
- 通识总览：[[sources/LLM/大模型.xmind|大模型.xmind]]：LLM 类型、推理流程、微调/RAG/量化/评估全景。
- 表示学习：[[sources/LLM/Token and Embedding.xmind|Token and Embedding.xmind]]。
- 架构演进：[[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]。
- 内部机制：[[sources/LLM/语言模型内部原理.xmind|语言模型内部原理.xmind]]。
- 训练/微调：[[sources/LLM/微调生成模型.xmind|微调生成模型.xmind]]、[[sources/LLM/State of GPT - Microsoft Build 2023 RD.pdf|State of GPT]]。

## Learning Path

1. 通识：读 [[concepts/模型工程（知识注入）|模型工程（知识注入）]]（上下文层 vs 参数层），建立 LLM 优化的全局坐标系；零基础可先过一遍 `python 深度学习入门` 的神经网络/梯度下降。
2. 表示：读 [[concepts/Token 和 Embedding|Token 和 Embedding]]，理解分词（BPE/WordPiece）、静态/上下文化/检索 embedding。
3. 架构：读 [[concepts/Transformer|Transformer]] 与 [[concepts/注意力机制|注意力机制]]，理解 q/k/v、多头、位置编码、因果掩码。
4. 模型路线：读 [[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]] 和 [[concepts/自回归语言模型|自回归语言模型]]，分清 BERT 理解派与 GPT 生成派。
5. 内部机制：读 [[concepts/解码与采样策略|解码与采样策略]]、[[concepts/KV Cache|KV Cache]]、[[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]]，看懂推理是怎么跑的。
6. 训练管线：读 [[concepts/预训练与微调范式|预训练与微调范式]]，掌握 Pretrain→SFT→RM→RL 四阶段。
7. 微调实战：读 [[concepts/LLM 微调|LLM 微调]]（阶段×参数×数据三轴）、[[concepts/指令微调（SFT）|指令微调（SFT）]]、[[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]]、[[concepts/PEFT 与 LoRA|PEFT 与 LoRA]]、[[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]]、[[concepts/模型量化|模型量化]]。
8. 评估：读 [[concepts/LLM Benchmark 评估|LLM Benchmark 评估]]，并互链他人维护的 [[concepts/LLM 评估|LLM 评估]]、[[concepts/LLM-as-a-Judge|LLM-as-a-Judge]]。
9. 选型：读 [[concepts/RAG|RAG]] 与 [[concepts/提示词缓存|提示词缓存]]，判断何时用检索/缓存代替或补充微调。

## Core Concepts

- 表示与架构：[[concepts/Token 和 Embedding|Token 和 Embedding]]、[[concepts/Transformer|Transformer]]、[[concepts/注意力机制|注意力机制]]、[[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]]
- 内部机制：[[concepts/自回归语言模型|自回归语言模型]]、[[concepts/解码与采样策略|解码与采样策略]]、[[concepts/KV Cache|KV Cache]]、[[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]]
- 训练与微调：[[concepts/预训练与微调范式|预训练与微调范式]]、[[concepts/LLM 微调|LLM 微调]]、[[concepts/指令微调（SFT）|指令微调（SFT）]]、[[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]]、[[concepts/PEFT 与 LoRA|PEFT 与 LoRA]]、[[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]]、[[concepts/模型量化|模型量化]]
- 评估与选型：[[concepts/LLM Benchmark 评估|LLM Benchmark 评估]]、[[concepts/模型工程（知识注入）|模型工程（知识注入）]]、[[concepts/提示词缓存|提示词缓存]]、[[concepts/RAG|RAG]]、[[concepts/LLM 评估|LLM 评估]]

## Key Entities

- [[entities/GPT 与 ChatGPT|GPT 与 ChatGPT]]、[[entities/BERT|BERT]]、[[entities/Llama|Llama]]、[[entities/Hugging Face|Hugging Face]]

## Synthesis To Read

- [[synthesis/RAG 与长上下文|RAG 与长上下文]]
- [[synthesis/LLM 应用数据处理流水线|LLM 应用数据处理流水线]]

## Review Queue

- 2026-06-06: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- 2026-06-06: [[concepts/Transformer|Transformer]]
- 2026-06-06: [[concepts/LLM 微调|LLM 微调]]
- 2026-06-06: [[concepts/注意力机制|注意力机制]]
- 2026-06-06: [[concepts/自回归语言模型|自回归语言模型]]
- 2026-06-06: [[concepts/预训练与微调范式|预训练与微调范式]]
- 2026-06-06: [[concepts/指令微调（SFT）|指令微调（SFT）]]
- 2026-06-06: [[concepts/RLHF 与偏好对齐|RLHF 与偏好对齐]]
- 2026-06-06: [[concepts/PEFT 与 LoRA|PEFT 与 LoRA]]
- 2026-06-06: [[concepts/Encoder 与 Decoder 模型|Encoder 与 Decoder 模型]]
- 2026-06-06: [[concepts/KV Cache|KV Cache]]
- 2026-06-06: [[concepts/解码与采样策略|解码与采样策略]]
- 2026-06-06: [[concepts/模型量化|模型量化]]
- 2026-06-06: [[concepts/Chat Template 与 Tokenizer|Chat Template 与 Tokenizer]]
- 2026-06-06: [[concepts/Self-Instruct 与合成数据|Self-Instruct 与合成数据]]
- 2026-06-06: [[concepts/模型工程（知识注入）|模型工程（知识注入）]]
- 2026-06-06: [[concepts/LLM Benchmark 评估|LLM Benchmark 评估]]
- 2026-06-06: [[concepts/提示词缓存|提示词缓存]]

## Open Gaps

- `State of GPT`、`claude skill.pdf` 等 PDF 当前只是 preview ingest，不是全文阅读。
- `BERT 模型微调.xmind`、`Hugging face transformers.xmind` 为 partial 占位源，相关页仅作待补全入口。
- 模型 API、prompt caching 和工具链事实具有时效性，使用前需要核验。
- `LLM 评估`、`LLM-as-a-Judge`、`RAG`、`上下文工程` 等由其他 wave 维护，本地图仅互链。
