#!/usr/bin/env python3
"""第13讲 · 无监督学习与 k-means 聚类。

对应课件 lecture13.md 的完整流程：
    造二维分团数据 → KMeans 聚类（标签/中心/惯性）→ 预测新点 →
    4 步手算对照 → 原始中心点影响（k-means++ vs 随机）→ 肘部法则选 K →
    聚类散点图（按簇着色 + 中心点）→ numpy 手写简化 k-means 对比。

用法：
    uv run kmeans_clustering.py            # 默认：完整流程 + 弹出聚类图
    uv run kmeans_clustering.py --no-plots # 无头环境：只打印文字结果
"""
from __future__ import annotations

import argparse

import numpy as np

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

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
# numpy 手写简化 k-means：选中心 → 分配 → 更新 → 迭代
# --------------------------------------------------------------------------
def kmeans_numpy(X: np.ndarray, k: int, n_iter: int = 100,
                 random_state: int | None = 42) -> tuple[np.ndarray, np.ndarray, float]:
    """返回 (labels, centers, inertia)。不依赖 sklearn.kmeans。"""
    rng = np.random.default_rng(random_state)
    # 1. 选初始中心点：随机挑 k 个样本
    centers = X[rng.choice(len(X), k, replace=False)]
    labels = np.zeros(len(X), dtype=int)
    for _ in range(n_iter):
        # 2. 分配：每个点归到最近的中心
        d2 = np.sum((X[:, None, :] - centers[None, :, :]) ** 2, axis=2)
        new_labels = d2.argmin(axis=1)
        # 3. 更新：每簇中心 = 簇内点均值
        new_centers = centers.copy()
        for c in range(k):
            mask = new_labels == c
            if mask.any():
                new_centers[c] = X[mask].mean(axis=0)
        # 4. 迭代终止：中心不再变化
        if np.allclose(new_centers, centers) and np.array_equal(new_labels, labels):
            break
        centers, labels = new_centers, new_labels
    inertia = float(np.sum(np.min(np.sum((X[:, None, :] - centers[None, :, :]) ** 2, axis=2), axis=1)))
    return labels, centers, inertia


def plot_clusters(X, labels, centers, title, no_plots=False):
    """聚类散点图：按簇着色 + 中心点（可选弹窗）。"""
    if no_plots:
        return
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6.4, 5.2))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap="viridis", alpha=0.7)
    plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="x",
                s=200, linewidths=3, label="簇中心")
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.4)
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-plots", action="store_true",
                        help="无头环境：不弹出 matplotlib 窗口")
    args = parser.parse_args()

    # 0. 造数据：故意分成两/三团的二维点 -------------------------
    # 课件手算用 10 个点；这里再用 make_blobs 生成更容易看清聚类过程的数据。
    X, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.2,
                      random_state=42, center_box=(-10, 10))
    # 标准化：让各维度量纲一致（课件的常见错误表里强调过）
    X = StandardScaler().fit_transform(X[:, :2])

    # 1. 最小 k-means：课件代码演示 -------------------------------
    km = KMeans(n_clusters=3, n_init=10, random_state=42)
    km.fit(X)
    print("每个点属于哪个簇 (前10个):", km.labels_[:10])
    print("簇中心点:\n", np.round(km.cluster_centers_, 3))
    print(f"惯性 inertia_: {km.inertia_:.3f}")

    new = np.array([-1.0, 0.5])
    print(f"新点 {new} 属于簇 {km.predict(new[:, np.newaxis].T)[0]}")

    # 2. 四步手算对照：中心点会"漂移"到簇内均值 ---------------
    mini = np.array([[1, 1], [1.5, 2], [2, 1.5], [2.5, 2], [2, 3],
                     [8, 8], [8.5, 8.5], [9, 8], [8.5, 9], [8, 9.5]])
    km2 = KMeans(n_clusters=2, n_init=10, random_state=42).fit(mini)
    print("\n[手算对照] 课件 10 点数据，k=2:")
    print("  簇标签:", km2.labels_)
    print("  中心点（已漂移到簇内均值）:\n", np.round(km2.cluster_centers_, 3))

    # 3. 重点：原始中心点的影响（随机初始 vs k-means++） ------------
    # k-means++ 是 sklearn 默认；随机初始需要显式 init='random'。
    km_pp = KMeans(n_clusters=3, init="k-means++", n_init=1,
                   random_state=42).fit(X)
    km_rand = KMeans(n_clusters=3, init="random", n_init=1,
                     random_state=7).fit(X)
    print("\n[中心点影响]")
    print(f"  k-means++  惯性 = {km_pp.inertia_:8.3f} (更稳、更易收敛到优解)")
    print(f"  随机初始   惯性 = {km_rand.inertia_:8.3f}")
    print("  同一数据两次跑不同 → 多半不是 bug，而是初始中心点随机所致；")
    print("  稳定方法：设 random_state、加大 n_init 或默认 k-means++")

    # 4. 肘部法则选 K --------------------------------------------
    print("\n[肘部法则] K -inertia 曲线（找拐点）")
    Ks = range(1, 8)
    inertias = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_
                for k in Ks]
    for k, v in zip(Ks, inertias):
        print(f"  K={k}  惯性={v:.3f}")
    print("  惯性随 K 增大而减小；由陡变缓的『拐点』处 K 最合理。")

    # 5. 用 numpy 手写简化 k-means 对比 ---------------------------
    labels_hand, centers_hand, inert_hand = kmeans_numpy(X, k=3, random_state=42)
    labels_sk, centers_sk, inert_sk = km.labels_, km.cluster_centers_, km.inertia_
    print("\n[numpy 手写 k-means vs sklearn]")
    print(f"  手写 惯性 = {inert_hand:8.3f}    sklearn 惯性 = {inert_sk:8.3f}")

    # 6. 聚类散点图 -------------------------------------------------
    plot_clusters(X, km.labels_, km.cluster_centers_,
                  "k-means 聚类 (K=3) 按簇着色 + 中心点", no_plots=args.no_plots)


if __name__ == "__main__":
    main()