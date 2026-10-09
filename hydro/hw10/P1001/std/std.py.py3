# P1001 定义类并调用（基础·无输入）标程
class Student:
    school = "xx学院"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"我是{self.name}，{self.age}岁，来自{self.school}"

s1 = Student("小明", 20)      # 实例化
s2 = Student("小红", 21)
print(s1.say_hello())          # 实例.方法()
print(s2.say_hello())