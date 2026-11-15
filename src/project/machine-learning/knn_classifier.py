#!/usr/bin/env python3
"""第12讲 · 机器学习与 KNN（含决策树）—— 鸢尾花分类。

对应课件 lecture12.md 的完整流程：
    加载数据 → 划分训练/测试 → 训练决策树与 KNN → 评估 → K 值实验 → 维度转换对比
并附一个「用 NumPy 手写最小 KNN」（不调库，体现 K 值 + 距离 + 多数表决三要素）。

用法：
    uv run knn_classifier.py            # 默认：完整流程 + 弹出 2D 决策边界图
    uv run knn_classifier.py --no-plots # 无头环境：只打印文字结果，不弹窗
"""
from __future__ import annotations

import argparse

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def setup_zh_font():
    import matplotlib.font_manager as fm
    import matplotlib.pyplot as plt
    """把可用的中文字体设为 matplotlib 默认字体，避免中文标签显示为方框/告警。"""
    candidates = [
        "PingFang SC", "Heiti SC", "Arial Unicode MS", "Songti SC",
        "Hiragino Sans GB", "WenQuanYi Zen Hei", "Noto Sans CJK SC",
        "Microsoft YaHei", "SimHei",
    ]
    installed = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            plt.rcParams["font.family"] = name
            plt.rcParams["axes.unicode_minus"] = False
            return name
    return None


setup_zh_font()


# --------------------------------------------------------------------------
# 手写最小 KNN：算距离 → 找 K 邻居 → 多数表决
# --------------------------------------------------------------------------
def knn_predict(X_train: np.ndarray, y_train: np.ndarray,
                X_test: np.ndarray, k: int = 5) -> np.ndarray:
    """对 X_test 每个样本，用欧氏距离找最近的 k 个训练样本，多数表决定类别。"""
    preds = []
    for x in X_test:
        # 欧氏距离平方：(训练样本 - 新样本) ** 2 沿特征轴求和
        d2 = np.sum((X_train - x) ** 2, axis=1)
        idx = np.argsort(d2)[:k]              # 距离最小的 k 个邻居的索引
        # 多数表决：取 k 个邻居标签中出现次数最多的
        labels, counts = np.unique(y_train[idx], return_counts=True)
        preds.append(labels[np.argmax(counts)])
    return np.asarray(preds)


# 2D 决策边界可视化（课件「降维便于画散点图」的兑现）
def plot_knn_boundary(X2, y, k=5, no_plots=False):
    """在 2D 特征空间画 KNN 决策边界 + 样本点。返回相关结果供打印，边界图可选。"""
    if not no_plots:
        setup_zh_font()
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        cmap_light = ListedColormap(["#ffd6cf", "#cfeaff", "#e2f6d5"])
        cmap_bold = ListedColormap(["#d95763", "#3a7ca5", "#4a8f54"])

        knn = KNeighborsClassifier(n_neighbors=k).fit(X2, y)
        x_min, x_max = X2[:, 0].min() - 0.5, X2[:, 0].max() + 0.5
        y_min, y_max = X2[:, 1].min() - 0.5, X2[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                             np.linspace(y_min, y_max, 300))
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

        plt.figure(figsize=(6.4, 5.2))
        plt.contourf(xx, yy, Z, cmap=cmap_light, alpha=0.8)
        plt.scatter(X2[:, 0], X2[:, 1], c=y, cmap=cmap_bold,
                    edgecolor="k", s=40)
        plt.xlabel("花瓣长度 (Petal length)")
        plt.ylabel("花瓣宽度 (Petal width)")
        plt.title(f"KNN(k={k}) 在 2 维花瓣特征上的决策边界")
        plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-plots", action="store_true",
                        help="无头环境：不弹出 matplotlib 窗口")
    args = parser.parse_args()

    # 1. 加载数据 + 训练/测试划分 --------------------------------
    iris = load_iris()
    X, y = iris.data, iris.target          # 150 样本 × 4 特征，3 类
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
    print(f"训练集形状: {X_train.shape}   测试集形状: {X_test.shape}")

    # 2. 训练决策树 与 KNN ---------------------------------------
    dt = DecisionTreeClassifier(max_depth=3, random_state=42)
    dt.fit(X_train, y_train)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    y_pred_dt = dt.predict(X_test)
    y_pred_knn = knn.predict(X_test)
    print(f"决策树准确率: {accuracy_score(y_test, y_pred_dt):.3f}")
    print(f"KNN(k=5) 准确率: {accuracy_score(y_test, y_pred_knn):.3f}")

    # 3. K 值的影响（重点实验）------------------------------------
    print("\n[k 值实验] 训练集上不同 K 的准确率（Iris 本身不难，差异主要体现在噪声数据）")
    for k in [1, 3, 5, 10, 20]:
        m = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
        print(f"  k={k:<3} 准确率={accuracy_score(y_test, m.predict(X_test)):.3f}")

    # 4. 难点：数据维度转换（4 维 vs 2 维）------------------------
    # 4 维原始特征无法直接画图；降到 2 维（花瓣长、宽）便于可视化。
    X2 = X[:, 2:]
    print(f"\n[维度转换] 4 维全特征 shape={X.shape} → 2 维花瓣特征 shape={X2.shape}")
    print("  4 维信息更多、精度通常更高；2 维好画散点图、好解释（见下图）")
    plot_knn_boundary(X2, y, k=5, no_plots=args.no_plots)

    # 5. 用 NumPy 手写最小 KNN（不调库）----------------------------
    X_tr2, X_te2, y_tr2, y_te2 = train_test_split(
        X2, y, test_size=0.3, random_state=42, stratify=y)
    hand_pred = knn_predict(X_tr2, y_tr2, X_te2, k=5)
    sk_pred = KNeighborsClassifier(n_neighbors=5).fit(X_tr2, y_tr2).predict(X_te2)
    print(f"\n[手写 KNN vs sklearn] 手写准确率={accuracy_score(y_te2, hand_pred):.3f}"
          f"   sklearn准确率={accuracy_score(y_te2, sk_pred):.3f}")


if __name__ == "__main__":
    main()