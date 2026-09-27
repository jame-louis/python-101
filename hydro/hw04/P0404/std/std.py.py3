# P0404 文本转小写清洗 标程  (NLP 批量处理)
n = int(input())
words = [input() for _ in range(n)]
cleaned = []
for w in words:
    cleaned.append(w.lower())
for c in cleaned:
    print(c)