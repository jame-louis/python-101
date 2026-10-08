#!/usr/bin/env python3
"""P0602 数据生成器: python3 gen.py <case_id> > testdata/N.in
本题为「无输入」基础题：程序不读取任何输入，输出固定。
.in 仅放一个占位标记以满足评测数据非空。"""
import sys

def main():
    _ = int(sys.argv[1])          # 忽略编号：所有测试点输出一致
    print("no-input")

if __name__ == "__main__":
    main()