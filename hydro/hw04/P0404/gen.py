#!/usr/bin/env python3
"""P0404 数据生成器: python3 gen.py <case_id> > testdata/N.in"""
import random
import string
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003 + 3)

    if case == 1:
        words = ["Hello", "WORLD", "python"]
        emit(words)
        return

    if case <= 3:
        n = random.randint(1, 12)
        max_len = 8
    elif case <= 7:
        n = random.randint(100, 1000)
        max_len = 20
    else:
        n = random.randint(5000, 100000)
        max_len = 30

    words = []
    for _ in range(n):
        ln = random.randint(1, max_len)
        w = ''.join(random.choice(string.ascii_letters) for _ in range(ln))
        words.append(w)
    emit(words)

def emit(words):
    print(len(words))
    for w in words:
        print(w)

if __name__ == "__main__":
    main()