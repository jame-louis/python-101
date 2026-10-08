# P0601 正负与奇偶判断（基础·无输入）标程
n = -5
# 正负：if-elif-else 三态判断
if n > 0:
    print("正数")
elif n < 0:
    print("负数")
else:
    print("零")
# 奇偶：if-else + 取模
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")