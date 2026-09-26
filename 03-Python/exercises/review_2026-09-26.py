# 复习 2026-09-26 —— 三题复习法
#
# 规则：不许翻工具箱、不许查之前的代码。
# 每题两件事：
#   ① 用一句话说出它是干嘛的 —— 直接在聊天里回答我
#   ② 手写一个最小例子并跑通 —— 写在下面，跑完把结果发我


# ---------------------------------------------------------------
# 第 1 题
# ① nums.sort() 和 sorted(nums) 有什么区别？各有什么坑？
# ② 写代码：nums = [3, 1, 2]
#    用两种写法各排一次序，每次把 nums 打印出来，
#    让我看到它们的行为差异（要打印 3 次结果）
#
# 你的代码：

nums = [3, 1, 2]

sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)

nums.sort()
print(nums)

s = "ab"
print(s)
print(s.upper())

values = [5, 3, 5, 7, 3]
first_index = {}
for idx, value in enumerate(values):
    if value not in first_index:
        first_index[value] = idx
print(first_index)
