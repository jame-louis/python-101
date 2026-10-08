# Plan — Lecture 07 materials (循环结构)

Date: 2026-10-08

## Goal
Full materials for lecture 07 (循环结构 / program structure · loops), matching the completed
01–05 pattern + hw + Hydro OJ set (user opted into full scope).

## Deliverables
1. `website/src/content/lectures/lecture07.md` — sync src draft → frontmatter + `##` sections +
   `实验任务` referencing Hydro P0701–P0705.
2. `slides/lecture07.md` — Slidev deck (three-act, 讲者备注, cover/section layouts, mermaid,
   v-clicks). Matches lecture06=条件 → 07=循环 → 08=函数 ordering in the 预告.
3. `src/assignments/hw07.md` + `website/src/content/assignments/hw07.md` (`lectureRef: lecture07`),
   task card referencing Hydro P0701–P0705.
4. `hydro/hw07/` — 5 Hydro problems (3 basic no-input + 2 comprehensive input+prompt), each with
   problem.yaml / problem_zh.md / gen.py / std/std.py.py3 / testdata(+config.yaml) / solution/题解.md,
   plus README.md + validate.py. Run validate to confirm byte-exact.

## Problem set (P0701–P0705)
- P0701 基础·无输入 — `for`+`range()` 累加求和 (1..200 和 + 偶数和)
- P0702 基础·无输入 — `break`/`continue` 控制流程
- P0703 基础·无输入 — 嵌套循环数字下三角 (变量追踪)
- P0704 综合·输入+提示 — `while` 读入统计, 到 -1 标记结束
- P0705 综合·输入+提示 — 质数判断 (循环+条件综合, 挑战)

## Knowledge constraint
By hw07 students know: 顺序、if/elif/else (讲6)、本讲循环 (for/while/break/continue/嵌套). So
problems may freely use `if`, `for`, `while`. Strict byte-match: prompts (含全角冒号) fixed; .out
generated from `std/std.py.py3`.

## Validation
`python3 hydro/hw07/validate.py` → all 5 problems pass.