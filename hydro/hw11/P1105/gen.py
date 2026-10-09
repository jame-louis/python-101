#!/usr/bin/env python3
"""P1105 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出两行：狗狗名字、猫咪名字。固定种子，可复现。"""
import random
import sys

random.seed(11105)
DOGS = ["大黄", "旺财", "阿黄", "lucky", "豆豆", "将军"]
CATS = ["小白", "咪咪", "雪球", "momo", "毛毛", "咪仔"]

def main():
    case = int(sys.argv[1])
    if case == 1:
        d, c = "大黄", "小白"       # 样例
    elif case == 2:
        d, c = "旺财", "咪咪"       # 样例2
    elif case == 3:
        d, c = "阿黄", "小白"       # 同名猫
    else:
        d = random.choice(DOGS)
        c = random.choice(CATS)
    print(d)
    print(c)

if __name__ == "__main__":
    main()