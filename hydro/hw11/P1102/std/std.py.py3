# P1102 方法重写（基础·无输入）标程
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 发出叫声"

class Dog(Animal):
    def speak(self):                  # 重写
        return f"{self.name} 汪汪叫！"

class Cat(Animal):
    def speak(self):                  # 重写
        return f"{self.name} 喵喵叫~"

d = Dog("旺财")
c = Cat("咪咪")
a = Animal("普通动物")
print(d.speak())   # 汪
print(c.speak())   # 喵
print(a.speak())   # 原始