# P0505 AI 模型配置参数映射表（综合·输入+提示，严格匹配）
# 一整行读入四个配置项，构造字典，按键名读取 + get 安全取值
lr, epochs, opt, dev = input("请输入 学习率 轮数 优化器 设备（空格分隔）：").split()
config = {
    "learning_rate": float(lr),     # 学习率（小数）
    "epochs": int(epochs),          # 训练轮数（整数）
    "optimizer": opt,               # 优化器（字符串）
    "device": dev,                  # 设备（字符串）
}
print()                             # 提示语后换行，输出独立成行

print("学习率：", config["learning_rate"])      # 按键名取值
print("轮数：", config["epochs"])
print("优化器：", config["optimizer"])
print("设备：", config["device"])
print("调度器：", config.get("scheduler", "未配置"))  # 安全取值：缺键返回默认值