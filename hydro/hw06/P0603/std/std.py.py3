# P0603 三数比大小（基础·无输入）标程
a, b, c = 9, 2, 5
if a >= b and a >= c:
    big = a
elif b >= c:
    big = b
else:
    big = c
print("最大的是：", big)