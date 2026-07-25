# Plan-Adjustment-2026-07-25

## 调整1：学习方式重构

### 变更
- 不再按Day严格推进，改为Phase目标驱动
- 评价标准：理解设计 > 完成速度

### 新增规范
- 每个项目：README.md、CHANGELOG.md、TODO.md
- 增加03-Python/PROGRESS.md记录长期进度
- 每日复盘固定模板（03-Python/notes/daily/YYYY-MM-DD.md）
- 每天20分钟代码阅读任务

### 长期路线
- Phase 1：Python恢复 + student_manager
- Phase 2：Python工程能力 + C++/数据结构恢复
- Phase 3：后端/Web/数据库/AI项目


## 调整2：student_manager 长期升级

| 版本 | 技术 | 状态 |
|:----|:-----|:----:|
| V1 | 命令行 + list/dict 存储 | 需重构为函数结构 |
| V2 | 文件存储（txt/JSON） | 待进行 |
| V3 | SQLite 数据库 | Phase 2 |
| V4 | Flask Web版 | Phase 3 |


## 调整3：Day6任务变更

原计划：文件操作 + JSON
调整为：重构 student_manager V1

### 具体任务
1. 函数拆分：main()、add_student()、delete_student()、update_student()、show_students()
2. 完善CLI菜单（添加/删除/修改/查看/退出）
3. 基础异常处理（try/except）
4. README.md 工程文档


## 调整原因

Day1-Day5 学的内容（变量、input、if、list、dict、for、函数基础）刚好够支撑V1重构。

如果直接进入文件读写→JSON→数据库，容易知道"怎么存数据"，但不知道"程序为什么这么组织"。

### 路线

Python语法恢复 → student_manager V1重构 ← 现在 → 文件存储 → 数据库 → Web
