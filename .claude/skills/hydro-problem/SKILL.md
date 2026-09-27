---
name: hydro-problem
description: |
  在 Hydro Online Judge 平台上创建、配置和管理算法竞赛题目。
  支持生成符合 Hydro 标准格式的题目包（problem.yaml + 题面 + 测试数据 + config.yaml），
  支持传统题、Special Judge、交互题、子任务（Subtask）等多种题型。
  当用户需要出题、制作测试数据、配置评测方式时使用此技能。
---

# Hydro 题目制作技能

## 概述

Hydro 是一个新一代高性能在线评测系统。本技能帮助你创建符合 Hydro 标准格式的题目，包括题面、测试数据、评测配置等。

## 题目包目录结构

```
problem_folder/
├── problem.yaml          # 题目配置（标题、标签等）
├── problem_zh.md         # 中文题面（Markdown 格式）
├── problem_en.md         # 英文题面（可选）
├── testdata/             # 测试数据目录
│   ├── config.yaml       # 评测配置（必需）
│   ├── 1.in              # 测试输入
│   ├── 1.out             # 测试输出
│   ├── 2.in
│   ├── 2.out
│   └── ...               # 更多测试点
├── additional_file/      # 附加文件（可选，图片、PDF、头文件等）
│   ├── figure.png
│   └── header.h
├── solution/             # 题解目录（可选）
│   └── 题解.md
└── std/                  # 标程目录（可选，最多5个）
    └── std.cpp
```

## problem.yaml 配置

```yaml
title: 题目名称
tag:
  - 算法标签1
  - 算法标签2
pid: P1001              # 题号（字母+数字）
difficulty: 2           # 难度 0-5，可选
```

## testdata/config.yaml 配置

### 基础配置（传统题）

```yaml
time: 1000ms            # 时间限制
memory: 256m            # 内存限制
cases:
  - input: 1.in
    output: 1.out
  - input: 2.in
    output: 2.out
```

### 子任务（Subtask）配置

```yaml
time: 1000ms
memory: 256m
subtasks:
  - score: 20
    id: 0
    cases:
      - input: data1-1.in
        output: data1-1.out
      - input: data1-2.in
        output: data1-2.out
  - score: 30
    id: 1
    if: [0]              # 依赖子任务0（可选）
    cases:
      - input: data2-1.in
        output: data2-1.out
  - score: 50
    id: 2
    cases:
      - input: data3-1.in
        output: data3-1.out
```

### Special Judge 配置

```yaml
time: 1000ms
memory: 256m
checker_type: testlib
checker: chk.cc          # SPJ 源代码文件
cases:
  - input: 1.in
    output: 1.out
```

### 交互题配置

```yaml
time: 1000ms
memory: 256m
type: interactive
interactor: interactor.cc
cases:
  - input: 1.in
    output: 1.out
```

## 题面 Markdown 格式

```markdown
# 题目描述

在这里写题目描述...

## 输入格式

描述输入格式...

## 输出格式

描述输出格式...

## 样例 #1

```input1
样例输入内容
```

```output1
样例输出内容
```

## 提示

- 数据范围说明
- 其他提示信息

## 数据范围

| 测试点编号 | 限制 |
|-----------|------|
| 1-3 | n ≤ 100 |
| 4-6 | n ≤ 1000 |
| 7-10 | n ≤ 100000 |
```

## 常用操作命令

### 1. 创建新题目骨架

当用户要求创建新题目时，生成完整的目录结构：

```bash
mkdir -p problem_folder/testdata problem_folder/additional_file
```

### 2. 生成测试数据

使用 Python 生成测试数据：

```python
import random
import os

random.seed(42)  # 固定种子，保证可复现

def gen_input(case_id):
    """生成第 case_id 个测试点的输入"""
    if case_id == 1:
        # 样例
        return "3
1 2 3
"
    elif case_id <= 3:
        n = random.randint(1, 100)
    elif case_id <= 6:
        n = random.randint(100, 1000)
    else:
        n = random.randint(1000, 100000)

    nums = [random.randint(1, 10**9) for _ in range(n)]
    return f"{n}\n{' '.join(map(str, nums))}\n"

# 生成测试数据
for i in range(1, 11):
    input_data = gen_input(i)
    with open(f'testdata/{i}.in', 'w') as f:
        f.write(input_data)
    print(f"Generated {i}.in")
```

