#!/usr/bin/env python3
"""P0504 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一串英文单词（空格分隔）。固定种子，可复现。"""
import random
import sys

random.seed(10504)
WORDS = ["the", "apple", "banana", "data", "model", "train", "loss",
         "python", "ai", "set", "dict", "算法", "token", "epoch"]

def main():
    case = int(sys.argv[1])
    if case == 1:
        print("the apple the banana the apple")   # 样例
    elif case == 2:
        print("cat")                             # 单元素
    elif case == 3:
        print("cat cat cat cat")                 # 全相同
    elif case == 4:
        print("x y z")                           # 全不重复
    elif case <= 6:
        n = random.randint(1, 30)                # 小数据
        print(" ".join(random.choice(WORDS) for _ in range(n)))
    elif case <= 8:
        n = random.randint(100, 500)             # 中数据
        print(" ".join(random.choice(WORDS) for _ in range(n)))
    else:
        n = random.randint(1000, 10000)          # 大数据
        print(" ".join(random.choice(WORDS) for _ in range(n)))

if __name__ == "__main__":
    main()