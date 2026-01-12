不要在 venv / virtualenv / poetry venv 创建的环境中使用 conda；
但可以、而且是常规做法，在 conda 创建的环境中使用 pip。

⚠️ 在 conda 环境里，用 pip 的正确顺序  
推荐顺序：  
系统 / 二进制依赖 → conda  
纯 Python 包 → pip

# 📘 Conda 常用指令速查文档

> 目标：**环境管理 + 包管理 + 日常排错**
> 覆盖：**95% 数据 / AI / 工程场景**

---

## 🥇 第一梯队（最核心 20%）

> **你每天 / 每周都会用**

---

## 1️⃣ `conda create` —— 创建环境（最重要）

### 用来干嘛

创建一个**隔离的 Python 运行环境**，避免版本冲突。

### 基础用法

```bash
conda create -n handllm python=3.11
```

### 常用参数

| 参数            | 作用           |
| ------------- | ------------ |
| `-n, --name`  | 环境名          |
| `python=3.x`  | 指定 Python 版本 |
| `-y`          | 自动确认         |
| `pkg=version` | 创建时顺便装包      |

### 变形用法

```bash
# 创建环境并安装多个包
conda create -n llm python=3.11 numpy pandas pytorch -y

# 从 requirements.txt（不推荐，见 pip）
conda create -n test --file requirements.txt
```

### 经验法则

> **一个项目 = 一个 conda 环境**
> 不要共用，哪怕浪费点磁盘。

---

## 2️⃣ `conda activate / deactivate` —— 进入 / 退出环境

### 用来干嘛

切换当前 shell 使用的 Python 环境。

### 用法

```bash
conda activate myenv
conda deactivate
```

### 常见问题

* **Windows / 新 shell 报错** → 先跑：

```bash
conda init
```

### 经验法则

> **任何 pip / python 操作前，先确认激活了对的环境**

---

## 3️⃣ `conda install` —— 安装包（优先）

### 用来干嘛

用 Conda 的二进制包管理器装依赖。

### 基础用法

```bash
conda install numpy
```

### 常用参数

| 参数            | 作用   |
| ------------- | ---- |
| `-y`          | 自动确认 |
| `-c channel`  | 指定源  |
| `pkg=version` | 指定版本 |

### 重要变形

```bash
# 指定 conda-forge（非常常用）
conda install -c conda-forge pytorch

# 指定版本
conda install numpy=1.26
```

### 经验法则（非常重要）

> **能 conda 装就别 pip 装**
> 尤其是：`numpy / scipy / pytorch / tensorflow`

---

## 4️⃣ `conda list` —— 查看已安装包

### 用来干嘛

查看当前环境装了什么、版本是多少。

```bash
conda list
```

### 常见变形

```bash
# 查单个包
conda list numpy
```

### 实战用途

* debug 依赖冲突
* 复制环境
* 写复现文档

---

## 5️⃣ `conda remove` —— 删除包 / 环境

### 删除包

```bash
conda remove numpy
```

### 删除整个环境（**极常用**）

```bash
conda remove -n myenv --all
```

### 经验法则

> 环境坏了？
> **删掉重建，比修更快**

---

## 🥈 第二梯队（高频但非每天）

---

## 6️⃣ `conda env list` / `conda info --envs`

### 用来干嘛

列出所有 conda 环境。

```bash
conda env list
```

### 输出示例

```text
base
llm
data
```

---

## 7️⃣ `conda update` —— 更新包 / conda 本身

### 更新单个包

```bash
conda update numpy
```

### 更新 conda

```bash
conda update conda
```

### ⚠️ 注意

> **不要随便全局 update**，可能引发大规模依赖重算

---

## 8️⃣ `conda search` —— 搜索包

```bash
conda search pytorch
```

### 指定源

```bash
conda search -c conda-forge cudatoolkit
```

---

## 9️⃣ `conda config` —— 源 & 配置管理

### 查看源

```bash
conda config --show channels
```

### 添加 conda-forge（强烈推荐）

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### 国内镜像（示例）

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
```

---

## 🥉 第三梯队（重要但偶尔用）

---

## 🔟 `conda env export` —— 导出环境

### 用来干嘛

**复现 / 分享环境**

```bash
conda env export > environment.yml
```

### 用它恢复

```bash
conda env create -f environment.yml
```

### 经验法则

> **environment.yml > requirements.txt**（conda 世界）

---

## 1️⃣1️⃣ `conda clean` —— 清理缓存

```bash
conda clean --all
```

### 什么时候用

* 磁盘爆了
* conda 奇怪报错
* 长期使用后

---

## 1️⃣2️⃣ `conda info` —— 系统诊断

```bash
conda info
```

### 用途

* 看 conda 版本
* 平台 / 架构
* base 环境路径

---

## 🚫 不推荐但你会见到的

---

### `pip install`（在 conda 里）

✔ **可以用，但要克制**

正确姿势：

```bash
conda install pip
pip install xxx
```

经验铁律：

> **conda 装底层依赖，pip 装纯 Python 包**

---

## 🧠 Conda 使用“心法总结”

### ✅ 推荐模式

```
项目
 └── 一个 conda 环境
      ├── conda install 底层包
      └── pip install 业务包
```

### ❌ 反模式

* 在 base 环境干活
* pip / conda 混装不管顺序
* 环境坏了硬修

---

## 📌 最小生存指令集（只记这 8 个）

```text
conda create
conda activate
conda install
conda list
conda remove
conda env list
conda env export
conda clean
```

# 杂
```
conda env create -f env.yml
```
这条命令里，-f 的意思是：指定环境定义文件的路径（environment definition file）,默认情况下，    `conda env create` 会自动在当前目录寻找名叫 environment.yml 的文件.

如果你的文件：不在当前目录，或者名字不是 environment.yml（比如叫 env.yml、myproject.yml 等）就需要用 -f（或写全 --file）来明确告诉 conda：“我要用这个文件来创建环境”

