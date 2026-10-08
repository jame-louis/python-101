#!/usr/bin/env python3
"""P0705 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一个正整数 n。固定种子，可复现。"""
import random
import sys

random.seed(10705)

def main():
    case = int(sys.argv[1])
    if case == 1:
        n = 7                       # 样例
    elif case == 2:
        n = 1                       # 边界：无数
    elif case == 3:
        n = 2                       # 最小素数
    elif case == 4:
        n = 10                      # 样例2
    elif case == 5:
        n = 20                      # 边界混合
    elif case <= 7:
        n = random.randint(1, 100)
    elif case <= 9:
        n = random.randint(500, 2000)
    else:
        n = random.randint(5000, 100000)
    print(n)

if __name__ == "__main__":
    main()