# 定义类并调用（基础）

## 题目描述

定义一个 `Student` 类，包含类属性 `school`、构造函数 `__init__` 和方法 `say_hello`，然后**实例化两个对象**并调用方法 / 属性，打印两行固定结果。

```python
class Student:
    school = "嘉庚学院"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        return f"我是{self.name}，{self.age}岁，来自{self.school}"
```

> 类是"模板"，实例是"个体"：一个类定义冲压出 `s1`、`s2` 两个对象，各自数据不同、方法共享。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共两行：

```
我是小明，20岁，来自嘉庚学院
我是小红，21岁，来自嘉庚学院
```

## 样例 #1

```input1
（本题无输入）
```

```output1
我是小明，20岁，来自嘉庚学院
我是小红，21岁，来自嘉庚学院
```

## 提示

- 定义类后：`s1 = Student("小明", 20)`、`s2 = Student("小红", 21)`。
- 调用方法：`print(s1.say_hello())`、`print(s2.say_hello())`。
- `self` 指向调用方法的那个对象，所以 `s1`、`s2` 各自输出自己的 name/age。

## 数据范围

无输入，使用题目给出的固定数据即可。