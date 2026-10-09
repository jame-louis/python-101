#!/usr/bin/env python3
"""P0804 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一个半径 r（可为小数）。固定种子，可复现。"""
import random
import sys

random.seed(10804)

def main():
    case = int(sys.argv[1])
    if case == 1:
        r = 2                  # 样例
    elif case == 2:
        r = 5                  # 样例2
    elif case == 3:
        r = 0.5                # 小数
    elif case == 4:
        r = 10                 # 整数
    elif case == 5:
        r = 0.1                # 小半径边界
    elif case <= 7:
        r = round(random.uniform(1, 100), 2)   # 小随机
    elif case <= 9:
        r = round(random.uniform(100, 1000), 2)  # 中随机
    else:
        r = round(random.uniform(1000, 100000), 2)  # 大随机
    print(r)

if __name__ == "__main__":
    main()