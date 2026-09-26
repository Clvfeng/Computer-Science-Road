import json


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def to_dict(self):
        return {"name": self.name, "score": self.score}

    @staticmethod
    def from_dict(record):
        return Student(record["name"], record["score"])


def load_data():
    """从文件读取数据"""
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            records = json.load(file)
            return [Student.from_dict(record) for record in records]
    except:
        return []


def save_data(students):
    """保存数据到文件"""
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file)


def add_student(students):
    name = input("输入名字:")
    try:
        score = int(input("输入成绩:"))
    except:
        print("输入无效，输入成绩必须是数字")
        return
    students.append(Student(name, score))


def show_students(students):
    if not students:
        print("该列表为空")
        return
    for order, student in enumerate(students, 1):
        print(f"{order}.{student.name}:{student.score}")


def search_student(students):
    if not students:
        print("该列表为空")
        return
    name = input("输入姓名:")
    found = False
    for student in students:
        if student.name == name:
            print(f"{student.name}:{student.score}")
            found = True
            break
    if not found:
        print("NOT FOUND")


def delete_student(students):
    if not students:
        print("该列表为空")
        return
    name = input("输入要删除学生的名字:")
    found = False
    for student in students:
        if student.name == name:
            students.remove(student)
            found = True
            break
    if not found:
        print("没有找到要删除的学生")


def update_student(students):
    if not students:
        print("该列表为空")
        return
    name = input("输入要修改的学生姓名:")
    found = False
    for student in students:
        if student.name == name:
            found = True
            try:
                score = int(input("输入成绩:"))
                student.score = score
            except:
                print("输入无效，输入成绩必须是数字")
                break
    if not found:
        print("没有找到要修改的学生")


def main():
    students = load_data()
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
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            show_students(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            update_student(students)
        elif choice == "6":
            print("再见")
            save_data(students)
            break
        else:
            print("输入无效，请重新选择:")


if __name__ == "__main__":
    main()