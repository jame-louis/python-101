#!/usr/bin/env python3
"""P0405 数据生成器: python3 gen.py <case_id> > testdata/N.in"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003 + 4)

    if case == 1:
        emit([78, 88, 95, 66, 90])
        return
    if case == 2:
        emit([78, 88, 95, 66])    # n=4 偶数，须输出中间两个
        return
    if case == 3:
        emit([100] * 7)           # 全相同
        return
    if case == 4:
        emit([50])                # 单元素
        return
    if case <= 7:
        n = random.randint(100, 1000)
        scores = [random.randint(0, 100) for _ in range(n)]
    else:
        n = random.randint(5000, 100000)
        scores = [random.randint(0, 10**6) for _ in range(n)]

    emit(scores)

def emit(scores):
    print(len(scores))
    print(' '.join(map(str, scores)))

if __name__ == "__main__":
    main()