"""Fashion MNIST 图像分类 —— 参考答案。

与 ``fashion_mnist.py`` 填空题一一对应的完整参考实现，与模板同一目录、共用同一环境。

教师分发给学生时，只需在打包 zip 时**排除**本文件（以及 ``grader.py``）即可；
留在同目录便于对答案与维护。

运行：
    uv run fashion_mnist_solution.py
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

FASHION_LABELS = [
    "T恤/上衣", "裤子", "套头衫", "连衣裙", "外套",
    "凉鞋", "衬衫", "运动鞋", "包", "短靴",
]


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


# --------------------------------------------------------------------------
# 步骤 1：加载数据
# --------------------------------------------------------------------------

def load_dataloaders(batch_size: int, data_root: str = "./data"):
    transform = transforms.Compose([
        transforms.ToTensor(),                          # 28×28 灰度图 -> [1,28,28] 张量 (0,1)
        transforms.Normalize((0.2860,), (0.3530,)),     # FashionMNIST 均值/标准差
    ])

    train_dataset = torchvision.datasets.FashionMNIST(
        root=data_root, train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.FashionMNIST(
        root=data_root, train=False, download=True, transform=transform
    )

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


# --------------------------------------------------------------------------
# 步骤 2：可视化样例
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
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


class CNN(nn.Module):
    """选做：卷积网络，通常准确率更高（可超过 92%）。"""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
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

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

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
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f"测试集准确率: {accuracy:.2f}%")
    return accuracy


# --------------------------------------------------------------------------
# 步骤 6：保存 / 加载
# --------------------------------------------------------------------------

def save_model(model, path: str):
    torch.save(model.state_dict(), path)
    print(f"模型已保存至 {path}")


def load_model(model, path: str):
    model.load_state_dict(torch.load(path, weights_only=True))
    print(f"模型已从 {path} 加载")


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fashion MNIST 分类（参考答案）")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--data-root", default="./data")
    parser.add_argument("--model", choices=["nn", "cnn"], default="nn")
    parser.add_argument("--save-path", default="checkpoints/fashion_model.pth")
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    train_loader, test_loader = load_dataloaders(args.batch_size, args.data_root)

    if not args.no_plots:
        images, labels = next(iter(train_loader))
        show_images(images[:10], labels[:10])

    model = CNN() if args.model == "cnn" else SimpleNN()
    print(model)
    model.to(device)

    train_losses = train(model, train_loader, args.epochs, device)

    evaluate(model, test_loader, device)

    Path(args.save_path).parent.mkdir(exist_ok=True)
    save_model(model, args.save_path)

    loaded = CNN() if args.model == "cnn" else SimpleNN()
    load_model(loaded, args.save_path)
    loaded.to(device).eval()
    print(f"重新加载后的准确率: {evaluate(loaded, test_loader, device):.2f}%")


if __name__ == "__main__":
    main()