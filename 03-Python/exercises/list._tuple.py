# 列表的创建
fruits = ["香蕉", "菠萝", "西瓜"]
print(fruits[0])
print(fruits)

# 列表的修改
tasks = []
tasks.append("写代码")          # 末尾添加
print(tasks)
tasks.append("学Python")        # 末尾添加
print(tasks)
tasks.insert(0, "早起")         # 在下标 0 处插入
print(tasks)
tasks.remove("学Python")        # 删除指定元素
print(tasks)
print(tasks.pop())              # 删除并返回最后一个
print(tasks)

# for 循环遍历
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# 元组的创建和只读特性
weeks = (1, 2, 3, 4, 5, 6, 7)   # 用 "()" 创建，不可修改

# 元组解包
mon, tue, wed, thu, fri, sat, sun = weeks
print(mon, tue, wed, thu, fri, sat, sun)