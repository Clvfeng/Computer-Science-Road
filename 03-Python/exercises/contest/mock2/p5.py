# P5 —— 题面见同目录 README.md

# TODO:
n = int(input())
free_at = 0                # 窗口什么时候空出来（一开始是空的）
for _ in range(n):
    t, w = map(int, input().split())
    start = max(t,free_at)           # 填空：这个人的开始时刻
    print(start)
    free_at = start+w         # 填空
