my_info = {
    "name": "张镕峰",
    "school": "CAUC",
    "grade": "大二"
}
print(my_info["name"])
print(my_info["school"])
print(my_info["grade"])

student = {"name": "张三", "score": 85}
print(student["name"])
student["score"] = 90
student["grade"] = "大二"
del student["name"]
for key, value in student.items():
    print(key, value)

fruits = {"苹果", "香蕉", "橘子"}
fruits.add("西瓜")
fruits.remove("香蕉")
print(fruits)
if "苹果" in fruits:
    print("在")
else:
    print("不在")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)