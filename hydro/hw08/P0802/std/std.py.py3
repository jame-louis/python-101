# P0802 默认参数（基础·无输入）标程
def brief(name, city="厦门"):
    return name + "-" + city

print(brief("小明"))             # 默认 city = 厦门
print(brief("小红", "福州"))      # 位置参数覆盖
print(brief("小刚", city="泉州"))  # 关键字参数覆盖