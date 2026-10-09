# 方法重写（基础）

## 题目描述

定义 `Animal` 父类，以及**重写 `speak` 方法**的 `Dog`、`Cat` 子类。实例化父类与两个子类，各自调用 `speak()` 打印三行固定结果。

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} 发出叫声"

class Dog(Animal):
    def speak(self):                  # 与父类同名 → 重写
        return f"{self.name} 汪汪叫！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫~"
```

> 方法重写：子类用**同名方法**覆盖父类方法，实现自己的行为。重写时方法名、参数须与父类一致。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共三行：

```
旺财 汪汪叫！
咪咪 喵喵叫~
普通动物 发出叫声
```

## 样例 #1

```input1
（本题无输入）
```

```output1
旺财 汪汪叫！
咪咪 喵喵叫~
普通动物 发出叫声
```

## 提示

- 父类 `Animal("普通动物")` 用原始 `speak`。
- `Dog("旺财")` 用重写后的"汪汪叫"；`Cat("咪咪")` 用"喵喵叫"。
- 先实例化再 `print(对象.speak())`，三行分别对应。

## 数据范围

无输入，使用题目给出的固定数据即可。