# mnist-pytorch

A reimplementation of the [PyTorch MNIST tutorial](https://pythonguides.com/pytorch-mnist/)
(pythonguides.com), managed with **uv**.

Trains a feed-forward network (`SimpleNN`) — or a CNN variant — on the MNIST
handwritten-digit dataset, plots the training loss, evaluates on the 10k-image
test set, visualizes predictions, and demonstrates model save / load.

## Setup

```bash
uv sync          # install torch, torchvision, matplotlib into .venv
```

## Run

Train the default feed-forward network for 5 epochs:

```bash
uv run mnist_nn.py
```

Train the CNN variant:

```bash
uv run mnist_nn.py --model cnn --epochs 5
```

Headless (`--no-plots`) — useful on CI or servers without a display:

```bash
uv run mnist_nn.py --no-plots
```

### Options

| Flag             | Default                          | Description                              |
|------------------|----------------------------------|------------------------------------------|
| `--model`        | `nn` (`nn`/`cnn`)                | Network architecture                     |
| `--epochs`       | `5`                              | Number of training epochs                |
| `--batch-size`   | `64`                             | Dataloader batch size                    |
| `--data-root`    | `./data`                         | Where MNIST is downloaded                |
| `--save-path`    | `checkpoints/mnist_model.pth`    | Where `state_dict` is saved              |
| `--plot-loss`    | `outputs/training_loss.png`      | Where the loss plot is written           |
| `--no-plots`     | `False`                          | Skip matplotlib windows (headless)       |

The first run downloads MNIST (≈10 MB) into `--data-root`.

## What it does

1. **Loads MNIST** — 60k train / 10k test, normalized with the tutorial's
   mean `(0.1307,)` and std `(0.3081,)`, batched at 64.
2. **Shows a sample grid** of 10 training digits.
3. **Trains** `SimpleNN`: `Flatten → Linear(784→128) → ReLU → Linear(128→64)
   → ReLU → Linear(64→10)` with `CrossEntropyLoss` and
   `SGD(lr=0.01, momentum=0.9)`.
4. **Plots the training loss** curve.
5. **Evaluates** test-set accuracy inside `torch.no_grad()`.
6. **Visualizes predictions** — correct in green, wrong in red.
7. **Saves / reloads** the `state_dict` and re-confirms accuracy.

A `CNN` (`conv1 → ReLU → pool → conv2 → ReLU → pool → fc1 → ReLU → fc2`)
is provided as the tutorial's higher-accuracy variant, often exceeding 99%.

## Layout

- `mnist_nn.py` — the full reimplementation, split into functions.
- `pyproject.toml` — uv project definition with pinned dependencies.

`data/`, `checkpoints/`, and `outputs/` are generated at runtime.