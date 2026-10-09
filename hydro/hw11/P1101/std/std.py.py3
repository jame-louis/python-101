# P1101 基础继承（基础·无输入）标程
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 发出叫声"

    def move(self):
        return f"{self.name} 在移动"

class Dog(Animal):       # 继承自 Animal
    pass                  # 直接用父类的全部内容

d = Dog("旺财")
print(d.speak())   # 继承来的方法
print(d.move())    # 继承来的方法