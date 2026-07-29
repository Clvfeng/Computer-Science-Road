import json
from student import Student
def load_data():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Student.from_dict(s) for s in data]
    except:
        return []

def save_data(students):                               # 接收列表
    with open("data.json", "w", encoding="utf-8") as f:
        data = [s.to_dict() for s in students]         # 先转成字典列表
        json.dump(data, f)                             # 再写入文件（不需要 return）
