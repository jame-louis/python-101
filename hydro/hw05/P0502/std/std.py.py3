# P0502 集合的交、并、差（基础·无输入）
userA = {"电子", "游戏", "运动"}
userB = {"运动", "摄影", "电子"}

# 全部用 sorted() 保证输出顺序确定
jiaji = sorted(userA & userB)   # 交集：共同兴趣
bingji = sorted(userA | userB)  # 并集：全部兴趣
chaji = sorted(userA - userB)   # 差集：仅用户A独有

print("共同兴趣：", jiaji, "，共", len(jiaji), "个")
print("全部兴趣：", bingji, "，共", len(bingji), "个")
print("用户A独有：", chaji, "，共", len(chaji), "个")