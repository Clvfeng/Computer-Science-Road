# Python 高频工具表（考前一页纸）

> 用途：比赛 / 考试 **不能翻资料**，这张表是拿来**背**的。
> 只练两件事：**怎么写** + **返回什么**。
> 原理和推导看 `Python-工具箱.md`，这里只放"想不起来就完了"的东西。

---

## 0. 先背这十条（今天之内要能默写）

```python
s[::-1]                            # 字符串倒序
ch.isupper()                       # 逐字符判断大写（不是 s.isupper()！）
cnt[k] = cnt.get(k, 0) + 1         # 字典计数
a.sort()                           # 没有返回值！不能 b = a.sort()
b = sorted(a)                      # 要副本用这个
a = list(map(int, input().split()))# 读一行整数
for i, x in enumerate(a):          # 边遍历边拿下标
print(f"{x:.2f}")                  # 保留几位小数
" ".join(a)                        # 列表粘成一行字符串
x in s / x in a / k in d           # 判断"在不在"
```

---

## 1. 字符串 str（重点）

### 取单个字符 / 切片

| 写法 | 作用 | 返回什么 |
|:---|:---|:---|
| `s[0]` `s[2]` | 第 0 / 第 2 个字符 | str（一个字符） |
| `s[-1]` | 最后一个 | str |
| `s[1:4]` | 下标 1 到 **3**（**含头不含尾**） | 新 str |
| `s[:3]` | 前 3 个 | 新 str |
| `s[3:]` | 从下标 3 到最后 | 新 str |
| `s[-2:]` | 最后 2 个 | 新 str |
| `s[::-1]` | **倒序** ★★ | 新 str |
| `len(s)` | 长度 | int |

★★ **含头不含尾**：结束位置那个字符**不拿**。这是最容易错的一条。

### 方法表（`s.xxx()` 全都**不改** s，返回新东西）

| 写法 | 作用 | 返回什么 |
|:---|:---|:---|
| `s.upper()` / `s.lower()` | 全变大写 / 小写 | 新 str |
| `s.strip()` | 去掉首尾空白（含换行、空格） | 新 str |
| `s.replace(a, b)` | 把 **a 全部** 换成 b | 新 str |
| `s.split()` | 按空白切开 | **list**（元素都是 str） |
| `s.split(",")` | 按逗号切开 | list |
| `",".join(列表)` | 用逗号把列表粘成串 | str |
| `s.count(x)` | x 出现了几次 | int |
| `s.find(x)` | x 第一次出现的下标；没有 → `-1` | int |
| `s.index(x)` | 同上，但**找不到会报错** | int |
| `x in s` | 有没有 x | bool |
| `s.isdigit()` | 是不是**全是数字字符** | bool |
| `s.isalpha()` | 是不是**全是字母** | bool |
| `s.isupper()` | 是不是**全是**大写字母 | bool |
| `s.islower()` | 是不是**全是**小写字母 | bool |
| `s.startswith(p)` / `s.endswith(p)` | 开头 / 结尾是不是 p | bool |

### ⚠️ 逐字符 vs 整串（2026-10-09 踩）

```python
s = "aBcDe"
s.isupper()          # False  ← 问的是"整串是不是全大写"
for ch in s:
    ch.isupper()     # 逐个字符问，"B""D" 才是 True
```

**想数大写字母个数 → 循环里写 `ch.isupper()`，不是 `s.isupper()`。**

### ⚠️ 字符串改不了（和列表最大的区别）

```python
s[0] = "H"                 # ✗ TypeError
s = s.replace("h", "H")    # ✓ 工具生成一个新串，再用变量接住
```

---

## 2. 「返回什么」的两条总规律（省掉一半错）

| 类型 | 例子 | 返回什么 |
|:---|:---|:---|
| **改自己**（原地修改） | `a.append` `a.insert` `a.remove` `a.sort` `a.reverse` `s.add` | **None**（所以不能 `b = a.sort()`） |
| **生成新的** | `sorted` `s.upper` `s.replace` `s.split` `s[::-1]` | 一个新的对象 |

记忆口诀：**"改自己"的都不给你返回东西。**

---

## 3. 数字与类型转换

| 写法 | 结果 | 返回什么 |
|:---|:---|:---|
| `int("123")` | 123 | int |
| `int("3.5")` | ✗ **报错**（小数要用 float） | — |
| `float("3.5")` | 3.5 | float |
| `str(123)` | "123" | str |
| `int(3.9)` | 3（**直接砍掉小数**，不是四舍五入） | int |
| `abs(-3)` | 3 | 数 |
| `round(3.567, 1)` | 3.6 | 数 |
| `a // b` | 整除 | int |
| `a % b` | 取余 | int |
| `a ** b` | 幂 | 数 |

**输出保留小数位不要用 `round`，用 f-string**（见第 9 节）。

---

## 4. 列表 list

