# machine-learning

覆盖 **第12–15讲** 机器学习入门课件的配套程序。每讲一个独立脚本，全部用 [uv](https://docs.astral.sh/uv/) 管理：

| 讲次 | 内容 | 脚本 |
|---|---|---|
| 第12讲 | 机器学习与 KNN（含决策树）· 鸢尾花分类 | `knn_classifier.py` |
| 第13讲 | 无监督学习与 k-means 聚类 | `kmeans_clustering.py` |
| 第14讲 | 线性回归 `y=kx+b` · 面积-价格 | `linear_regression.py` |
| 第15讲 | 神经网络与 BP · 1-16-1 非线性拟合 | `neural_net.py` |

## 环境准备

```bash
cd machine-learning
uv sync    # 安装 numpy / scikit-learn / matplotlib 到 .venv
```

## 运行

每个脚本默认会弹出 matplotlib 图（决策边界 / 聚类图 / 拟合线 / 拟合对比+损失曲线）。
在**无显示环境（CI / 服务器）**加 `--no-plots` 只打印文字结果。

```bash
uv run knn_classifier.py             # 第12讲 KNN + 决策树
uv run knn_classifier.py --no-plots

uv run kmeans_clustering.py          # 第13讲 k-means 聚类 + 肘部法则
uv run kmeans_clustering.py --no-plots

uv run linear_regression.py          # 第14讲 线性回归
uv run linear_regression.py --no-plots

uv run neural_net.py                 # 第15讲 神经网络 BP 非线性拟合（约几秒）
uv run neural_net.py --no-plots
uv run neural_net.py --lr 0.001      # 调学习率对比（>0.01 容易发散）
```

## 各脚本要点（与课件对应）

### `knn_classifier.py` —— 第12讲
- 加载 Iris → `train_test_split` 划分 → 训练决策树 与 KNN(k=5) → 打印并比较准确率。
- **K 值实验**：`k = 1/3/5/10/20`，直观体会"K 太大过度平均、K 太小噪声敏感"。
- **维度转换难点**：4 维全特征降为 2 维（花瓣长、宽），画 KNN 决策边界散点图。
- 末尾用 **NumPy 手写最小 KNN**（算距离→找 K 邻居→多数表决），与 sklearn 对比。

### `kmeans_clustering.py` —— 第13讲
- 用 `make_blobs` 造二维数据并**标准化**，`KMeans(n_clusters=3)` 聚类，打印标签/中心/惯性，预测新点。
- **四步手算对照**：课件 10 点小数据，看中心点如何"漂移到簇内均值"。
- **原始中心点影响（重点）**：对比 `init="k-means++"`（默认、更稳）与 `init="random"` 的惯性差异。
- **肘部法则选 K**：打印 `K=1..7` 的惯性曲线，找拐点。
- 用 **NumPy 手写简化 k-means** 与 sklearn 对比。

### `linear_regression.py` —— 第14讲
- 面积-价格数据 `LinearRegression` 拟合，读取 `coef_`/`intercept_`。
- 预测 95㎡ 公园，并与手写公式 `ŷ = b + k·x` 核对（两者应一致）。
- **进阶**：温度-能耗数据 + 预测新温度点。**挑战**：加入离群点看系数变化（最小二乘对离群点敏感）。
- 散点 + 拟合直线可视化。

### `neural_net.py` —— 第15讲
- 曲线数据 `y = 0.5·sin(2u) + 0.3u`，**手写 3 层 MLP(1→16→1, tanh)** 训练 5000 轮。
- 实现「前向传播 → 反向传播 → 梯度下降更新」完整循环（`MLP.forward`/`backward`）。
- 对比线性回归（一条直线，MSE≈0.34）与神经网络（能弯曲，MSE≈0.001），打印倍数差异与损失曲线。
- `--lr` 参数可调学习率；把 `tanh` 换 `ReLU` 是上机挑战，回传导数改为 `1/0`。

## 说明
- 脚本彼此独立、共享同一个 `.venv`；`uv sync` 一次即可。
- 固定随机种子（`random_state=42`），每次运行结果可复现。
- 需弹窗时请在本机运行（`plt.show()`）；无人值守用 `--no-plots`。