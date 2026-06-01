---
name: ai-wiki-cook-github
description: 将 GitHub 仓库 URL 烹饪成 AI wiki human inbox 笔记。用户给出 github.com 的仓库、branch/tag 或 commit 链接，并希望 clone 到临时 cache、创建 low-effort 子 Agent 做只读仓库探索、生成中文项目消化报告和信息图，而不是 ingest 进 canonical wiki graph 时使用。
---

# AI Wiki Cook GitHub

## 目标

把一个 GitHub 仓库 cook 成一篇可以直接阅读、复习和复用的 inbox 笔记。它不是 canonical ingest：默认只写入 `human/inbox/cook-github/`，frontmatter 使用 `ingest_policy: on-request`。除非用户明确要求后续 ingest 或 compile，否则不要更新 `index.md`、`log.md`、`sources/`、`human/sources/`、concepts、entities、synthesis、maps 或 questions。

## 输出边界

Obsidian 可见输出：

```text
human/inbox/cook-github/YYYY-MM-DD_<中文项目主题>_<owner_repo>.md
human/inbox/cook-github/assets/YYYY-MM-DD_<中文项目主题>_<owner_repo>/infographic.webp
```

机器缓存：

```text
.codex/cache/cook-github/<owner>-<repo>-<ref-or-commit>/
  repo/
  repo-metadata.json
  file-inventory.txt
  exploration-report.md
  imagegen-original.*
```

`.codex/cache/` 必须保持 git ignored。`exploration-report.md` 是 low-effort 子 Agent 返回、由父 Agent 落盘的只读探索报告，不是最终笔记。

## 必读上下文

写最终笔记前，读取 `AGENTS.md` 中与 human boundary、`human/inbox/`、`human/raw/` 有关的规则。不要把 cooked note 当作 source note。

## 硬规则

- 默认只做 read-only 静态分析。不要运行仓库代码，不要安装依赖，不要执行 repo scripts、测试、构建、Docker、未知二进制或联网拉取依赖。
- 必须创建一个 low-effort 子 Agent 探索仓库。父 Agent 可以补读关键文件，但不能省略子 Agent 探索报告。
- 子 Agent 不直接写父工作区文件。它只返回探索报告正文；父 Agent 负责把该正文写入 `.codex/cache/cook-github/<id>/exploration-report.md`。子 Agent 不写最终 Obsidian note，不生成信息图，不改仓库文件。
- 不设硬性文件数、大小或读取预算限制；但应跳过明显无价值或危险的目录和产物，如 `.git/`、`node_modules/`、`.venv/`、`dist/`、`build/`、`target/`、large binary/media，除非它们是项目核心证据。
- 信息图是必选输出。如果 imagegen 不可用、生成失败、无法复制原图到 cache、或无法产出最终 `infographic.webp`，本次 cook 视为 blocked：保留 clone、metadata、inventory、exploration report 和诊断材料，向用户说明 blocker，不写最终 cooked note。
- 不默认联网补充 GitHub 平台状态。除 `git clone` / `git fetch` 取得指定代码版本外，不查 stars、issues、PR、releases、Actions 当前状态或 README 网页渲染结果。

## 输入和 Ref 解析

支持输入：

```text
https://github.com/<owner>/<repo>
https://github.com/<owner>/<repo>/tree/<branch-or-tag>
https://github.com/<owner>/<repo>/commit/<sha>
```

规则：

- 普通仓库 URL：clone 默认分支。
- `tree/<branch-or-tag>`：clone 后 checkout 该 branch/tag。
- `commit/<sha>`：fetch/checkout 该 commit。
- 记录 `requested_ref`、`resolved_commit` 和 `default_branch`。如果 ref 解析失败，fail fast，不写最终 note。

推荐命令形态：

```bash
git clone --depth 1 --no-recurse-submodules "<github-url>" ".codex/cache/cook-github/<id>/repo"
git -C ".codex/cache/cook-github/<id>/repo" rev-parse HEAD
git -C ".codex/cache/cook-github/<id>/repo" branch --show-current
git -C ".codex/cache/cook-github/<id>/repo" ls-files > ".codex/cache/cook-github/<id>/file-inventory.txt"
```

需要指定 branch/tag/commit 时可以调整 fetch/checkout，但仍保持 read-only。不要初始化 submodules，除非用户明确要求并接受额外来源边界。

## 父/子 Agent 工作流

1. 父 Agent 解析 GitHub URL，建立 cache 目录，clone 仓库。
2. 父 Agent 写 `repo-metadata.json`：
   - input URL、normalized GitHub URL、owner、repo。
   - requested ref、resolved commit、default branch。
   - clone command、cloned_at、cache path。
   - read-only boundary 和已知 clone/ref 限制。
3. 父 Agent 写 `file-inventory.txt`。
4. 父 Agent 创建一个 low-effort 子 Agent，并只给它探索任务：
   - 在 cloned repo 中做 read-only 静态探索。
   - 读取 README、docs、入口文件、配置、CI、examples、核心源码路径。
   - 不运行代码，不安装依赖，不修改文件。
   - 返回符合“子 Agent 探索报告要求”的完整 Markdown 报告正文。
