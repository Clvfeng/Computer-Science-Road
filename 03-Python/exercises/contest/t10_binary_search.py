# t10 二分查找 —— 返回元素 k 的起始位置和终止位置
#
# ===== 题目（2025 校赛真题，和你做过的 t06 是同一道）=====
# 给定一个按照升序排列的长度为 n 的整数数组，以及 q 个查询。
# 对于每个查询，返回一个元素 k 的起始位置和终止位置（位置从 0 开始计数）。
# 如果数组中不存在该元素，则返回 -1 -1
#
# ===== 输入格式 =====
# 第一行：n q（数组长度、询问个数）
# 第二行：n 个整数（均在 1 ~ 100000 范围内）
# 接下来 q 行：每行一个整数 k
# 1 <= n, q <= 100000，1 <= k <= 100000
#
# ===== 输出格式 =====
# 共 q 行，每行两个整数：起始位置 终止位置
#
# ===== 样例（自造 —— 原截图的样例部分被截断了）=====
# 输入：
# 6 3
# 1 2 2 2 3 5
# 2
# 4
# 5
# 输出：
# 1 3
# -1 -1
# 5 5
#
# ===== 今天的目标 =====
# 你在 9/25 用「字典预处理」做过这道题（t06），能过。
# 今天要用**二分**再做一遍 —— 二分才是这道题的正解，也是天梯赛高频考点。
#
# 目标 1：先写「二分判断 k 在不在数组里」的最基础版本，跑通
# 目标 2：改成「找第一个等于 k 的位置」和「找最后一个等于 k 的位置」
#
# ===== 提示 =====
# 提示 1：二分骨架 —— 用两个指针 left / right 圈出"还在考虑的区间"。
#         每轮看区间中间那个数：比 k 小 → 去右半边；比 k 大 → 去左半边。
#         什么时候停？区间空了（left > right）就停。
# 提示 2：二分最容易写出死循环。每轮必须保证区间**一定变小**，
#         所以要么 left = mid + 1，要么 right = mid - 1，
#         千万不能写成 left = mid（那样区间可能不变 → 卡死）。
#
# TODO: 目标 1 —— 二分判断 k 在不在

# TODO: 目标 2 —— 找左右边界
n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = []
for _ in range(q):
    queries.append(int(input()))
for k in queries:
    first=-1
    last=-1
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == k:
            first=mid
            right=mid-1
        elif nums[mid] < k:
            left=mid+1
        else:
            right=mid-1
    left = 0
    right = n - 1
    while left <= right:
            mid = (left + right) // 2
            if nums[mid] == k:
                last=mid
                left=mid+1
            elif nums[mid] < k:
                left=mid+1
            else:
                right=mid-1
    print(first,last)
