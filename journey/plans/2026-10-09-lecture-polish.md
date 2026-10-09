# Plan — Polish all lectures into a consistent 90-min beginner format

Date: 2026-10-09
Decision (user-confirmed via AskUserQuestion): **Standardize + fix**, sync to **src + website/content** (slides deferred).

## Why
- `lecture02.md` is **JavaScript** in a Python course — blocking bug.
- `lecture01.md` has no course intro (CLAUDE.md contract) and no env-setup/first-program content (`hw01` expects it).
- Lectures 06/07/08 frame lessons as "you already know C" — wrong for beginners.
- Lectures 04–16 have solid content but no consistent 90-min step-by-step scaffold. `lecture03` is the gold-standard model to generalize.

## Standard template (all lectures 03–16)
`# 第N讲·标题` → 导览时长表(Σ=90 including practice) → 学习目标 → 回顾/导入 → 分步环节(概念·示例·易错点·教师话术) → 随堂练习 → 上机实践(基础/进阶+验证) → 小结 → 作业(链接 hwNN) → 附录速查卡(如适用). Keep zh-CN; drop C-assumptions; normalize ad-hoc `（N分钟）` into the top table.

## Tier A — rewrite
- **lecture01**: = 课程认知/介绍(本质·发展·与编译型区别·本课目标·教材·考核) + 环境搭建(对齐 hw01) + 第一个程序 + Hydro OJ 使用教程(保留现有优质内容).
- **lecture02**: JS→Python 第一课: 变量命名/常量/基本类型(type())/运算符与表达式/print. Boundary: lecture02 owns numbers/bool/operators/print; lecture03 owns strings + input/类型转换.

## Tier B — scaffold 03–16, keep subject
- lecture03: add导览表 only (already timed). 04–16: add导览表 + 回顾/导入 + section headers + 随堂练习 + 上机实践 + 作业链接. Fix C-framing in 06/07/08.

## Sync to website
`src/lectures/lectureNN.md` → `website/src/content/lectures/lectureNN.md`: keep YAML frontmatter (update `title` to match new H1), replace body with src body minus H1. Preserve `draft`/`slidevUrl`.

## Verify
`npm --prefix website run build` (no content errors); `python3` runs of key snippets; grep C-references gone; 导览表 sums 90; `npm run dev` visual check. Slides rebekken deferred.

## Order
01 → 02 → sync 01/02 → scaffold 03–16 (batches) → remove C-assumptions → build+verify → logs.