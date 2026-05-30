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

### nsjail MVP 与威胁模型差异（来自 `沙箱PRD.md`）

- 闪极 `沙箱PRD` 是一个基于 `nsjail` 的多用户 Shell 命令执行服务 MVP：Gateway 按 `user_id` 找到或创建用户级 `NsJailService`，`bash -lc` 执行脚本，SSE 流式返回 `status`/`stdout`/`stderr`/`end` 事件，SQLite `commands` 表记录元数据和聚合结果。
- 资源边界明确量化：每用户最多 5 并发（超出排队，排队/运行均可取消），workspace 2GB 配额，单命令 1core/512MB/默认 30 分钟（自定义超时 ≤ 1800s）；完成/取消/超时必须回收整个进程组，空闲 15 分钟可淘汰。
- 隔离边界：jail 内只暴露最小宿主资源，不直接看到宿主 `/app`、其他用户目录或系统数据目录；结果文件放系统目录而非用户 workspace；结果 ≤256KB 入库、>256KB 落文件、>10MB 截断。
- 威胁模型差异是关键：该 PRD 明确声明「不追求强安全对抗」，定位是「可信上游 + 基础隔离 + 可观测执行」，不是不可信代码执行平台；与 `沙箱.xmind` 讨论的强隔离容器/VM 方案处于不同威胁等级，编译时不可混为一谈。

### 沙箱产品化要素

- Shell 输出协议（SSE 事件、不裸 `[DONE]`、客户端断开后命令继续执行）也是沙箱产品的一部分，而不只是隔离机制。

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
- part-of: [[concepts/Agent Runtime|Agent Runtime]]
- used-in: [[concepts/AI Agent|AI Agent]]
- used-in: [[synthesis/Agent 系统工程综述|Agent 系统工程综述]]
- implemented-by: [[entities/闪极智能体|闪极智能体]]
- map-entry: [[maps/Agent 学习地图|Agent 学习地图]]
- entity-candidate: OpenSandbox
- entity-candidate: nsjail

## My Understanding

当前理解：Agent 沙箱是把“允许 Agent 执行”变成“允许它在受控空间执行”的工程边界。

## Review Questions

- 多用户账号、容器、虚拟机和轻量沙箱分别适合什么场景？
- Agent 沙箱为什么需要日志和生命周期管理？
- Shell 输出协议为什么也是沙箱产品的一部分？
- 闪极 nsjail MVP 的「不追求强安全对抗」意味着它适合什么威胁等级？
- nsjail MVP 在并发、配额、超时和进程回收上有哪些具体边界？

## Open Questions

- OpenSandbox、agent-infra/sandbox、nsjail 等当前能力未联网核验。
