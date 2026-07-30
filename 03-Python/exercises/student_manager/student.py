class Person:
    def __init__(self,name):
        self.name = name



class Student(Person):
    def __init__(self,name,score):
        super().__init__(name)
        self._score =  score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if value < 0 or value >100:
            print("成绩必须在 0-100 之间")
        else:
            self._score = value

    def to_dict(self):
        return {"name":self.name,"score":self.score}

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["score"])
