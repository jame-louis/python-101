# 构造器继承 super（基础）

## 题目描述

用"写法B"定义 `Point2D` 父类与 `Point3D(Point2D)` 子类：子类重写 `__init__`，先用 `super().__init__(x, y)` 调用父类构造器初始化前两个维度，再新增 `z`。实例化并打印 `(q.x, q.y, q.z)` 一行固定结果。

```python
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # 先初始化父类 x,y
        self.z = z               # 再新增自己 z
```

> `super()` 是"指向父类的代理"，用来调用父类构造器/方法。子类自己重写 `__init__` → **必须** `super().__init__(父参)` 补父类初始化。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

仅一行：

```
(1, 2, 3)
```

## 样例 #1

```input1
（本题无输入）
```

```output1
(1, 2, 3)
```

## 提示

- 实例化：`q = Point3D(1, 2, 3)`。
- 打印：`print((q.x, q.y, q.z))`（三元素数组元组，直接打印）。
- 验证：`super().__init__(1, 2)` 让 `x=1, y=2`；`self.z = 3` 让 `z=3`。

## 数据范围

无输入，使用题目给出的固定数据即可。