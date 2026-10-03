# t09 大数据生成器（测超时用，用完可以删）
#
# 用法（在 contest 目录下）：
#   py t09_bigtest.py
# 会生成两个输入文件：
#   t09_big_2000.txt   → T=1, n=2000   （小，先试这个）
#   t09_big_10000.txt  → T=1, n=10000  （大，会明显卡）
#
# 数据特点：m = 999999999（非常大），a[i] 全是 1
#   → 任何区间的和都不到 m，答案一定是 No
#   → 逼着程序把 n 平方量级的组合全部试完，这就是最坏情况

n_list = [2000, 10000]

for n in n_list:
    m = 999999999
    with open(f"t09_big_{n}.txt", "w") as f:
        f.write("1\n")                      # T = 1
        f.write(f"{n} {m}\n")               # n m
        f.write(" ".join(["1"] * n) + "\n") # n 个 1
    print(f"已生成 t09_big_{n}.txt")