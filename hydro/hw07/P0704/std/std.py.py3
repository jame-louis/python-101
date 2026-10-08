# P0704 while 读入统计（综合·输入+提示，严格匹配）
count = 0
total = 0
while True:
    print("请输入整数（输入-1结束）：")
    x = int(input())          # 每行一个整数
    if x == -1:               # 标记值 → 结束
        break
    total += x
    count += 1
print("个数：", count)
print("总和：", total)