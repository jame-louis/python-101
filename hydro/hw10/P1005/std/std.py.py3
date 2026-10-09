# P1005 银行账户存取（综合·输入+提示，严格匹配）
class BankAccount:
    def __init__(self, initial):
        self.__balance = initial    # 私有余额

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return "成功"
        return "失败"

    def balance(self):
        return self.__balance

print("请输入初始余额：")
init = int(input())
acc = BankAccount(init)
print("请输入存入金额：")
acc.deposit(int(input()))
print("请输入取出金额：")
w = int(input())

print("取款结果：", acc.withdraw(w))
print("当前余额：", acc.balance())