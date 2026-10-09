# P1002 类属性 vs 实例属性（基础·无输入）标程
class Student:
    school = "嘉庚学院"          # 类属性（共享）

    def __init__(self, name):
        self.name = name        # 实例属性（独立）

s1 = Student("小明")
s2 = Student("小红")
print(s1.school, s2.school)     # 共享：都一样

s1.name = "阿明"                # 改实例属性，只影响 s1
print(s1.name, s2.name)         # 阿明 小红

Student.school = "新学院"        # 改类属性，影响所有实例
print(s1.school, s2.school)     # 新学院 新学院