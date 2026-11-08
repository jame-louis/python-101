"""Fashion MNIST 图像分类课程作业 —— 学生模板。

本文件是一个"填空式"模板（TODO-gap）：函数签名、文档字符串和整体结构已经给出，
你需要补全标记为 ``# TODO`` 的实现，让整个训练 / 评测流程跑通。

完成任务后对照 ``solution/fashion_mnist_solution.py`` 参考答案自查。

运行：
    uv run fashion_mnist.py
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


def setup_zh_font():
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

# Fashion MNIST 的 10 个类别（按类别索引排序）。
FASHION_LABELS = [
    "T恤/上衣", "裤子", "套头衫", "连衣裙", "外套",
    "凉鞋", "衬衫", "运动鞋", "包", "短靴",
]


# --------------------------------------------------------------------------
# 步骤 1：加载数据
# --------------------------------------------------------------------------

def load_dataloaders(batch_size: int, data_root: str = "./data"):
    """构建 FashionMNIST 训练 / 测试 DataLoader。

    要求：
      - 用 ``transforms.Compose`` 组合 ``ToTensor()`` 与 ``Normalize``。
      - 归一化均值 / 标准差使用 FashionMNIST 的标准值：mean=0.2860, std=0.3530。
        （MNIST 用 (0.1307, 0.3081)；FashionMNIST 用 (0.2860, 0.3530)。）
      - ``root=data_root, train=True, download=True`` 得到训练集；
        ``train=False`` 得到测试集。
      - 训练 DataLoader 打乱（shuffle=True），测试 DataLoader 不打乱。
    """
    # TODO 1：定义 transform（Compose + ToTensor + Normalize）

    # TODO 2：用 torchvision.datasets.FashionMNIST 创建 train_dataset / test_dataset

    # TODO 3：用 DataLoader 创建 train_loader / test_loader，batch_size 打乱规则如上
    return train_loader, test_loader


# --------------------------------------------------------------------------
# 步骤 2：可视化样例（已给出，无需修改）
# --------------------------------------------------------------------------

def show_images(images, labels, rows=2, cols=5):
    fig, axes = plt.subplots(rows, cols, figsize=(10, 4 * rows))
    axes = axes.flatten()
    for i in range(min(len(images), rows * cols)):
        axes[i].imshow(images[i].reshape(28, 28), cmap="gray")
        axes[i].set_title(FASHION_LABELS[labels[i]])
        axes[i].axis("off")
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------------
# 步骤 3：定义模型
# --------------------------------------------------------------------------

class SimpleNN(nn.Module):
    """前馈网络：三个全连接层。

    输入：784 维（28×28）向量；输出：10 个类别得分（logits）。
    """

    def __init__(self):
        super().__init__()
        # TODO 4：补齐模型结构
        #   - Flatten() 把 28×28 展平为 784
        #   - Linear(784, 128) -> ReLU -> Linear(128, 64) -> ReLU -> Linear(64, 10)
        # 请为每个层创建属性并赋值，例如  self.fc1 = nn.Linear(...)

    def forward(self, x):
        # TODO 5：实现前向传播，把 x 依次经过各层
        return x


# --------------------------------------------------------------------------
# 步骤 4：训练循环
# --------------------------------------------------------------------------

def train(model, train_loader, num_epochs, device):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

    train_losses = []
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            # TODO 6：一个训练 step，顺序为
            #   1) optimizer.zero_grad()     清空梯度
            #   2) outputs = model(inputs)   前向
            #   3) loss = criterion(outputs, labels)  计算损失
            #   4) loss.backward()           反向传播
            #   5) optimizer.step()          更新参数

            running_loss += loss.item()
            if (i + 1) % 100 == 0:
                avg = running_loss / 100
                print(f"Epoch [{epoch + 1}/{num_epochs}], "
                      f"Step [{i + 1}/{len(train_loader)}], Loss: {avg:.4f}")
                train_losses.append(avg)
                running_loss = 0.0

    print("训练完成!")
    return train_losses


# --------------------------------------------------------------------------
# 步骤 5：评估准确率
# --------------------------------------------------------------------------

def evaluate(model, test_loader, device):
    """在测试集上计算准确率（%），并打印。"""
    # TODO 7：实现评测
    #   提示：model.eval()；用 with torch.no_grad() 包裹；
    #   torch.max(outputs.data, 1) 取每行最大得分对应的类别；
    #   累计 correct / total，accuracy = 100 * correct / total。
    return accuracy


# --------------------------------------------------------------------------
# 步骤 6：保存 / 加载模型
# --------------------------------------------------------------------------

def save_model(model, path: str):
    # TODO 8：把 model.state_dict() 保存到 path
    pass


def load_model(model, path: str):
    # TODO 9：从 path 加载 state_dict 写入 model（提示：torch.load/load_state_dict）
    pass


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fashion MNIST 分类")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--data-root", default="./data")
    parser.add_argument("--save-path", default="checkpoints/fashion_model.pth")
    parser.add_argument("--no-plots", action="store_true", help="跳过弹窗（无显示环境）")
    args = parser.parse_args()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    train_loader, test_loader = load_dataloaders(args.batch_size, args.data_root)

    if not args.no_plots:
        images, labels = next(iter(train_loader))
        show_images(images[:10], labels[:10])

    model = SimpleNN()
    print(model)
    model.to(device)

    train_losses = train(model, train_loader, args.epochs, device)

    evaluate(model, test_loader, device)

    Path(args.save_path).parent.mkdir(exist_ok=True)
    save_model(model, args.save_path)

    loaded = SimpleNN()
    load_model(loaded, args.save_path)
    loaded.to(device).eval()
    print("重新加载后的准确率: %.2f%%" % evaluate(loaded, test_loader, device))


if __name__ == "__main__":
    main()