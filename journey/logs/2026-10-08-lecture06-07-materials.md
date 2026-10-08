# Lecture 06 + 07 materials (条件结构 / 循环结构)

Date: 2026-10-08

Built the full materials for lectures **06 (条件结构)** and **07 (循环结构)**, each matching the
completed 01–05 pattern. Both were already drafted in `src/` but unsynced; no homework/hydro existed
for either.

## Deliverables (per lecture)
- `website/src/content/lectures/lectureNN.md` — synced from `src/` (title → frontmatter, `#`→`##`,
  subtitle dropped, `上机任务`→`实验任务` referencing P0701–P0705 / P0601–P0605).
- `slides/lectureNN.md` — Slidev deck, three-act house style (cover, section 幕卡, 讲者备注 with
  镜头类型, mermaid, v-clicks).
- `src/assignments/hwNN.md` + `website/src/content/assignments/hwNN.md` (`lectureRef` set).
- `hydro/hwNN/` — 5 Hydro problems, validated: `python3 hydro/hwNN/validate.py` → all ✓.
  - 3 basic (no-input, fixed output, 5 cases each) + 2 comprehensive (input+prompt, 10 cases each),
    with per-problem `.zip` + `hwNN-all.zip` for Hydro upload parity.

## Key knowledge constraints (drives problem design)
- **hw06**: students know sequential + `if/elif/else` only — problems are **zero-loop** (正负/奇偶、
  成绩等级、三数最大; 比大小三态、成绩等级 five-band).
- **hw07**: students now know loops too — `for`+`range`, `while`+`break`, `continue`, nested
  (累加求和、break/continue、嵌套图案; while 读到 -1 标记、质数判断 nested+condition).

## Lesson learned (applied to both sets)
`input("提示：")` prints the prompt **inline** (no trailing newline), so multiple prompts/reads
concatenate on one line. For clean, problem-statement-consistent strict-matching output, each prompt
must be its own line = **`print(提示语)` then bare `input()`**. Applied this to P0604/P0605 and
P0704; kept P0705 `input("...")` because it reads exactly one value (single prompt → one line).

## Status
- Lecture 07 site title kept placeholder naming style `程序结构 · 循环结构`; lecture 06 `程序结构 · 条件结构`.
- Website build NOT run in this session (user stopped it); run `npm run build` in `website/` to confirm
  content collections before pushing.
- Plan file: `journey/plans/2026-10-08-lecture07-materials.md` (covers both); design.md not changed.