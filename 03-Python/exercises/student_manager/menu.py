from student import Student
def add_student(students):
        name = input("输入名字:")
        try:
            score=int(input("输入成绩:"))
        except:
            print("输入无效，输入成绩必须是数字")
            return
        students.append(Student(name,score))

def show_students(students):
    if not students:
        print("该列表为空")
        return
    for i,s in enumerate(students,1):
        print(f"{i}.{s.name}:{s.score}")

def search_student(students):
    name = input("输入姓名:")
    if not students:
        print("该列表为空")
        return
    for s in students:
        index = 0
        if s.name == name:
            print(f"{s.name}:{s.score}")
            index=1
            break
    if index == 0:
        print("NOT FOUND")

def delete_student(students):
    name = input("输入要删除学生的名字:")
    if not students:
        print("该列表为空")
        return
    for s in students:
            index = 0
            if s.name == name:
                students.remove(s)
                index=1
                break
    if index == 0:
        print("没有找到要删除的学生")

def update_student(students):
    name = input("输入要修改的学生姓名:")
    # 遍历查找，找到后让用户输入新成绩，更新 s["score"]
    if not students:
        print("该列表为空")
        return
    index = 0
    for s in students:
        if s.name == name:
            index = 1
            try:
                score = int(input("输入成绩:"))
                s.score = score
            except:
                print("输入无效，输入成绩必须是数字")
                break
    if index == 0:
        print("没有找到要修改的学生")

def show_menu():
    print("\n===== 学生信息管理系统 =====")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 显示所有学生")
    print("4. 删除指定学生")
    print("5. 修改指定学生")
    print("6. 退出")
