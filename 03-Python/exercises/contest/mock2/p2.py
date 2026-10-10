# P2 —— 题面见同目录 README.md

# TODO:
n=int(input())
grades={}
bestscore=-1
bestname=""
for _ in range(n):
    name,grade=input().split()
    grade=int(grade)
    grades[name]=grades.get(name,grade)
sums=0
for k,v in grades.items():
    sums=sums+v
    if bestscore<v:
        bestscore=v
        bestname=k
print(f"{bestname}")
print(f"{sums/n:.02f}")
