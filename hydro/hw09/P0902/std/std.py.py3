# P0902 sorted 按 key 排序（基础·无输入）标程
pairs = [("b", 2), ("a", 4), ("c", 1)]
print(sorted(pairs, key=lambda t: t[1]))            # 按第二个元素升序
print(sorted(pairs, key=lambda t: t[1], reverse=True))  # 降序