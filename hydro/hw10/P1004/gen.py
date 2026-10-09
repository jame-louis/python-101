#!/usr/bin/env python3
"""P1004 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出两行：姓名（字符串）、年龄（整数）。固定种子，可复现。"""
import random
import sys

random.seed(11004)
NAMES = ["小明", "小红", "小刚", "小丽", "小华", "阿杰", "乐乐", "冬冬"]

def main():
    case = int(sys.argv[1])
    if case == 1:
        name, age = "小明", 20       # 样例
    elif case == 2:
        name, age = "小红", 21       # 样例2
    elif case == 3:
        name, age = "小刚", 18       # 边界小年龄
    elif case == 4:
        name, age = "小华", 30       # 边界大年龄
    else:
        name = random.choice(NAMES)
        age = random.randint(18, 30)
    print(name)
    print(age)

if __name__ == "__main__":
    main()