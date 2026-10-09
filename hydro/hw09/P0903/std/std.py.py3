# P0903 map 与 filter（基础·无输入）标程
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * x, nums)))       # 每个数平方

a = [22, 18, 30, 16, 25]
print(list(filter(lambda x: x >= 18, a)))     # 保留成年