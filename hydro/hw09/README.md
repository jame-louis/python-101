# hw09 —— 函数（续）：lambda · 内置函数 · 异常（Hydro 题目集）

对应课程第 9 讲实验任务卡 `src/assignments/hw09.md`，共 **5 道 Python 传统题**，每题一个自包含
Hydro 题目包（`problem.yaml` + `problem_zh.md` + `testdata/` + `std/` + `solution/`）。

## 知识点约束

本套题贴合**当前学生已学内容**：本讲学习匿名函数 `lambda`、内置函数 `sorted`/`map`/`filter`、
异常处理 `try/except/else/finally`、多返回值。题目将**刻意聚焦这些新增能力**。

- **基础题（P0901–P0903）无输入，固定输出**：lambda 改写 def、sorted 按 key 排序、map 与 filter。
- **综合题（P0904–P0905）有输入 + 带提示语**：安全除法（try/except 捕获 ZeroDivisionError）、
  预测结果 + 置信度（多返回值与条件表达式）。

> ⚠️ 严格逐字匹配：P0904–P0905 提示语（含全角冒号）与输出格式必须逐字复现。

## 题目一览

| PID | 题目 | 类型 | 考点 | 处理方式 |
|-----|------|------|------|----------|
| P0901 | lambda 改写 def（基础） | 无输入 | `lambda` 单表达式匿名函数 | 固定输出 |
| P0902 | sorted 按 key 排序（基础） | 无输入 | `sorted(key=lambda)`、`reverse` | 固定输出 |
| P0903 | map 与 filter（基础） | 无输入 | `map` 变换、`filter` 筛选、`list()` | 固定输出 |
| P0904 | 安全除法（综合选做） | 输入+提示 | `try/except` 捕获、两位小数 | 严格逐字匹配 |
| P0905 | 预测结果 + 置信度（综合选做） | 输入+提示 | 多返回值元组、条件表达式、格式化 | 严格逐字匹配 |

## 使用

校验全部题目：

```bash
python3 hydro/hw09/validate.py
```

（数据生成/重放：`python3 gen.py N > testdata/N.in` + `python3 std/std.py.py3 < *.in > *.out`）

## 说明

- Hydro 评测为**传统题**，语言放开 Python 即可；`std` 后缀 `std.py.py3` 与 Hydro 的 Python3 语言键一致。
- 基础题为固定输出便于自查；综合题覆盖样例、除零、负数/大数、通过/不通过、边界 60/0/100 等，并保留随机测试点。
- P0904、P0905 恰好对应 hw09 任务卡的两个进阶任务（🔴 安全除法、🔴 预测结果+置信度），
  与基础题一起完整覆盖了"lambda、排序、变换/筛选、异常捕获、多返回值"五条主线。