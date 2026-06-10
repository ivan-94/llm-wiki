---
source_type: xmind
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind"
source_relpath: "Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind"
raw_created_at: 2026-06-07T13:45:46.670921+00:00
raw_modified_at: 2026-06-10T08:17:29.296168+00:00
raw_size: 1992719
raw_fingerprint: "size=1992719;birth=2026-06-07T13:45:46.670921+00:00;mtime=2026-06-10T08:17:29.296168+00:00"
raw_snapshot_at: 2026-06-10T13:15:10.229472+00:00
ingested_at: 2026-06-10
status: ingested
---

# 垃圾治理(DeSlop).xmind

## Source

- Raw file: [Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/Vibe%20Coding%20%E9%9A%8F%E6%89%8B%E8%AE%B0/%E5%A4%A7%E8%A7%84%E6%A8%A1%20AI%20Coding/%E5%9E%83%E5%9C%BE%E6%B2%BB%E7%90%86%28DeSlop%29.xmind>)
- Raw ref: `raw:Vibe/Vibe Coding 随手记/大规模 AI Coding/垃圾治理(DeSlop).xmind`
- Type: xmind
- Status: ingested
- Raw metadata: created `2026-06-07T13:45:46.670921+00:00`; modified `2026-06-10T08:17:29.296168+00:00`; size `1992719`; snapshot `2026-06-10T13:15:10.229472+00:00`
- Coverage: XMind helper discovered and exported all sheets; sheet count `1`; sheets: `画布 1` (116 topics).

## Source Cluster

- Directory cluster: Vibe/Vibe Coding 随手记/大规模 AI Coding
- Cluster role: expansion
- Neighbor sources:
  - extends-source: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/先污染后治理.xmind|先污染后治理.xmind]] — 本 source 把“污染”具体化为 AI 生成垃圾的来源和治理框架。
  - same-cluster: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/异常治理.xmind|异常治理.xmind]] — 两者都把治理做成可观测、可分诊、可修复的闭环。
  - contrasts-source: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/claude code 大型项目落地.PNG|claude code 大型项目落地.PNG]] — 该图偏落地条件，本 source 偏落地后代码库衰退治理。

## Summary

这份 XMind 把 AI Coding 垃圾定义为“高通量生成、低约束输入、弱验证机制、持久化代码库”的乘积，并提出生成前约束、生成中限权、生成后准入、合并后观测、演化中删除的治理方向。

## Source Digest

source 将 AI 代码垃圾的成因拆成四类机制：补全机制让模型填补未声明假设；局部机制让当前文件或当前报错成立，却破坏全局一致；激励机制让模型和用户被“可见进展”奖励；经济机制让生成变便宜但维护仍昂贵，导致生成速度大于验证速度。

治理方向覆盖代码进入系统的全生命周期：生成前用约束说明什么不能做；生成中按风险分配权限；生成后要求 AI 生成物携带假设、证据、风险和回滚路径；合并后用真实运行观测隐藏假设是否破裂；演化中要求临时代码有删除条件。它还强调复杂度税、上下文清理、reviewer/architect/deleter 等角色治理。

开源工具部分把 `desloppify` 作为机械扫描和主观分析结合的例子：机械侧覆盖调试日志、未使用声明、死 export、废弃符号、大文件、复杂度、God 组件、混合职责、扁平目录、props 膨胀、单次抽象、耦合违规、循环依赖、孤儿文件、门面 re-export、命名、签名、测试覆盖、代码味道、React/Next.js/security/重复等；审查侧覆盖命名、逻辑清晰度、类型安全、契约一致性、错误处理、抽象合理性、AI 生成痕迹、设计一致性、迁移半成品、跨模块架构、初始化耦合、依赖健康、测试策略、API 表面、授权一致性和包组织。source 还提到 `taste-skill` 的设计/前端品味与 `brooks-lint` 的经典工程著作审查路线。

## Key Claims

- explicit: AI 代码垃圾来自高通量生成、低约束输入、弱验证机制和持久化代码库的叠加。
- explicit: 未声明假设、局部最优、进展感奖励和生成/维护经济差，是垃圾积累的主要机制。
- explicit: 治理方向应覆盖生成前约束、生成中限权、生成后准入、合并后观测和演化中删除。
- explicit: AI 生成物准入时应携带假设、证据、风险和回滚路径。
- explicit: `desloppify` 结合机械扫描、主观审查、分诊和 next/resolve 修复循环。
- inferred: DeSlop 治理不是单个 linter，而是把复杂度、上下文、角色、运行时反馈和删除机制合成一套代码库健康治理系统。

## External Links

- tool: [desloppify](https://github.com/peteromallet/desloppify) — source 列为 DeSlop 开源项目；not verified.
- tool: [taste-skill](https://github.com/Leonxlnx/taste-skill) — source 列为设计和前端品味工具；not verified.
- tool: [brooks-lint](https://github.com/hyhmrright/brooks-lint) — source 列为植根经典工程著作的 AI 代码审查工具；not verified.

## Links

- compiled-concept: [[concepts/AI 代码垃圾治理|AI 代码垃圾治理]] — 本 source 提供成因、治理阶段和工具维度。
- updates: [[concepts/软件工厂陷阱|软件工厂陷阱]] — 补充“生成速度大于验证速度”造成代码库衰退的机制。
- updates: [[concepts/Agent Coding Guardrails|Agent Coding Guardrails]] — 补充约束、限权、准入、复杂度和删除条件。
- updates: [[synthesis/Vibe Coding 工程化深度模型|Vibe Coding 工程化深度模型]] — 增强 L3/L4/L5 的治理工具箱。
- map-entry: [[maps/Vibe Coding 学习地图|Vibe Coding 学习地图]] — 纳入大规模 AI Coding 治理路径。
- extends-source: [[sources/Vibe/Vibe Coding 随手记/大规模 AI Coding/先污染后治理.xmind|先污染后治理.xmind]] — 展开“污染”产生机制和治理闭环。

## Maintenance Notes

- 工具链接均未联网核验；当前只记录 raw 中出现的 URL 和用途。
- `desloppify` 指标清单较细，本 note 已消化到维度层；具体阈值仍应回 raw 或工具文档核对。
