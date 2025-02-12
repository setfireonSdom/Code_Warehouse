// 定义一个异步函数 main，用于执行部署合约的任务
async function main() {
    // 1. 获取部署者的签名者对象（deployer）
    // ethers.getSigners() 返回一个包含所有可用账户的数组
    // 这里通过解构获取第一个签名者，用于部署合约
    //
    const [deployer] = await ethers.getSigners();
  
    // 2. 打印出用于部署合约的账户地址
    // deployer.address 包含当前签名者（钱包）的地址
    console.log("Deploying contract with account:", deployer.address);
  
    // 3. 获取合约工厂（Contract Factory）
    // ethers.getContractFactory("HelloWorld") 加载 "HelloWorld" 合约的编译结果
    // Contract Factory 是一个可以用来部署新合约的对象
    const HelloWorld = await ethers.getContractFactory("Contract_name");
  
    // 4. 部署合约
    // HelloWorld.deploy() 会发送一笔交易到区块链，部署合约并返回合约实例
    const helloWorld = await HelloWorld.deploy();
  
    // 5. 输出合约部署后的地址
    // ethers.js v6 中，合约地址存储在 .target 属性（v5 中是 .address）
    console.log("HelloWorld deployed to:", helloWorld.target);
  }
  
  // 6. 执行 main 函数，并在执行完成后正常退出
  main()
    .then(() => process.exit(0)) // 成功时，正常退出进程，状态码为 0
    .catch((error) => {
      // 如果 main 函数执行出错，捕获错误信息并打印
      console.error("Error during deployment:", error);
      process.exit(1); // 异常退出进程，状态码为 1
    });
  