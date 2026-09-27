# P0405 成绩统计（排序、最高、最低、中位数） 标程
n = int(input())
scores = list(map(int, input().split()))
scores.sort()
print(' '.join(map(str, scores)))
print(max(scores))
print(min(scores))
if n % 2 == 1:
    print(scores[n // 2])                 # 奇数个：取正中间
else:
    print(scores[n // 2 - 1], scores[n // 2])  # 偶数个：取中间两个