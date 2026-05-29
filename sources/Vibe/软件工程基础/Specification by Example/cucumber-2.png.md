---
source_type: image
raw_path: "/Users/ivan/Library/Mobile Documents/com~apple~CloudDocs/思维导图/AI/Vibe/软件工程基础/Specification by Example/cucumber-2.png"
source_relpath: "Vibe/软件工程基础/Specification by Example/cucumber-2.png"
raw_created_at: 2026-05-05T05:23:15.902016+00:00
raw_modified_at: 2026-05-05T05:23:37.810365+00:00
raw_size: 1813140
raw_fingerprint: "size=1813140;birth=2026-05-05T05:23:15.902016+00:00;mtime=2026-05-05T05:23:37.810365+00:00"
raw_snapshot_at: 2026-05-29T16:15:48+00:00
ingested_at: 2026-05-30
status: ingested
---

# cucumber-2.png

## Source

- Raw file: [Vibe/软件工程基础/Specification by Example/cucumber-2.png](<finderx://open?icloud=%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE/AI/Vibe/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80/Specification%20by%20Example/cucumber-2.png>)
- Raw ref: `raw:Vibe/软件工程基础/Specification by Example/cucumber-2.png`
- Type: image
- Status: ingested
- Raw metadata: created `2026-05-05T05:23:15.902016+00:00`; modified `2026-05-05T05:23:37.810365+00:00`; size `1813140`; snapshot `2026-05-29T16:15:48+00:00`
- Coverage: Vision read of a 1086x1448 infographic about engineering complex Web/Mobile/API end-to-end tests with Cucumber.

## Summary

这张图把复杂 App 的 Cucumber E2E 落地原则概括为：Feature 写业务意图，技术细节下沉到 Step Definitions、Workflow/Service、Page Object/Screenplay、自动化执行层和被测系统；复杂度向下沉，业务语义向上浮。

## Source Digest

图中指出复杂 App 的 E2E 不能把所有点击、输入、跳转都直接写进 Gherkin。错误示例把下单流程拆成打开浏览器、点击登录、输入邮箱密码、点击商品、加入购物车、结算等 UI 细节，导致场景过长、业务看不懂、维护成本高。更好的写法聚焦业务行为：已登录用户可以买有库存的商品，购买后订单成功且库存减少。

真实项目分层架构将 Feature/Scenario 作为业务场景层，Step Definitions 作为步骤绑定层，Workflow/Service 封装跨页面业务流程，Page Object/Screenplay 隔离页面细节，Playwright/Selenium/Appium/API Client 负责驱动浏览器、App 或接口，底层是 Web/Mobile/Backend 被测系统。图中电商购买示例把登录状态准备、库存准备、购买流程和结果验证拆到执行逻辑。工程化配套包括 Hooks、World/Context、Test Data、Tags/CI。最佳实践强调 Feature 写业务不写 selector，Step Definition 保持轻薄，关键流程用 Workflow 封装，只让少量关键路径做 E2E；常见误区包括把 Cucumber 当脚本翻译器、一个 Scenario 写 30 多步、过度复用万能步骤、所有测试都堆成端到端。

## Key Claims

- explicit: 复杂 App 的 E2E 不应把所有点击、输入、跳转直接写进 Gherkin。
- explicit: 更好的 Feature 写法应聚焦业务行为、规则与结果，而不是暴露 UI 操作细节。
- explicit: 真实项目中的 Cucumber 分层包括 Feature/Scenario、Step Definitions、Workflow/Service、Page Object/Screenplay、自动化执行层和被测系统。
- explicit: Hooks、World/Context、Test Data、Tags/CI 是复杂测试稳定运行的工程化配套。
- explicit: 最佳实践包括 Feature 写业务、Step Definition 保持轻薄、关键流程用 Workflow 封装、只让少量关键路径做 E2E。
- inferred: 这张图可与 `cucumber-1.png` 共同支撑 Cucumber 从机制理解到工程分层落地的学习路径。

## External Links

No external links found in extracted content.

## Links

- compiled-concept: Cucumber — 本图补充复杂项目中的 Cucumber 分层架构和反模式。
- compiled-concept: 端到端测试分层 — 本图说明 E2E 复杂度下沉和业务语义上浮。
- map-entry: [[maps/Vibe 软件工程基础学习地图|Vibe 软件工程基础学习地图]] — 可作为 Cucumber 工程化落地模块。

## Maintenance Notes

- Vision-based ingest; exact Gherkin examples should be rechecked against raw image before verbatim reuse.
- No compiled pages were created in this batch by scope constraint.
