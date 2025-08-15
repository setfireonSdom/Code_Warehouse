## **1️⃣ 新项目初始化并首次提交**

**场景**：新建本地仓库并推送到远程

```bash
git init                         # 初始化本地仓库
git add .                        # 暂存所有文件
git commit -m "Initial commit"   # 提交记录
git branch -M main               # 重命名主分支为 main
git remote add origin <url>      # 绑定远程仓库
git push -u origin main          # 首次推送并关联
```

---

## **2️⃣ 从远程克隆并更新**

**场景**：已有远程仓库，先下载，后续更新

```bash
git clone <url>                  # 克隆远程仓库
git pull origin main              # 拉取更新并合并
```

---

## **3️⃣ 开发分支的标准流程**

**场景**：多人协作时的常规开发流程

```bash
git checkout -b feature_x         # 从当前分支新建并切换到 feature_x
# ...修改代码...
git add .                         # 暂存修改
git commit -m "实现功能X"         # 提交
git push -u origin feature_x      # 推送到远程分支
```

---

## **4️⃣ 合并分支并更新远程**

**场景**：开发完成，把功能分支合并到主分支

```bash
git checkout main                 # 切换到主分支
git pull origin main              # 确保主分支是最新的
git merge feature_x               # 合并功能分支
git push origin main              # 推送更新
git branch -d feature_x            # 删除本地分支
git push origin --delete feature_x # 删除远程分支
```

---

## **5️⃣ 修复线上 Bug（Hotfix）**

**场景**：生产环境出现紧急问题

```bash
git checkout main                 # 切到主分支
git pull origin main               # 确保是最新的
git checkout -b hotfix_bug         # 创建修复分支
# ...修复代码...
git add .                          
git commit -m "修复bug"
git push -u origin hotfix_bug
# 提交合并请求或直接合并
git checkout main
git merge hotfix_bug
git push origin main
```

---

## **6️⃣ 处理冲突的常用组合**

**场景**：拉取或合并时出现冲突

```bash
git pull origin main               # 拉取最新代码
# Git 提示冲突，手动编辑文件解决冲突
git add .                          # 标记冲突已解决
git commit                         # 完成合并
```

---

## **7️⃣ 回滚到某个版本**

**场景**：误提交，需要回到之前的状态

```bash
git log                            # 找到目标 commit id
git checkout <commit_id>           # 切到该版本（分离头指针）
# 如果要回退 main 分支：
git reset --hard <commit_id>       # 永久回退
git push origin main --force       # 强制推送
```

---

## **8️⃣ 变基更新**

**场景**：在功能分支开发期间，主分支有了更新，需要同步

```bash
git checkout feature_x
git fetch origin                   # 获取远程更新
git rebase origin/main              # 在最新 main 上重放你的提交
# 如果有冲突，解决后：
git add .
git rebase --continue
git push --force-with-lease origin feature_x
```