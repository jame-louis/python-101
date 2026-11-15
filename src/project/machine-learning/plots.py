#!/usr/bin/env python3
"""共享绘图工具：matplotlib 中文字体配置。

各脚本凡是要用 matplotlib 显示中文标签（标题/坐标轴/图例）的，都从这里
import，避免每个脚本重复一份字体配置。用法：

    from plots import setup_zh_font
    setup_zh_font()
"""
from __future__ import annotations


def setup_zh_font():
    """把可用的中文字体设为 matplotlib 默认字体，避免中文标签显示为方框/告警。

    返回命中的字体名；若本机一个中文字体都没装则返回 None（matplotlib 会
    退回到默认字体并显示告警，属预期）。
    """
    import matplotlib.font_manager as fm
    import matplotlib.pyplot as plt

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