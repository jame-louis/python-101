# P0701 for+range() 累加求和（基础·无输入）标程
total = 0          # 1 到 200 的和
even = 0           # 其中的偶数和
for i in range(1, 201):   # range 差 1 缺尾，到 201 才含 200
    total += i
    if i % 2 == 0:
        even += i
print("1到200的和：", total)
print("其中偶数的和：", even)