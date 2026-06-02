---
page_type: concept
updated_at: 2026-06-01
status: active
source_count: 9
learning_status: new
confidence: 2
difficulty: 4
review_after: 2026-06-08
---

# HAT（Hand Acceptance Test）

## Definition

HAT（Hand Acceptance Test）是 Agentic delivery 中面向用户路径的验收层：在单元测试、TDD、CI 和 review 之外，准备可复现环境、数据、账号、清单和运行证据，验证变更是否真的能被人类或 Agent 按业务路径使用。

## Why It Matters

Agent 很容易通过局部测试却漏掉真实路径：认证、权限、数据种子、服务生命周期、浏览器可达性、复杂组件状态和人工判断都可能不在单元测试里。HAT 把这些验收条件变成可交接产物，避免“代码已改完”和“用户能用”之间断裂。

## Mental Model

HAT 是交付闭环中的验收协议层：

```text
TDD / CI / review -> hat-prepare -> hat-run / human HAT -> PR evidence -> merge
```

- `hat-prepare` 定义验收环境、数据、账号、清单和幂等准备脚本。
- `hat-run` 只消费 prepare 产物，按 P0/P1/P2 执行并保存证据。
- `hat-dispatch` 批量调度 HAT，但必须先判断环境、数据和任务冲突。
- `hat-copilot` 和 `hat-prepare-for-human` 把 HAT 产物降门槛给人类验收。

## Key Claims

- explicit: HAT 不是单元测试替代品，而是补足用户视角完整路径验证。
- explicit: `hat-prepare` 的环境模式可分为 blank、fork、attach；输出应包含 guide、账号/数据需求、P0/P1/P2 清单和幂等 `prepare.sh`。
- explicit: `hat-run` 的输入只认 `hat-prepare` 产物，报告应包含 summary、人工介入项、截图和 logs。
- explicit: P0 主路径失败时应优先停止，避免继续执行低优先级探索项掩盖核心失败。
- explicit: HAT-friendly 前端需要稳定 testid/aria、URL 化状态、关键日志和低脆弱度操作入口。
- explicit: HAT-friendly 后端至少需要可观测、日志、OTEL console 输出和 Request Id 串联。
- inferred: HAT 的核心难点不是选哪个自动化工具，而是把认证、数据、服务生命周期、权限和人工判断组织成可恢复协议。
- inferred: 批量 HAT 只有在环境隔离和数据依赖清晰时才适合并发，否则调度器应降级为串行或要求人工介入。

## Common Confusions

- HAT 不是“再跑一遍测试”；它检查的是用户路径、环境准备、数据可用性和证据可交接性。
- HAT-friendly 不是只给项目加 Playwright；它要求产品状态、选择器、日志和后端追踪都对 Agent 可读。
- 自动化 HAT 不能覆盖所有判断；当验证码、权限或视觉判断无法稳定自动化时，应显式输出 human manual 步骤。

## Evidence

- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Prepare验收测试准备hat-prepare.xmind|hat-prepare]] — 定义 HAT 准备阶段的环境模式、P0/P1/P2 清单和幂等 `prepare.sh`。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT - Hand Acceptance Test Run验收测试执行hat-run.xmind|hat-run]] — 定义 HAT 执行阶段、工具选择、P0 停止规则、报告和现实阻碍。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext HAT workerHAT 批量执行器hat-dispatch.xmind|hat-dispatch]] — 补充批量 HAT 调度的冲突风险。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext hat-copilot Agent 辅助验收.xmind|hat-copilot]] — 补充 Agent 辅助人类验收的位置。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext hat-prepare-for-human给人类准备的验收向导.xmind|hat-prepare-for-human]] — 补充把 HAT 产物转成人类验收向导的桥接角色。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 前端项目如何 Agents HAT Friendly.xmind|hat-frontend-friendly]] — 说明前端项目如何降低自动化验收脆弱性。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/Ext 后端项目如何 Agents HAT Friendly.xmind|hat-backend-friendly]] — 说明后端 HAT-friendly 的可观测性最低要求。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/我的流程.xmind|我的流程]] — 把 HAT 放入实现、review、PR 和合并之间的完整工作流。
- [[sources/Vibe/工具/mattpocock:skills  ⭐/定制化.xmind|定制化]] — 早期 HAT skill 体系证据。

## Relations

- part-of: [[concepts/Agent 工作流技能编排|Agent 工作流技能编排]] — HAT 是 workflow skills 中的验收协议层。
- part-of: [[concepts/Agent Harness|Agent Harness]] — HAT 属于 harness feedback layer 和 acceptance baseline。
- enables: [[concepts/反捷径证据|反捷径证据]] — HAT 用用户路径和运行证据补足测试过拟合风险。
- used-in: [[synthesis/GitHub 驱动的 Agent 开发闭环|GitHub 驱动的 Agent 开发闭环]] — HAT 是 PR 合并前的证据门。
- used-in: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — HAT 是 L4 Evidence 层的核心工具。
- related: [[concepts/Agent 可观测性|Agent 可观测性]] — HAT 运行依赖日志、截图、请求链路和 artifacts。
- map-entry: [[maps/Vibe Coding 工具地图|Vibe Coding 工具地图]]

## My Understanding

当前理解：HAT 是把“我看过能用”工程化成 Agent 和人类都能接力执行的验收协议。

## Review Questions

- `hat-prepare` 和 `hat-run` 的边界是什么？
- 为什么 HAT-friendly 前端需要 URL 化状态和稳定选择器？
- 批量 HAT 为什么不能默认并发？

## Open Questions

- HAT 在不同项目风险等级下的最小可用版本还需要真实项目案例校准。
