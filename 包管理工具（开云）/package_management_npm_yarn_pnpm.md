# Node.js 是一个 JavaScript 运行时环境，提供服务器端 JavaScript 开发能力。
# npm 是 Node.js 的包管理器，用于管理 JavaScript 项目中的依赖包。
npm --version # npm版本
node --version # node版本
npm --help # 检查 npm 的帮助信息
which npm # 检查npm 的安装路径
npm list # 查看所有包（包括依赖的依赖）
npm list -g --depth=0 # 查看全局安装的包,--depth=0：限制显示的深度为 0，只显示顶层的包，不  
                      # 显示依赖的依赖。
npm list --depth=0 # 查看项目依赖的包