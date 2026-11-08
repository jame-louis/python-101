"""Fashion MNIST 作业自动判分脚本。

它会作为模块加载学生提交的 ``fashion_mnist.py``，然后逐一驱动其中的函数
（数据加载 → 模型 → 训练 → 评测 → 保存/加载），按评分表打分，总分 100。

原则上不需要管学生代码里是怎么写的，只要函数行为正确就能拿分；
未完成（TODO 残留 / 函数返回错误类型 / 训练不收敛）会被自动扣分。

运行（在含 pyproject.toml 的目录，用同一套 venv）：
    uv run grader.py                     # 判学生模板（当前目录 fashion_mnist.py）
    uv run grader.py --module solution/fashion_mnist_solution.py   # 对答案自测
常用参数：
    --epochs 5       训练轮数（判分用，默认 3；轮数越多越接近真实准确率）
    --threshold 85   准确率达标线（默认 85）
    随机种子固定为 42，同一提交每次判分结果一致。
    --batch-size 64
    --data-root ./data
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import tempfile
from pathlib import Path

# 先强制无头后端，避免判分时弹出 matplotlib 窗口。
os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib

matplotlib.use("Agg")

import torch


# --------------------------------------------------------------------------
# 工具
# --------------------------------------------------------------------------

def load_module(path: str, name: str = "submission"):
    """按文件路径加载一个 .py 模块（不打包成包，便于判分任意提交）。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载模块: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def device_auto() -> torch.device:
    return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def has_count(attrs: dict[str, object]) -> int:
    """统计模型中需学习的参数量。"""
    return sum(p.numel() for mod in attrs.values() for p in mod.parameters())


# --------------------------------------------------------------------------
# 判分器
# --------------------------------------------------------------------------

