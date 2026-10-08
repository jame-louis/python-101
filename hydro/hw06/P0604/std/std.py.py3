# P0604 比大小（综合·输入+提示，严格匹配）
print("请输入a：")
a = int(input())
print("请输入b：")
b = int(input())
if a > b:
    print(f"{a} > {b}")
elif a == b:
    print(f"{a} == {b}")
else:
    print(f"{a} < {b}")