# Lectures 08–16 materials (full course completion)

Date: 2026-10-08/09
Completed the rest of the course in batches, per 2026-10-08-lectures08-16-materials.md.

## What was built
- **08–11 (Python 语法深化)** — full set: website lecture + Slidev deck + hw (src+website) + **Hydro OJ**
  (5 problems each; 3 basic no-input fixed-output + 2 comprehensive input+prompt strict-match; validate.py green):
  - hw08 (函数): P0801 圆面积 / P0802 默认参数 / P0803 global / P0804 圆面积计算器 / P0805 *args 求和
  - hw09 (函数续): P0901 lambda / P0902 sorted / P0903 map&filter / P0904 安全除法 / P0905 预测+置信度
  - hw10 (类): P1001 定义类调用 / P1002 类vs实例属性 / P1003 私有+getter / P1004 自我介绍 / P1005 银行账户
  - hw11 (继承多态): P1101 基础继承 / P1102 方法重写 / P1103 super / P1104 三维点 / P1105 多态动物叫
- **12–15 (ML lab, NO hydro)** — website + slides + lab hw (code+图+报告), per user scope choice:
  - 12 决策树&KNN, 13 k-means, 14 线性回归, 15 神经网络&BP
- **16 (期末)** — website + slides + hw16 course-design brief (选题说明表), no hydro.

## Consistency fixes applied to previews
Src previews were stale post-restructure (e.g. lecture12→"逻辑回归", lecture13→"DBSCAN/PCA",
lecture15→"多层网络"). Pointed each 预告 at the **actual** next lecture: 12→无监督/k-means(13),
13→线性回归(14), 14→神经网络(15), 15→课程设计+总复习(16).

## House pattern locked in for all hydro sets
- `std/std.py.py3` (Hydro Python3 key); prompts on their own line via `print(提示语)+input()` (lessons
  learned from lecture 06/07); each problem = problem.yaml + problem_zh.md + gen.py(seed) + testdata
  (+config.yaml; 5 basic / 10 comprehensive) + solution/题解.md + per-problem & hw-all `.zip`.
- validate.py derived per-set from hw06 template; all hw06–hw11 (30 problems) pass.

## Status
- All lectures 01–16 now have website content; slides decks exist for 01,03,04,05,06,07,08,09,10,11,12,
  13,14,15,16 (note: 02 has no deck in the repo — pre-existing).
- Website build NOT run (user interrupts it); heavy ML code (sklearn/numpy) not executed locally.
- env auto-commits progress between turns; I do not commit/push.