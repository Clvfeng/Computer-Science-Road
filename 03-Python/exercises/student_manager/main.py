from storage import load_data, save_data
from menu import show_menu, add_student, show_students, search_student, delete_student, update_student

def main():
    students = load_data()
    # 在这里写 while True 循环：显示菜单 → 根据选择调用函数 → 退出时保存
    while True:
        show_menu()
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
            save_data(students)
            break

        else:
            print("输入无效，请重新选择:")
if __name__ == "__main__":
    main()
