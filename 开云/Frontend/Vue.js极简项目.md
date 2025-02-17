这个项目是直接在HTML里面引用一个CDN链接，另一种方式是用`npm install vue`以另一种方式开发，这个方式有点麻烦，不够极简，所以拿最简单的举例。

# 创建一个HTML文件
创建一个index.html文件，在里面输入：<br>
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue 3 Minimal Example</title>
    <!-- 引入 Vue 3 CDN -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body>
    <div id="app">
        <!-- 数据绑定 -->
        <h1>{{ title }}</h1>
        
        <!-- 事件处理 -->
        <button @click="increment">点击次数: {{ count }}</button>
        
        <!-- 双向绑定 -->
        <input v-model="message" placeholder="输入内容">
        <p>输入的内容是: {{ message }}</p>
        
        <!-- 组件使用 -->
        <simple-component></simple-component>
    </div>

    <script>
        // 创建组件
        const SimpleComponent = {
            template: `<div style="color: blue;">这是一个简单组件</div>`
        }

        // 创建 Vue 应用
        const app = Vue.createApp({
            // 数据选项
            data() {
                return {
                    title: "Vue 极简示例",
                    count: 0,
                    message: ''
                }
            },
            // 方法
            methods: {
                increment() {
                    this.count++
                }
            },
            // 注册组件
            components: {
                'simple-component': SimpleComponent
            }
        })

        // 挂载到 DOM
        app.mount('#app')
    </script>
</body>
</html>
```
`<script>`部分创建了一个组件`SimpleComponent`,以及`app`，组件本身也是`app`的一部分。<br>
接下来讲解这个方法Vue.createApp():
* data函数里面的对象的key，代表定义的变量名称，value代表的变量的值，像它那样定义好之后，就可以通过`{{xxx}}`的形式在HTML里面直接使用。<br>
* methods定义的是应用的方法，上述的例子定义了一个计数的函数，每点击一次按钮，count增加1.`@click="increment"`表示点击后，执行`increment`方法。<br>
* components表示定义的组件，从上述例子看，组件是HTML元素。