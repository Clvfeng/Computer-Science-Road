# P3 —— 题面见同目录 README.md

# TODO:
s=input()
count=0
flag=False
for i in s:
    if flag == True:
        if i == "1":
            continue
        elif i == "0":
            flag=False
    elif flag == False:
        if i == "1":
            count=count+1
            flag=True
        else:
            continue
print(count)
