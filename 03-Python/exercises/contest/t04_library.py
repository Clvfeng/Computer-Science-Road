# 天梯赛刷题 t04 —— 字典计数 + 格式化输出
# 对应截图：微信图片_20260923104254_100_61.png → ..._104310_102_61.png
#
# 【题目描述】
# 某图书馆需要统计一周内的图书借阅情况，找出最受欢迎的图书类别
# （借阅次数最多的类别），并计算该类别的平均每次借阅时长。
#
# 【已知条件】
# 1. 图书分为 3 类：A（文学类）、B（科技类）、C（教辅类）
# 2. 每次借阅记录包含：图书类别、借阅时长（小时，整数，1 <= 时长 <= 72）
# 3. 若有多个类别借阅次数相同且均为最多，选类别字母最小的那个
#    （如 A 和 B 次数相同，选 A）
# 4. 输入可能缺少某些类别，只统计有借阅记录的类别
#
# 【输入格式】
# 第一行一个整数 N（1 <= N < 100），表示一周内的借阅总次数。
# 接下来 N 行，每行一条记录，格式：类别 时长（空格分隔，类别为 A/B/C）
#
# 【输出格式】
# 两行：
#   第一行：Most popular: X      （X 为类别字母）
#   第二行：Average time: Y      （Y 保留 1 位小数）
# ★ 冒号后面有一个空格，格式必须完全一致
#
# 【样例 1】（输出已由题目提示确认，输入为我据提示重建，请对照你的截图核对）
# 输入：
#   5
#   A 30
#   B 24
#   A 18
#   C 16
#   A 24
# 输出：
#   Most popular: A
#   Average time: 24.0
#   （A 借 3 次，总时长 72，平均 72/3 = 24.0；B、C 各 1 次）
#
# 【样例 2】（同上）
# 输入：
#   4
#   C 16
#   B 24
#   C 12
#   B 8
# 输出：
#   Most popular: B
#   Average time: 16.0
#   （B、C 都借 2 次，B 字母更小所以选 B；B 总时长 32，平均 16.0）
#
# 【提示】
# - 需要两个字典：一个记"每个类别借了几次"，一个记"每个类别的总时长"
#   字典计数你暑假学过
# - 保留 1 位小数要用 f-string 的格式控制，形如 f"{值:.1f}"
# - "次数最多且字母最小"怎么保证？想想按什么顺序去比
#
# TODO:
count={"A":0,"B":0,"C":0}
Time={"A":0,"B":0,"C":0}
n = int(input())
for _ in range(n) :
    name,hour=input().split()
    if name == 'A':
        Time["A"]+=int(hour)
        count["A"]=count.get("A",0)+1
    elif name == 'B':
        Time["B"]+=int(hour)
        count["B"]=count.get("B",0)+1
    elif name == 'C':
        Time["C"]+=int(hour)
        count["C"]=count.get("C",0)+1
mindex = "A"
for k,v in count.items():
    if count[mindex] < count[k]:
        mindex=k
print(f"Most popular: {mindex}")
print(f"Average time: {Time[mindex]/count[mindex]:.1f}")
