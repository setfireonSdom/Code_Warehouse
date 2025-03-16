# 安装Ethers.js
这会在 node_modules/ 目录下安装 ethers。
```
npm install ethers
```
package.json 里会添加如下类似代码：
```
"dependencies": {
  "ethers": "^6.0.0"
}
```
如果你想查看 ethers.js 版本：
```
npm list ethers
```
# 极简项目
功能：输入metamask地址，输出speolia eth数目。
```js
const { JsonRpcProvider, formatEther } = require("ethers");

// 使用公共 RPC 或 Infura/Alchemy 替换
const SEPOLIA_RPC_URL = "RPC link";
const provider = new JsonRpcProvider(SEPOLIA_RPC_URL);

/**
 * 查询指定地址的 ETH 余额（单位 ETH）
 * @param {string} address - MetaMask 地址
 * @returns {Promise<string>} - 返回 ETH 余额
 */
async function getSepoliaBalance(address) {
    try {
        if (!address) {
            throw new Error("地址不能为空");
        }

        // 获取余额（单位：Wei）
        const balanceWei = await provider.getBalance(address);

        // 转换为 ETH 并返回
        return formatEther(balanceWei);
    } catch (error) {
        console.error("获取余额失败:", error);
        return "查询失败";
    }
}

// 运行示例：手动输入 MetaMask 地址
const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("请输入 MetaMask 地址: ", async (userAddress) => {
    const balance = await getSepoliaBalance(userAddress);
    console.log(`地址 ${userAddress} 的余额: ${balance} ETH`);
    readline.close();
});
```
输出：
```
地址 0x... 的余额: 0.105452450135871459 ETH
```
上面是要在终端输入地址，可以改成直接写代码里面：
```
// 运行示例2：输入 MetaMask 地址
const testAddress = "0xD1FAB21ff192c9838c1242d155879FBa2dA37810"; // 这里换成你的 MetaMask 地址
getSepoliaBalance(testAddress).then(balance => {
    console.log(`地址 ${testAddress} 的余额: ${balance} ETH`);
});
```

注意ethers.js的版本！上述版本是：6.13.5
