#!/usr/bin/env python3
"""P0402 数据生成器: python3 gen.py <case_id> > testdata/N.in"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003 + 1)

    if case == 1:
        init = [1, 2, 3]
        ops = [
            ('append', 4),
            ('extend', 5, 6),
            ('insert', 1, 99),
        ]
        # 特殊：append 单个列表，与 extend 对比
        ops = [
            ('append', 4),
            ('append', 5),
            ('insert', 1, 99),
            ('extend', [7, 8]),
        ]
        emit(init, ops)
        return

    if case <= 3:
        m = random.randint(1, 12)
        k = random.randint(1, 12)
    elif case <= 7:
        m = random.randint(60, 200)
        k = random.randint(100, 300)
    else:
        m = random.randint(5000, 100000)
        k = random.randint(5000, 50000)

    init = [random.randint(0, 100) for _ in range(m)]
    work = init[:]
    ops = []
    for _ in range(k):
        t = random.choice(['append', 'extend', 'insert'])
        if t == 'append':
            x = random.randint(0, 1000)
            ops.append(('append', x))
            work.append(x)
        elif t == 'extend':
            cnt = random.randint(1, 5)
            vals = [random.randint(0, 1000) for _ in range(cnt)]
            ops.append(('extend',) + tuple(vals))
            work.extend(vals)
        else:
            i = random.randint(0, len(work))
            x = random.randint(0, 1000)
            ops.append(('insert', i, x))
            work.insert(i, x)

    emit(init, ops)

def emit(init, ops):
    print(' '.join(map(str, init)))
    print(len(ops))
    for op in ops:
        if op[0] == 'extend' and isinstance(op[1], list):
            print('extend ' + ' '.join(map(str, op[1])))
        else:
            print(' '.join(map(str, op)))

if __name__ == "__main__":
    main()