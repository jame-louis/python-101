# P1103 构造器继承 super（基础·无输入）标程
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # 先初始化父类 x,y
        self.z = z               # 再新增 z

q = Point3D(1, 2, 3)
print((q.x, q.y, q.z))          # (1, 2, 3)