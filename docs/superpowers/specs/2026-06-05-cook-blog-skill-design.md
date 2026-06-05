# Cook Blog Skill Design

## Status

Approved for design by user on 2026-06-05. This spec describes the first implementation slice only: create a DSL-backed `ai-wiki-cook-blog` skill. It does not implement the skill yet.

## Goal

Create `ai-wiki-cook-blog`, a new AI wiki cook skill that turns one public, readable blog article URL into a Chinese `human/inbox` note with a required infographic. The skill is a human-inbox cooking workflow, not canonical wiki ingest.

## Scope

The first version supports only a single public blog article URL. It should handle the main article page itself: title, author, visible publication date, article body, body images, code blocks, tables, and body links.

It must not handle site homepages, series index pages, search results, newsletters as mail artifacts, X/Twitter posts, GitHub repositories, Apple Podcasts episodes, user thought snapshots, canonical ingest, source coverage, or external research.

## Design Decisions

- Use a new independent skill directory: `.codex/skills/ai-wiki-cook-blog/`.
- Generate the skill with the Python Skill Contract DSL style required by `create-dsl-skills`.
- Keep the first version pure contract-driven: no bundled extraction script.
- Use browser observation first, then same-URL public HTML/readability extraction as fallback.
- Do not log in, use account state, search, open external links, or switch to another source.
- Do not save the article's full extracted text in cache or final note.
- Treat the infographic as required; image generation or asset persistence failure blocks final note creation.
- Do not update `index.md`, `log.md`, `sources/`, `human/sources/`, `concepts/`, `entities/`, `synthesis/`, `maps/`, or `questions/` unless the user separately asks for ingest or compile.

## Files

Add:

```text
.codex/skills/ai-wiki-cook-blog/SKILL.md
.codex/skills/ai-wiki-cook-blog/agents/openai.yaml
```

Runtime outputs, created only when the skill is used:

```text
.codex/cache/cook-blog/<url-hash>/
  capture.md
  screenshot.png          # optional, only when useful for later review
  imagegen-original.*

human/inbox/cook-blog/YYYY-MM-DD_<中文主题标题>_<站点或作者>.md
human/inbox/cook-blog/assets/YYYY-MM-DD_<中文主题标题>_<站点或作者>/infographic.webp
```

## Skill Frontmatter

Use:

```yaml
---
name: ai-wiki-cook-blog
description: 将单篇公开可见博客文章 URL 烹饪成 AI wiki human inbox 笔记。用户给出 blog/article URL，并希望浏览器优先、同 URL 公开 HTML/readability fallback 地消费主文章正文、生成中文消化笔记和必选信息图，而不是 ingest 进 canonical wiki graph 时使用。
---
```

## DSL Contract Shape

`SKILL.md` should contain only the frontmatter and one Python Skill Contract DSL block.

The contract should include:

- `skill(...)`: declares `ai-wiki-cook-blog`.
- `activate_when(...)`: public blog/article URL to human inbox note.
- `do_not_activate_when(...)`: excludes tweet, GitHub, podcast, user thought, canonical ingest, site crawling, external research, and link verification workflows.
- `inputs(...)`: required `article_url`; optional user focus or title preference.
- `outputs(...)`: `capture_record`, `cooked_note`, `infographic_asset`, and `source_manifest`.
- `environment(...)`: browser automation, `python3` or equivalent HTML/readability fallback, image generation, and agent-initiated network access limited to the input URL plus same-URL HTML retrieval.
- `decision_rules(...)`: single-article gate, same-URL fallback, no external links, no comments, no full-text cache, and blocking behavior.
- `workflow(...)`: linear execution with `call_tool(...)` markers for browser capture, HTML/readability fallback, and imagegen.
- `quality_bar(...)`: final note quality, boundary compliance, image requirement, evidence separation, and source manifest completeness.
- `examples(...)`: a small set covering a readable blog article, a login/paywall blocker, and a non-article URL blocker.

## Workflow

1. Read `AGENTS.md` rules for `human/inbox`, human boundary, and non-canonical cook outputs.
2. Validate that the input is a single article URL. Block homepages, series pages, aggregation pages, and search results.
3. Open the URL with browser automation and observe the readable page.
4. Extract only the main article surface: title, author, publication date, body structure, body media references, code/table content summaries, and body links.
5. Exclude comments, recommendation modules, ads, newsletter signup forms, nav, footer, and unrelated site chrome.
6. If browser capture does not reveal enough article body, use public HTML/readability extraction from the same URL.
7. If both capture paths fail, write an optional blocker `capture.md`, report the blocker, and do not create a final note or infographic.
8. Write `.codex/cache/cook-blog/<url-hash>/capture.md` as structured observation, not full text.
9. Cook the article into a Chinese learning note that distinguishes author claims, Agent inference, and personal inspiration.
10. Generate a Chinese infographic from the cooked understanding.
11. Copy the imagegen original into cache and write final `infographic.webp` under colocated inbox assets.
12. Write the final Obsidian Markdown note to `human/inbox/cook-blog/`.

