class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"{self.name}:{self.score}")

    def update_score(self, new_score):
        self.score = new_score


student1 = Student("张三", 90)
student1.show()

student2 = Student("王五", 89)
student2.update_score(88)
student2.show()