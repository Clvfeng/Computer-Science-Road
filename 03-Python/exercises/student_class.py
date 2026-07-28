# Python 面向对象练习：Student 类

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"{self.name}:{self.score}")

    def update_score(self,new_score):
        self.score = new_score
# ========== 练习1：创建对象 ==========
# 创建两个 Student 对象，调用 show() 方法
# 你的代码：
s = Student("张三",90)
s.show()




# ========== 练习2：添加方法 ==========
# 给 Student 类添加一个 update_score(new_score) 方法
# 然后测试：创建学生，改成绩，再打印
# 你的代码：
s1 = Student("王五",89)
s1.update_score(88)
s1.show()



# ========== 练习3：思考题 ==========
# 如果要把 student_manager.py 里的字典学生改成 Student 对象
# 你觉得需要改哪些地方？
# 把你的想法写在注释里
#添加剩下的函数，比如：删除指定学生函数,查询学生函数，当然这些有的是成员函数有的是全局函数；其次要引入数据库，导入json文件
