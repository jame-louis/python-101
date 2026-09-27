#!/usr/bin/env python3
"""P0403 数据生成器: python3 gen.py <case_id> > testdata/N.in"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003 + 2)

    if case == 1:
        points = [(3, 5), (1, 2), (10, 20)]
        emit(points)
        return

    if case <= 3:
        m = random.randint(1, 10)
    elif case <= 7:
        m = random.randint(100, 1000)
    else:
        m = random.randint(5000, 100000)

    points = []
    for _ in range(m):
        # case >= 4 时允许负坐标，覆盖更多边界
        lo = -10**9 if case >= 4 else 0
        x = random.randint(lo, 10**9)
        y = random.randint(lo, 10**9)
        points.append((x, y))
    emit(points)

def emit(points):
    print(len(points))
    for x, y in points:
        print(x, y)

if __name__ == "__main__":
    main()