## 🧩 JavaScript 定义函数的方式

### ✅ 1. **函数声明（Function Declaration）**

```js
function sayHello(name) {
  return `Hello, ${name}`;
}
```

- **特性**：
  - **可提升（Hoisting）**：定义可以提前使用
  - 在代码中作为“常规函数”最常见

---

### ✅ 2. **函数表达式（Function Expression）**

```js
const sayHello = function(name) {
  return `Hello, ${name}`;
};
```

- **特性**：
  - 不可提升，定义前使用会报错
  - 可以作为回调函数、立即执行函数等灵活使用

---

### ✅ 3. **箭头函数（Arrow Function）**

```js
const sayHello = (name) => `Hello, ${name}`;
```

- **特性**：
  - 语法简洁，适合单行函数
  - **没有自己的 this、arguments、super、new.target**
  - 无法作为构造函数（不能 `new`）

---

### ✅ 4. **函数构造器（Function Constructor）**

```js
const sayHello = new Function('name', 'return `Hello, ${name}`');
```

- **特性**：
  - 类似 eval，**动态创建函数**
  - 安全性差、不推荐使用
  - 了解原理即可，真实项目中几乎不用

---

### ✅ 5. **立即执行函数（IIFE, Immediately Invoked Function Expression）**

```js
(function(name) {
  console.log(`Hello, ${name}`);
})("Alice");
```

或使用箭头函数：
```js
(() => {
  console.log("Executed immediately");
})();
```

- **特性**：
  - 声明后立即执行
  - 常用于创建“私有作用域”（在模块化出现之前常见）

---

### ✅ 6. **对象中的方法简写（Method Shorthand in Objects）**

```js
const person = {
  sayHello(name) {
    return `Hello, ${name}`;
  }
};
```

- **特性**：
  - 简洁语法，等价于 `sayHello: function(name) {...}`
  - 会绑定 this 到对象（适合对象方法）

---

### ✅ 7. **类方法（Class Method）**

```js
class Greeter {
  sayHello(name) {
    return `Hello, ${name}`;
  }
}
```

- **特性**：
  - 定义在类中，绑定到实例
  - 支持继承、super、构造函数等高级用法

---

## 📌 可选补充（适合高级读者）

| 方式 | 示例 | 特点 |
|------|------|------|
| generator 函数 | `function* gen() { yield 1; }` | 用于生成器，可配合 `for...of` |
| async 函数 | `async function fetchData() {}` | 用于异步处理，返回 Promise |
| async arrow 函数 | `const f = async () => {}` | 语法简洁，适合配合 await |

---

## 🧠 建议你文章结构可以这样写：

1. ✨ 开头引入：为什么 JS 有这么多种定义方式（历史 + 语法演进）
2. 🧩 各种函数定义方式示例 + 优劣对比
3. 🎯 使用建议：什么场景用什么（箭头函数适合 callback，声明函数适合通用工具，类方法适合组件逻辑等）
4. 🚨 附录：提升、this 绑定、作用域的细节比较

---

需要我帮你把这份内容整理成 markdown 格式文章正文结构吗？或者直接帮你写一部分草稿？