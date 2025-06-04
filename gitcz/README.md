# 学习记录
```text
    创建一个目录 mkdir <dirName>
1. git init 初始化一个git仓库，可以使用 git init <fileName>指定创建 .git 目录
2. git add . 将目录中的变更添加到暂存区
3. git commit -m "首次提交" 将暂存区中的内容提交
4. git remote add <remoteName> <fenzhi> <url> 添加一个远程仓库
5. git status 查看暂存区中的内容
6. git remote 查看远程仓库
7. git checkout -b <branchName> 创建并进入新的分支
8. git branch -d <branchName> 删除分支
9. git switch <branchName> 切换分支
10. git merge <branchName> 将另一个分支合并到当前分支
11. git pull <remoteName> <fenzhi> 从远程仓库拉取并合并分支
12. git push <remoteName> <fenzhi>
13.git rm <name> 删除某个文件
 推送到远程仓库，如果远程仓库不存在分支就创建新分支
```

## 1. 初始化和克隆
```text
git init 初始化一个 git 仓库
git clone <git_url> 从远程仓库克隆到本地
```
## 2. 快照和基本操作
```text
git status 显示工作目录和暂存区的状态
git add <fileName> 将文件添加到暂存区
git diff 显示未提交的更改
git diff --staged 比较暂存区与最后一次提交的差异
git commit -m "<message>"  提交暂存区的内容到本地仓库，并且附带提交信息
```
# 2. 分支管理
```text
git branch 列出所有分支，当前分支会以 * 标注
git branch <new branch name> 创建新的分支
git checkout <branch-name> 切换到指定分支并更新工作区
git checkout -b <branch-name> 创建并进入新的分支
git merge <branch-name> 合并指定分支到当前分支
git branch -d <branch-name> 删除指定分支
```

## 3. 远程操作
```text
git remote -v 查看所有远程仓库地址
git remote add <remote-name> <remote-url> 添加远程仓库
git fetch <remote-name> 从远程仓库获取最新内容但不自动合并和修改当前工作
git pull <remote-name> <branch-name> 拉取远程仓库的更新并合并到当前分支
git push <remote-name> <branch-name> 推送本地分支到远程仓库
```

# 4. 查看历史提交日志
```text
git log 显示提交日志
git log --oneline 以简洁的一行显示提交日志
git log -p 显示每次提交的具体差异
git show <commit> 显示某次特定提交的详情
```


# 5. 撤销操作
```text
git reset <filename> 取消暂存区中的文件更改
git reset <commit-id>  回退到特定的提交（这可能会影响到后续的提交历史）
git checkout -- <filename> 丢弃工作区内的更改恢复至最近一次提交的状态
```

# 6. 标签操作
Git 标签（Tag）用于给仓库中的特定提交点加上标记，通常用于发布版本（如 v1.0, v2.0）
```text
git add tag <tag-name> 添加一个标签
git add -a tag <tagname> [-a] 选项可以添加注解，执行 git tag -a 命令时，Git 会打开你的编辑器，让你写一句标签注解，就像你给提交写注解一样。

git tag -a <tag-name> <commit-id>   如果我们忘了给某个提交打标签，又将它发布了，我们可以给它追加标签。

git tag 查看所有标签
git push <remote-name> <branch-name> --tags    默认情况下，git push 不会推送标签，需要显式地推送标签。

git tag -d <tagname> 删除本地 tag

git push <remote-name> --delete <tagnaem>  远程删除tag

git tag -a <tagname> -m "<message>" 附注标签
```