---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Langchain(Legacy)/Langchain  DevOps.xmind"
source_relpath: "Langchain(Legacy)/Langchain  DevOps.xmind"
raw_created_at: 2024-04-30T00:29:18.165614+00:00
raw_modified_at: 2024-05-15T01:13:01.678171+00:00
raw_size: 1173164
raw_fingerprint: "size=1173164;birth=2024-04-30T00:29:18.165614+00:00;mtime=2024-05-15T01:13:01.678171+00:00"
raw_snapshot_at: 2026-05-29T22:11:31.021024+00:00
ingested_at: 2026-05-30
status: ingested
---

# Langchain  DevOps.xmind

## Source

- Raw file: [Langchain(Legacy)/Langchain  DevOps.xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Langchain%28Legacy%29/Langchain%20%20DevOps.xmind>)
- Raw ref: `raw:Langchain(Legacy)/Langchain  DevOps.xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2024-04-30T00:29:18.165614+00:00`; modified `2024-05-15T01:13:01.678171+00:00`; size `1173164`; snapshot `2026-05-29T22:11:31.021024+00:00`
- Coverage: exported and read 1 sheet, `画布 1`, with 175 topics via `ai-wiki-xmind-ingest`.

## Summary

这份图把 LangSmith 定位为 LangChain 的 DevOps 平台，围绕开发协作、测试评估、部署和监控展开。高信号内容集中在数据集、评估器、离线/在线评估、CI 回归、人工反馈、内置评估器、成本/延迟/质量监控等 LLM 应用工程实践。

## Source Digest

这份 source 的核心判断是：LLM 应用因为自然语言输入和模型输出都具有不确定性，传统软件工程中的单元测试、集成测试和部署监控需要重新适配。LangSmith 被放在 LLM DevOps 的中心，承担开发协作、trace 分享、prompt hub、测试、部署和监控等职责。它不是单纯的日志工具，而是把运行记录、数据集、评估和监控连成一个质量反馈系统。

数据集分支把 dataset 定义为输入输出对的结构化集合，并区分训练集、验证集和测试集在模型工程中的用途。在 LangSmith 语境里，数据集既可以用于评估，也可作为 few-shot 样本或微调素材；构建方式包括从已运行结果中添加、导入和 SDK 创建。管理分支还提到版本化、导入导出和发布，这说明数据集被视为可维护资产，而不是一次性测试样本。

测试和评估分支把 evaluator 定义为函数：接收输入、输出和可选期望输出，返回一个或多个分数。评估方式包括人类反馈、AI 辅助评估和启发式评估；评价维度包括相关性、正确性、危害性等。流程上先定义 LLM 应用或目标任务，再选择数据集，根据评价标准配置 evaluator，运行 experiment 并查看结果。source 还区分离线评估、CI 集成回归和在线评估：离线评估用于数据集上的变更比较，CI 用于部署前防回归，在线评估用于持续监控真实应用的质量漂移。

内置评估器分支列出 correctness、criteria、labeled criteria、字符串/嵌入距离等类型。它把 `qa`、`context_qa`、`cot_qa` 等正确性评估与 RAG、真实答案和推理链结合起来；标准评估则在没有标准答案时，根据简洁性、相关性、正确性、连贯性、有害性、帮助性等 criteria 给出判断。整体上，这份图适合补充 LLM 评估与 LLMOps：把 prompt、chain、dataset、evaluator、experiment、feedback、monitoring 作为持续改进闭环。

## Key Claims

- explicit: LangSmith 被定位为 LangChain 的 DevOps 平台，覆盖开发、协作、测试、部署和监控。
- explicit: LLM 应用的输入和输出不确定性更强，因此传统测试实践需要适配到评估、数据集和反馈闭环。
- explicit: 数据集是输入输出对的结构化集合，可用于评估、few-shot 样本和微调。
- explicit: 评估器本质上是函数，接收输入、输出和可选期望输出，返回分数或多个分数。
- explicit: 评估可以按执行方分为人类反馈、AI 辅助评估和启发式评估，也可以按运行阶段分为离线评估、CI 回归和在线评估。
- explicit: LangChain/LangSmith 相关评估器包括正确性、criteria、labeled criteria、字符串距离和嵌入距离等类型。
- inferred: 这份 source 可把 LangSmith 从“观测平台”扩展为 LLM 应用的 DevOps/LLMOps 闭环节点。

## External Links

- documentation: [UI 上绑定评估器](https://docs.smith.langchain.com/how_to_guides/evaluation/bind_evaluator_to_dataset) — 评估器绑定到数据集分支引用；not verified.
- documentation: [LangChain evaluation](https://www.langchain.com/evaluation) — 扩展阅读中的评估和测试资料；not verified.

## Links

- related: [[concepts/LLM 评估|LLM 评估]] — source 补充 dataset、evaluator、offline/online evaluation、CI 回归和内置评估器类型。
- related: [[entities/Langfuse|Langfuse]] — 可作为 LangSmith/Langfuse 两类 LLM 评估观测平台后续对比的参照，但本 note 未创建 LangSmith 实体页。

## Maintenance Notes

- No raw files were modified.
- Source uses `Langchain` capitalization inconsistently; preserved source title while normalizing prose to LangChain where referring to the ecosystem.
- Compile candidates: LangSmith, LLM DevOps, LLMOps, LangChain Evaluation, Dataset for Evaluation, Evaluator Function, Online Evaluation, CI Regression for LLM Apps.
