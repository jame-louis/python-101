# 类属性 vs 实例属性（基础）

## 题目描述

定义 `Student` 类，用一段可运行的程序演示**类属性（共享）**与**实例属性（独立）**的区别，输出三行固定结果。

```python
class Student:
    school = "xx学院"          # 类属性 → 所有实例共享
    def __init__(self, name):
        self.name = name        # 实例属性 → 每实例独立
```

程序依次做三件事并打印：

1. 两个实例的 `school`（共享，应相同）。
2. 给 `s1.name` 重新赋值后打印 `s1.name`、`s2.name`（改实例属性只影响 `s1`）。
3. 修改 `Student.school` 后打印 `s1.school`、`s2.school`（改类属性影响所有实例）。

> 一句话："共性"放类里共享，"个性"放 `__init__` 里各不同。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共三行：

```
xx学院 xx学院
阿明 小红
新学院 新学院
```

## 样例 #1

```input1
（本题无输入）
```

```output1
xx学院 xx学院
阿明 小红
新学院 新学院
```

## 提示

- 实例化：`s1 = Student("小明")`、`s2 = Student("小红")`。
- 第一步：`print(s1.school, s2.school)` → 共享，都xx学院。
- 第二步：`s1.name = "阿明"`；`print(s1.name, s2.name)` → 阿明 小红。
- 第三步：`Student.school = "新学院"`；`print(s1.school, s2.school)` → 都新学院。

## 数据范围

无输入，使用题目给出的固定数据即可。