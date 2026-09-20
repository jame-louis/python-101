---
theme: default
title: 简单数据类型 · 字符串基本操作与输入输出
info: |
  第3讲：字符串基本操作与输入输出
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# 简单数据类型
## 字符串基本操作与输入输出

第3讲 · Python 基础

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 p-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    开始学习 <carbon:arrow-right class="inline"/>
  </span>
</div>

---

# 学习目标

学完本节后，你能够：

- 调用常见字符串方法：strip / split / join / 大小写 / 替换 / 查找
- 用 input() 获取输入，并用 int() / float() 正确转换类型
- 用 f 字符串 / format 实现格式化输出
- 理解 strip / split / 格式化在 AI 文本处理中的作用


---

# 回顾

<v-clicks>

1. Python中简单数据类型有哪些？
<v-click>（int、float、bool、str）</v-click>
2. 如何查看一个变量的类型？
<v-click> type() </v-click>
3. `'123'` 和 `123` 一样吗？
<v-click>（不一样，前者是字符串，后者是整数）</v-click>
4. 字符串**定义与分片**：
<v-click>

```python
s = "Python"
print(s[0], s[-1])   # P n
print(s[0:3])        # Pyt
```

</v-click>

> 今天学字符串的**操作方法**——注意：方法与分片是两种语法形态。

</v-clicks>

---

# 开场思考点

> **Python 字符串能否为空？**

试一试（交互模式）：

```python
s = ""          # 空字符串
print(len(s))   # 0
print(bool(s))  # False
print(bool(" "))  # True —— 注意：空格不是空！
```

<div class="mt-8 text-xl">
一句话：<b>空字符串 <code>""</code> 长度为 0；但含空格 <code>" "</code> 不是空</b>
</div>

---

# 字符串方法：调用方式

- 字符串方法用 `s.方法名(...)` 调用，就像"对字符串做动作"
- 与分片（`s[..]`）的区别：方法是**调用函数**，分片是**取片段**

```python
s = "  Python  "
print(s.strip())     # 去两端空白："Python"
print(s.lower())     # 全小写
print(s.upper())     # 全大写
```

---

# 重点方法 ①：strip 清洗

**`strip()`** 去掉字符串**两端**的空白（空格、换行、Tab）——AI 文本清洗第一步：

```python
raw = "  欢迎学习Python  \n"
print(repr(raw.strip()))       # '欢迎学习Python'
```

`lstrip()` / `rstrip()`：只去左 / 右端空白。

<div class="mt-16 p-4 rounded bg-blue-50 dark:bg-blue-900 text-blue-900 dark:text-blue-100">

⭐ **AI 赋能**：自然语言处理中，爬取/读取的文本常带多余空白，`strip()` 先清洗。

</div>

---

# 重点方法 ②：split 分句 / 分词

**`split(分隔符)`** 把字符串按分隔符**拆成列表**：

```python
s = "今天上课,讲了,字符串"
print(s.split(","))        # ['今天上课', '讲了', '字符串']
words = "I love Python".split()
print(words)               # ['I', 'love', 'Python']
```

<div class="mt-6 p-4 rounded bg-blue-50 dark:bg-blue-900 text-blue-900 dark:text-blue-100">

⭐ **AI 赋能**：**对话文本分句**——按句号/换行把长篇对话拆成一句句再处理。

</div>

---

# 重点方法 ③：join 拼接

**`join()`** 把**列表合成字符串**——与 split 相反（一个"拆"、一个"合"）：

```python
words = ['I', 'love', 'Python']
print(" ".join(words))     # I love Python
print("-".join(words))     # I-love-Python
```

<div class="mt-16 p-4 rounded bg-yellow-50 dark:bg-yellow-900 text-yellow-900 dark:text-yellow-100">

❗ 记法：`"分隔符".join(列表)`，分隔符写在前。

</div>

---

# 其他常用方法

```python
s = "Hello, Python"
print(s.replace("Hello", "Hi"))   # Hi, Python
print(s.find("Python"))           # 7（找不到返回 -1）
print(s.count("o"))               # 2
print(len(s), "Python" in s)      # 13 True
print(s.startswith("He"))         # True
print(s.endswith("on"))           # True
```

- `len(s)`：长度；`in`：成员判断——注意是**函数 / 运算符**，不是方法。

---

# 常见错误：方法与分片混淆

| 错误 | 原因 | 正确做法 |
|---|---|---|
| `s.upper` 漏括号 | 忘记方法调用要加 `()` | `s.upper()` |
| `s.upp` 拼写错 | 大小写/拼写 | 方法都用小写：`s.upper()` |
| `s.upper ()` 多空格 | 多余空格 | `s.upper()` |
| 把 `split` 当合并 | 方向记反 | split 拆、join 合 |

