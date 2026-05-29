---
page_type: concept
updated_at: 2026-05-30
status: active
source_count: 3
learning_status: new
confidence: 3
difficulty: 4
review_after: 2026-06-06
---

# Agent 沙箱

## Definition

Agent 沙箱是为 Agent 执行命令、读写文件、运行代码、访问浏览器或调用外部工具提供隔离、资源控制、审计和生命周期管理的运行环境。

## Why It Matters

Agent 越能行动，越需要隔离。没有沙箱，代码执行、文件修改、依赖安装、浏览器操作和工具调用会直接暴露主机、用户数据和其他任务。

## Mental Model

沙箱是 Agent 的工作间：允许它动手，但限制它能动哪些东西、用多少资源、留下什么证据、什么时候销毁。

## Key Claims

- 同机多用户账户实现简单，但资源隔离和逃逸风险弱，适合可信小团队。
- 独立容器或虚拟机提供更强文件系统、进程空间和资源配额隔离。
- `nsjail`、`bubblewrap`、`firejail` 是比完整容器更轻量的候选隔离层。
- Agent 沙箱不只是代码执行，还应覆盖 shell、file、browser、MCP、VSCode server、日志和回收机制。
- 沙箱选型应比较隔离强度、资源控制、生命周期成本、工具覆盖和编排复杂度。

## Examples

- `沙箱.xmind` 比较多用户账号、容器/虚拟机、轻量沙箱和 OpenSandbox/agent-infra。
- `沙箱PRD.md` 将 nsjail MVP、SSE 命令输出和会话隔离落到产品需求。
- `闪极智能体 2.excalidraw` 中的运行时图展示沙箱与 Agent 执行链路关系。

## Common Confusions

- Docker 容器不是唯一沙箱，也不自动等于安全边界完整。
- 沙箱不是只防危险命令，也负责资源配额、可回放日志、运行环境一致性和清理。
- 给 Agent 远程 shell 前，应先明确用户/任务隔离和输出协议。

## Evidence

- [[sources/Agent/沙箱.xmind|沙箱.xmind]]
- [[sources/Agent/闪极智能体/沙箱PRD|沙箱PRD]]
- [[sources/Agent/闪极智能体/闪极智能体 2.excalidraw|闪极智能体 2.excalidraw]]

## Relations

- part-of: [[concepts/Agent Harness|Agent Harness]]
- used-in: [[concepts/AI Agent|AI Agent]]
- used-in: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]

## My Understanding

当前理解：Agent 沙箱是把“允许 Agent 执行”变成“允许它在受控空间执行”的工程边界。

## Review Questions

- 多用户账号、容器、虚拟机和轻量沙箱分别适合什么场景？
- Agent 沙箱为什么需要日志和生命周期管理？
- Shell 输出协议为什么也是沙箱产品的一部分？

## Open Questions

- OpenSandbox、agent-infra/sandbox、nsjail 等当前能力未联网核验。
