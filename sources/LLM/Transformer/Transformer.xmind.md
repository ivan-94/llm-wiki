---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/LLM/Transformer/Transformer.xmind"
source_relpath: "LLM/Transformer/Transformer.xmind"
raw_created_at: 2024-05-05T09:40:10.273378+00:00
raw_modified_at: 2024-05-06T03:49:47.771377+00:00
raw_size: 521846
raw_fingerprint: "size=521846;birth=2024-05-05T09:40:10.273378+00:00;mtime=2024-05-06T03:49:47.771377+00:00"
raw_snapshot_at: 2026-05-29T22:10:06.205379+00:00
ingested_at: 2026-05-30
status: ingested
---

# Transformer.xmind

## Source

- Raw file: [LLM/Transformer/Transformer.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/LLM/Transformer/Transformer.xmind>)
- Raw ref: `raw:LLM/Transformer/Transformer.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-05-05T09:40:10.273378+00:00`; modified `2024-05-06T03:49:47.771377+00:00`; size `521846`; snapshot `2026-05-29T22:10:06.205379+00:00`
- Coverage: exported and digested all discovered sheets with `ai-wiki-xmind-ingest`; sheet count `1`; sheets: `画布 1`.

## Summary

这份思维导图把 Transformer 放在 NLP 表示学习的发展脉络中理解：从 n-gram、词袋模型、词向量、NPLM、RNN/LSTM、注意力机制一路过渡到 Transformer，再连接 GPT、BERT、ChatGPT/GPT-4、指令微调、RLHF 和 Seq2Seq。它适合作为“为什么 Transformer 成为现代 LLM 基础架构”的入门路线图。

## Source Digest

导图的主线不是只解释 Transformer 架构，而是先铺垫语言模型如何从离散统计走向连续向量和神经网络。基础概念部分强调分词、余弦相似度、稀疏/稠密向量、分布式表示、自回归训练、无监督预训练、指令微调、RLHF 与过拟合。这些概念共同构成 LLM 的底层词汇表：模型先把文本转成 token 和向量，再通过预测目标学习语言规律，最后用微调和人类反馈调整行为。

早期模型部分用 n-gram 和词袋模型说明传统文本表示的局限。n-gram 简单、可解释、可用于输入法、拼写检查、语音识别和翻译，但会遭遇维度爆炸、过拟合、长距离依赖不足和固定上下文长度问题。词袋模型通过词频向量表示文本，适合分类和主题识别，但丢失词序、向量高维稀疏，且不能处理同义词和深层语义。导图随后把 Word2Vec 作为关键转折点：CBOW 通过上下文预测目标词，Skip-Gram 通过目标词预测上下文，最终学习低维稠密词向量，用向量距离承载语义相似性。

在序列建模路径上，导图把 NPLM、RNN、LSTM 和注意力机制组织成 Transformer 的前置台阶。NPLM 让神经网络学习词序列概率和词的连续表示；RNN 通过隐状态处理序列，但面对梯度消失、梯度爆炸和长期依赖问题；LSTM/GRU 通过门控改进记忆能力。注意力机制进一步改变信息选择方式：模型不再只能依赖压缩后的隐状态，而是可对输入序列不同部分打分、softmax 加权并汇总上下文。自注意力让序列内部位置相互关联，多头注意力让模型从多个表示空间并行观察关系。

Transformer 被解释为完全依赖注意力机制处理序列的架构。它用自注意力捕捉任意位置之间的依赖，用多头注意力增加表达角度，用位置编码补足无循环结构带来的顺序信息，用编码器/解码器层和前馈网络完成信息转换。与 RNN 逐步处理序列相比，Transformer 更适合并行处理，也更擅长长距离依赖。导图还把 GPT 与 BERT 放在 Transformer 的两条使用路线里：GPT 偏单向自回归生成，BERT 偏双向上下文理解和 MLM；ChatGPT/GPT-4 则是在超大规模预训练、提示/指令模式、思维链、RLHF、聊天场景微调和安全约束上继续演进。

## Key Claims

- explicit: 分布式表示用连续向量空间表达词、短语或文档，比 one-hot/词袋等局部表示更能压缩信息、衡量相似性并捕捉语义关系。
- explicit: n-gram 和词袋模型是简单有效的文本基线，但分别受限于局部上下文、维度爆炸、词序丢失和语义捕捉不足。
- explicit: Word2Vec 通过 CBOW 或 Skip-Gram 学习低维稠密词向量，相比词袋模型更能保留上下文和语义相似性。
- explicit: RNN 可以处理序列和历史状态，但长序列训练会遇到梯度消失/爆炸和长期依赖问题，LSTM/GRU 是针对这些问题的门控改进。
- explicit: 注意力机制通过打分、softmax 权重和加权求和选择关键输入，自注意力和多头注意力是 Transformer 的核心构件。
- explicit: Transformer 不依赖循环结构，而用自注意力、多头注意力、位置编码、编码器/解码器和前馈网络处理序列。
- explicit: GPT 采用单向语境，更偏生成连续文本；BERT 采用双向语境和 MLM，更偏上下文理解。
- inferred: 这份 source 最适合编译为“LLM 基础与 Transformer 演进”的学习节点，而不是单独的论文级 Transformer 技术细节页。

## External Links

No external links found in extracted content.

## Links

- related: no downstream wiki pages were updated in this scoped ingest batch; compile candidates are listed in `Maintenance Notes` as plain text.

## Maintenance Notes

- Export status: helper returned `ok=true`, `sheets_error` empty, one sheet exported.
- Structure note: source contains some AI-generated explanatory prose and several broad introductory branches; exact technical wording should be rechecked against raw if used for high-precision definitions.
- Compile candidates: Transformer, 注意力机制, 词向量, 神经概率语言模型, RNN/LSTM, Seq2Seq, GPT vs BERT, LLM 基础学习地图.
