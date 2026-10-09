# P0904 安全除法（综合·输入+提示，严格匹配）
print("请输入 被除数 除数（空格分隔）：")
a, b = map(int, input().split())
try:
    print(f"商 = {a / b:.2f}")
except ZeroDivisionError:
    print("除数不能为 0")