# P0402 三种插入方法 标程  (append / extend / insert)
lst = [int(x) for x in input().split()]
k = int(input())
for _ in range(k):
    parts = input().split()
    op = parts[0]
    if op == 'append':
        lst.append(int(parts[1]))
    elif op == 'extend':
        lst.extend(int(x) for x in parts[1:])
    elif op == 'insert':
        lst.insert(int(parts[1]), int(parts[2]))
print(' '.join(map(str, lst)))