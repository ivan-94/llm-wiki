---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 3
review_after: 2026-06-06
---

# Agent MessageBus

## Definition

Agent MessageBus 是 Agent Runtime 中解耦「设备/渠道」与「Agent 主循环」的消息中枢：渠道适配器只负责把外部事件变成标准入站消息，定时任务、控制指令、工具结果和子代理回灌都通过同一条总线流入同一个 Agent Loop。

## Why It Matters

没有 MessageBus，每接一个新渠道（眼镜、IM、cron、webhook）都要改 Agent 主循环，状态容易分裂成多份。有了它，渠道与运行时之间只剩一个稳定契约，新增渠道、定时和子代理都变成「往总线发消息」，不动核心循环。

## Mental Model

MessageBus 像公司前台：不管访客从大门、电话还是邮件进来，都先到前台登记成统一工单，再派给同一个处理流程。Agent 只面对总线，不直接面对千变万化的渠道。

## Key Claims

- `Nano Bot .xmind`：用 `MessageBus` 解耦 channels 与 agent，事件形状集中定义；`AgentLoop.run()` 持续消费 inbound，对 `/stop`、`/restart` 等控制面消息特殊处理，其余进入完整对话链路。
- 定时任务和 heartbeat 最终也回到同一个 Agent 处理，避免状态分裂。
- 子代理结果通过 MessageBus 回灌为下一条入站消息，进入同一主循环（异步结果作为助手侧补充）。
- `闪极智能体.xmind`：MessageBus 承载 inbound、outbound、定时任务、控制指令和第三方 Channel，是设备交互层与 Agent runtime 之间的解耦层。
- `闪极智能体 2.excalidraw`：消息字段含 type、category、id、user_id、session_id、stream_id、context；category 覆盖 toolcall、toolcall_result、answer_start/stream/complete、toast、ask、cron、device_call 等事件类型。

## Examples

- 主动消息（唤醒词/按键）和被动消息（通知/任务回调）都进同一总线，分别触发会话保持或通知确认。
- 平台适配器只需把 IM 事件转成入站消息，不需要理解 Agent 内部逻辑。

## Common Confusions

- MessageBus 不是消息队列产品的同义词；这里强调的是「渠道与 Agent 之间的统一消息契约 + 单一消费循环」。
- 控制消息（`/stop`、`/restart`）与对话消息走同一总线但分流处理，不要混为一类。
- 子代理回灌也是一条入站消息，而不是另起一个独立循环。

## Evidence

- [[sources/Agent/变体/Nano Bot .xmind|Nano Bot .xmind]]
- [[sources/Agent/闪极智能体/闪极智能体.xmind|闪极智能体.xmind]]
- [[sources/Agent/闪极智能体/闪极智能体 2.excalidraw|闪极智能体 2.excalidraw]]

## Relations

- part-of: [[concepts/Agent Runtime|Agent Runtime]]
- enables: [[concepts/子代理委派模式|子代理委派模式]]
- used-in: [[concepts/多 Agent 协作协议|多 Agent 协作协议]]
- implemented-by: [[entities/Nano Bot|Nano Bot]]
- implemented-by: [[entities/闪极智能体|闪极智能体]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：MessageBus 是让「多渠道 + 定时 + 子代理 + 控制指令」共用一个 Agent Loop 的关键解耦点；新增能力变成发消息，而不是改循环。

## Review Questions

- MessageBus 解耦的是哪两层？
- 为什么定时任务和子代理结果也要回到同一条总线？
- 控制消息和对话消息在总线上如何区分处理？

## Open Questions

- 高并发、多用户场景下 MessageBus 的背压和顺序保证策略尚未在 source 中展开。
