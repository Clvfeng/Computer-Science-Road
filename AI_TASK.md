# AI_TASK.md

> 每天开始工作时，AI助手优先读取本文件和 AI_MEMORY.md。
>
> 本文件记录当前阶段任务、已完成内容和下一步计划。
>
> 每天更新。

---


## ⏸ 暂停状态（2026-08-05 起）

- 原因：个人事务，学习计划暂停一段时间
- 长期路线不变：Python工程能力 → C++/数据结构 → 后端/Web/AI
- 恢复方法：回来后直接说"恢复学习"，AI 会读取本文件从暂停点继续

### 暂停点（恢复时从这里继续）

1. **链表练习未完成**：01-C++/linked_list_ops.cpp 的 add_tail / insert_after 还有 2 个 bug 未修
   - add_tail：循环条件应为 while (cur->next != nullptr)（找最后一个节点，不是 nullptr）
   - insert_after：应比较 target 不是 value；循环里缺 cur = cur->next;
2. **20分钟代码阅读**：素材 tqdm（1000-5000行Python小项目），任务：README → 文件结构 → std.py 开头 → 回答3个问题（未完成）
3. **栈（Stack）入门**：未开始

## 当前阶段

Phase 1：Python基础恢复 ✅ 已完成

## Phase 2：Python工程能力（当前）

目标：具备工程化开发能力，恢复数据结构基础

学习内容：面向对象、项目结构、Git流程、Debug能力
C++复习 + 数据结构（数组、链表、栈、队列、树）

进度记录：03-Python/PROGRESS.md


## 已完成

- Day1：hello.py（个人信息卡片）
- Day2：function.py（函数版计算器）
- Day3：函数进阶（默认参数、作用域、global）
- Day4：列表和元组（增删改查、for遍历、解包）
- 补充：可变对象 vs 不可变对象
- Day5：字典和集合 + 学生信息管理小程序
- Day6：student_manager V1 函数重构 + V2 JSON文件存储
- Day7：模块化重构（4文件结构）
- Day8：OOP深化（继承、property、classmethod）
- Day9：虚拟环境 venv + pip


## 当前目标

完成Python基础恢复，进入数据结构阶段。


## Phase 1 已完成项目

| 项目 | 状态 |
|:-----|:----:|
| student_manager V1（函数结构 + CLI菜单） | ✅ |
| student_manager V2（JSON文件存储 + 异常处理） | ✅ |
| README.md + 工程文档 | ✅ |

## 当前任务

C++ 复习 + 数据结构恢复（数组、链表、栈、队列、树）
数据结构实现（C++）

## Phase 2 已完成

| 内容 | 状态 |
|:-----|:-----:|
| 面向对象 class（继承、property、classmethod） | ✅ |
| 模块化 import + 多文件结构 | ✅ |
| 虚拟环境 venv + pip | ✅ |

## Phase 2 当前：C++/数据结构恢复

| 内容 | 项目 |
|:-----|:-----|
| C++ 语法复习 | 基础练习 |
| 数组 + 指针 | C++实现 |
| 链表：节点、遍历、头插、删除 | ✅ 01-C++/linked_list_ops.cpp |
| 链表：中间插入、尾插、双向链表 | 下一步 |
| 栈、队列 | C++实现 |
| 树、排序 | C++实现 |


## Phase 3：AI应用开发（待开始）

| 内容 | 项目 |
|:-----|:-----|
| API调用、JSON、HTTP | AI学习助手 V1-V4 |

---

## 提醒事项

1. 每天提交 Git：add / commit / push
2. 每天记录学习日志到 03-Python/notes/daily/YYYY-MM-DD.md
3. 每个项目包含：README.md + CHANGELOG.md + TODO.md
4. 更新 03-Python/PROGRESS.md 记录进度
5. 不赶进度，理解代码结构 > 完成速度
6. 软件工程能力 > 单纯Python语法数量
7. 每天20分钟代码阅读（素材由AI指定：1000-5000行Python小项目，不随机浏览GitHub）
