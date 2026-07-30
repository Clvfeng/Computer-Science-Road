# OOP 继承练习
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name}发出声音")

# ========== 练习1：添加子类 ==========
# 写一个 Cat 类，继承 Animal，重写 speak() 方法让猫叫"喵"
# 你的代码：
class Cat(Animal):
    def speak(self):
        print("喵")
cat = Cat("布丁")
cat.speak()


# ========== 练习2：super() ==========
# 子类 __init__ 中调用父类的 __init__
# 比如 Dog 加一个 breed(品种) 属性，调用 super().__init__(name)
# 你的代码：
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name}({self.breed}) 汪汪")
dog = Dog("旺财", "金毛")
dog.speak()
