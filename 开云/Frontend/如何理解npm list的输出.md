In order to work with React in the browser, we need to include two libraries: React and ReactDOM.

所以写一些关于React和ReactDOM命令：

```bash
npm list react
npm list react-dom
```
上述指令的输出例子
```bash
my-dapp@0.1.0 /react_project/my-dapp
├─┬ @testing-library/react@16.2.0
│ └── react@19.0.0 deduped
├─┬ react-dom@19.0.0
│ └── react@19.0.0 deduped
├─┬ react-scripts@5.0.1
│ └── react@19.0.0 deduped
└── react@19.0.0

my-dapp@0.1.0 /react_project/my-dapp
├─┬ @testing-library/react@16.2.0
│ └── react-dom@19.0.0 deduped
└── react-dom@19.0.0
```
上面的输出，光看内容的话，不知道它是什么意思。拿 npm list react 来举例：

## 1. 项目结构
你的项目结构如下：
```bash
my-dapp@0.1.0 /react_project/my-dapp
├─┬ @testing-library/react@16.2.0
│ └── react@19.0.0 deduped
├─┬ react-dom@19.0.0
│ └── react@19.0.0 deduped
├─┬ react-scripts@5.0.1
│ └── react@19.0.0 deduped
└── react@19.0.0
```

## 2. 逐行解释
顶层包
my-dapp@0.1.0：这是你的项目名称和版本号。my-dapp 是你的项目名，0.1.0 是项目的版本号。
@testing-library/react@16.2.0：这是一个你直接安装的包，版本号是 16.2.0。它是一个用于测试 React 组件的库。
react-dom@19.0.0：这是另一个你直接安装的包，版本号是 19.0.0。它是 React 的 DOM 渲染库。
react-scripts@5.0.1：这是你直接安装的另一个包，版本号是 5.0.1。它是一个用于创建 React 应用的脚手架工具。
react@19.0.0：这是你直接安装的 React 核心库，版本号是 19.0.0。

依赖包
@testing-library/react@16.2.0 依赖 react@19.0.0。
deduped 表示 react@19.0.0 已经被安装在其他地方，所以这里不需要重复安装。
react-dom@19.0.0 依赖 react@19.0.0。
deduped 表示 react@19.0.0 已经被安装在其他地方，所以这里不需要重复安装。
react-scripts@5.0.1 依赖 react@19.0.0。
deduped 表示 react@19.0.0 已经被安装在其他地方，所以这里不需要重复安装。

## 3. 总结
顶层包：
你直接安装的包，包括 @testing-library/react、react-dom、react-scripts 和 react。

依赖包：
这些顶层包所依赖的其他包，例如 @testing-library/react 依赖 react，react-dom 依赖 react，react-scripts 依赖 react。
deduped：
表示某个包已经被安装在其他地方，不需要重复安装。这样可以节省磁盘空间，避免重复文件。

也就是说@testing-library/react@16.2.0依赖react@19.0.0，react-dom@19.0.0依赖 react@19.0.0，react-scripts@5.0.1也依赖react@19.0.0。它 └──符号指向的是依赖。

## 4. 为什么会有 deduped？
因为 react@19.0.0 被多个包依赖（@testing-library/react、react-dom 和 react-scripts），npm 会尝试只安装一次 

react@19.0.0，而不是为每个依赖它的包都安装一次。这样可以节省磁盘空间，提高性能。

## 5. 项目为什么需要版本？
项目需要版本号的原因是为了 追踪和管理项目的不同阶段。版本号可以帮助你和你的团队（或其他开发者）知道项目的当前状态，以及项目的不同版本之间的差异。版本号通常遵循一定的规则，例如 主版本号.次版本号.修订号（如 1.2.3）。

主版本号：当你做了不兼容的 API 修改时，主版本号会增加。

次版本号：当你添加了向下兼容的功能时，次版本号会增加。

修订号：当你做了向下兼容的问题修正时，修订号会增加。

例如：
1.0.0：初始版本。

1.1.0：添加了新功能。

1.1.1：修复了某个问题。

2.0.0：做了不兼容的修改。
