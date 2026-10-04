# Python 工具箱

> **用途**：忘了语法就翻这里。不用从头读，去目录里跳。
>
> **标记含义**：★ = 刷题/天梯赛高频，必须熟练到不用查
>
> **维护规则**：每次学习有新内容，当天必须补进来。查不到的东西 = 工具箱失效。
>
> 最后更新：2026-09-23

---

## 目录

1. [输入输出](#1-输入输出)
2. [字符串 str](#2-字符串-str)
3. [列表 list](#3-列表-list)
4. [元组 tuple](#4-元组-tuple)
5. [字典 dict](#5-字典-dict)
6. [集合 set](#6-集合-set)
7. [控制流 if](#7-控制流-if)
8. [循环 for / while](#8-循环-for--while)
9. [函数 def](#9-函数-def)
10. [类 class](#10-类-class)
11. [文件与 JSON](#11-文件与-json)
12. [异常处理 try](#12-异常处理-try)
13. [常用内置函数速查](#13-常用内置函数速查)
14. [踩过的坑](#14-踩过的坑)
15. [刷题常用套路](#15-刷题常用套路)

---

## 1. 输入输出

### 读一行文字 ★

```python
s = input()
```

★ **重点**：`input()` 拿回来的永远是**字符串**。输入 `35`，你拿到的是 `"35"` 而不是数字。

### 读一个整数 ★

```python
n = int(input())
```

### 读两个整数（一行，空格分隔）★

```python
a, b = map(int, input().split())
```

拆开看这三层：
- `input()` → 拿到整行字符串 `"3 5"`
- `.split()` → 按空格切开，变成列表 `["3", "5"]`
- `map(int, ...)` → 把每个都转成整数
- 最后 `a, b = ` → 把两个值分别装进两个变量

### 读一整行整数，装成列表 ★

```python
nums = list(map(int, input().split()))
```

**为什么这里要套 `list()`，而上面不用？**
- 上面用了 `a, b =`，已经手动把值拆开了，不需要 `list`
- 这里想留一个完整的列表，而 `map` 给的**不是列表**（是个「加工厂」），所以要 `list()` 把它装出来
- 对比：`input().split()` **本身就是列表**，**不用**再套 `list()`

### 读 N 行 ★

```python
n = int(input())
for _ in range(n):
    line = input()
```

`_` 是「这个变量我不用」的约定写法。

### 读一行浮点数

```python
x = float(input())
```

### 打印一个值

```python
print(x)
```

### 一行打印多个值，用空格隔开 ★

```python
print(a, b)          # 输出：12 36
```

`print` 会自动在每个逗号处补一个空格，**不用自己加空格**。

### 一行打印多个值，用别的符号隔开

```python
print(a, b, sep=",")   # 输出：12,36
print(a, b, sep="")    # 输出：1236
```

### 打印时不换行

```python
print(x, end="")
print(y)
```

`print` 每次默认结尾带一个换行；`end=""` 把它改成别的（这里是空）。

### f-string 插变量 ★

```python
name = "小明"
age = 18
print(f"{name}今年{age}岁")
```

花括号里可以直接放变量、也能放表达式（`f"{a+b}"`）。

### 保留小数位 ★

```python
x = 72 / 3
print(f"{x:.1f}")     # 24.0   保留 1 位小数
print(f"{x:.2f}")     # 24.00  保留 2 位小数
print(f"{x:.0f}")     # 24     不要小数
```

和 C 的 `printf("%.1f", x)` 是同一套格式，只是从 `%` 挪到了花括号里、用冒号分隔。

### 把列表连成一行输出 ★

```python
words = ["olleH", "dlroW"]
print(" ".join(words))   # olleH dlroW
print(*words)            # olleH dlroW（星号=把列表摊开，也是空格隔开）
```

### 输出变量的几种写法（从推荐到不推荐）

```python
print(f"年龄：{age}")        # 1. f-string，推荐
print("年龄", age)           # 2. 逗号，自动空格
print("年龄：%d" % age)      # 3. C 风格
print("年龄：{}".format(age)) # 4. 老写法
```

### ★ 字符串和数字不能直接相加

```python
age = 18
print("年龄：" + age)        # ✗ TypeError
print("年龄：" + str(age))   # ✓ 先用 str() 转
print(f"年龄：{age}")        # ✓ f-string 自动处理
```

---

## 2. 字符串 str

### 创建

```python
s = "hello"
s = input()
```

### 取单个字符（下标从 0 开始）★

```python
s = "hello"
s[0]   # h
s[1]   # e
s[-1]  # o   负数 = 从后往前数
s[-2]  # l
```

### 长度

```python
len(s)   # 5
```

### 切片 ★

写法：`s[开始 : 结束 : 步长]`，三个位置都可以省略。

```python
s = "hello"
s[1:4]    # ell     从下标1开始，到下标4之前停（含头不含尾）
s[:3]     # hel     开头省略 = 从头开始
s[3:]     # lo      结束省略 = 一直到最后
s[-2:]    # lo      最后两个
s[::2]    # hlo     每隔一个取
s[::-1]   # olleh   ★ 倒序，刷题超常用
```

★★ **含头不含尾**：结束位置那个字符**不拿**。这是最容易错的一条。

### 遍历每个字符

```python
for ch in s:
    print(ch)
```

### 大小写转换 ★

```python
s.lower()   # 全部转小写，"Gu" → "gu"
s.upper()   # 全部转大写
```

### 替换 ★

```python
s.replace(旧, 新)
"2023".replace("2", "1")   # "1013"
```

默认替换**所有**出现的地方。

### 计数 ★

```python
"ggggugu".count("gu")   # 2
```

### 查找位置

```python
s.find("ll")    # 2   找不到返回 -1
"gu" in s       # True/False，只判断有没有
```

### 按分隔符切开 ★

```python
"a b c".split()        # ["a", "b", "c"]  不填参数=按空格切
"a,b,c".split(",")     # ["a", "b", "c"]  按逗号切
```

### 拼接（split 的反操作）★

```python
" ".join(["a", "b"])   # "a b"   引号里是什么就用什么当分隔符
"-".join(["a", "b"])   # "a-b"
```

### 类型转换

```python
str(123)     # "123"
int("123")   # 123
float("3.5") # 3.5
```

### ★★ 字符串是不可变的

```python
s = "hello"
s[0] = "H"        # ✗ TypeError，字符串改不了
s = s.replace("h", "H")   # ✓ 用工具生成一个"新"字符串，再存回去
```

**所有看起来像"修改字符串"的工具（replace / lower / upper / strip），其实都是返回一个**新**字符串，原来的没变。** 想留住结果，一定要用变量接住。

对比：**列表可以直接改**（`nums[0] = 9` 是合法的），字符串不行。

### 其他常用

```python
s.strip()        # 去掉首尾空白
s.isdigit()      # 是不是全是数字
s.isalpha()      # 是不是全是字母
s.replace(" ", "")  # 去掉所有空格
```

---

## 3. 列表 list

### 创建

```python
nums = [10, 20, 30]
empty = []
nums = list(map(int, input().split()))
nums = [0] * 5          # [0, 0, 0, 0, 0]
```

### 取元素 ★

```python
nums[0]    # 10    第一个
nums[-1]   # 30    最后一个
len(nums)  # 3     有几个
```

### 加元素 ★

```python
nums.append(40)          # 末尾追加（刷题最常用）
nums.insert(1, 99)       # 在下标1处插入
nums.extend([50, 60])    # 一次追加多个
```

### 删元素

```python
nums.remove(20)   # 删掉值为 20 的那个（按值删）
nums.pop()        # 删掉并返回最后一个
nums.pop(0)       # 删掉并返回下标 0 的
del nums[1]       # 按下标删
```

### 排序 ★

```python
nums.sort()             # 直接改自己，没有返回值
sorted(nums)            # 返回一个新的排好序的列表，自己不变
nums.sort(reverse=True) # 从大到小
sorted(nums, key=lambda x: -x)   # 也可反过来排
```

★ **易错**：`nums.sort()` 返回 `None`。写 `nums = nums.sort()` 会把列表弄丢。

### 反转

```python
nums.reverse()       # 直接改自己
nums[::-1]           # 生成一个反过来的新列表
```

### 统计 ★

```python
sum(nums)      # 求和
max(nums)      # 最大
min(nums)      # 最小
len(nums)      # 个数
nums.count(2)  # 值为2的出现几次
```

### 遍历 ★

```python
for x in nums:                 # 最常用
    print(x)

for i, x in enumerate(nums):   # 同时要下标（从0开始）
    print(i, x)

for i, x in enumerate(nums, 1): # 下标从1开始
    print(i, x)
```

### 判断存在

```python
20 in nums     # True
```

### 累加套路 ★

```python
total = 0
for x in nums:
    total += x
```

---

## 4. 元组 tuple

```python
weeks = (1, 2, 3, 4, 5, 6, 7)
weeks[0]     # 1
weeks[0] = 9 # ✗ 报错，元组只读
```

### 解包

```python
a, b, c, d, e, f, g = weeks
```

### 什么时候用

一组「本来就不会变」的数据，比如一年的月份、方向向量。用元组可以防止被误改。

---

## 5. 字典 dict

一个**键**对应一个**值**，靠名字取，不靠位置。

### 创建

```python
d = {"A": 3, "B": 1, "C": 0}
d = {}
```

### 取值 ★

```python
d["A"]        # 3
d["Z"]        # ✗ 键不存在直接 KeyError
d.get("Z", 0) # ★ 安全取值：没有这个键就返回你给的默认值
```

★ 刷题一律用 `.get(键, 默认值)`，别用 `d[键]` 去取不确定存不存在的键。

### 改值 / 新增 ★

```python
d["A"] = 5        # 键已存在 = 改值
d["D"] = 2        # 键不存在 = 新增
```

### 判断键在不在

```python
"A" in d     # True
```

### 删除

```python
del d["A"]
d.pop("A")
```

### 遍历 ★

```python
for k in d:                 # 遍历所有键
    print(k)

for k, v in d.items():      # ★ 同时拿键和值，最常用
    print(k, v)

for v in d.values():        # 只要值
```

★ 字典的遍历顺序 = **插入顺序**。（旧版 Python 是无序的，现在是有序的，这点在刷题里能利用。）

### 计数套路 ★★

```python
d[键] = d.get(键, 0) + 1
```

读法：「取出这个键现在的次数（没有就当 0），加 1，再存回去」

完整例子：
```python
count = {}
for ch in "hello":
    count[ch] = count.get(ch, 0) + 1
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### 累加套路（按类别汇总）

```python
total = {}
for name, value in data:
    total[name] = total.get(name, 0) + value
```

### 取最大值 / 找最大对应的键

```python
max(d.values())                       # 最大的值
max(d, key=d.get)                     # 值最大的那个键
max(d.items(), key=lambda kv: kv[1])  # 返回 (键, 值)
```

### 按值排序

```python
sorted(d.items(), key=lambda kv: kv[1], reverse=True)
```

### 其他

```python
len(d)          # 有几个键值对
d.keys()        # 所有键
d.values()      # 所有值
d.items()       # 所有键值对
list(d)         # 键的列表
```

---

## 6. 集合 set

```python
s = {1, 2, 3}
s = set()          # ★ 空集合只能这么写，{} 是空字典
s = set([1, 1, 2]) # 自动去重 → {1, 2}
```

- 特点：**不重复、无序**
- 用途：去重、快速判断某元素在不在
- 运算：

```python
a & b    # 交集
a | b    # 并集
a - b    # 差集
a.add(x) # 加
```

---

## 7. 控制流 if

### 形状 ★

```python
if 条件1:
    事情1
elif 条件2:
    事情2
else:
    事情3
```

### 和 C 的对照

| C 语言 | Python |
|---|---|
| `if (x > 0) { }` | `if x > 0:` 换行缩进 |
| `else if` | `elif` |
| `else { }` | `else:` |
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |
| `{ }` 包代码块 | **缩进**表示代码块 |

### 三条铁律

1. **冒号 `:` 不能丢**
2. **没有大括号，靠缩进**（缩进相同的几行 = 同一个代码块）
3. **`elif` 是连写的**，不是 `else if`

### 比较运算符

```python
==  !=  <  >  <=  >=
```

`=` 是赋值，`==` 是判断相等 —— 这个坑 C 里也有。

### 什么算"真"

**假**：`0`、`0.0`、`""`（空字符串）、`[]`、`{}`、`None`
**真**：其他一切非空的

所以判断「列表是不是空的」直接写 `if nums:` 就行。

### 三目运算（一行版 if）

```python
result = "及格" if score >= 60 else "不及格"
```

### ★ 判断是有顺序的

`if / elif` 从上往下检查，**谁写在前面谁先命中，后面的就不看了**。利用这点可以省掉一堆判断（比如「打平时留字母最小的」，只要保证字典按键从小到大的顺序遍历，然后只在「严格大于」时才换人，就自动实现了）。

---

## 8. 循环 for / while

### for 遍历容器 ★

```python
for x in 列表或字符串或字典:
    ...
```

**Python 直接遍历东西本身，不需要下标、不需要长度。** 这是和 C 最大的区别。

### range ★

```python
range(5)         # 0 1 2 3 4          （5个，不含5）
range(1, 6)      # 1 2 3 4 5          （含头不含尾）
range(0, 10, 2)  # 0 2 4 6 8          （步长2）
range(5, 0, -1)  # 5 4 3 2 1          （倒着数）
```

### 重复 N 次 ★

```python
for _ in range(n):
    ...
```

### while

```python
while 条件:
    ...
```

### break / continue

```python
break      # 直接跳出整个循环
continue   # 跳过这一圈剩下的部分，进入下一圈
```

### 累加 / 计数套路 ★

```python
total = 0
count = 0
for x in nums:
    total += x      # 累加
    count += 1      # 计数
```

### enumerate（边遍历边拿下标）★

```python
for i, x in enumerate(nums):
    print(i, x)

for i, x in enumerate(nums, 1):   # 下标从 1 开始
    print(i, x)
```

### zip（同时遍历两个列表）

```python
for a, b in zip(list1, list2):
    print(a, b)
```

---

## 9. 函数 def

### 基本形状

```python
def 函数名(参数):
    做事情
    return 结果
```

### 返回 vs 打印

```python
def greet(name):
    print(f"你好，{name}")     # 只是打印出来，外面拿不到

def greet2(name):
    return f"你好，{name}"     # 返回给外面，外面能接着用

msg = greet2("小明")           # 这里能接到
```

★ 想在外面继续用结果，就用 `return`。

### 默认参数

```python
def add(a, b=10):
    return a + b

add(5)      # 15   b 用了默认值
add(5, 3)   # 8    b 被传入覆盖
```

★ 默认参数必须写在普通参数**后面**。

### 关键字参数

```python
add(b=3, a=5)    # 按名字传，顺序随便
```

### 作用域

```python
x = 5
def f():
    x = 10      # 这是函数内部的局部变量，外面的 x 没变
```

- **函数内部新建的变量，函数一结束就消失**
- 想在函数里改**外面的数字/字符串**，要写 `global x`
- 但如果是**列表、字典**，在函数里 `append`、改键值**不需要** `global`（因为改的是对象内容，没有重新赋值）

### 函数是一段可以重复用的逻辑

拆函数的意义：一段逻辑只写一遍，需要时调用。名字要能说明它做什么（`add_student`、`show_students`）。

---

## 10. 类 class

> 这部分是暑假学的，还没在刷题里用上，先把形状记住。

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        return f"{self.name}: {self.score}"
```

- `class 类名:` —— 类名习惯用大写开头
- `__init__` = **构造函数**，创建对象时自动执行，用来初始化
- `self` = 指「这个对象自己」，每个方法第一个参数都是它
- `self.name = name` —— 把传进来的值存成**对象的属性**
- 方法 = 类里面的函数

### 继承

```python
class GradStudent(Student):
    def __init__(self, name, score, major):
        super().__init__(name, score)   # 调用父类的构造函数
        self.major = major
```

### @ 开头的东西是什么

**`@` 叫装饰器**：意思是「给下面这个函数额外加一层功能」。

```python
@property
def score(self):
    return self._score

@score.setter
def score(self, value):
    if value < 0:
        raise ValueError("分数不能为负")
    self._score = value
```

- `@property` —— 让「这个方法」表现得像「一个属性」。外面写 `stu.score` 就行，不用写 `stu.score()`
- `@score.setter` —— 专门管「给它赋值的时候做什么」，可以在里面加检查
- `@staticmethod` —— 表示这个方法**不需要 `self`**，它跟具体某个对象无关，是个"挂在类下面的普通函数"
- `@classmethod` —— 第一个参数是 `cls`（类本身）而不是 `self`

**判据**：看到 `@` 就问一句「它给我下面这个函数加了什么额外功能？」

---

## 11. 文件与 JSON

```python
# 读
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 写
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("内容")
```

`with` 的好处：代码块结束时自动关文件，不用手动 `close()`。

### JSON 读写

```python
import json

# 读
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 写
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

- `json.load` = 文件 → Python 对象
- `json.dump` = Python 对象 → 文件
- `ensure_ascii=False` 让中文正常显示（不然会变成 `\uXXXX`）
- `indent=2` 让输出好看、能读

---

## 12. 异常处理 try

```python
try:
    可能出错的代码
except ValueError:
    出错了怎么办
else:
    没出错时额外做什么（可选）
finally:
    不管出没出错都要做（可选）
```

### 什么时候用

- 用户输入的东西不可信（要转数字）
- 文件可能不存在
- 网络可能断

### try 和 if 的区别

- `if` 判断「**我预想到的**情况」（比如 `if num2 != 0`）
- `try` 兜住「**我没想到或者懒得逐个判断的**意外」（比如把一串乱七八糟的输入转成数字）

**刷题时**：判题数据一般合法，不需要 try；工程代码里必须有。

---

## 13. 常用内置函数速查

| 函数 | 作用 | 例子 |
|---|---|---|
| `len(x)` | 长度 | `len([1,2,3])` → 3 |
| `sum(x)` | 求和 | `sum([1,2,3])` → 6 |
| `max(x)` / `min(x)` | 最大 / 最小 | `max([1,9,3])` → 9 |
| `abs(x)` | 绝对值 | `abs(-5)` → 5 |
| `round(x, n)` | 四舍五入 | `round(3.14159, 2)` → 3.14 |
| `sorted(x)` | 排序，返回新列表 | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(x)` | 反转 | `reversed([1,2,3])` |
| `range(a,b)` | 数字序列 | `range(1,4)` → 1,2,3 |
| `enumerate(x)` | 带下标遍历 | 见循环章节 |
| `zip(a,b)` | 同时遍历两个 | 见循环章节 |
| `int(x)` / `float(x)` / `str(x)` | 类型转换 | `int("3")` → 3 |
| `list(x)` | 转成列表 | `list("abc")` → `['a','b','c']` |
| `map(f, x)` | 对每个元素做 f | `map(int, ["1","2"])` |
| `type(x)` | 看它是什么类型 | `type(5)` → `<class 'int'>` |

★ **`type()` 是排查问题的利器**：不确定一个变量到底是什么，就 `print(type(x))`。

---

## 14. 踩过的坑

> 这些是真踩过的，不是编的。考前翻一遍。

1. **`input()` 拿回来是字符串** —— `"3" + "5"` 得到 `"35"` 而不是 `8`。要算就得 `int()`
2. **`map()` 不是列表** —— 要 `list()` 装出来才能用。但 `split()` **已经是列表**，不用再套 `list()`
3. **`for i in n`** —— `n` 是数字，不能被遍历。要 `for i in range(n)`
4. **变量名不能撞内置函数** —— 已踩：`sum`、`list`、`max`。也别用 `min`、`type`、`input`、`str`、`int`
5. **`print` 放在循环里** → 输出成多行。要合成一行就把 `print` 挪到循环**外面**
6. **字符串不能和数字直接 `+`** —— 要先 `str(数字)` 或用 f-string
7. **字符串不可变** —— `s[0] = "x"` 报错，只能用工具生成新字符串
8. **变量名拼写不一致** → `NameError`。Python 认名字是逐字比较的
9. **切片方括号里是冒号不是逗号** —— `s[1:4]` ✓，`s[1,4]` ✗
10. **切片含头不含尾** —— `s[0:2]` 只拿两个字符
11. **工具要"接住"结果** —— `s.replace(...)` 不改 `s`，要用变量接住新结果
12. **`nums.sort()` 返回 `None`** —— 别写 `nums = nums.sort()`
13. **`d[键]` 取不存在的键会崩** —— 用 `d.get(键, 默认值)`
14. **用 `//` 会丢掉小数** —— 想算平均值用 `/`

---

## 15. 刷题常用套路

### 读入 N 行数据

```python
n = int(input())
for _ in range(n):
    a, b = input().split()
```

### 多组数据（第一行给 T）★

```python
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
```

### 一行数字求和

```python
nums = list(map(int, input().split()))
print(sum(nums))
```

### 统计每个东西出现几次 ★

### 预处理：用空间换时间 ★★

**什么时候想到它**：

- 数据量很大（n 或 q 到 10^5 以上），但你发现**同一个问题被反复问**
- 「统计每个……出现几次/第一次在哪/最后一次在哪」
- 如果你对每次询问都重新扫一遍全表，总次数量级会到 10^10，必然超时

**思路**：先花一遍时间（O(n)）把所有答案**提前算好存进字典**，之后每次询问只要查一次字典（O(1)）。

**模板：记录第一次 / 最后一次出现的位置**

```python
first = {}
last = {}
for i, v in enumerate(nums):
    if v not in first:      # 只有没见过才记 → 保住"第一次"
        first[v] = i
    last[v] = i             # 无条件覆盖 → 扫完留下"最后一次"
```

这个模板一次性解决了所有特殊情况：

- 只出现一次 → first 和 last 是同一个位置
- 所有元素相同 → 不需要任何分界点判断
- 最后一个元素 → 它没有"下一个"，但这里根本不看下一个

**对比：不要用「找相邻分界点」的做法**

那种做法要额外处理上面三种情况，还要小心 `nums[i+1]` 越界。

**反问自己**：我这个问题，是不是被问了很多次？如果是 → 考虑预处理。


```python
count = {}
for x in data:
    count[x] = count.get(x, 0) + 1
```

### 按类别汇总总和

```python
total = {}
for name, value in records:
    total[name] = total.get(name, 0) + value
```

### 求"最多"且并列时有规则 ★

```python
best = 第一个
for k in 有序的键:
    if 当前值 > best的值:     # 只在严格大于时换人
        best = k
```

利用「遍历顺序 + 严格大于」自动处理并列。

### 字符串处理三件套

```python
s.replace(旧, 新)   # 替换
s.lower()           # 统一小写（大小写不敏感时先转）
s.count(要找的)      # 计数
s[::-1]             # 倒序
" ".join(列表)       # 拼回一句话
```

### 数字太长（上千位）

**当字符串处理**，不要转 `int`。题目给「n < 10^1000」这种就是明示你别用数字类型。

### 输出格式要求

- 冒号后面的空格也算格式的一部分，抄题目抄全
- 保留小数：`f"{x:.1f}"`
- 多行输出：一个 `print` 一行


---

## 16. 变量命名规范

> 一句话：**让三天后的自己能看懂。**

### 三条原则

1. **名字要说明里面装的是什么** —— 变量叫 `num` 但装的是字符串，回看就会误判
2. **同一个名字在不同文件里保持同一种含义** —— 否则读到一半会愣住
3. **别撞 Python 自带的名字** —— `sum`、`list`、`max`、`min`、`type`、`input`、`str`、`int`

### 常见对应表

| 装的是什么 | 推荐名字 |
|:---|:---|
| 一行字符串 | `s` / `text` / `line` |
| 一组数字 | `nums` / `values` |
| 一个数字 | `n` / `x` |
| 一组单词 | `words` |
| 字典：计数 | `count` |
| 字典：累计 | `total_time` / `total_score` |
| 下标 | `i` / `idx` |
| 循环里不用的 | `_` |
| 布尔标志 | `found` / `is_valid` |
| 结果 | `result` / `answer` |
| 位置 | `pos` |
| 累计次数 | `jumps` / `steps` |
| 上一个选中的值 | `last_picked` |
| 两个以上的集合 | 用复数（`nums`、`words`、`students`） |

### 反面例子（都是实际踩过的）

| 差 | 好 | 问题 |
|:---|:---|:---|
| `fh` | `operator` | 拼音缩写，只有当时的自己看得懂 |
| `tice` / `Time` | `count` / `total_time` | 只差大小写，含义还刚好反了 |
| `xb` | `first_index` | 拼音缩写 |
| `pl` | `pos` | 看不出是什么的缩写 |
| `s`（装平台列表） | `platforms` | `s` 在别的文件里一直是字符串 |
| `index = 0 / 1` 当布尔用 | `found = False / True` | 名字说它是下标，其实在装「有没有找到」 |

### 唯一的例外

**数学公式里约定俗成的短名字可以用**：循环下标 `i`、坐标 `x y`、临时交换 `tmp`、公式里的 `n m d`。
题目里叫 `m`，你就叫 `m`，这不算不规范。

### 自查方法

**写完一题，隔天回看一遍。**
哪个名字让你停顿了一下，那个就是该改的。

## 17. 两种输入模型（多组数据）

刷题时数据怎么给，只有两种模型。**判据：看样例怎么排版。**

### 模型 1（最常见）：第一行 T，后面 T 行，每行一个数

```python
T = int(input())
for _ in range(T):
    n = int(input())
    print(n * 2)
```

- T 的作用就是**控制循环次数**
- 读一组 → 算一组 → 输出一组，**全都在循环体里面**
- 每组输出一行 → `print` 在循环里

### 模型 2：第一行 T，第二行把 T 个数一次性给全（空格隔开）

```python
T = int(input())
nums = list(map(int, input().split()))
for n in nums:
    print(n * 2)
```

- 一次读完，这时候 **T 其实用不上**
- 别把 T 和数据塞进同一个列表（`T = nums[0]`）—— 样例一换行就崩

### 判据与踩过的坑

- **先数题目要几行输出**：每组一行 → `print` 在循环里；全部凑成一行 → `print` 在循环外
- 处理逻辑写在循环外 → 只输出最后一组（10/2 踩过）
- 想不清就**先用样例手推**：样例几行输入、几行输出

### 字典计数固定写法

```python
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
```

`表.get(键, 默认值)`：键不存在时返回默认值，**不报错**。（写 `表[键]` 会 `KeyError`。）

### 下标 + 元素一起拿

```python
for i, v in enumerate(values):
    ...
```

`enumerate(序列)` 遍历时同时给**下标**和**元素**，默认从 0 开始；`enumerate(values, 1)` 从 1 开始。

## 18. 前缀和 / 同余 / 对拍（2026-10-03 新增）

### 前缀和

`pre[i]` = **前 i 个数**的和，规定 `pre[0] = 0`。

区间 `[l, r]` 的和 = `pre[r] - pre[l-1]`

```python
a   = [2, 5, 1, 4]
pre = [0, 2, 7, 8, 12]
# 第 2 个数到第 3 个数 = pre[3] - pre[1] = 8 - 2 = 6
```

⚠️ `pre[i]` 的 `i` 是「**前 i 个**」，不是「第 i 个」。自检技巧：拿极端例子代入
（「第 1 个到第 1 个」必须是 `pre[1] - pre[0]`）。

### 同余等价 —— 判断「区间和是 m 的倍数」

```
pre[r] - pre[l-1] 是 m 的倍数   ⟺   pre[r] 和 pre[l-1] 除以 m 的余数相同
```

所以「存不存在一段区间、它的和是 m 的倍数」= 「所有前缀和里有没有两个余数相同」
→ 一遍扫描 + 集合查重，O(n)

```python
s = {0}          # 先把 0 放进去（它对应 pre[0]）
cur = 0
for v in values:
    cur = (cur + v) % m
    if cur in s:
        ...       # 找到，输出 Yes
    s.add(cur)
```

### 鸽巢原理（这题名字的来历）

`pre[0] ~ pre[n]` 一共 **n+1** 个余数，而模 m 只有 **m** 种可能。
`n+1 > m`（即 **n ≥ m**）时必然有两个余数相同 → 答案一定是 Yes。

### 集合 set

```python
s = set()
s.add(x)
x in s      # O(1)，非常快
```

### 对拍 —— 验证自己的解法对不对

1. 先写一个**暴力版**（慢，但逻辑简单、容易保证对）
2. 造几百组**随机小数据**
3. 两个程序跑同一份输入，逐行比对输出
4. 有不一致 → 那组数据就是定位 bug 的钥匙

### 复杂度直觉（Python 参考）

| 规模 | 耗时 |
|:---|:---|
| n = 10^4 时 n²/2 ≈ 5000 万次 | 约 5 秒 |
| n = 10^4 时 n 次 | 约 0.05 秒 |

比赛 3 小时 20 题 → 每题约 9 分钟，**单题跑超过几秒就要警惕**。

## 19. 二分查找（2026-10-04 新增）

### 什么时候用

数组**有序**时找东西。每次砍一半 → **O(log n)**。

| n | 一个个找（最坏） | 二分（最坏） |
|:---|:---|:---|
| 8 | 8 次 | 3 次 |
| 100000 | 100000 次 | **17 次** |

### 骨架（判断 k 在不在）

```python
left = 0
right = n - 1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == k:
        ...                # 找到
    elif a[mid] < k:
        left = mid + 1     # 去右半边
    else:
        right = mid - 1    # 去左半边
```

### ⚠️ 死循环的坑（必背）

`mid = (left + right) // 2` 是**向下取整**。区间只剩 2 个数时 mid 正好 = left，所以：

- 写成 `left = mid` → 区间一个数都没丢掉 → **死循环**
- 比赛里的表现是 **TLE（超时），不是报错** —— 比崩溃更阴
- 必须写 `left = mid + 1` / `right = mid - 1`：**每轮至少丢掉一个数**

### 找边界（数组里有重复值时）

普通二分命中就停，但你不知道停在第几个。要"第一个 / 最后一个"时：

```python
# 找第一个等于 k 的位置
if a[mid] == k:
    first = mid
    right = mid - 1      # 命中也不停，继续往左挤

# 找最后一个等于 k 的位置
if a[mid] == k:
    last = mid
    left = mid + 1       # 命中也不停，继续往右挤
```

**关键**：候选变量必须在循环**之前**先初始化成 `-1`（找不到就保持 -1），否则某条分支一次都没走到时会 `UnboundLocalError`。

### 「q 个询问」题的通用结构

```
读 n, q
读数组
读 q 个询问
for 每个询问:              ← 外层遍历询问
    重置这一轮的所有变量      ← left / right / 结果变量都要重置
    算这一次
    print 这一行            ← 每轮输出一行（判据：数题目要几行输出）
```

### Python 缩进 = 代码块边界（2026-10-04 踩坑）

Python 没有大括号，**缩进就是"谁属于谁"**：

- 和 `for` **齐平** → 兄弟，**在循环外面**
- 比 `for` **深** → 在**循环里面**

写完一个循环，回头**数字符缩进**是必修动作。VS Code：选中多行 `Tab` 右移、`Shift+Tab` 左移，`Ctrl+Z` 撤销。