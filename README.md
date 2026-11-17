# git-practice

一个用来练 Git / GitHub 基本流程的练习仓库。

## 这是什么

记录我第一次完整走通「建仓库 → 克隆/初始化 → 改文件 → 提交 → 推送」的小项目。
代码本身没有业务价值，但流程和这个仓库的结构是真实项目的做法。

## 环境要求

- Python 3.8 或更高版本
- Git 2.30 或更高版本

## 如何运行

```bash
python src/greet.py
python src/greet.py 队友
```

## 如何使用

直接运行即可，参数是要问候的人名，省略时默认问候「世界」。

## 修改流程

日常改动不要直接动 `main`，按这个顺序走：

```bash
git switch -c feature/xxx     # 从当前分支切一条新分支出来干活
# 改文件
git add -A
git commit -m "feat: 这次具体加了什么"
git push -u origin feature/xxx
```

推完之后在 GitHub 网页上开 Pull Request，review 通过再合并回 `main`。
合并后本地回到主干并同步：

```bash
git switch main
git pull
git branch -d feature/xxx     # 分支已合并，可以删掉
```

## 目录结构

```
git-practice/
├─ README.md      项目说明（就是本文件）
├─ .gitignore     告诉 Git 哪些文件不要提交
└─ src/
   └─ greet.py    示例脚本
```
