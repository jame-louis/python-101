# P0404 成绩统计（综合·输入+提示，严格匹配）标程
# 一整行读入、split、map 一次转成整数列表，全程无需循环/分支
scores = list(map(int, input("请输入成绩（空格分隔）：").split()))
print()                    # 提示语后换行，让输出清晰独立成行

s = sorted(scores)         # 排序（返回新列表，不改变原列表）
n = len(s)

print("升序排序：", " ".join(map(str, s)))
print("最高分：", s[-1])
print("最低分：", s[0])
print("总分：", sum(scores))
print("平均分：", f"{sum(scores) / n:.2f}")
# 中位数：奇数取正中间，偶数取中间两个的平均 —— 用除法一次算好，无需分支
print("中位数：", f"{(s[(n - 1) // 2] + s[n // 2]) / 2:.2f}")