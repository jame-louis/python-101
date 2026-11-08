"""Reimplementation of the pythonguides.com PyTorch MNIST tutorial.

https://pythonguides.com/pytorch-mnist/

Trains a feed-forward network (SimpleNN) on MNIST, plots the training loss,
evaluates on the test set, visualizes predictions, and demonstrates
save / load. A CNN variant is provided too.

Usage:
    uv run mnist_nn.py --model cnn --epochs 5 --batch-size 64
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


# --------------------------------------------------------------------------
# 1. Dataset loading
# --------------------------------------------------------------------------

def load_dataloaders(batch_size: int, data_root: str = "./data"):
    """Build MNIST train/test loaders, normalized with the tutorial's stats."""
    transform = transforms.Compose([
        transforms.ToTensor(),                    # images -> tensors
        transforms.Normalize((0.1307,), (0.3081,)),  # MNIST mean/std
    ])

    train_dataset = torchvision.datasets.MNIST(
        root=data_root, train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.MNIST(
        root=data_root, train=False, download=True, transform=transform
    )

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


# --------------------------------------------------------------------------
# 3. Sample-image visualization
# --------------------------------------------------------------------------

def show_images(images, labels, rows=2, cols=5):
    fig, axes = plt.subplots(rows, cols, figsize=(10, 4 * rows))
    axes = axes.flatten()
    for i in range(len(images)):
        axes[i].imshow(images[i].reshape(28, 28), cmap="gray")
        axes[i].set_title(f"Label: {labels[i]}")
        axes[i].axis("off")
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------------
# 4. Model architectures
# --------------------------------------------------------------------------

class SimpleNN(nn.Module):
    """Feed-forward network with three fully connected layers."""

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
    """Convolutional variant — typically more accurate on images."""

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
# 5. Training loop
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

    print("Training finished!")
    return train_losses


# --------------------------------------------------------------------------
# 6. Loss plot
# --------------------------------------------------------------------------

def plot_loss(train_losses, save_path=None):
    plt.figure(figsize=(10, 5))
    plt.plot(train_losses)
    plt.title("Training Loss")
    plt.xlabel("Training Steps (x100)")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.tight_layout()
    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(exist_ok=True)
        plt.savefig(save_path)
        print(f"Loss plot saved to {save_path}")
    plt.show()


# --------------------------------------------------------------------------
# 7. Evaluation
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
    print(f"Accuracy on the test set: {accuracy:.2f}%")
    return accuracy


# --------------------------------------------------------------------------
# 8. Prediction visualization
# --------------------------------------------------------------------------

def show_predictions(images, labels, preds, rows=2, cols=5):
    fig, axes = plt.subplots(rows, cols, figsize=(10, 4 * rows))
    axes = axes.flatten()
    for i in range(min(len(images), rows * cols)):
        axes[i].imshow(images[i].cpu().reshape(28, 28), cmap="gray")
        color = "green" if preds[i] == labels[i] else "red"
        axes[i].set_title(f"Pred: {preds[i]}, True: {labels[i]}", color=color)
        axes[i].axis("off")
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Reimplement the pythonguides.com PyTorch MNIST tutorial.")
    parser.add_argument("--model", choices=["nn", "cnn"], default="nn",
                        help="network to train: feed-forward (nn) or CNN")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--data-root", default="./data")
    parser.add_argument("--save-path", default="checkpoints/mnist_model.pth")
    parser.add_argument("--plot-loss", default="outputs/training_loss.png")
    parser.add_argument("--no-plots", action="store_true",
                        help="skip matplotlib windows (CI / headless)")
    args = parser.parse_args()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_loader, test_loader = load_dataloaders(args.batch_size, args.data_root)

    # Optional grid preview of a batch
    if not args.no_plots:
        images, labels = next(iter(train_loader))
        show_images(images[:10], labels[:10])

    # Build model
    if args.model == "cnn":
        model = CNN()
    else:
        model = SimpleNN()
    print(model)
    model.to(device)

    # Train + plot loss
    train_losses = train(model, train_loader, args.epochs, device)
    if not args.no_plots:
        plot_loss(train_losses, save_path=args.plot_loss)

    # Evaluate
    evaluate(model, test_loader, device)

    # Predictions preview
    if not args.no_plots:
        images, labels = next(iter(test_loader))
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, preds = torch.max(outputs, 1)
        show_predictions(images[:10], labels[:10], preds[:10])

    # Save + reload as a sanity check
    Path(args.save_path).parent.mkdir(exist_ok=True)
    torch.save(model.state_dict(), args.save_path)
    print(f"Model saved to {args.save_path}")

    loaded_model = SimpleNN() if args.model == "nn" else CNN()
    loaded_model.load_state_dict(torch.load(args.save_path, weights_only=True))
    loaded_model.to(device).eval()
    print(f"Model loaded back from {args.save_path}")
    print(f"Reloaded accuracy: {evaluate(loaded_model, test_loader, device):.2f}%")


if __name__ == "__main__":
    main()