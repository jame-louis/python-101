#!/usr/bin/env python3
"""机器学习课程项目(第12–15讲)启动器：选择要运行的讲次脚本。

用法：
    uv run main.py                  # 列出脚本并提示
    uv run main.py 12               # 运行第12讲 KNN
    uv run main.py --no-plots 12    # 无头环境运行

对应脚本：
    12  knn_classifier.py      机器学习与 KNN(含决策树)
    13  kmeans_clustering.py   无监督学习与 k-means 聚类
    14  linear_regression.py   线性回归 y=kx+b
    15  neural_net.py          神经网络与 BP 非线性拟合
"""
from __future__ import annotations

import subprocess
import sys

SCRIPTS = {
    "12": "knn_classifier.py",
    "13": "kmeans_clustering.py",
    "14": "linear_regression.py",
    "15": "neural_net.py",
}


def main(argv: list[str] | None = None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return

    no_plots = "--no-plots" in argv
    lectures = [a for a in argv if a in SCRIPTS]
    if not lectures:
        print("请指定讲次: uv run main.py <12|13|14|15> [--no-plots]")
        return

    lectures = lectures[:1]  # 每次只运行一个
    script = SCRIPTS[lectures[0]]
    cmd = [sys.executable, script] + (["--no-plots"] if no_plots else [])
    print(f"运行第{lectures[0]}讲: {script}")
    subprocess.run(cmd)


if __name__ == "__main__":
    main()