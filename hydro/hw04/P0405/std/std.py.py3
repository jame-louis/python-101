# P0405 训练损失分析（综合·输入+提示，严格匹配）标程
# 一整行读入、split、map 一次转成浮点列表，全程无需循环/分支
losses = list(map(float, input("请输入各轮损失（空格分隔）：").split()))
print()

best = min(losses)             # 最低损失
epoch = losses.index(best) + 1 # 第一次出现的位置 + 1 = 轮次
record = (epoch, best)         # 用元组保存「轮次, 损失」

print("最低损失：", best)
print("最优轮次：", epoch)
desc = sorted(losses, reverse=True)
print("从高到低：", " ".join(map(str, desc)))
print("最优记录（轮次, 损失）：", record)