---

# 输入输出：input()

**`input()`** 从键盘读入**一行文本**，永远返回**字符串**：

```python
name = input("请输入你的名字：")   # 提示词只显示，不进入变量
print("你好，" + name)
```
<div class="mt-16 p-4 rounded bg-red-50 dark:bg-red-900 text-red-900 dark:text-red-100">

❗ 关键：即使你输入的是数字，`input()` 返回的也是**字符串**！

</div>

---

# 难点❗：输入类型的转换

**忘记转换 → 报错（TypeError）**

```python
n = input("请输入数字：")   # 假设输入 3
print(n + 5)    # ❌ TypeError: can only concatenate str (not "int") to str
print(n * 2)    # ⚠️ 得到 "33"，是字符串重复，不是 6！
```

**正确做法 —— 先转换再运算**

```python
n = int(input("请输入数字："))    # 不要再输入相同变量已占用，新变量
print(type(input("请输入数字：")))  # <class 'str'>   ← 看清楚它的类型
x = int(input("a = "))           # 转换
y = float(input("b = "))         # 小数用 float
print(x + y)                     # 正常数值运算
```

---

# 难点❗：转换易错点小结

| 常见错误 | 后果 | 正确做法 |
|---|---|---|
| 用 `int()` 转小数 | 报 ValueError | 小数用 `float()` |
| 直接对 `input()` 结果做运算 | TypeError | 先 `int()`/`float()` |
| 用户输入了非数字 | ValueError | 先了解，本讲不展开异常处理 |
| 转换后再重复用原字符串 | 混淆 | 转换后赋值给数值变量 |

---

# 格式化输出：f 字符串（推荐）

在字符串前加 `f`，用 `{}` 填变量，最直观：

```python
name, score = "小明", 87.5
print(f"姓名：{name}，成绩：{score}")        # 姓名：小明，成绩：87.5
print(f"成绩保留一位：{score:.1f}")          # 87.5
```

`format()` / `%` 也可以：

```python
print("姓名：{}，成绩：{}".format(name, score))
print("成绩 %.1f" % score)
```

<div class="mt-4 p-4 rounded bg-blue-50 dark:bg-blue-900 text-blue-900 dark:text-blue-100">

⭐ **AI 赋能**：**格式化生成 AI 模型提示词模板**——把用户输入填充进预设模板。

</div>

---

# print() 的参数

```python
print(1, 2, 3)              # 1 2 3（默认空格分隔）
print(1, 2, 3, sep="-")     # 1-2-3（改分隔符）
print("a", end=" ")         # 结尾不换行，改空格
print("b")                  # 接着同一行：a b
```

---

# AI 赋能场景：文本清洗与提示词模板

```python
# ① strip 清洗 NLP 文本噪声
text = "  我正在学习中文自然语言处理  \n"
clean = text.strip()

# ② split 对话文本分句
dialog = "你好\n我想学Python\n应该怎么开始"
for line in dialog.split("\n"):
    print("句：" + line)

# ③ 格式化生成 AI 提示词模板
topic = "字符串"
prompt = f"请你用通俗的语言，为初学者讲解 Python 的{topic}。"
print(prompt)
```

---

# 实验任务（上机）

- 🔵 **基础任务（必做）**：字符串方法清理文本 + 输入两个数求和/平均
- 🟡 **进阶任务（选做）**：规范化清洗英文（split+join+首字母大写）+ f 字符串自我介绍
- 🔴 **挑战任务（选做）**：对话文本分句统计 或 AI 提示词模板生成器

<div class="mt-8 text-lg opacity-80">
提交要求：源文件 + 运行结果截图
</div>

---

# 思考点

> **Python 字符串能否为空？**

1. `""` 与 `" "` 有什么区别？长度分别是多少？
2. `bool("")`、`bool("abc")` 分别是 True 还是 False？
3. 在清洗文本时，为什么 `" "`（空格）不能当作空处理？

---

# 小结 + 预告

<div class="text-left">

- 本课要点：字符串方法（重点 strip/split/join）、输入转换（难点）、f 字符串格式化
- 下次课：**组合数据类型**（列表、元组）
- 预习：Python 的组合数据类型；完成 HW02 作业

</div>

<div class="mt-12 text-2xl opacity-80">
会拆（split）、会合（join）、会洗（strip），你就会处理大部分文本了 ✂️
</div>
