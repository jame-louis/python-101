# 字典的增删改查（基础）

## 题目描述

小 A 用一句话字典保存用户信息：

```
user = {"name": "Alice", "age": 20}
```

请按下面**给定步骤**操作这本"电话簿"，用 `print` 依次输出，理解字典的**查、改、增、遍历、安全取值**：

1. 用键 `"name"` 打印姓名。
2. 把 `"age"` 改为 `21`；新增键 `"city"` 值为 `"Xiamen"`；打印此时的字典。
3. 分别用 `keys()` / `values()` / `items()` 生成并打印**键列表、值列表、键值对列表**。
4. 用 `get("email", "无邮箱")` 访问一个不存在的键，确认它**不报错**并返回默认值。

> 本题无输入，输出固定。字典保持插入顺序，改用 `list(字典.keys())` 输出列表形式。

## 输入格式

本题**无输入**，程序不读取任何内容。

## 输出格式

共六行：

```
Alice
{'name': 'Alice', 'age': 21, 'city': 'Xiamen'}
['name', 'age', 'city']
['Alice', 21, 'Xiamen']
[('name', 'Alice'), ('age', 21), ('city', 'Xiamen')]
无邮箱
```

## 样例 #1

```input1
（本题无输入）
```

```output1
Alice
{'name': 'Alice', 'age': 21, 'city': 'Xiamen'}
['name', 'age', 'city']
['Alice', 21, 'Xiamen']
[('name', 'Alice'), ('age', 21), ('city', 'Xiamen')]
无邮箱
```

## 提示

- 查：`d["name"]`（键存在）；改/新增：`d["age"] = 21`、`d["city"] = "Xiamen"`（键不存在就是新增）。
- 遍历视图：`list(d.keys())`、`list(d.values())`、`list(d.items())`，返回列表便于直接打印。
- 安全取值：`d.get("email", "无邮箱")` —— 键不存在返回默认值；而 `d["email"]` 会报 `KeyError`。这里只需输出 `get` 的结果。
- 字典**键须不可变**，值任意；打印字典用 `print(user)` 直接输出。

## 数据范围

无输入，使用题目给出的固定数据即可。