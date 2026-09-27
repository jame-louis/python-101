#!/usr/bin/env python3
"""P0401 数据生成器: python3 gen.py <case_id> > testdata/N.in"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003)

    if case == 1:
        # 样例
        init = [78, 88, 95, 66]
        ops = [
            ('append', 100),
            ('insert', 1, 99),
            ('remove', 95),
        ]
        n = len(init)
    elif case <= 3:
        n = random.randint(1, 10)
        k = random.randint(1, 8)
    elif case <= 6:
        n = random.randint(50, 200)
        k = random.randint(50, 150)
    else:
        n = random.randint(5000, 100000)
        k = random.randint(5000, 50000)

    if case != 1:
        init = [random.randint(0, 1000) for _ in range(n)]
        work = init[:]
        ops = []
        for _ in range(k):
            t = random.choice(['append', 'insert', 'remove'])
            if t == 'append':
                x = random.randint(0, 1000)
                ops.append(('append', x))
                work.append(x)
            elif t == 'insert':
                i = random.randint(0, len(work))
                x = random.randint(0, 1000)
                ops.append(('insert', i, x))
                work.insert(i, x)
            else:
                if not work:
                    x = random.randint(0, 1000)
                    ops.append(('append', x))
                    work.append(x)
                else:
                    x = random.choice(work)
                    ops.append(('remove', x))
                    work.remove(x)

    print(n)
    print(' '.join(map(str, init)))
    print(len(ops))
    for op in ops:
        print(' '.join(map(str, op)))

if __name__ == "__main__":
    main()