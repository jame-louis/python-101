# 基础继承（基础）

## 题目描述

定义 `Animal` 父类（含 `__init__`、`speak`、`move`）与 `Dog(Animal)` 子类，实例化 `Dog` 并调用**继承来**的方法，打印两行固定结果。

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} 发出叫声"
    def move(self):
        return f"{self.name} 在移动"

class Dog(Animal):       # 继承自 Animal
    pass                  # 什么都不写，直接用父类的内容
```

> 继承 = 代码复用：子类 `Dog` 没写任何方法，却自动拥有父类的 `speak`、`move`。子类没有的成员沿继承链向上找父类。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共两行：

```
旺财 发出叫声
旺财 在移动
```

## 样例 #1

```input1
（本题无输入）
```

```output1
旺财 发出叫声
旺财 在移动
```

## 提示

- 定义父类与子类后：`d = Dog("旺财")`。
- 打印：`print(d.speak())`、`print(d.move())`。
- 验证：`Dog("旺财")` 的 `__init__` 也来自父类，`name` 被正确初始化。

## 数据范围

无输入，使用题目给出的固定数据即可。