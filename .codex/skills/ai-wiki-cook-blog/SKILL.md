---
name: ai-wiki-cook-blog
description: 用户给出单篇公开可见 blog/article URL，并要求 cook、烹饪或消化成 AI wiki human inbox 笔记和必选信息图时使用；浏览器优先，同 URL 公开 HTML/readability fallback，不进入 canonical wiki ingest。
---

```python
from skill_contract import *

skill(
    name="ai-wiki-cook-blog",
    purpose="将单篇公开可见博客文章烹饪成带信息图的 AI wiki human inbox 笔记。",
)

activate_when([
    "用户给出单篇公开可见 blog、博客文章、article 或网页长文 URL，并要求 cook、烹饪、消化或整理成 AI wiki human inbox 笔记",
])

do_not_activate_when([
    "用户给出 X/Twitter、GitHub repository、Apple Podcasts 或 cook my mind 输入；改用对应 cook skill",
    "用户要求 ingest、compile、source coverage、human/raw 处理、source note、index 或 log 更新",
    "用户要求抓取整个网站、从首页发现文章、RSS/feed 解析、系列综述、外链研究或事实核验",
    "输入不是单篇文章 URL，而是主页、目录页、搜索结果、tag 页、newsletter archive 或聚合页",
])

inputs(
    required=[
        input("article_url", type=URL, description="要 cook 的单篇公开博客文章 URL。"),
    ],
    optional=[
        input("user_focus", type=NaturalLanguage, description="用户特别希望关注的问题、角度或用途。", required=False),
        input("title_preference", type=Text, description="用户给出的笔记标题偏好。", required=False),
    ],
)

outputs(
    required=[
        output("capture_record", type=File, description=".codex/cache/cook-blog/<url-hash>/capture.md，结构化观察和限制记录，不保存完整正文。"),
        output(
            "cooked_note",
            type=File,
            description="human/inbox/cook-blog/YYYY-MM-DD_<中文主题标题>_<站点或作者>.md。",
            required_sections=[
                "速读",
                "原文",
                "内容地图",
                "关键论点",
                "核心内容",
                "关键洞察",
                "批判性点评",
                "对我的启发",
                "可以继续追的问题",
                "信息图",
                "遗漏与不确定",
                "Source Manifest",
            ],
        ),
        output("infographic_asset", type=File, description="human/inbox/cook-blog/assets/<note-stem>/infographic.webp。"),
        output("source_manifest", type=Text, description="最终 note 中的 Source Manifest。"),
    ],
)

environment(
    commands=["python3", "rg"],
    dependencies=["browser automation", "public HTML/readability extraction when needed", "image generation"],
    network="required",
    filesystem="workspace",
)

decision_rules([
    when("article_url is missing", then="ask for exactly one public article URL"),
    when("input is a neighboring cook type", then="stop and route to the matching cook skill"),
    when("input is not a single article URL", then="block and ask for a single article URL; do not discover articles automatically"),
    when("browser capture exposes enough main article body", then="use browser capture as source of truth", else_="try same-URL public HTML/readability fallback"),
    when("fallback is needed", then="fetch only the input URL or a page-declared canonical same-article URL; do not search, open mirrors, use third-party caches, or open external links"),
    when("browser capture and fallback both fail", then="write optional blocker capture.md and stop without infographic or final note"),
    when("imagegen, cache-original persistence, or final infographic.webp persistence fails", then="block and do not write the final note"),
])

workflow([
    step(
        "read_project_rules",
        "Read AGENTS.md human boundary, human/inbox workflow, and non-canonical cook output rules before writing any output.",
        writes=["project_rules"],
    ),
    step(
        "classify_and_prepare",
        "Confirm article_url is one public article, reject neighboring cook and non-article inputs, then derive .codex/cache/cook-blog/<url-hash>/ and human/inbox/cook-blog/ paths.",
        reads=["article_url", "title_preference"],
        writes=["input_classification", "cache_paths", "note_paths"],
    ),
    step(
        "capture_article",
        f"""
        Capture only the main article surface: title, site, author, date, headings, body structure, short evidence excerpts, body links, images, code, and tables. Exclude comments, recommendations, ads, signup forms, navigation, footer, and unrelated page chrome.
        Use {call_tool(
            "browser automation",
            how="open article_url without login or account state, wait for the page to settle, inspect the public visible article, and judge whether the main body is readable",
            expect="structured browser observations or a clear browser blocker",
            on_failure="record the browser failure and try same-URL public HTML/readability fallback",
        )}.
        If browser observations are insufficient, use {call_tool(
            "python3 public HTML/readability fallback",
            how="fetch only article_url or a visibly declared canonical same-article URL; extract structured article observations without saving full extracted text",
            expect="structured article observations or a clear blocker",
            on_failure="write optional blocker capture.md and stop without final note or infographic",
        )}.
        """,
        reads=["article_url", "input_classification"],
        writes=["article_observations"],
    ),
    step(
        "write_capture_record",
        "Write capture.md with input URL, canonical URL if known, captured_at, capture method, browser/readability actions, article outline, key claims, short excerpts, body links marked not verified, media/code/table observations, exclusions, limitations, and blockers. Do not preserve full article text.",
        reads=["article_observations", "cache_paths"],
        writes=["capture_record"],
    ),
    step(
        "stop_on_blocker",
        "If capture_record shows unreadable, paywalled, login-gated, non-article, or too-sparse content, report the blocker and cache evidence path; do not generate an infographic or final note.",
        reads=["capture_record"],
    ),
    step(
        "draft_note",
        "Write the Chinese cooked note draft from capture_record. Preserve the original URL, include a content map, distinguish 作者明确说法 / Agent 推断 / 我的启发, include critical commentary, and apply user_focus only when supported by the article evidence.",
        reads=["capture_record", "user_focus", "project_rules"],
        writes=["cooked_note_draft"],
    ),
    step(
        "generate_and_persist_infographic",
        f"""
        Generate and persist the required Chinese infographic.
        Use {call_tool(
            "imagegen",
            how="create a bitmap infographic from the cooked understanding; make it a review aid covering core thesis, structure, claims, tensions, and useful implications",
            expect="imagegen original copied to cache and final infographic.webp written to human/inbox/cook-blog/assets/<note-stem>/",
            on_failure="block and do not write the final note",
        )}.
        """,
        reads=["cooked_note_draft", "cache_paths", "note_paths"],
        writes=["infographic_asset"],
    ),
    step(
        "write_final_note",
        "Write the final Obsidian Markdown note under human/inbox/cook-blog/ with cook-blog frontmatter, required sections, infographic wikilink, limitations, and Source Manifest. Do not update canonical graph files unless the user separately asks for ingest or compile.",
        reads=["cooked_note_draft", "capture_record", "infographic_asset", "note_paths"],
        writes=["cooked_note", "source_manifest"],
    ),
    step(
        "report_result",
        "Report note path, infographic path, cache path, and limitations; if blocked, report blocker and cache evidence path instead.",
        reads=["cooked_note", "infographic_asset", "capture_record"],
    ),
])

quality_bar(
    must=[
        "只处理单篇公开可见博客文章 URL。",
        "只写 human/inbox/cook-blog/ 和 .codex/cache/cook-blog/；不进入 canonical ingest。",
        "浏览器优先；fallback 只能读取同 URL 或页面声明的同文章 canonical URL。",
        "不登录、不用账号态、不搜索、不换来源、不打开外链、不用第三方缓存或镜像。",
        "只消费主文章正文；排除评论、推荐、广告、signup、导航、页脚和无关页面外壳。",
        "capture.md 只保存结构化观察、关键论点、少量短摘录、正文链接线索和限制，不保存完整正文。",
        "最终 note 为中文，frontmatter 使用 type: cook-blog、ingest_policy: on-request、inbox_status: unread、source_kind: blog-article、source_url、captured_at。",
        "最终 note 包含 required_sections，并在关键论点中区分作者明确说法、Agent 推断和我的启发。",
        "外链只记录可见 anchor text 和 URL，并标注未核验。",
        "信息图必选；imagegen、cache 原图或 infographic.webp 任一步失败，都不写最终 note。",
        "Source Manifest 列出 input URL、canonical URL if known、capture method/actions、cache paths、infographic path、exclusions and limitations。",
    ],
    should=[
        "内容地图优先使用 Mermaid mindmap；流程、因果链或决策树可用 flowchart。",
        "文件名优先中文可读，末尾保留站点名、作者或关键英文术语。",
        "作者、日期或 canonical URL 不可见时继续 cook，并在遗漏与不确定中说明。",
    ],
    must_not=[
        "不要更新 index.md、log.md、sources/、human/sources/、concepts/、entities/、synthesis/、maps 或 questions，除非用户明确另行要求 ingest 或 compile。",
        "不要处理站点首页、系列页、搜索结果、tag 页、RSS/feed、newsletter archive 或多个 URL。",
        "不要把评论、推荐阅读或作者 bio 当成主文章论据。",
        "不要把 Agent 推断写成作者原话。",
        "不要声称外链或外部事实已经核验。",
    ],
)

```
