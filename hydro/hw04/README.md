# hw04 —— 列表与元组（Hydro 题目集）

对应课程第 4 讲实验任务卡 `src/assignments/hw04.md`，共 **5 道 Python 传统题**，每题一个自包含
Hydro 题目包（`problem.yaml` + `problem_zh.md` + `testdata/` + `std/` + `solution/`）。

| PID | 题目 | 考点 | 对应实验任务 |
|-----|------|------|--------------|
| P0401 | 分数表增删改查 | `append` / `insert` / `remove`、最值 | 任务 1 |
| P0402 | 三种插入方法 | `append` vs `extend` vs `insert` 的区别 | 任务 3 |
| P0403 | 元组解包与坐标统计 | 元组、解包 unpacking | 任务 5 |
| P0404 | 文本转小写清洗 | for 循环 + append 批量、`str.lower()` | 任务 6（NLP） |
| P0405 | 成绩统计与中位数 | `sort()`、最值、中位数 | 任务 7（挑战） |

## 目录约定

```
P04xx/
├── problem.yaml          # 标题、标签、PID、难度
├── problem_zh.md         # 中文题面
├── testdata/
│   ├── config.yaml       # 时限/内存 + 10 个测试点
│   ├── 1..10.in          # 输入（1 号即样例）
│   └── 1..10.out         # 标准输出（由标程生成）
├── std/std.py.py3        # Python 标程
├── gen.py                # 数据生成器（固定种子、可复现）
└── solution/题解.md       # 思路 + 参考代码
```

## 使用

生成/重放数据（每个题目包内）：

```bash
cd P0401
for i in $(seq 1 10); do python3 gen.py $i > testdata/$i.in; done
for i in $(seq 1 10); do python3 std/std.py.py3 < testdata/$i.in > testdata/$i.out; done
```

校验全部题目（仓库根目录执行）：

```bash
python3 hydro/hw04/validate.py
```

## 说明

- Hydro 评测为**传统题**，语言放开 Python 即可；`std` 后缀 `std.py.py3` 与 Hydro 的 Python3 语言键一致。
- 每个测试点数据规模梯次递增，并覆盖样例、边界（全相同、单元素、偶/奇、负坐标等）与大数据，
  详见各题 `problem_zh.md` 的「数据范围」。