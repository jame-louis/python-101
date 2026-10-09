# P0905 预测结果 + 置信度（综合·输入+提示，严格匹配）
def predict(score):
    pred = "通过" if score >= 60 else "不通过"
    conf = min(score / 100, 0.99) + 0.01     # 简化置信度
    return pred, conf                        # 返回元组

print("请输入成绩：")
s = int(input())
result, confidence = predict(s)              # 一行解包
print(f"预测: {result}, 置信度: {confidence:.2f}")