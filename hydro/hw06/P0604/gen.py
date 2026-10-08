#!/usr/bin/env python3
"""P0604 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出两个整数 a、b，各占一行。固定种子，可复现。"""
import random
import sys

random.seed(10604)

def main():
    case = int(sys.argv[1])
    if case == 1:
        a, b = 5, 8          # 样例：小于
    elif case == 2:
        a, b = 8, 8          # 相等
    elif case == 3:
        a, b = 9, 2          # 样例：大于
    elif case == 4:
        a, b = -1, 0         # 负数 < 零
    elif case == 5:
        a, b = 0, -1         # 零 > 负数
    elif case == 6:
        a, b = 7, 7          # 相等
    elif case <= 8:
        a = random.randint(-50, 50)
        b = random.randint(-50, 50)
    else:
        a = random.randint(-10**9, 10**9)
        b = random.randint(-10**9, 10**9)
        if case == 10:
            b = a            # 大数据相等
    print(a)
    print(b)

if __name__ == "__main__":
    main()