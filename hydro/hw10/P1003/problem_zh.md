# 私有属性与 getter（基础）

## 题目描述

定义一个含**"私有"属性**与 **getter** 的类，打印三行固定结果，演示公开访问、getter 访问、名称修饰访问。

```python
class Student:
    def __init__(self, name, sid):
        self.name = name          # 公有属性
        self.__sid = sid          # "私有"（名称修饰）
    def get_sid(self):            # getter：公开的读取通道
        return self.__sid
```

程序依次打印：

1. 公有属性 `s.name`（可直接读）。
2. getter `s.get_sid()`（通过公开方法读私有）。
3. 名称修饰后的 `s._Student__sid`（能访问，但本不该这么用）。

> `__x` 不是铁锁，而是被改名为 `_类名__x` 的"约定"——提醒合作者走 getter，保护内部数据。
> **本题无输入**，输出固定。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共三行：

```
小明
2025001
2025001
```

## 样例 #1

```input1
（本题无输入）
```

```output1
小明
2025001
2025001
```

## 提示

- 实例化：`s = Student("小明", "2025001")`。
- 三行分别 `print(s.name)`、`print(s.get_sid())`、`print(s._Student__sid)`。
- 直接写 `print(s.__sid)` 会 `AttributeError`（名被改写成 `_Student__sid`）；题目用名称修饰写法演示"能访问但不该用"。

## 数据范围

无输入，使用题目给出的固定数据即可。