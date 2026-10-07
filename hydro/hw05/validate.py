#!/usr/bin/env python3
"""hw05 题目集数据校验与标程回归

用法: python3 hydro/hw05/validate.py
对每一题：按 testdata/config.yaml 声明的所有测试点，校验输入/输出非空，
并用标程重新计算输出，与 .out 逐字节一致。
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = ["P0501", "P0502", "P0503", "P0504", "P0505"]
STD = "std.py.py3"

def case_count(problem: str) -> int:
    cfg = (ROOT / problem / "testdata" / "config.yaml").read_text()
    return len(re.findall(r"input:\s*(\d+)\.in", cfg))

def check(problem: str) -> bool:
    ok = True
    pdir = ROOT / problem
    std = pdir / "std" / STD
    for i in range(1, case_count(problem) + 1):
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
        print(f"  ✓ {problem}: {case_count(problem)} 个测试点全部通过")
    return ok

def main() -> int:
    all_ok = True
    for p in PROBLEMS:
        all_ok &= check(p)
    print("全部通过 ✅" if all_ok else "存在失败 ❌")
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())