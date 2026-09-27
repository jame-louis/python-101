# P0403 元组解包与坐标统计 标程
m = int(input())
points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x, y))

sum_x = 0
sum_y = 0
for point in points:
    x, y = point          # 元组解包
    sum_x += x
    sum_y += y
    print(f"{x} + {y} = {x + y}")
print(f"sum_x = {sum_x}")
print(f"sum_y = {sum_y}")