### 3. 编译运行标程生成输出

```bash
# 编译标程
g++ -O2 -std=c++17 std.cpp -o std

# 对每个测试点生成输出
for i in {1..10}; do
    ./std < testdata/${i}.in > testdata/${i}.out
done
```

### 4. 验证测试数据

```python
def validate(input_file, output_file):
    """验证测试数据格式是否正确"""
    with open(input_file) as f:
        input_content = f.read().strip()
    with open(output_file) as f:
        output_content = f.read().strip()

    # 添加自定义验证逻辑
    assert input_content, f"{input_file} is empty"
    assert output_content, f"{output_file} is empty"

    print(f"✓ {input_file} / {output_file} valid")

# 验证所有测试点
for i in range(1, 11):
    validate(f'testdata/{i}.in', f'testdata/{i}.out')
```

## Special Judge (SPJ) 模板

使用 testlib.h 编写 SPJ：

```cpp
#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    // 读取输入
    int n = inf.readInt();
    vector<int> a(n);
    for (auto& x : a) x = inf.readInt();

    // 读取选手输出
    int user_ans = ouf.readInt();

    // 读取标准答案
    int std_ans = ans.readInt();

    if (user_ans == std_ans) {
        quitf(_ok, "Correct! Answer = %d", std_ans);
    } else {
        quitf(_wa, "Expected %d, got %d", std_ans, user_ans);
    }
}
```

## 数据生成器模板

```python
#!/usr/bin/env python3
"""
Hydro 数据生成器
用法: python gen.py <test_case_id>
输出: 对应测试点的输入数据（输出到 stdout）
"""

import sys
import random

def main():
    case_id = int(sys.argv[1])
    random.seed(case_id * 1000003)  # 每个测试点使用不同种子

    # 根据 case_id 定义数据规模
    if case_id == 1:
        n, m = 3, 3           # 样例
    elif case_id <= 3:
        n, m = 10, 20         # 小数据
    elif case_id <= 6:
        n, m = 1000, 2000     # 中数据
    else:
        n, m = 100000, 200000 # 大数据

    print(n, m)

    # 生成具体数据
    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
            print(u, v)

if __name__ == "__main__":
    main()
```

## 完整工作流程

当用户要求制作一道 Hydro 题目时，按以下步骤执行：

### Step 1: 确定题目信息
- 题目名称
- 题目类型（传统题/SPJ/交互题/子任务）
- 算法标签
- 数据范围
- 时空限制

### Step 2: 创建目录结构
```bash
mkdir -p {problem_id}/testdata {problem_id}/additional_file
```

### Step 3: 编写 problem.yaml

### Step 4: 编写题面 problem_zh.md

### Step 5: 编写数据生成器 gen.py

### Step 6: 编写标程 std.cpp

### Step 7: 生成测试数据
```bash
cd {problem_id}
for i in $(seq 1 10); do
    python3 gen.py $i > testdata/${i}.in
done
g++ -O2 -std=c++17 std.cpp -o std
for i in $(seq 1 10); do
    ./std < testdata/${i}.in > testdata/${i}.out
done
```

### Step 8: 编写 config.yaml

### Step 9: 验证并打包
```bash
# 验证数据
python3 validate.py

# 打包（可选）
zip -r {problem_id}.zip {problem_id}/
```

## 注意事项

1. **测试点命名**: 文件名必须包含数字，如 `1.in`, `1.out`，不能是 `sample.in`
2. **标程后缀**: std 文件后缀需与语言设置中的配置一致（如 `.cpp`, `.py.py3`）
3. **题解格式**: 题解必须以 `.md` 格式存放，其他格式会乱码
4. **数据强度**: 确保大数据不会导致标程 TLE/MLE
5. **边界情况**: 包含最小/最大数据、特殊边界（空、全相同、极端值）
6. **随机种子**: 固定随机种子保证数据可复现
7. **SPJ 比较器**: 使用 testlib.h 时确保 `checker_type: testlib`

## 参考资源

- Hydro 官方文档: https://hydro.js.org/
- 系统测试题域（可下载参考配置）: https://hydro.ac/d/system_test/
- testlib.h: https://github.com/MikeMirzayanov/testlib
