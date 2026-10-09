#!/usr/bin/env python3
"""P0905 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一个 0~100 的整数成绩。固定种子，可复现。"""
import random
import sys

random.seed(10905)

def main():
    case = int(sys.argv[1])
    if case == 1:
        score = 85          # 样例：通过
    elif case == 2:
        score = 59          # 样例：不通过
    elif case == 3:
        score = 60          # 边界：恰好通过
    elif case == 4:
        score = 90          # 通过
    elif case == 5:
        score = 100         # 上限
    elif case == 6:
        score = 0           # 下限
    elif case <= 8:
        score = random.randint(0, 100)
    else:
        score = random.randint(40, 100)
    print(score)

if __name__ == "__main__":
    main()