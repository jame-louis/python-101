#!/usr/bin/env python3
"""P0505 数据生成器: python3 gen.py <case_id> > testdata/N.in
输出四个值：学习率(小数) 轮数(整数) 优化器(英文) 设备(英文)。
固定种子，可复现。"""
import random
import sys

random.seed(10505)
OPTS = ["adam", "sgd", "rmsprop", "adagrad"]
DEVS = ["cpu", "cuda", "mps"]

def main():
    case = int(sys.argv[1])
    if case == 1:
        print("0.01 50 adam cuda")      # 样例
    elif case == 2:
        print("0.0001 10 sgd cpu")      # 样例2：小学习率+不同设备
    elif case == 3:
        print("0.1 1 rmsprop mps")      # 边界：1 轮
    elif case == 4:
        print("1.0 3 adagrad cpu")      # 边界：学习率 1.0
    else:
        lr = f"{random.uniform(0.0001, 1.0):.4f}"     # 4 位小数
        ep = str(random.randint(1, 1000))
        opt = random.choice(OPTS)
        dev = random.choice(DEVS)
        print(f"{lr} {ep} {opt} {dev}")

if __name__ == "__main__":
    main()