# P0503 字典的增删改查（基础·无输入）
user = {"name": "Alice", "age": 20}

# 查：用键取值
print(user["name"])

# 改 / 增：改 age，新增 city
user["age"] = 21
user["city"] = "Xiamen"
print(user)

# 遍历键 / 值 / 键值对
print(list(user.keys()))
print(list(user.values()))
print(list(user.items()))

# 安全取值：get 找不到返回默认值，不报错
print(user.get("email", "无邮箱"))