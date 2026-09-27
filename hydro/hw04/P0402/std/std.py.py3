# P0402 三种插入方法（基础·无输入）标程
lst = [1, 2, 3]
lst.append(4)        # 追加一个元素
print(lst)           # [1, 2, 3, 4]

lst2 = [1, 2, 3]
lst2.extend([4, 5])  # 展开拼接
print(lst2)          # [1, 2, 3, 4, 5]

lst3 = [1, 2, 3]
lst3.insert(1, 99)   # 位置 1 前插入
print(lst3)          # [1, 99, 2, 3]

lst5 = [1, 2, 3]
lst5.append([4, 5])  # 易错：整体追加一个列表
print(lst5)          # [1, 2, 3, [4, 5]]