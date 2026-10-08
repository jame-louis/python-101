#!/usr/bin/env python3
"""P0605 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出一个 0~100 的整数成绩。固定种子，可复现。"""
import random
import sys

random.seed(10605)

def main():
    case = int(sys.argv[1])
    if case == 1:
        score = 85          # 样例：良好
    elif case == 2:
        score = 59          # 样例：不及格（边界）
    elif case == 3:
        score = 90          # 边界：优秀（>=90）
    elif case == 4:
        score = 89          # 边界：良好（恰低于 90）
    elif case == 5:
        score = 60          # 边界：及格（>=60）
    elif case == 6:
        score = 100         # 满绩
    elif case == 7:
        score = 0           # 最低
    elif case <= 9:
        score = random.randint(50, 100)   # 中高带
    else:
        score = random.randint(0, 100)    # 全带
    print(score)

if __name__ == "__main__":
    main()