## Capture Record

`capture.md` should include:

- input URL and canonical URL if visible or derivable from the page.
- captured timestamp.
- capture method: browser, readability fallback, or both.
- page title, site, visible author, and visible published date.
- article outline and section structure.
- key claims and a small number of short high-signal excerpts.
- body links with anchor text and target URL, marked not verified.
- body media/code/table observations when relevant.
- explicit exclusions: comments, ads, recommendations, signup boxes, nav, footer.
- limitations and blockers.

It must not preserve the full article text.

## Final Note

Frontmatter:

```yaml
---
type: cook-blog
ingest_policy: on-request
inbox_status: unread
inbox_created_at: YYYY-MM-DD
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: blog-article
source_url: <input URL>
canonical_url: <canonical URL if known>
site: <site name if visible>
author: <author if visible>
published_at: <date if visible>
captured_at: YYYY-MM-DDTHH:MM:SS+TZ
---
```

Recommended body:

```markdown
# <中文主题标题>

## 速读
## 原文
## 内容地图
## 关键论点
## 核心内容
## 关键洞察
## 批判性点评
## 对我的启发
## 可以继续追的问题
## 信息图
![[human/inbox/cook-blog/assets/<note-stem>/infographic.webp]]
## 遗漏与不确定
## Source Manifest
```

The note should be Chinese by default, preserve necessary English terms, avoid full-text copying, and make the original URL available. `关键论点` must distinguish `作者明确说法`, `Agent 推断`, and `我的启发`.

## Failure Policy

Blocked conditions:

- The URL is not a single article URL.
- The page requires login, subscription, payment, or account state to reveal enough article body.
- Browser capture and same-URL public HTML/readability fallback both fail.
- The available body is too sparse to support a useful note.
- Image generation fails.
- The imagegen original cannot be copied into cache.
- The final `infographic.webp` cannot be written.

Non-blocking limitations:

- External links are not opened or verified.
- Publication date, author, or canonical URL may be missing.
- Body images may be visible but not deeply interpreted.
- Readability fallback may omit some inline formatting.

All non-blocking limitations must be recorded in `遗漏与不确定` and `Source Manifest`.

## Validation

After implementation, run:

```bash
python3 /Users/ivan/.agents/skills/create-dsl-skills/scripts/validate_contract.py \
  .codex/skills/ai-wiki-cook-blog \
  --examples
```

Also perform semantic review:

- Frontmatter description is no broader than `activate_when`.
- `do_not_activate_when` excludes neighboring cook and ingest skills.
- Required inputs are consumed by workflow steps.
- Required outputs are written by workflow steps.
- Browser-first and same-URL fallback rules do not permit source switching.
- Blocked paths do not write final notes.
- Image failure blocks final note creation.
- The note remains `human/inbox`, not canonical source coverage.

## Non-Goals

- No crawler.
- No site discovery.
- No feed parsing.
- No series summarization.
- No external link research.
- No claim verification beyond the article itself.
- No bundled extraction script in the first version.
- No modification of existing cook skills.

## Source Manifest

- User request: add a `cook blog` skill similar to `cook tweet`, aligned through brainstorming.
- User decisions: public single blog article only; browser first plus same-URL public HTML/readability fallback; single URL only; infographic required; no full-text cache; no external link opening; main article body only.
- Project guide: `AGENTS.md` human inbox and non-canonical cook boundaries.
- Existing patterns: `.codex/skills/ai-wiki-cook-tweet/SKILL.md`, `.codex/skills/ai-wiki-cook-github/SKILL.md`, `.codex/skills/ai-wiki-cook-podcast/SKILL.md`, `.codex/skills/ai-wiki-cook-my-mind/SKILL.md`.
- DSL source: `/Users/ivan/.agents/skills/create-dsl-skills/SKILL.md` and `/Users/ivan/.agents/skills/create-dsl-skills/references/contract.pyi`.
- Cache/output convention: existing `cook-*` skills use `.codex/cache/cook-*` and `human/inbox/cook-*`.
