# P0702 break/continue 控制流程（基础·无输入）标程
print("continue跳过3：", end="")
for i in range(1, 7):
    if i == 3:
        continue          # 跳过 3，其余继续
    print(i, end=" ")
print()
print("break遇到5停止：", end="")
for i in range(1, 7):
    if i == 5:
        break             # 到 5 就停（不含 5）
    print(i, end=" ")
print()