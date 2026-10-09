# P1003 私有属性与 getter（基础·无输入）标程
class Student:
    def __init__(self, name, sid):
        self.name = name          # 公有属性
        self.__sid = sid          # "私有"（名称修饰）

    def get_sid(self):            # getter：公开的读取通道
        return self.__sid

s = Student("小明", "2025001")
print(s.name)              # 公有，直接可读
print(s.get_sid())         # 通过 getter 读私有
print(s._Student__sid)     # 名称修饰后仍可访问（但不该这么用）