#!/usr/bin/env python3
"""P0404 数据生成器: python3 gen.py <case_id> > testdata/N.in
一行内给出若干整数成绩（程序用 input().split()+map 一次性读取）。"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003)

    if case == 1:
        print("78 88 95 66 90"); return      # 样例（奇数个）
    if case == 2:
        print("78 88 95 66"); return         # 偶数个，测中位数取中间两个
    if case == 3:
        print("100 100 100 100 100"); return # 全相同
    if case == 4:
        print("42"); return                  # 单元素
    if case == 5:
        print("90 50 50 80 50 20 5 5 5"); return  # 大量重复，测去重排序与中位数
    if case <= 7:
        n = random.randint(50, 300)
    else:
        n = random.randint(5000, 100000)
    vals = [random.randint(0, 1000) for _ in range(n)]
    print(" ".join(map(str, vals)))

if __name__ == "__main__":
    main()