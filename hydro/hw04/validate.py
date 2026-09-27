#!/usr/bin/env python3
"""hw04 题目集数据校验与标程回归

用法: python3 hydro/hw04/validate.py
对每一题：所有测试点输入/输出非空，且用标程重新计算输出，与 .out 逐字节一致。
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = ["P0401", "P0402", "P0403", "P0404", "P0405"]
STD = "std.py.py3"

def check(problem: str) -> bool:
    ok = True
    pdir = ROOT / problem
    std = pdir / "std" / STD
    for i in range(1, 11):
        fin = pdir / "testdata" / f"{i}.in"
        fout = pdir / "testdata" / f"{i}.out"
        if not fin.exists() or fin.stat().st_size == 0:
            print(f"  ✗ {problem}: {fin.name} 缺失或为空")
            ok = False
            continue
        if not fout.exists() or fout.stat().st_size == 0:
            print(f"  ✗ {problem}: {fout.name} 缺失或为空")
            ok = False
            continue
        inp = fin.read_text()
        want = fout.read_text()
        got = subprocess.run(
            [sys.executable, str(std)], input=inp, capture_output=True, text=True
        )
        if got.returncode != 0:
            print(f"  ✗ {problem}: {fin.name} 标程运行失败: {got.stderr.strip()}")
            ok = False
        elif got.stdout != want:
            print(f"  ✗ {problem}: {fin.name} 输出与 .out 不一致")
            ok = False
    if ok:
        print(f"  ✓ {problem}: 10 个测试点全部通过")
    return ok

def main() -> int:
    all_ok = True
    for p in PROBLEMS:
        all_ok &= check(p)
    print("全部通过 ✅" if all_ok else "存在失败 ❌")
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())