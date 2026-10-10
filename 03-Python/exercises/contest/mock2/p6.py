# P6 —— 题面见同目录 README.md

# TODO:
n, S = map(int, input().split())
a = list(map(int, input().split()))

left = 0
window_sum = 0
ans = n + 1                       # "还没找到"的标记：比任何合法长度都大
for right in range(n):
    window_sum += a[right]
    while window_sum >= S:              # 填空①：什么时候可以试着缩窗口？
        ans = min(ans, right-left+1)      # 填空②：现在这个窗口有多长？
        window_sum -= a[left]     # 填空③：缩窗口 = 把左边那个数移出去，移的是谁？
        left += 1                 # 填空④
print(ans if ans <= n else -1)
