#!/usr/bin/env python3
"""P0704 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出若干整数，每行一个，以 -1 结束。固定种子，可复现。"""
import random
import sys

random.seed(10704)

def main():
    case = int(sys.argv[1])
    if case == 1:
        nums = [5, 10, -1]          # 样例
    elif case == 2:
        nums = [7, -1]              # 单个数
    elif case == 3:
        nums = [-1]                 # 直接结束，无数
    elif case == 4:
        nums = [3, 3, 3, 3, -1]     # 全相同
    elif case == 5:
        nums = [-5, 0, 5, -1]       # 含负数与 0
    elif case <= 7:
        n = random.randint(1, 5)
        nums = [random.randint(-100, 100) for _ in range(n)] + [-1]
    elif case <= 9:
        n = random.randint(5, 50)
        nums = [random.randint(-10**6, 10**6) for _ in range(n)] + [-1]
    else:
        n = random.randint(50, 200)
        nums = [random.randint(0, 10**6) for _ in range(n)] + [-1]
    for x in nums:
        print(x)

if __name__ == "__main__":
    main()