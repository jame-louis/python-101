# P0705 质数判断（综合·输入+提示，严格匹配）
n = int(input("请输入一个正整数："))
primes = []
for x in range(2, n + 1):
    is_prime = True
    for d in range(2, int(x ** 0.5) + 1):   # 检查 2..sqrt(x) 有无约数
        if x % d == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)
print()                                     # 提示语后换行，输出独立成行

line = ""
for p in primes:
    line += str(p) + " "
print(line.strip())                         # 去尾部空格，单空格分隔
print("共", len(primes), "个素数")