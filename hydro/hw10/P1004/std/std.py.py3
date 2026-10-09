# P1004 学生自我介绍（综合·输入+提示，严格匹配）
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"我是{self.name}，{self.age}岁"

print("请输入姓名：")
name = input()
print("请输入年龄：")
age = int(input())

s = Student(name, age)
print(s.say_hello())