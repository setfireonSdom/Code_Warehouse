# 什么是JavaScript对象？

在JavaScript中，**对象**是一种复合数据类型，它可以**存储**多个**键值对**（key-value pairs）。你可以把对象想象成一个“容器”，里面存放着各种各样的数据，每个数据都有一个唯一的名字（键）。

# 为什么我们需要对象？
1.组织数据<br>
例如，我们可以用一个对象来表示一个“人”，包含姓名、年龄、地址等信息。
2.表示现实世界的实体<br>
例如，一个“汽车”对象可以包含颜色、型号、速度等属性。
3.创建复杂的数据结构
对象可以嵌套，即一个对象可以包含其他对象，从而创建复杂的数据结构。

# 如何创建JavaScript对象？
1.最常用的创建对象的方法。
使用花括号{}来定义对象，键值对之间用逗号,分隔。
```js
let person = {
    name: "张三",
    age: 30,
    city: "北京",
  };
console.log(person);

person.age = 31;
console.log(person);

person.city = "上海";
console.log(person);
```
输出：
```
{ name: '张三', age: 30, city: '北京' }
{ name: '张三', age: 31, city: '北京' }
{ name: '张三', age: 31, city: '上海' }
```
2.构造函数
可以使用new关键字和构造函数来创建对象。
```
function Person(name, age, city) {
    this.name = name;
    this.age = age;
    this.city = city;
  }
  
  let person1 = new Person("李四", 25, "上海");
  let person2 = new Person("张三", 30, "北京");
  let person3 = new Person("王五", 28, "广州");

  console.log(person1);
  console.log(person2);
  console.log(person3);
```
输出：
```
Person { name: '李四', age: 25, city: '上海' }
Person { name: '张三', age: 30, city: '北京' }
Person { name: '王五', age: 28, city: '广州' }
```
this 指的是通过 new 关键字创建的新的对象实例。
当你使用 new Person() 创建对象时：
1. new 关键字会创建一个新的空对象。
2. 这个新对象的 __proto__ 会被设置为 Person.prototype
3. 在函数内部的 this 会被绑定到这个新创建的对象
4. 函数会给 this（也就是新对象）添加属性

在 JavaScript 中，每个对象都有一个隐藏的属性叫做 `__proto__`，它指向另一个对象（通常称为原型）。这个原型对象决定了新对象可以继承哪些属性和方法。
```
function Person(name) {
    this.name = name;
}
// 在 Person.prototype 上加一个方法
Person.prototype.sayHello = function() {
    console.log("Hello, " + this.name);
};

let person1 = new Person("李四");
console.log(person1.__proto__ === Person.prototype); // true
person1.sayHello(); // 输出 "Hello, 李四"
```
这里 `person1.__proto__` 指向 `Person.prototype`，所以 person1 能用 sayHello 方法，尽管它本身没有定义这个方法。

`__proto__`决定了新对象的“出身”，让它能继承 Person.prototype 里的东西。
this 是构造函数用来操作新对象的“代号”，让你给新对象添加属性。

3.Object.create()：

Object.create()方法创建一个新对象，使用现有的对象来提供新创建的对象的`__proto__`（原型）。

# 如何访问对象属性
1. 点表示法：
使用点.来访问对象的属性。
`console.log(person.name);
2. 使用方括号[]来访问对象的属性。
`console.log(person["age"]);`

# 对象中包含方法
```
let person = {
    name: "王五",
    sayHello: function () {
      console.log("你好，我是" + this.name);
    },
  };
  
  person["sayHello"](); // 输出：你好，我是王五
  person.sayHello(); // 输出：你好，我是王五
```
输出：
```
你好，我是王五
你好，我是王五
```