class Grader:
    def __init__(self, module, batch_size, epochs, threshold):
        self.mod = module
        self.batch_size = batch_size
        self.epochs = epochs
        self.threshold = threshold
        self.device = device_auto()
        self.report: list[tuple[str, int, int, str]] = []  # (板块, 得分, 满分, 说明)

    def add(self, section: str, score: int, total: int, note: str):
        self.report.append((section, score, total, note))

    # -- 0. 完成度：源码不应残留 TODO 占位 ----------
    def check_todo(self, path: str):
        total = 10
        text = Path(path).read_text(encoding="utf-8")
        n_todo = text.count("# TODO") + text.count("NotImplementedError")
        if n_todo == 0:
            self.add("完成度（无 TODO 残留）", total, total, "通过")
        else:
            self.add("完成度（无 TODO 残留）", 0, total,
                     f"仍有 {n_todo} 处 TODO/NotImplementedError 未实现")

    # -- 1. 数据加载（TODO 1-3） ----------
    def check_data(self):
        total = 15
        try:
            train_loader, test_loader = self.mod.load_dataloaders(
                self.batch_size, data_root="./data")
        except Exception as e:
            self.add("数据加载 load_dataloaders", 0, total, f"报错: {type(e).__name__}: {e}")
            return None, None

        try:
            xs, ys = next(iter(train_loader))
            if xs.dim() != 4 or tuple(xs.shape[-3:]) != (1, 28, 28):
                raise ValueError(f"输入张量形状异常: {tuple(xs.shape)}，应为 [B,1,28,28]")
            if tuple(ys.shape) != (xs.shape[0],):
                raise ValueError(f"标签形状异常: {tuple(ys.shape)}，应为 [{xs.shape[0]}]")
            self.add("数据加载 load_dataloaders", total, total,
                     f"train={len(train_loader.dataset) if hasattr(train_loader,'dataset') else '?'}, "
                     f"batch 形状 {tuple(xs.shape)} 正确")
        except Exception as e:
            self.add("数据加载 load_dataloaders", 0, total, f"校验失败: {type(e).__name__}: {e}")
            return None, None
        return train_loader, test_loader

    # -- 2. 模型结构（TODO 4-5） ----------
    def check_model(self, train_loader):
        total = 15
        cls = getattr(self.mod, "SimpleNN", None)
        if cls is None:
            self.add("模型 SimpleNN", 0, total, "未定义 SimpleNN 类")
            return None, False

        try:
            model = cls().to(self.device)
            needed = ["flatten", "fc1", "relu", "fc2", "fc3"]
            missing = [a for a in needed if not hasattr(model, a)]
            n_params = has_count({k: getattr(model, k) for k in ["fc1", "fc2", "fc3"]
                                  if hasattr(model, k)})
            xs, _ = next(iter(train_loader))
            out = model(xs.to(self.device))
            shape_ok = tuple(out.shape) == (self.batch_size, 10)
        except Exception as e:
            self.add("模型 SimpleNN", 0, total, f"报错: {type(e).__name__}: {e}")
            return None, False

        msg_bits = []
        if missing:
            self.add("模型 SimpleNN", 0, total, f"缺少结构层 {missing}")
            return None, False
        if not shape_ok:
            self.add("模型 SimpleNN", 0, total,
                     f"forward 输出形状 {tuple(out.shape)}，应为 [{self.batch_size}, 10]")
            return None, False
        if n_params <= 0:
            self.add("模型 SimpleNN", 0, total, "没有可训练参数")
            return None, False
        self.add("模型 SimpleNN", total, total,
                 f"结构完整，forward 输出 [B,10]，参数量 {n_params}")
        return model, True

    # -- 3. 训练循环（TODO 6） ----------
    def check_train(self, model, train_loader):
        total = 25
        try:
            losses = self.mod.train(model, train_loader, self.epochs, self.device)
        except Exception as e:
            self.add("训练 train", 0, total, f"报错: {type(e).__name__}: {e}")
            return False
        if not isinstance(losses, list) or not losses:
            self.add("训练 train", 0, total, "train 未返回非空的损失序列")
            return False
        decreased = losses[-1] < losses[0]
        self.add("训练 train", total if decreased else 8, total,
                 f"损失 {losses[0]:.4f} -> {losses[-1]:.4f}"
                 f"{'（下降，收敛正常）' if decreased else '（未下降，可能缺训练步骤）'}")
        return True

    # -- 4. 评测（TODO 7） ----------
    def check_eval(self, model, test_loader):
        total = 15
        try:
            acc = self.mod.evaluate(model, test_loader, self.device)
        except Exception as e:
            self.add("评测 evaluate", 0, total, f"报错: {type(e).__name__}: {e}")
            return None
        if not isinstance(acc, (int, float)) or not (0 <= acc <= 100):
            self.add("评测 evaluate", 0, total, f"返回值异常: {acc!r}，应为 0-100 的准确率")
            return None
        self.add("评测 evaluate", total, total, f"返回准确率 {acc:.2f}%")
        return float(acc)

    # -- 5. 保存 / 加载（TODO 8-9） ----------
    def check_persistence(self, model, test_loader):
        total = 10
        tmp = tempfile.mktemp(suffix=".pth")
        try:
            self.mod.save_model(model, tmp)
            loaded = self.mod.SimpleNN().to(self.device)
            self.mod.load_model(loaded, tmp)
            model.eval()
            loaded.eval()
            with torch.no_grad():
                ref_x, _ = next(iter(test_loader))
                same = torch.allclose(model(ref_x.to(self.device)),
                                      loaded(ref_x.to(self.device)), atol=1e-5)
        except Exception as e:
            self.add("保存/加载 save+load", 0, total, f"报错: {type(e).__name__}: {e}")
            return False
        finally:
            try:
                os.remove(tmp)
            except OSError:
                pass
        if same:
            self.add("保存/加载 save+load", total, total, "保存→加载后输出一致")
        else:
            self.add("保存/加载 save+load", 0, total, "加载后输出与原模型不一致（可能未 load_state_dict）")
        return same

    # -- 6. 准确率达标 ----------
    def check_accuracy(self, acc):
        total = 10
        if acc is None:
            self.add("准确率达标", 0, total, "无法获取准确率")
        elif acc >= self.threshold:
            self.add("准确率达标", total, total, f"{acc:.2f}% ≥ {self.threshold}%")
        else:
            self.add("准确率达标", 0, total, f"{acc:.2f}% < {self.threshold}%")

    # -- 汇总 ----------
    def run(self, module_path: str) -> int:
        self.check_todo(module_path)

        train_loader, test_loader = self.check_data()
        if train_loader is None or test_loader is None:
            # 数据加载失败，后续依赖数据，直接汇总
            total = sum(t for _, _, t, _ in self.report)
            return self.finish(total)

        model, model_ok = self.check_model(train_loader)
        if not model_ok:
            total = sum(t for _, _, t, _ in self.report)
            return self.finish(total)

        trained = self.check_train(model, train_loader)
        acc = self.check_eval(model, test_loader) if trained else None
        if model_ok and trained:
            self.check_persistence(model, test_loader)
        self.check_accuracy(acc)

        total = sum(t for _, _, t, _ in self.report)
        return self.finish(total)

    def finish(self, total: int) -> int:
        earned = sum(score for _, score, _, _ in self.report)
        print("\n" + "=" * 64)
        print(f"{'板块':<42}{'得分':>8}")
        print("-" * 64)
        for section, score, _, note in self.report:
            print(f"{section:<40}{score:>6} / {note}")
        print("-" * 64)
        print(f"\n总分: {earned} / {total}")
        self.total = earned
        return earned


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fashion MNIST 作业自动判分")
    parser.add_argument("--module", default="fashion_mnist.py",
                        help="要判分的学生文件（默认当前目录 fashion_mnist.py）")
    parser.add_argument("--epochs", type=int, default=3,
                        help="训练轮数（判分用，默认 3；轮数越多越接近真实准确率）")
    parser.add_argument("--threshold", type=float, default=85.0,
                        help="准确率达标线（默认 85）")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--data-root", default="./data")
    args = parser.parse_args()

    # 固定随机种子，保证同一份提交每次判分结果一致（准确率不抖动）。
    torch.manual_seed(42)

    print(f"使用设备: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    print(f"判分文件: {args.module}  ({args.epochs} epoch, batch {args.batch_size})")

    module = load_module(args.module)
    grader = Grader(module, args.batch_size, args.epochs, args.threshold)
    score = grader.run(args.module)

    print(f"\n结果: {'PASS ✅' if score >= 60 else 'FAIL ❌'}  ({score} 分)")
    return 0


if __name__ == "__main__":
    main()