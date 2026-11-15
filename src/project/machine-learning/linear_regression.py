#!/usr/bin/env python3
"""第14讲 · 机器学习入门 —— 线性回归。

对应课件 lecture14.md 的完整流程：
    准备 面积-价格 数据 → LinearRegression 拟合（读系数/截距）→
    预测新样本并核对手写公式 ŷ=k·x+b → 散点+拟合线可视化 → 进阶：温度-能耗 → 挑战：离群点/多特征。

用法：
    uv run linear_regression.py            # 默认：完整流程 + 弹出拟合线图
    uv run linear_regression.py --no-plots # 无头环境：只打印文字结果
"""
from __future__ import annotations

import argparse

import numpy as np

from plots import setup_zh_font

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

setup_zh_font()


def manual_predict(model: LinearRegression, x: float) -> float:
    """用手写公式 ŷ = b + k·x 核对 model.predict。"""
    return float(model.intercept_ + model.coef_[0] * x)


def plot_fit(x, y, model, title, xlabel, ylabel, no_plots=False):
    """散点 + 拟合直线（可选弹窗）。"""
    if no_plots:
        return
    import matplotlib.pyplot as plt
    xs = np.linspace(x.min() - 5, x.max() + 5, 100)
    ys = model.intercept_ + model.coef_[0] * xs
    plt.figure(figsize=(6.4, 4.8))
    plt.scatter(x, y, color="blue", label="原始数据")
    plt.plot(xs, ys, color="red", label="拟合直线 y=kx+b")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.4)
    plt.show()


def run_housing(no_plots: bool) -> None:
    """课件主体演示：面积-价格。"""
    area = np.array([50, 70, 80, 100, 120, 130, 150]).reshape(-1, 1)
    price = np.array([45, 62, 70, 88, 105, 112, 130])

    model = LinearRegression()
    model.fit(area, price)                       # 内部自动做最小二乘求最优 k、b

    print("=== 面积-价格 线性回归 ===")
    print(f"斜率 k (coef_) = {model.coef_[0]:.4f}")
    print(f"截距 b (intercept_) = {model.intercept_:.4f}")

    # 预测新样本 + 与手写公式核对
    new_area = np.array([[95]])
    pred = model.predict(new_area)
    print(f"95㎡ 预测价格 = {pred[0]:.2f} 万元")
    manual = manual_predict(model, 95)
    print(f"手写公式 ŷ=k·x+b = {manual:.2f} 万元  （与 predict 一致 ✓）")

    # 进阶：温度-能耗
    temp = np.array([5, 10, 15, 20, 25, 30, 35]).reshape(-1, 1)
    energy = np.array([9, 7, 5.8, 5, 5.5, 7.2, 10])
    m2 = LinearRegression().fit(temp, energy)
    print("\n=== 进阶：温度-能耗 ===")
    print(f"斜率 k = {m2.coef_[0]:.4f}, 截距 b = {m2.intercept_:.4f}")
    t_new = np.array([[18]])
    print(f"18℃ 预测能耗 = {m2.predict(t_new)[0]:.2f} （手写核对 = "
          f"{manual_predict(m2, 18):.2f}）")

    # 挑战：加入离群点，看系数变化
    area_out = np.array([50, 70, 80, 100, 120, 130, 150, 155]).reshape(-1, 1)
    price_out = np.array([45, 62, 70, 88, 105, 112, 130, 300])  # 离群点 300
    m3 = LinearRegression().fit(area_out, price_out)
    print("\n=== 挑战：加入离群点(155㎡,300万) ===")
    print(f"斜率由 {model.coef_[0]:.3f} → {m3.coef_[0]:.3f}")
    print("  离群点把拟合线往上拽，说明最小二乘对离群点敏感。")

    # 可视化
    plot_fit(area, price, model, "房屋面积-价格 线性回归",
             "面积 (㎡)", "价格 (万元)", no_plots=no_plots)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-plots", action="store_true",
                        help="无头环境：不弹出 matplotlib 窗口")
    args = parser.parse_args()
    run_housing(no_plots=args.no_plots)


if __name__ == "__main__":
    main()