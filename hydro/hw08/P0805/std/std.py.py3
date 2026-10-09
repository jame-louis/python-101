# P0805 可变参数求和（综合·输入+提示，严格匹配）
def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total

print("请输入若干整数（空格分隔）：")
nums = []
for x in input().split():       # 把一整行按空格拆
    nums.append(int(x))
print("和 =", sum_all(*nums))    # *nums 解包成多个实参
print("共", len(nums), "个")