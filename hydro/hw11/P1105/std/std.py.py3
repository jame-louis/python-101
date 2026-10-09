# P1105 多态动物叫（综合·输入+提示，严格匹配）
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} 发出叫声"

class Dog(Animal):
    def speak(self):
        return f"{self.name} 汪汪叫！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫~"

print("请输入狗狗名字：")
dog_nm = input()
print("请输入猫咪名字：")
cat_nm = input()

for a in [Dog(dog_nm), Cat(cat_nm)]:   # 多态：统一调用 speak()
    print(a.speak())