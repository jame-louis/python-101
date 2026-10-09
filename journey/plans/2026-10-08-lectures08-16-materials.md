# Plan — Lectures 08–16 materials

Date: 2026-10-08
Decision: build the rest of the course. Pattern varies by track (user-confirmed via AskUserQuestion):

- **08–11 (Python 语法深化)**: full set — website lecture + Slidev + hw (src + website) + **Hydro OJ set** (5 problems: 3 basic no-input + 2 comprehensive input+prompt, validated).
- **12–15 (ML, scikit-learn/numpy)**: website + slides + **lab hw** (code + 图表 + 报告; NO Hydro). Lab reports do not fit stdin/stdout byte-match judges.
- **16 (期末)**: website + slides + **hw16 = course-design brief** (no Hydro).

Pace: sequential, checkpoint after every 2 lectures (after 08, 10, 12, 14, 16).

## Topics (src/lectures/)
- 08 函数: def/return、四种参数（位置/默认/*args/**kwargs）、作用域、可变 vs 不可变
- 09 函数续: lambda、sorted/map/filter、异常 try/except/else/finally
- 10 类与OOP: class、__init__、实例/类属性、公有/私有
- 11 继承性与多态
- 12 机器学习入门: 决策树 & KNN (sklearn)
- 13 无监督: k-means
- 14 线性回归
- 15 神经网络原理 & BP
- 16 课程设计布置 + 总复习

## Hydro knowledge constraints (08-11)
Progression: 08 functions (params, return), 09 lambda/异常, 10 class/__init__, 11 继承多态.
Each problem package = problem.yaml + problem_zh.md + gen.py + std/std.py.py3 + testdata(+config.yaml)
+ solution/题解.md; prompts on own line via `print(提示语)+input()`; validate via hydro/hwNN/validate.py.

## Checkpoints
After 08 and 09 → report & pause (batch 1). Then 10+11, 12+13, 14+15, 16.