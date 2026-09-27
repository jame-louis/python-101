# P0401 列表增删改查（基础·无输入）标程
scores = [78, 88, 95, 66]

print(scores[0], scores[-1], len(scores))  # 第一个、最后一个、长度

scores[1] = 99        # 修改：把第 2 个改成 99
scores.append(100)    # 末尾追加 100
print(scores)         # 改动+追加后的列表

scores.insert(0, 50)  # 在开头插入 50
scores.remove(95)     # 删除 95
print(scores)         # 最终列表