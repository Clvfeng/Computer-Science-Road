# Day5 练习：字典和集合
# 在这个文件里直接写代码运行

# ========== 练习1：创建字典 ==========
# 创建一个字典 my_info，包含你的姓名、学校、年级
# 然后打印每个字段

# 你的代码写在这里：

my_info = {
    "name":"张镕峰",
    "school":"CAUC",
    "grade":"大二"
}
print(my_info["name"])
print(my_info["school"])
print(my_info["grade"])


# ========== 练习2：字典增删改查 ==========
# 从下面这个字典开始：
student = {"name": "张三", "score": 85}

# 1. 打印 name
# 2. 把 score 改成 90
# 3. 新增一个字段 "grade": "大二"
# 4. 删除 name（用 del）

# 你的代码写在这里：
print(student["name"])
student["score"] = 90
student["grade"] = "大二"
del student["name"]



# ========== 练习3：遍历字典 ==========
# 用 for 循环遍历 student，把 key 和 value 都打印出来
# 提示：使用 .items()

# 你的代码：
for key,value in student.items():
    print(key,value)




# ========== 练习4：集合基础 ==========
# 创建一个集合 fruits = {"苹果", "香蕉", "橘子"}
# 1. 添加 "西瓜"
# 2. 删除 "香蕉"
# 3. 打印集合
# 4. 用 in 判断 "苹果" 是否在集合中

# 你的代码：
fruits={"苹果", "香蕉", "橘子"}
fruits.add("西瓜")
fruits.remove("香蕉")
print(fruits)
if "苹果" in fruits:
    print("在")
else:
    print("不在")


# ========== 练习5：集合运算 ==========
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 用集合运算求出：
# 1. 交集 (a & b)
# 2. 并集 (a | b)
# 3. 差集 (a - b)

# 你的代码：
print(a & b)
print(a | b)
print(a - b)
