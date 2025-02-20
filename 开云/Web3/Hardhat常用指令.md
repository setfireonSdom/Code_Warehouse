查看hardhat是否安装
```bash
// 检查版本
npx hardhat --version

// 查看本地安装
npm list hardhat

// 全局安装检查
npm list -g hardhat

// 安装hardhat
npm install --save-dev hardhat

// 全局安装
npm install -g hardhat
```
全局安装，全局只有一个 Hardhat 版本，可能导致不同项目对 Hardhat 版本的需求冲突。\
本地安装，每个项目可以独立指定 Hardhat 版本，避免冲突。\

### 1. `npx hardhat init`
   **解释**：这个命令用来初始化一个新的 Hardhat 项目。它会在当前目录创建一个包含配置文件和基础目录结构的 Hardhat 项目。

### 2. `npx hardhat compile`
   **解释**：这个命令用来编译你项目中的 Solidity 智能合约。如果合约有改动或者首次运行，你需要执行这个命令来生成编译后的文件。

### 3. `npx hardhat test`
   **解释**：运行项目中的单元测试。Hardhat 支持 JavaScript 和 TypeScript 编写测试。此命令会执行 `test/` 目录中的所有测试文件，确保智能合约的功能如预期工作。

### 4. `npx hardhat node`
   **解释**：启动一个本地的以太坊节点，常用于开发和测试。你可以将智能合约部署到这个本地节点上，进行调试和测试，避免每次都与实际的以太坊网络交互。

### 5. `npx hardhat run <script>`
   **解释**：执行一个脚本文件。这个命令通常用于部署智能合约或者进行其他的自动化操作。`<script>` 需要是 `scripts/` 目录下的一个文件，比如部署合约的脚本。

### 6. `npx hardhat deploy`
   **解释**：用于部署智能合约。通常通过 `hardhat-deploy` 插件来实现。这个命令将合约部署到你设置的网络（本地或测试网络），并可以自动生成部署的记录。

### 7. `npx hardhat verify --network <network> <contract-address>`
   **解释**：在区块链网络上验证智能合约。这个命令将合约代码与链上的地址匹配，用于验证你已部署的合约的源代码。

### 8. `npx hardhat console`
   **解释**：启动一个交互式的 JavaScript 控制台，允许你通过脚本与部署的智能合约进行交互。这对于调试或测试智能合约的功能非常方便。

### 9. `npx hardhat coverage`
   **解释**：运行代码覆盖率工具，检查你的测试覆盖了多少代码。它会生成一个报告，帮助你识别哪些代码未被测试到。

### 10. `npx hardhat clean`
   **解释**：清理项目中编译产生的文件。通常在你需要重新编译时，可以先运行这个命令来删除旧的编译文件。
