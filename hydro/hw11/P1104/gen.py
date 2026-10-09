#!/usr/bin/env python3
"""P1104 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出三个整数 x y z（空格分隔）。固定种子，可复现。"""
import random
import sys

random.seed(11104)

def main():
    case = int(sys.argv[1])
    if case == 1:
        vals = [1, 2, 3]        # 样例
    elif case == 2:
        vals = [3, 1, 4]        # 样例2
    elif case == 3:
        vals = [0, 0, 0]        # 全零
    elif case == 4:
        vals = [10, -5, 2]      # 负数
    elif case == 5:
        vals = [-1, -2, -3]     # 全负
    elif case <= 7:
        vals = [random.randint(-100, 100) for _ in range(3)]
    elif case <= 9:
        vals = [random.randint(-10**6, 10**6) for _ in range(3)]
    else:
        vals = [random.randint(-10**9, 10**9) for _ in range(3)]
    print(" ".join(map(str, vals)))

if __name__ == "__main__":
    main()