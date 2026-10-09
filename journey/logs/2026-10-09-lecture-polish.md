# Log — Polish all 16 lectures into a consistent 90-min beginner format

Date: 2026-10-09
Plan: journey/plans/2026-10-09-lecture-polish.md
Scope (user-confirmed): Standardize + fix; sync to **src + website/content** (slides deferred).

## What changed
**src/lectures/ — all 16 now share one beginner 90-min scaffold:**
`# 第N讲 · 标题` → `## 一、本讲导览`（时长表，Σ=90 含上机实践）→ 学习目标 → 回顾/导入 → 分步环节（保留原内容，含易错点/教师话术）→ 随堂练习 → 上机实践（基础/进阶/挑战）→ 小结 + 作业（链接 ../assignments/hwNN）→ 附录速查卡(01/02)。

- **lecture01**: was only a Hydro tutorial → now = 课程认识(Python/应用/解释vs编译/课程安排) + 环境搭建(对齐 hw01) + 第一个程序 + Hydro 使用(核心) + 附录 OJ FAQ。满足 CLAUDE.md「课程介绍在 lecture01 顶部」约定。
- **lecture02**: was **JavaScript** (let/const/console.log/typeof) in a Python course → rewritten to 真实 Python：变量/常量/命名、int·float·bool·str + `type()`、运算符与表达式、字符串索引分片（含 `s[::-1]`）、类型转换。与 lecture03 画清边界（03 = 字符串方法 + 格式化 + input/类型转换易错点）。已与 hw02 对齐。
- **lecture03–16**: 逐讲加导览表、回顾/导入、随堂练习、上机实践命名、作业链接；内容主体保留。
- 移除 C 假设措辞：lecture06（开场/`{}`拼块/常见错误）、07（「对比 C 的习惯」）、08（「你有 C 函数基础」）、10（「用 C 写结构体」）。
- 清除 src 里残留的 YAML frontmatter（08–16），src 回归纯 Markdown。

## Bug fixes
- lecture11 Pig.speak() f-string 缺闭合引号（`return f"... 哼哼~~` → 加 `"`），顺便 Python 跑通验证。
- lecture02 `s[1::2]` 注释结果 `yh`→`yhn`。

## Verification
- 每个导览表 Σ 时长 = 90（脚本校验，lecture01–16 全 OK）。
- 全课无游离 `^title:`（08–16 的 src frontmatter 已除）；无退化 C 假设（仅保留 lecture02「和 C 的一大区别」这一合理对比）。
- `npm --prefix website run build`：33 页（16 lectures + 16 hw + index/sitemap）构建通过，无内容集合错误。
- 关键代码片段经 python3 实跑核对（01/02 全量；04/07/11/14 抽样）。

## website sync
`src → website/src/content/lectures/` 手动镜像（按约定无自动化脚本）：O keep 各文件既有 frontmatter（title/lectureNumber/slidevUrl/draft，title 保留描述性写法），body = src 去 H1。

## Not done / follow-ups
- **slides/ 16 套 Slidev 未同步**（本次范围外，用户选择）。deck 仍是旧/部分陈旧内容；如需对齐需逐套重写 + `npm run build:slides --force`。
- 未重建 `site/` 镜像（构建工件，gitignored；CI 部署时自动生成）。建议 `npm run build`（根）再本地 `npm run dev` 目检。