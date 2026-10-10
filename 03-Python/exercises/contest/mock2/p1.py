# P1 —— 题面见同目录 README.md

# TODO:
T=int(input())
for _ in range(T):
    s=input()
    count=0
    for i in s:
        if i.isupper():
            count=count+1
    print(s[::-1],count)
