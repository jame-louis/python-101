#!/usr/bin/env python3
"""P1005 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出三个非负整数：初始余额、存入金额、取出金额。固定种子，可复现。"""
import random
import sys

random.seed(11005)

def main():
    case = int(sys.argv[1])
    if case == 1:
        vals = [100, 50, 30]      # 样例：成功
    elif case == 2:
        vals = [100, 0, 200]      # 样例：失败
    elif case == 3:
        vals = [50, 0, 50]        # 恰好相等 → 成功
    elif case == 4:
        vals = [50, 10, 100]      # 失败
    elif case == 5:
        vals = [0, 100, 50]       # 0 起步
    elif case == 6:
        vals = [100, 100, 100]    # 恰好取完
    elif case <= 8:
        init = random.randint(0, 1000)
        depo = random.randint(0, 1000)
        witd = random.randint(0, 1500)   # 含失败概率
        vals = [init, depo, witd]
    else:
        init = random.randint(0, 10**6)
        depo = random.randint(0, 10**6)
        witd = random.randint(0, 10**6)
        vals = [init, depo, witd]
    for v in vals:
        print(v)

if __name__ == "__main__":
    main()