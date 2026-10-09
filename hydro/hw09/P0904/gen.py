#!/usr/bin/env python3
"""P0904 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出两个整数 a b（空格分隔）。固定种子，可复现。"""
import random
import sys

random.seed(10904)

def main():
    case = int(sys.argv[1])
    if case == 1:
        vals = [10, 5]        # 样例：整除
    elif case == 2:
        vals = [5, 0]         # 样例：除零
    elif case == 3:
        vals = [7, 3]         # 非整除小数
    elif case == 4:
        vals = [21, 7]        # 整除
    elif case == 5:
        vals = [-8, 4]        # 负被除数
    elif case == 6:
        vals = [0, 5]         # 被除数为 0
    elif case <= 8:
        a = random.randint(0, 100)
        b = random.choice([random.randint(1, 50), 0])   # 偶发除零
        vals = [a, b]
    else:
        a = random.randint(-10**9, 10**9)
        b = random.choice([random.randint(-10**6, 10**6), 0])  # 含除零大数
        if b == 0 and case == 9:
            pass
        vals = [a, b]
    print(vals[0], vals[1])

if __name__ == "__main__":
    main()