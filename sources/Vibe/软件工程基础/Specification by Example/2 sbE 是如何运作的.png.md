---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png"
raw_created_at: 2026-05-04T21:45:00+08:00
raw_modified_at: 2026-05-04T21:46:09+08:00
raw_size: 1796151
raw_fingerprint: "size=1796151;birth=2026-05-04T21:45:00+08:00;mtime=2026-05-04T21:46:09+08:00"
raw_snapshot_at: 2026-05-30T00:14:12+08:00
ingested_at: 2026-05-30
status: ingested
---

# 2 sbE 是如何运作的.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/2%20sbE%20%E6%98%AF%E5%A6%82%E4%BD%95%E8%BF%90%E4%BD%9C%E7%9A%84.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/2 sbE 是如何运作的.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-04T21:45:00+08:00`; modified `2026-05-04T21:46:09+08:00`; size `1796151`; snapshot `2026-05-30T00:14:12+08:00`
- Coverage: Agent vision inspected the full 1184x1328 course infographic. Workflow, example mapping table, generalization panel, specification table, payment case, value list, and anti-patterns are readable.

## Summary

这张图说明 SbE 的运行机制：从业务场景出发，用 Example Mapping 收集主流程、备选路径、异常和边界示例，再从示例中归纳业务规则，最后以 Given/When/Then 形成可读、可验证、可自动化执行的规格。核心思想是示例不是补充说明，而是需求表达方式；规则来自示例归纳，而不是凭空猜测。

## Source Digest

图像顶部给出流程本质：业务场景到示例，再到规则，最后到自动化测试。Example Mapping 部分要求用具体、可理解的例子覆盖业务活动中的不同路径，包括 happy path、alternate、exception 和 edge case；讨论示例的过程本身就是澄清需求的过程，示例必须业务可理解，避免过早进入技术细节。

第二步从多个示例中抽象规则。图中支付例子包括余额 100 支付 50 成功、余额 0 支付 10 失败、余额 -10 支付 10 失败、余额 100 支付 200 失败，由此归纳出余额必须大于等于订单金额、支付金额必须大于 0、用户必须已登录等规则。第三步把规则写成共同认可的规格，典型形式为 Given/When/Then：Given 表示前提条件，When 表示触发行为，Then 表示期望结果。完整案例继续把在线支付拆成业务场景、示例、规则、规格和自动化测试，并用 Cucumber 指向持续验证。

## Key Claims

- explicit: SbE 的流程是业务场景、示例、规则、自动化测试。
- explicit: Example Mapping 需要覆盖主流程、备选流程、异常流程和边界/特殊值。
- explicit: 规则是对示例的归纳总结，而不是一开始就编写规则。
- explicit: 规格的典型形式是 Given/When/Then，分别表达前提条件、触发行为和期望结果。
- explicit: 规格的特点包括业务可读、明确无歧义、可自动化、既是文档也是验收标准。
- explicit: 常见误区包括一开始就写规则、示例写成技术用例、规则过于实现化、示例过少或过多。
- inferred: SbE 把抽象规则放在示例之后，可以降低团队对同一业务词汇的误读概率。

## External Links

No external links found in extracted content.

## Links

- compiled-concept candidate: [[concepts/Specification by Example|Specification by Example]] — 可沉淀 SbE 从示例到规则再到可执行规格的核心流程。
- compiled-concept candidate: [[concepts/Example Mapping|Example Mapping]] — 可沉淀主流程、备选、异常、边界示例的需求澄清方法。
- compiled-concept candidate: [[concepts/Gherkin|Gherkin]] — 可补充 Given/When/Then 在 SbE 中的规格表达角色。
- map-entry candidate: [[maps/软件工程基础学习地图|软件工程基础学习地图]] — 可作为行为规格与自动化验收的学习节点。

## Maintenance Notes

- 图中 Cucumber 仅作为自动化测试工具示例出现；未联网核验工具细节。
- 规格表和案例表字号较小，但核心字段和示例可读。
- 未修改 `index.md`、`log.md` 或编译页；本批 worker 只记录 compile 候选关系。
