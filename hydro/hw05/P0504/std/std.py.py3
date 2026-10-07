# P0504 NLP 词频统计（综合·输入+提示，严格匹配）
# 一整行读入单词，用循环遍历 + 字典 get 统计词频
words = input("请输入一串英文单词（空格分隔）：").split()
freq = {}
for w in words:                     # 遍历每个单词
    freq[w] = freq.get(w, 0) + 1    # 词频 = 原值+1，无则从 0 起
print()                             # 提示语后换行，输出独立成行

for w in sorted(freq):              # 按键排序输出，保证顺序确定
    print(w, freq[w])