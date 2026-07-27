# Day5 项目：学生信息管理小程序

# 需求：
# 用列表存储多个学生，每个学生是一个字典
# 实现功能：
#   1. 添加学生（姓名 + 成绩）
#   2. 查询学生（输入姓名查成绩）
#   3. 显示所有学生
#   4. 删除指定学生
#   5. 修改指定学生
#   6. 退出
def add_student(students):
        name = input("输入名字")
        try:
            score=int(input("输入成绩"))
        except:
            print("输入无效，输入成绩必须是数字")
            return
        students.append({"name":name,"score":score})

def show_students(students):
    if not students:
        print("该列表为空")
        return
    for i,s in enumerate(students,1):
        print(f"{i}.{s['name']}:{s['score']}")

def search_student(students):
    name = input("输入姓名")
    if not students:
        print("该列表为空")
        return
    for s in students:
        index = 0
        if s["name"] == name:
            print(f"{s['name']}:{s['score']}")
            index=1
            break
    if index == 0:
        print("NOT FOUND")

def delete_student(students):
    name = input("输入要删除学生的名字")
    if not students:
        print("该列表为空")
        return
    for s in students:
            index = 0
            if s["name"] == name:
                students.remove(s)
                index=1
                break
    if index == 0:
        print("没有找到要删除的学生")

def update_student(students):
    name = input("输入要修改的学生姓名")
    # 遍历查找，找到后让用户输入新成绩，更新 s["score"]
    if not students:
        print("该列表为空")
        return
    index = 0
    for s in students:
        if s["name"] == name:
            index = 1
            try:
                score = int(input("输入成绩"))
                s["score"] = score
            except:
                print("输入无效，输入成绩必须是数字")
                break
    if index == 0:
        print("没有找到要修改的学生")
def main():

    students = []  # 列表，每个元素是一个字典
    while True:
        print("\n===== 学生信息管理系统 =====")
        print("1. 添加学生")
        print("2. 查询学生")
        print("3. 显示所有学生")
        print("4. 删除指定学生")
        print("5. 修改指定学生")
        print("6. 退出")
        choice = input("请选择(1-6): ")

        if choice == "1":
            # 你的代码：输入姓名和成绩，添加到 students 列表
            add_student(students)

        elif choice == "2":
            # 你的代码：输入姓名，在 students 列表中查找并打印
           search_student(students)
        elif choice == "3":
            # 你的代码：遍历打印所有学生
            show_students(students)

        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            update_student(students)
        elif choice == "6":
            print("再见")
            break

        else:
            print("输入无效，请重新选择")
if __name__ == "__main__":
    main()
