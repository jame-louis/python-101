# P0401 分数表增删改查 标程
n = int(input())
scores = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    parts = input().split()
    op = parts[0]
    if op == 'append':
        scores.append(int(parts[1]))
    elif op == 'insert':
        scores.insert(int(parts[1]), int(parts[2]))
    elif op == 'remove':
        scores.remove(int(parts[1]))
print(' '.join(map(str, scores)))
print(max(scores))
print(min(scores))