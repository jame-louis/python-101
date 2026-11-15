#!/usr/bin/env python3
"""第15讲 · 神经网络原理与 BP 非线性拟合 —— 1-16-1 numpy 手写。

对应课件 lecture15.md：
    造曲线状数据 y = 0.5·sin(2u) + 0.3u → 手写 3 层 MLP(1→16→1, tanh) 训练 5000 轮
    → 前向/反向/更新循环 → 对比线性回归（一条直线）与神经网络的均方误差
    → 观察损失曲线是否一路下降。

用法：
    uv run neural_net.py            # 默认：完整流程 + 弹出 拟合对比图 + 损失曲线
    uv run neural_net.py --no-plots # 无头环境：只打印文字结果，不弹窗
"""
from __future__ import annotations

import argparse

import numpy as np

from plots import setup_zh_font

setup_zh_font()


class MLP:
    """3 层网络 1 -> n_hidden -> 1，tanh 激活，随机梯度下降更新。"""

    def __init__(self, n_hidden: int = 16, lr: float = 0.001):
        # He 初始化（课件代码沿用 sqrt(2.0)），截距初始为 0
        self.w1 = np.random.randn(1, n_hidden) * np.sqrt(2.0)
        self.b1 = np.zeros((1, n_hidden))
        self.w2 = np.random.randn(n_hidden, 1) * np.sqrt(2.0 / n_hidden)
        self.b2 = np.zeros((1, 1))
        self.lr = lr

    def forward(self, X: np.ndarray) -> np.ndarray:
        z1 = X @ self.w1 + self.b1
        self.a1 = np.tanh(z1)                    # 激活函数引入非线性
        return self.a1 @ self.w2 + self.b2

    def backward(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """一次『前向算误差 → 反向传播 → 梯度下降更新』，返回前向预测。"""
        y_pred = self.forward(X)
        dz2 = y_pred - y                         # 输出层误差
        # 更新输出层
        self.w2 -= self.lr * (self.a1.T @ dz2)
        self.b2 -= self.lr * dz2.sum(axis=0)
        # 误差反向传播到隐藏层（tanh 导数 = 1 - tanh²）
        dz1 = (dz2 @ self.w2.T) * (1 - self.a1 ** 2)
        self.w1 -= self.lr * (X.T @ dz1)
        self.b1 -= self.lr * dz1.sum(axis=0)
        return y_pred


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-plots", action="store_true",
                        help="无头环境：不弹出 matplotlib 窗口")
    parser.add_argument("--lr", type=float, default=0.001,
                        help="学习率，默认 0.001（课件建议；调太大会发散）")
    args = parser.parse_args()

    rng = np.random.default_rng(42)
    u = np.linspace(-2, 2, 200).reshape(-1, 1)
    y_true = 0.5 * np.sin(2 * u) + 0.3 * u

    # ---- 线性回归：只能画一条直线（对照） -------------------------
    from sklearn.linear_model import LinearRegression
    lin = LinearRegression().fit(u, y_true)
    y_lin = lin.predict(u)
    mse_lin = mse(y_true, y_lin)

    # ---- 神经网络：1-16-1 手写 BP ---------------------------------
    # 记录每轮损失，便于查看是否一路下降
    net = MLP(n_hidden=16, lr=args.lr)
    losses = []
    epochs = 5000
    for epoch in range(epochs):
        y_pred = net.backward(u, y_true)
        if epoch % 500 == 0:
            losses.append((epoch, mse(y_true, y_pred)))
    y_nn = net.forward(u)
    mse_nn = mse(y_true, y_nn)

    print("=== 神经网络(1-16-1, tanh) vs 线性回归 ====")
    print(f"线性回归 均方误差 = {mse_lin:.4f}")
    print(f"神经网络 均方误差 = {mse_nn:.5f}  （小了 {mse_lin/mse_nn:.0f} 倍）")
    print("\n  训练过程损失（每 500 轮采样）：")
    for ep, l in losses:
        arrow = " ←" if ep == 0 else ""
        print(f"    epoch {ep:>4}: loss={l:.5f}{arrow}")
    print("  损失应一路下降 → 训练有效；若震荡或 nan → 学习率过大。")

    # ---- 故意踩坑提示（不跑） ------------------------------------
    print("\n  ⚠️ 学习率 > ~0.01 容易发散（loss→nan）；本脚本默认 0.001。")
    print("  ⚠️ 改成 ReLU 试试：把 tanh 换成 relu，回传导数相应改 1(正)/0(负)。")

    # ---- 可视化（可选）：拟合对比 + 损失曲线 ----------------------
    if not args.no_plots:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(11, 4.5))
        plt.subplot(1, 2, 1)
        plt.plot(u, y_true, "k-", label="真实曲线")
        plt.plot(u, y_lin, "r--", label=f"线性回归 (MSE={mse_lin:.3f})")
        plt.plot(u, y_nn, "b-", label=f"神经网络 (MSE={mse_nn:.3f})")
        plt.title("非线性拟合对比")
        plt.xlabel("u"); plt.ylabel("y")
        plt.legend(); plt.grid(alpha=0.4)

        plt.subplot(1, 2, 2)
        eps = [e for e, _ in losses]
        lss = [l for _, l in losses]
        plt.plot(eps, lss, "g-")
        plt.title("神经网络损失曲线")
        plt.xlabel("epoch"); plt.ylabel("MSE")
        plt.grid(alpha=0.4)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()