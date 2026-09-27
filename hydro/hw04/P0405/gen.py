#!/usr/bin/env python3
"""P0405 数据生成器: python3 gen.py <case_id> > testdata/N.in
一行内给出若干轮训练损失（一位小数的浮点数，保证 str 输出精确）。
程序用 input().split()+map 一次性读取。"""
import random
import sys

def main():
    case = int(sys.argv[1])
    random.seed(case * 1000003 + 7)

    if case == 1:
        print("1.2 0.8 0.6 0.3 0.2"); return        # 样例
    if case == 2:
        print("0.5 0.5 0.5"); return                 # 全相同（易错：index 取第一个）
    if case == 3:
        print("3.0"); return                         # 单元素
    if case == 4:
        print("0.1 2.5 0.9 9.9 0.1"); return        # 最小值在首位且重复
    if case == 5:
        # 若干一位小数，混合大小
        vals = [random.randint(1, 500) / 10.0 for _ in range(random.randint(5, 20))]
        print(" ".join(str(v) for v in vals)); return
    if case <= 7:
        n = random.randint(50, 300)
    else:
        n = random.randint(5000, 100000)
    vals = [random.randint(1, 500) / 10.0 for _ in range(n)]
    print(" ".join(f"{v:.1f}" for v in vals))

if __name__ == "__main__":
    main()