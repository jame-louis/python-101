#!/usr/bin/env python3
import sys
import random

case_id = int(sys.argv[1])
random.seed(case_id * 1000003)

if case_id == 1:
    a, b = 1, 2
elif case_id == 2:
    a, b = -5, 5
elif case_id <= 5:
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
elif case_id <= 8:
    a = random.randint(-10**6, 10**6)
    b = random.randint(-10**6, 10**6)
else:
    a = random.randint(-10**9, 10**9)
    b = random.randint(-10**9, 10**9)

print(a, b)
