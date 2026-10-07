# P4 —— 题面见同目录 README.md

# TODO:
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    values=list(map(int,input().split()))
    flag=False
    sums=0
    mod=set()
    mod.add(0)
    for l in range(n):
        sums=sums+values[l]
        x=sums%m
        if x in mod:
            flag=True
        elif x not in mod:
            mod.add(x)
    if flag:
        print("Yes")
    else:
        print("No")
