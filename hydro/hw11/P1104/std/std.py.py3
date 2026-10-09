# P1104 三维点 super 扩展（综合·输入+提示，严格匹配）
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # 补父类 x,y
        self.z = z               # 新增 z

print("请输入 x y z（空格分隔）：")
x, y, z = map(int, input().split())
q = Point3D(x, y, z)
print((q.x, q.y, q.z))