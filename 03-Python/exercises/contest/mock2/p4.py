# P4 —— 题面见同目录 README.md

# TODO:
n = int(input())
acts = []
for _ in range(n):
    st, et = map(int, input().split())
    acts.append((et,st))     # 填空①：谁放前面，排完序才是"按结束时间排"？

acts.sort()                       # 填空②

count = 0
last_end = -1                     # 上一个选中的活动什么时候结束
for et, st in acts:
    if st >= last_end:          # 填空③
        count += 1
        last_end = et           # 填空④
print(count)
