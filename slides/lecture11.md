---
theme: default
transition: fade
title: 第11讲 · 继承与多态
highlighter: shiki
---

<!-- 片头 · 空镜 -->
## 动物千百种，「叫」「动」不必各写一遍

---
layout: cover
---

# 第11讲 · 类的继承性与多态
## 封装 · 继承 · 多态 —— 三大特性收尾

<!-- 讲者备注：【空镜】开场钩子。动物有很多种,是不是每一类都要重写「叫」「动」的代码?不用——把共性放父类,子类继承复用。本讲三件武器:继承(类套类)、重写(子类改造)、多态(同一接口不同实现),最后落到 AI 模型的 train/predict 接口范式。节奏:先继承复用,再 super 构造,最后多态扩展。 -->

---
transition: slide-left
---

# 这一讲，你会收获四件事

- 继承：`class B(A)`，子类复用父类
- 重写：子类同名方法覆盖
- `super()`：重写构造器时补父类初始化
- 多态：同一接口，不同实现

<!-- 讲者备注：【全景】抛路线图,只给骨架。教学目标:学完能解释 class B(A) 的继承语义;会对比两种构造器继承写法并会用 super();能用继承/重写/super 编层级类;能用多态写可扩展程序;体会 AI 模型类的接口封装。 -->

---
layout: section
---

## 第一幕 · 继承复用

<!-- 转场
讲者备注：【转场】幕卡,淡入切幕。一句话预告本幕:共性放父类、个性放子类,子类一行 class Dog(Animal) 就白捡了父类的属性与方法。 -->

---

# class B(A)：子类白捡父类

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} 发出叫声"
    def move(self):
        return f"{self.name} 在移动"

class Dog(Animal):       # Dog 继承自 Animal
    pass                  # 没写任何东西

d = Dog("旺财")
print(d.speak())   # 旺财 发出叫声   ← 继承来的
print(d.move())    # 旺财 在移动     ← 继承来的
```

> 继承 = 代码复用：共性在父类，个性在子类

<!-- 讲者备注：【特写】继承语法一行就够:class Dog(Animal)。Dog 里一个 pass 就自动拥有父类的 __init__、speak、move。强调"白捡"——子类没有的成员沿继承链向上找父类。这是继承最直白的样子。 -->

---
layout: section
---

## 第二幕 · 重写与 super

<!-- 转场
讲者备注：【转场】幕卡,淡入切幕。一句话预告本幕:继承给的脾气不想要,就重写;要给子类加新属性,构造器就得靠 super 把父类那部分补上。 -->

---

# 方法重写：同名覆盖，各说各话

```python
class Dog(Animal):
    def speak(self):          # 与父类同名 → 重写
        return f"{self.name} 汪汪叫！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫~"

print(Dog("旺财").speak())   # 旺财 汪汪叫！
print(Cat("咪咪").speak())   # 咪咪 喵喵叫~
```

> 重写时方法名、参数必须与父类一致（这里是 self）

<!-- 讲者备注：【特写】子类用同名方法盖掉父类的。Dog 说汪汪、Cat 说喵喵,方法名都是 speak,参数都是 self。叮咛:方法名拼写必须和父类一字不差,否则悄悄变新方法,没"重写"成。 -->

---

# ❗ 构造器继承：两种写法

**写法A：不写 `__init__` → 直接用父类构造器**

```python
class Point3D_A(Point2D):
    z = 0            # 只能靠类属性补默认值
```

**写法B：写 `__init__` + `super()__init__()` 扩展**

```python
class Point3D_B(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # 先初始化父类 x,y
        self.z = z               # 再新增 z
q = Point3D_B(1, 2, 3)
print((q.x, q.y, q.z))           # (1, 2, 3)
```

<!-- 讲者备注：【难点】两种构造器继承对照。A:子类不写 __init__ 白用父类,但补不了新增属性; B:子类重写 __init__,必须 super().__init__() 先把父类 x,y 初始化,再设自己的 z。铁律:自己重写 __init__ 就必须 super 补父类。 -->

---
layout: section
---

## 第三幕 · 多态与 AI 接口

<!-- 转场
讲者备注：【转场】幕卡,淡入切幕。一句话预告本幕:重写加上一个"统一调用"的循环,就是多态。再加一个 AI 模型类,把 train/predict 接口封装收束成三大特性齐活。 -->

---

# 多态：一个 speak，各自动作

```python
animals = [Dog("大黄"), Cat("小白"), Animal("普通动物")]
for a in animals:          # 统一调用同一个方法名
    print(a.speak())
```

```
大黄 汪汪叫！
小白 喵喵叫~
普通动物 发出叫声
```

> 调用者只认识"会 speak() 的东西"，不关心它是 Dog 还是 Cat → 面向接口编程

<!-- 讲者备注：【特写】多态的真身:一个 for 循环调同一方法名,却因对象类型不同给出不同结果。调用方只认接口 speak(),不认具体类型。给一句:对扩展开放、对修改关闭——加新子类不用改循环。 -->

---

# ✨ AI 赋能：train / predict 接口封装

```python
class BaseModel:
    def train(self, X, y):     # 公共接口
        raise NotImplementedError("子类必须实现 train")
    def predict(self, X):      # 公共接口
        raise NotImplementedError("子类必须实现 predict")

model = LinearModel()          # 子类实现具体算法
model.train(X, y)              # 对外：训练
result = model.predict(X_new)  # 对外：预测
```

- 公有 `train()/predict()`：统一入口
- 私有 `_w`/`_b`/`_lr`：权重与超参数，防外部误改
- 使用者只关心"喂数据→训练→拿预测"，不关心内部算法

<!-- 讲者备注：【思政/AI】把多态接口接到 AI 模型开发。BaseModel 定接口,子类 LinearModel 给实现,私有权重防误改。这一个 train/predict 范式 = 继承+多态+封装的合体。落点:三大特性在模型类里齐了。 -->

---

# 常见错误：四个坑

| 想干嘛 | 坑 | 对的做法 |
|---|---|---|
| 重写构造器 | 忘 `super().__init__()` | 先 super() 补父类 |
| 重写方法 | 方法名拼错 | 与父类名一字不差 |
| 父类属性 | 未初始化就报错 | 先 super 再设新属性 |
| 该用多态 | 一堆类型判断 | 统一接口 + 子类实现 |

<!-- 讲者备注：【全景】四坑速查:忘 super、方法名拼错、父类没初始化、多用类型判断。每个都能抛错给学生猜再给正解。是评论区高频。 -->

---

# 结课：封装继承多态，至此齐了

> 子类继承父类，白捡属性和方法，
> 重写同名定个性，构造器要 super 补，
> 一个接口多态实现，对扩展开放——
> 面向对象三大特性，到此收束成一套。

🔜 下节预告：机器学习入门

<!-- 讲者备注：【空镜】收尾口诀 + 悬念。四句把继承、重写、super、多态一剑收束,点出三大特性在 AI 模型类里合体。预告:下节正式进入机器学习,用类封装好的接口喂数据、训练、预测。致谢。 -->