# P5 —— 题面见同目录 README.md

# TODO:
n=int(input())
count={"A":0,"B":0,"C":0}
time={"A":0,"B":0,"C":0}
for _ in range(n):
    k,h=input().split()
    if k == "A":
        count["A"]=count["A"]+1
        time["A"]=time["A"]+int(h)
    elif k == "B":
        count["B"]=count["B"]+1
        time["B"]=time["B"]+int(h)
    elif k == "C":
        count["C"]=count["C"]+1
        time["C"]=time["C"]+int(h)
max_index="A"
for k,v in count.items():
    if v > count[max_index]:
        max_index=k
print(f"Most popular: {max_index}")
print(f"Average time: {time[max_index]/count[max_index]:.1f}")
