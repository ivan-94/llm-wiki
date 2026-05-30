---
source_type: pdf
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/LLM/State of GPT - Microsoft Build 2023 RD.pdf"
source_relpath: "LLM/State of GPT - Microsoft Build 2023 RD.pdf"
raw_created_at: 2025-01-21T08:42:52.709815+00:00
raw_modified_at: 2025-01-21T08:42:52.744397+00:00
raw_size: 12269318
raw_fingerprint: "size=12269318;birth=2025-01-21T08:42:52.709815+00:00;mtime=2025-01-21T08:42:52.744397+00:00"
raw_snapshot_at: 2026-05-29T22:09:39.318445+00:00
ingested_at: 2026-05-30
status: ingested
---

# State of GPT - Microsoft Build 2023 RD.pdf

## Source

- Raw file: [LLM/State of GPT - Microsoft Build 2023 RD.pdf](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/LLM/State%20of%20GPT%20-%20Microsoft%20Build%202023%20RD.pdf>)
- Raw ref: `raw:LLM/State of GPT - Microsoft Build 2023 RD.pdf`
- Type: pdf
- Status: ingested
- Raw metadata: created `2025-01-21T08:42:52.709815+00:00`; modified `2025-01-21T08:42:52.744397+00:00`; size `12269318`; snapshot `2026-05-29T22:09:39.318445+00:00`
- Coverage: Preview pages processed: 1-3 of 45. First-three-page visual preview only; no full-PDF OCR or complete reading.

## Summary

这份 PDF 预览页显示它是一组讲解如何训练 GPT/ChatGPT Assistant 的英文幻灯片。前 3 页覆盖标题、GPT Assistant 训练管线，以及预训练数据收集示例；后续 42 页未读取。

## Source Digest

预览内容把 assistant 训练拆成一个从通用语言模型到对齐助手的管线：先用大规模公开文本做 pretraining 得到 base model，再用高质量人工 demonstration 做 supervised finetuning 得到 SFT model，之后用人工 comparison 训练 reward model，最后用 reinforcement learning 生成更符合偏好的 RL model。第 3 页进一步说明预训练阶段依赖大规模公开数据混合，并以 LLaMA 预训练数据配比为例展示 CommonCrawl、C4、GitHub、Wikipedia、Books、ArXiv、StackExchange 等来源的采样比例、epoch 和磁盘规模。

这份资料适合后续补充“LLM 训练流程”“SFT/RM/RLHF”“预训练数据组成”等基础学习节点，但当前 ingest 只读了前 3 页，不能代表整份 45 页材料的完整观点。

## Key Claims

- explicit: 预览页把 GPT Assistant 训练流程分为 Pretraining、Supervised Finetuning、Reward Modeling、Reinforcement Learning 四个阶段。
- explicit: Pretraining 使用 trillions of words 级别的 raw internet text，并通过 language modeling 预测 next token 得到 base model。
- explicit: Supervised Finetuning 使用人工编写的 prompt-response demonstrations，仍以 language modeling 方式训练 SFT model。
- explicit: Reward Modeling 使用人工 comparison 数据训练 binary classification 风格的 reward model。
- explicit: Reinforcement Learning 阶段从 SFT 初始化并使用 reward model，使生成 token 最大化 reward。
- explicit: 预训练数据示例包含 CommonCrawl、C4、GitHub、Wikipedia、Books、ArXiv、StackExchange 等公开数据来源。
- inferred: 该 deck 可能用于解释 ChatGPT 类 assistant 的训练 recipe，而不是只讲单一模型架构或单一工具。

## External Links

No external links found in extracted content.

## Links

No wiki pages created or modified in this task.

## Maintenance Notes

- PDF ingest used the `ai-wiki-pdf-ingest` preview mode: pages 1-3 rendered as images and inspected visually.
- This is not full-PDF OCR, text extraction, or complete reading. Exact wording and later-slide claims must be checked against the raw PDF before citation-heavy compile.

- Link cleanup candidate: Compile candidates: LLM 训练流程; SFT/RM/RLHF; 预训练数据; GPT Assistant 训练管线.
