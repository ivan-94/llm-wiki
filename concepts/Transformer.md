---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 5
learning_status: new
confidence: 3
difficulty: 5
review_after: 2026-06-06
---

# Transformer

## Definition

Transformer 是一种以自注意力、多头注意力、位置编码、前馈网络和残差/归一化结构为核心的序列建模架构，是现代 LLM、BERT、GPT 等模型的基础。

## Why It Matters

Transformer 让语言模型从 RNN 的顺序处理转向高度并行的上下文建模，显著改善长距离依赖、训练效率和大规模预训练可行性。

## Mental Model

每个 token 都带着一个向量进入多层“注意力交换所”：它向其他 token 发出 query，用 key 找相关信息，再聚合 value 形成新的上下文表示。

## Key Claims

- Transformer 不依赖循环结构，而用自注意力捕捉任意位置之间的依赖。
- 多头注意力让模型在多个表示空间中并行观察关系。
- 位置编码补足无循环结构带来的顺序信息。
- Transformer block 通常由注意力层和前馈网络组成，前馈网络承载大量训练后知识。
- GPT 偏 decoder-only 自回归生成，BERT 偏 encoder-only 双向理解。

## Examples

- `Transformer.xmind` 从 n-gram、词袋、Word2Vec、RNN/LSTM、注意力机制一路过渡到 Transformer。
- `语言模型内部原理.xmind` 拆解 LM Head、KV cache、query/key/value 和解码策略。
- `Token and Embedding.xmind` 将 Transformer 放入表示学习演进路径。
- `图解ChatGPT.xmind` 用 ChatGPT/RLHF 语境连接 Transformer 到对话模型。

## Common Confusions

- 注意力机制不是 Transformer 的全部；位置编码、前馈层、残差和归一化同样重要。
- Transformer 能处理长距离依赖，不等于长上下文内所有信息都会被可靠使用。
- BERT 和 GPT 都基于 Transformer，但训练目标和使用方向不同。

## Evidence

- [[sources/LLM/Transformer/Transformer.xmind|Transformer.xmind]]
- [[sources/LLM/语言模型内部原理.xmind|语言模型内部原理]]
- [[sources/LLM/Token and Embedding.xmind|Token and Embedding]]
- [[sources/LLM/图解ChatGPT.xmind|图解ChatGPT]]

## Relations

- prerequisite: [[concepts/Token 和 Embedding|Token 和 Embedding]]
- enables: [[concepts/LLM 微调|LLM 微调]]
- used-in: [[concepts/RAG|RAG]]
- map-entry: [[maps/LLM 基础学习地图|LLM 基础学习地图]]

## My Understanding

当前理解：Transformer 的突破在于把序列处理转成并行的上下文关系计算，并使大规模预训练成为可扩展工程。

## Review Questions

- query/key/value 分别承担什么？
- 为什么位置编码对 Transformer 必要？
- GPT 和 BERT 的架构/训练目标差异是什么？

## Open Questions

- 当前页是学习概念页，不替代论文级 Transformer 技术细节。
