# P0703 嵌套循环数字图案（基础·无输入）标程
for i in range(1, 6):            # 外层：行号 1..5
    for j in range(1, i + 1):    # 内层：每行打印 i 个数
        print(j, end="")         # 数字直接相连、不换行
    print()                      # 一行结束换行