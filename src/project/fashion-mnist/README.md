# Fashion MNIST 图像分类课程作业

> 在 PyTorch 中完成一个 **时尚服饰图像分类** 任务：用神经网络区分 **10 类**服饰
> （T恤 / 裤子 / 套头衫 / 连衣裙 / 外套 / 凉鞋 / 衬衫 / 运动鞋 / 包 / 短靴）。

本题改编自上一讲的 MNIST 分类教程，把数据集换成 **FashionMNIST**，思路与代码结构几乎一致，
但更贴近真实工业场景（服饰图片比手写数字更难分类）。适合作为逐步练手。

- 数据集官方文档：<https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html>
- 参考题解（别忘了对答案时打开它）：`fashion_mnist_solution.py`

---

## 目录结构与分工

```
fashion-mnist/
├── README.md                     ← 你正在读的这份指南
├── pyproject.toml                ← 本项目的 uv 配置（环境都在同一个 .venv）
├── fashion_mnist.py              ← ★ 你要填写的学生模板（带 TODO 空洞）
├── fashion_mnist_solution.py     ← 教师用参考答案（与模板同目录）
└── grader.py                     ← 自动判分脚本（教师用，评分表见 §5）
```

> **教师分发**：打包给学生的 zip 只需排除三个文件即可——`fashion_mnist_solution.py`、
> `grader.py`，以及仓库里的 `solution/` 历史目录（见 git history）。模板与题解同目录
> 便于维护；学生拿到的包里不含它们。`.venv/`、`data/`、`checkpoints/`、`outputs/`
> 均为运行时生成，无需打包。

---

## 0. 环境准备

本项目用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境，无需单独装 PyTorch。

```bash
# 进入本作业目录（含 pyproject.toml）
cd fashion-mnist
# 安装依赖（torch / torchvision / matplotlib）到 .venv
uv sync
# 运行模板（现在会因 TODO 未填而报错，属正常）
uv run fashion_mnist.py
```

> 模板与参考题解共用同一个 `.venv`，直接 `uv run fashion_mnist_solution.py` 即可跑题解，
> 无需再次 `uv sync`。

---

## 1. 项目背景与任务

### 1.1 数据集：FashionMNIST

- 与经典 MNIST 同为 **28×28 灰度图**，但内容是服饰图片而非手写数字。
- **6 万**训练样本、**1 万**测试样本，共 **10 类**（类别索引 `0–9` 对应 `FASHION_LABELS`）。
- 分类比 MNIST 更难：例如「套头衫」与「衬衫」外观相近，模型需要学到更细的特征。

### 1.2 任务目标

用前馈全连接网络把灰度图正确归类为 10 类之一，目标：**测试集准确率达到 ~88% 以上**
（MNIST 同一结构约 ~97%；FashionMNIST 更高难度，参考值约 88–90%）。

---

## 2. 逐步实现（对照 `fashion_mnist.py` 的 `# TODO`）

整体流程与 MNIST 教程一致：**数据 → 可视化 → 建模型 → 训练 → 评测 → 保存/加载**。

### 步骤 1　加载数据（TODO 1–3）

在 `load_dataloaders(...)` 中：

1. **TODO 1** 定义 `transform`：
   - `transforms.ToTensor()`：把 `PIL` 图变成 `[1, 28, 28]` 的张量，范围 `[0,1]`。
   - `transforms.Normalize((mean,), (std,))` 归一化。
   - ⚠️ **注意**：MNIST 用 `(0.1307, 0.3081)`；本作业要求 **FashionMNIST** 的标准值
     `mean=0.2860, std=0.3530`。差值不大，但能体现"换数据集要同步换统计量"的意识。
2. **TODO 2** 用 `torchvision.datasets.FashionMNIST(root, train=True/False, download=True, transform)` 建训练/测试集。
3. **TODO 3** 用 `DataLoader(dataset, batch_size, shuffle=…)` 建 loader。
   - 训练 loader：`shuffle=True`（打乱，利于收敛）；测试 loader：`shuffle=False`。

### 步骤 2　可视化样例（无需修改）

已给出 `show_images`；会打印 10 张样例图及其类别名，帮你确认数据加载正确。

### 步骤 3　定义模型（TODO 4–5）

`SimpleNN` 为三层全连接前馈网络：

```
输入 784 (28×28)  →  [Linear(784→128)]  →  ReLU  →  [Linear(128→64)]  →  ReLU  →  [Linear(64→10)]
```

- **TODO 4**：在 `__init__` 里把每层建为属性（`self.flatten` / `self.fc1` / `self.relu` …）。
- **TODO 5**：在 `forward` 里把输入依次经过各层并返回 logits（10 维）。

> 为什么不用激活函数输出层？ `nn.CrossEntropyLoss` 已内置 Softmax，直接喂 logits 即可。

### 步骤 4　训练循环（TODO 6）

每个 `step` 五句话、顺序固定（这是 PyTorch 的标准模式，务必记牢）：

```python
optimizer.zero_grad()        # 1. 清空上一次累积的梯度
outputs = model(inputs)      # 2. 前向传播
loss = criterion(outputs, labels)  # 3. 计算损失
loss.backward()              # 4. 反向传播，自动求梯度
optimizer.step()             # 5. 用梯度更新参数
```

