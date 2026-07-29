class Student:
    def __init__(self,name,score):
        self.name = name
        self.score =  score

    def to_dict(self):
        return {"name":self.name,"score":self.score}

    @staticmethod
    def from_dict(data):
        return Student(data["name"],data["score"])