5. 父 Agent 将子 Agent 返回正文原样落盘到 `.codex/cache/cook-github/<id>/exploration-report.md`。
6. 父 Agent 读取 `exploration-report.md`，必要时补读关键文件。
7. 父 Agent 生成信息图。
8. 父 Agent 写最终 cooked note 到 `human/inbox/cook-github/`。

## 子 Agent 探索报告要求

`exploration-report.md` 必须包含：

````markdown
# Exploration Report

## One-line Positioning

## README Claims

## Repository Map

## Tech Stack And Dependencies

## Entry Points

## Core Modules

## Architecture Sketch

```mermaid
flowchart LR
```

## Data Flow Or Control Flow

## Usage And Deployment Clues

## Risks And Unknowns

## Files Read
````

`Files Read` 必须列出实际读取过的文件路径。无法完整覆盖时，在 `Risks And Unknowns` 说明 coverage limitation。

## Cook 工作流

1. 最终报告以学习型 cooked note 为主，附带轻量工程判断；不要写成安全审计、性能评测或代码质量打分。
2. 可以保留少量高信号短摘录：public API signature、CLI usage、配置片段、入口函数/模块名、README 自述短句。不要粘贴长源码、完整 README、大段 license、完整 dependency list 或 exploration report 全文。
3. 生成信息图：
   - 使用 `imagegen` skill/tool 的内置模式。
   - prompt 来自已经 cook 过的理解：项目定位、解决的问题、核心特性、架构组件、数据流、关键模块、设计亮点和风险。
   - 默认中文信息图；必要英文术语、包名、模块名、CLI 名称可保留原文并加中文解释。
   - 小项目可以做结构卡；库/框架可以做 API 使用路径或模块关系图；应用可以做用户问题到核心组件的数据流图；CLI 可以做输入到输出的执行路径图。
   - built-in imagegen 默认会把图生成到 `$CODEX_HOME/generated_images/...`；必须把选定原图复制到 `.codex/cache/cook-github/<id>/imagegen-original.<ext>`，再把最终选定图移动、复制或转换为 `human/inbox/cook-github/assets/<note-stem>/infographic.webp`。
4. 最终 Markdown note 由父 Agent 直接写作。不要使用 note builder 脚本拼模板。

## 最终笔记要求

Frontmatter：

```yaml
---
type: cook-github
ingest_policy: on-request
inbox_status: unread
inbox_created_at: YYYY-MM-DD
inbox_read_at:
raw_path:
ingested_at:
archive_reason:
source_kind: github-repository
github_url: <input URL>
normalized_url: <https://github.com/owner/repo>
owner: <owner>
repo: <repo>
requested_ref: <branch/tag/sha/default>
resolved_commit: <sha>
default_branch: <branch if known>
cloned_at: YYYY-MM-DDTHH:MM:SS+TZ
---
```

推荐正文结构：

````markdown
# <中文项目标题>

## 速读

## 仓库定位

## 解决什么问题

## 项目特性

## 典型使用方式

## 主要架构

```mermaid
flowchart LR
```

## 代码地图

## 核心模块

## 数据流 / 控制流

## 依赖与技术栈

## 设计亮点

## 风险与不确定

## 对我的启发

## 可以继续追的问题

## 信息图
![[human/inbox/cook-github/assets/<note-stem>/infographic.webp]]

## Source Manifest
````

质量规则：

- 正文默认中文，保留必要英文术语、包名、模块名和 CLI 名称。
- 文件标题和一级标题默认中文；owner/repo 保留在文件名末尾。
- `主要架构` 默认使用 Mermaid `flowchart`。如果项目更像状态机、时序流程或模块依赖，也可以改用更合适的 Mermaid 图。
- `关键论点` 不是必选章节；仓库报告优先用“特性、架构、代码地图、模块、数据流、风险”组织。
- 风险只写静态阅读可支持的维护风险、文档缺口、架构不清点或未覆盖区域；不要伪装成安全审计结论。
- 默认不联网扩写或核验外链；README/docs 中出现的外链标注 `未联网核验`。

## Source Manifest 要求

最终 note 的 `Source Manifest` 必须列出：

- input GitHub URL。
- normalized URL。
- requested ref、resolved commit、default branch。
- clone command 和 cloned_at。
- cache path、repo path、repo-metadata path、file-inventory path、exploration-report path。
- 子 Agent 创建和完成情况；说明子 Agent 报告由父 Agent 落盘。如果子 Agent 工具不可用或未返回可用报告正文，必须 blocked，不写最终 note。
- 父 Agent 补读过的关键文件。
- imagegen 状态、imagegen-original path、infographic path。
- read-only boundary：未运行代码、未安装依赖、未执行测试/构建/Docker。
- coverage limitations：未覆盖的大目录、二进制/媒体、submodules、生成产物、无法理解的模块；没有问题写 `issues: none`。