- 损失：`nn.CrossEntropyLoss()`；优化器：`optim.SGD(lr=0.01, momentum=0.9)`（已给）。
- 记得把 `inputs, labels` 先 `.to(device)`。

### 步骤 5　评估准确率（TODO 7）

在 `evaluate(...)` 里遍历测试集：

```python
model.eval()                          # 切到评测模式
with torch.no_grad():                 # 关闭梯度计算，省内存且更快
    for images, labels in test_loader:
        ...
        _, predicted = torch.max(outputs.data, 1)  # 每行最大值对应的类别
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
accuracy = 100 * correct / total
```

### 步骤 6　保存 / 加载模型（TODO 8–9）

- `save_model`：`torch.save(model.state_dict(), path)`。
- `load_model`：`model.load_state_dict(torch.load(path))`。
- 只存**参数**（`state_dict`），加载前需先 `SimpleNN()` 建一个空模型再装入。
- `main()` 末尾会"保存 → 重新加载 → 再测一遍准确率"，应得到一致结果。

---

## 3. 提交物与自检清单

尽量做到：

- [ ] `fashion_mnist.py` 的 TODO 1–9 全部填完，脚本能从头跑到尾。
- [ ] 训练损失逐 **epoch** 下降。
- [ ] 测试集准确率 ≥ **85%**（第 5 个 epoch 左右）。
- [ ] 保存的模型重新加载后准确率与训练时一致。
- [ ] （选做/加分）把 `SimpleNN` 换成 `CNN`（见题解），目标 ≥ **92%**：
      `conv(1→32) → ReLU → MaxPool2d → conv(32→64) → ReLU → MaxPool2d → fc(3136→128) → ReLU → fc(128→10)`。
- [ ] 能把数据、模型、训练、评测流程用中文讲清楚。

---

## 4. 常见坑

| 现象 | 原因 / 解法 |
| --- | --- |
| `RuntimeError: Expected input batch_size (...) to match target (...) ` | 训练/评测的 `labels` 没和 `inputs` 一样 `.to(device)`，或 batch 不匹配。 |
| 准确率徘徊在 ~10%（= 乱猜） | 梯度没更新，大概率丢了 `optimizer.zero_grad()` 或 `optimizer.step()`。 |
| 损失不降，反而震荡 | 试试更大的 epoch、减小 `lr`，或换优化器（如 Adam）。 |
| 保存/加载报 `size mismatch` | 加载前用了不同结构的模型，务必先建 `SimpleNN()`。 |
| 忘记 `model.eval()` | 训练后的 Dropout/BatchNorm 行为不同，评测前要切回 eval 模式。 |
| ⚠️ 用了 MNIST 的均值标准差 | 本作业要求 FashionMNIST 的 `(0.2860, 0.3530)`。 |

---

## 5. 自动判分（教师用）

同目录下的 `grader.py` 会加载学生提交的 `fashion_mnist.py`，**驱动其内部函数**逐项验证
（数据 → 模型 → 训练 → 评测 → 保存/加载），按评分表自动打分，总分 **100**。

```bash
uv run grader.py                                    # 判当前目录 fashion_mnist.py
uv run grader.py --module <提交文件路径>              # 判任意提交
uv run grader.py --epochs 5 --threshold 88          # 调高训练轮数 / 达标线
```

评分表：

| 板块 | 分值 | 考察的 TODO |
| --- | --- | --- |
| 完成度（无 TODO 残留） | 10 | 是否填完 1–9 |
| 数据加载 `load_dataloaders` | 15 | 1–3（数据量、`[B,1,28,28]` 形状） |
| 模型 `SimpleNN` 结构与前向 | 15 | 4–5（层齐全、输出 `[B,10]`、有参数） |
| 训练 `train`（损失下降） | 25 | 6（返回损失序列且收敛） |
| 评测 `evaluate` | 15 | 7（返回 0–100 的准确率） |
| 保存 / 加载 | 10 | 8–9（加载后输出一致） |
| 准确率达标（默认 ≥85%） | 10 | — |

- 判分**不跑学生代码的 `main()`**，只调用其中名命名的函数，避免弹窗阻塞。
- 未完成（TODO 残留、函数报错、训练不收敛、准确率不够）会被精确扣分并说明原因。
- 判分时若数据未下载会自动下载到 `./data`。
- 固定随机种子（42），**同一提交每次判分结果一致**，不因运米抖动。
- 教师可在判分命令中调 `--epochs` / `--threshold` 控制耗时与难度。

对答案自测（默认参数下参考答案应拿满分）：

```bash
uv run grader.py --module fashion_mnist_solution.py
```

---

## 6. （选做）思考题

1. 为什么 `CrossEntropyLoss` 不需要手动加一个 Softmax 层？
2. 归一化（Normalize）为什么要用"整个数据集的均值/标准差"，损失的取值和收敛速度有何变化？
3. 为什么 FashionMNIST 比 MNIST 难？对同样结构的网络，期望准确率大约差多少？
4. CNN 相比全连接网络强在哪（感受野 / 共享权重 / 局部性）？