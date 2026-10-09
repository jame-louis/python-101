#!/usr/bin/env python3
"""P0805 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一行空格分隔的若干整数。固定种子，可复现。"""
import random
import sys

random.seed(10805)

def main():
    case = int(sys.argv[1])
    if case == 1:
        vals = [3, 5, 8]          # 样例
    elif case == 2:
        vals = [7]                # 单数
    elif case == 3:
        vals = [4, 4, 4]          # 全相同
    elif case == 4:
        vals = [-5, 0, 6, -1]     # 负数与 0
    elif case <= 6:
        vals = [random.randint(-100, 100) for _ in range(random.randint(1, 5))]
    elif case <= 8:
        vals = [random.randint(-10**6, 10**6) for _ in range(random.randint(5, 50))]
    else:
        vals = [random.randint(-10**9, 10**9) for _ in range(random.randint(50, 200))]
    print(" ".join(map(str, vals)))

if __name__ == "__main__":
    main()