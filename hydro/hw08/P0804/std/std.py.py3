# P0804 圆面积计算器（综合·输入+提示，严格匹配）
PI = 3.14159

def area(r):
    return PI * r * r

print("请输入半径 r：")
r = float(input())
print(f"面积 = {area(r):.2f}")