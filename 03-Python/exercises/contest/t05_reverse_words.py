# 天梯赛刷题 t05 —— 整句里单词倒序
# 对应截图：微信图片_20260923104319_103_61.png
#
# 【题目描述】
# 给定一个英文句子（单词之间仅用 1 个空格分隔，无开头或结尾空格，
# 单词由大小写英文字母组成），请把句子中每个单词的字符顺序单独反转
# （空格位置保持不变），最后输出反转后的句子。
#
# 例：输入 Hello World    → 输出 olleH dlroW
#     输入 a Bc Defg      → 输出 a cB gfeD
#
# 【输入格式】
# 一行字符串（单词间 1 个空格，无首尾空格，仅含大小写字母和空格）
#
# 【输出格式】
# 一行字符串，每个单词反转后的结果（空格位置与输入一致）
#
# 【样例】
# 输入：Hello World
# 输出：olleH dlroW
#
# 【提示】
# - 先把整句切成一个个单词（用 split()，不填参数就是按空格切）
# - 每个单词的反转你刚在 t03/recover_01 里已经会了
# - 拼回去有两种写法，自己想想：一种是把列表再粘成字符串，
#   另一种是直接 print 的时候把列表"摊开"
#
# TODO:

words = input().split()
reversed_words = []
for w in words:
    rev = w[::-1]
    reversed_words.append(rev)
result = " ".join(reversed_words)
print(result)

# 另一种写法：print(*列表名字)，把列表摊开，中间用空格分隔
