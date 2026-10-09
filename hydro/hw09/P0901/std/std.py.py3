# P0901 lambda 改写 def（基础·无输入）标程
add = lambda a, b: a + b      # 匿名函数：等价于 def add(a,b): return a+b
print(add(3, 4))              # 7
print(add(10, 20))            # 30
print(add(-1, 1))             # 0