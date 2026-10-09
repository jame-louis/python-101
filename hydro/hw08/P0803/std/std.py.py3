# P0803 global 作用域（基础·无输入）标程
g = 10

def change():
    global g          # 声明后才会改全局
    g = 99

change()
print("全局修改后 g =", g)        # 99

g = 10
def no_change():
    g = 5             # 局部变量，没写 global，不影响全局
no_change()
print("局部赋值不影响全局 g =", g)  # 10