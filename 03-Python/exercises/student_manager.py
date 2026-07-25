# Day5 项目：学生信息管理小程序

# 需求：
# 用列表存储多个学生，每个学生是一个字典
# 实现功能：
#   1. 添加学生（姓名 + 成绩）
#   2. 查询学生（输入姓名查成绩）
#   3. 显示所有学生
#   4. 退出

students = []  # 列表，每个元素是一个字典

while True:
    print("\n===== 学生信息管理系统 =====")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 显示所有学生")
    print("4. 退出")
    choice = input("请选择(1-4): ")

    if choice == "1":
        # 你的代码：输入姓名和成绩，添加到 students 列表
        name=input("输入姓名")
        score=int(input("输入成绩"))
        students.append({"name":name,"score":score})

    elif choice == "2":
        # 你的代码：输入姓名，在 students 列表中查找并打印
        index=0
        name=input("输入姓名")
        for s in students:
            if s["name"] == name:
                index=index+1
                print(f"{s['name']}:{s['score']}")
        if index == 0:
            print("NOT FOUND")
    elif choice == "3":
        # 你的代码：遍历打印所有学生
        index = 0
        for s in students:
            index=index+1
            print(f"{index}.{s['name']}:{s['score']}")
        if index == 0:
            print("该列表为空")
    elif choice == "4":
        print("再见！")
        break

    else:
        print("输入无效，请重新选择")