| 写法 | 作用 | 返回什么 | 改自己？ |
|:---|:---|:---|:---:|
| `a[i]` | 取第 i 个 | 元素 | — |
| `a[-1]` | 最后一个 | 元素 | — |
| `a[1:4]` | 切片 | 新 list | 否 |
| `a.append(x)` | 末尾加一个 | `None` | ✓ |
| `a.insert(i, x)` | 插到下标 i | `None` | ✓ |
| `a.remove(x)` | 删掉第一个 x（没有就报错） | `None` | ✓ |
| `a.pop()` | 删掉并**返回**最后一个 | **被删的元素** | ✓ |
| `a.pop(i)` | 删掉并返回第 i 个 | 同上 | ✓ |
| `a.sort()` | 从小到大 | `None` | ✓ |
| `a.sort(reverse=True)` | 从大到小 | `None` | ✓ |
| `sorted(a)` | 排好序的**副本** | 新 list | 否 |
| `a.reverse()` | 倒过来 | `None` | ✓ |
| `a[::-1]` | 倒过来的副本 | 新 list | 否 |
| `a.count(x)` / `a.index(x)` | 出现次数 / 下标 | int | — |
| `x in a` | 在不在 | bool | — |
| `len(a)` `sum(a)` `max(a)` `min(a)` | | int | — |

⚠️ **`max` `min` `sum` `list` `sorted` 不能拿来当变量名**（撞内置 → 后面就崩）。

---

## 5. 字典 dict

| 写法 | 作用 | 返回什么 |
|:---|:---|:---|
| `d[k]` | 取值，键不存在 → **KeyError** | 值 |
| `d.get(k, 默认)` | 取值，键不存在 → 默认值 | 值或默认值 |
| `d.get(k, 0) + 1` | **计数固定写法** | — |
| `d[k] = v` | 改 / 新增 | None |
| `k in d` | 键在不在 | bool |
| `d.items()` | 遍历键值对：`for k, v in d.items()` | 键值对 |
| `d.keys()` / `d.values()` | 只遍历键 / 值 | — |
| `d.pop(k)` | 删掉并返回 | 值 |

遍历顺序 = **插入顺序**（新版本 Python 保证）。

---

## 6. 集合 set

```python
s = set()          # ⚠️ 空集合只能这么写；{} 是空【字典】
s = {1, 2, 3}
s.add(x)           # 加一个，返回 None
if x in s:         # O(1) 飞快；列表是 O(n)
list(set(a))       # 列表去重（顺序会打乱）
```

---

## 7. 内置函数

| 写法 | 作用 | 返回什么 |
|:---|:---|:---|
| `len(x)` | 个数 | int |
| `sum(x)` | 求和 | 数 |
| `max(x)` / `min(x)` | 最大 / 最小 | **元素本身** |
| `sorted(x)` | 排好序的副本 | 新 list |
| `enumerate(a, 1)` | 下标从 1 开始：`for i, x in enumerate(a, 1)` | (下标, 元素) |
| `zip(a, b)` | 同时遍历两个列表 | (a的元素, b的元素) |
| `map(int, ...)` | 批量转换 | **不是列表** |
| `range(n)` | 0 ~ n-1 | **不是列表** |
| `abs(x)` `round(x, n)` | 绝对值 / 四舍五入 | 数 |
| `math.gcd(a, b)` | 最大公因数（先 `import math`） | int |

⚠️ **`map()` `range()` `zip()` `enumerate()` `reversed()` 都不是列表**，要当列表用必须外面套 `list(...)`。

---

## 8. 输入

```python
s = input()                             # str
n = int(input())                        # int
x, y = map(int, input().split())        # 一行两个整数 ★
a = list(map(int, input().split()))     # 一行 N 个整数 ★（map 一定套 list）
row = input().split()                   # list，但元素都是【字符串】
```

⚠️ **`input()` 拿到的一律是字符串**。要比大小、要算数，先转 int：
```python
print("9" > "10")    # True ← 字符串是逐字符比，不是比数值
```

---

## 9. 输出

```python
print(a, b)                  # 空格隔开（print 自动加空格）—— 最省事
print(f"{a} {b}")            # 也行
print(f"{x:.1f}")            # 保留 1 位小数 ★
print(f"{x:.2f}")            # 保留 2 位
print(" ".join(a))           # 列表接成一行
```

---

## 10. 每次写代码前扫一眼这 5 条（都是自己踩过的）

1. **读进来的都是字符串** —— 比大小 / 算数前先 `int()`
2. **样例会过不代表对** —— 再补一条反分支数据跑一遍
3. **8 分钟没思路就跳** —— 死磕的十几分钟最贵
4. **输出在循环里还是外面** —— 判据：数题目要几行输出
5. **候选变量先设 `-1`**，`max/min/sum/list` 不当变量名
---

## 11. 双指针 / 滑动窗口（10/10 新学）

**信号**：「连续」子段 + 全是**正数** + 求**最短/最长**。

```python
left = 0
window_sum = 0
ans = n + 1                 # "还没找到"的标记
for right in range(n):
    window_sum += a[right]
    while window_sum >= S:                 # ★ while，不是 if
        ans = min(ans, right - left + 1)   # 长度含头含尾
        window_sum -= a[left]
        left += 1
print(ans if ans <= n else -1)
```

记三件事：**while 不是 if**、**长度 = right - left + 1**、**ans 先设成 n+1**。