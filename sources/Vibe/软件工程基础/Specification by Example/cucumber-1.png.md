---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/cucumber-1.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/cucumber-1.png"
raw_created_at: 2026-05-05T05:23:00.833374+00:00
raw_modified_at: 2026-05-05T05:23:16.428693+00:00
raw_size: 1713255
raw_fingerprint: "size=1713255;birth=2026-05-05T05:23:00.833374+00:00;mtime=2026-05-05T05:23:16.428693+00:00"
raw_snapshot_at: 2026-05-29T16:15:48+00:00
ingested_at: 2026-05-30
status: ingested
---

# cucumber-1.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/cucumber-1.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/cucumber-1.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/cucumber-1.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T05:23:00.833374+00:00`; modified `2026-05-05T05:23:16.428693+00:00`; size `1713255`; snapshot `2026-05-29T16:15:48+00:00`
- Coverage: Vision read of a 1055x1491 infographic explaining how Cucumber works from Gherkin scenarios to automation execution and reports.

## Summary

这张图说明 Cucumber 是把业务可读的 Given-When-Then 场景映射到自动化测试代码的运行器；它负责理解业务场景与步骤匹配，真正执行动作的是 Playwright、Selenium、Appium 或 API Client 等自动化工具。

## Source Digest

图中先定义 Cucumber：它不是点击按钮、打开浏览器或操作 App 的执行框架，而是把业务可读场景转换成可执行自动化代码的翻译层。核心运行链路是 `.feature` 中的 Feature/Scenario/Given-When-Then，经步骤匹配找到 Step Definitions，再由自动化工具执行，随后做断言验证并输出通过/失败、截图或日志报告。

组件层面，图中列出 `.feature` 文件、Step Definitions、Hooks、World/Context 和自动化框架。`.feature` 承载业务语言，Step Definitions 把自然语言绑定到代码，Hooks 做场景前后初始化和清理，World/Context 在一个场景内共享状态，自动化框架负责驱动 Web、Mobile 或 API。最小登录示例展示 Gherkin 步骤如何对应到 page.goto、fill/click、assert URL/欢迎语等执行逻辑。图底部把同一机制扩展到 Web App、Mobile App 和 API/Backend，说明 Cucumber 职责稳定：场景、步骤、执行。

## Key Claims

- explicit: Cucumber 负责读懂业务场景，Playwright/Selenium/Appium/API Client 负责真正执行自动化。
- explicit: Cucumber 的核心链路是 Feature/Scenario 到 Step 匹配，再到 Step Definitions、自动化执行、断言验证和报告输出。
- explicit: Feature 是业务语言，Step Definitions 是翻译层，Framework 是执行层。
- explicit: Hooks 用于场景前后初始化和清理，World/Context 用于在单个场景内共享 page、user、response 等状态。
- explicit: 同一机制可用于 Web App、Mobile App 和 API/Backend。
- inferred: 这张图适合支撑“Cucumber 是协作规格运行器而不是自动化框架本身”的概念边界。

## External Links

No external links found in extracted content.

## Links

- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]] — 可放入 Cucumber 和 BDD 工具链模块。

## Maintenance Notes

- Vision-based ingest; no URLs are visible in the image.
- No compiled pages were created in this batch by scope constraint.

- Link cleanup candidate: compiled-concept: Cucumber — 本图提供 Cucumber 的职责边界、运行链路和组件结构。.
- Link cleanup candidate: compiled-concept: Gherkin — 本图展示 Given-When-Then 场景如何绑定到执行代码。.
