## list 常用方法
#1 .append() 往后加一条数据
rows = []
rows.append(1)
rows.append([1,2,3])
print(rows)
# output: [1, [1, 2, 3]]

#2 .extend(iterable) —— 批量追加
rows = []
rows.extend([2, 3, 4])
print(rows)
# output: [2, 3, 4]

#3 .pop(index=-1) —— 取出并删除(默认从最后一位开始删除)
rows = [0, 1, 2, 3, 4]
rows.pop(0)
print(rows)
# output: [1, 2, 3, 4]

#4 .insert() 往指定位置加一条数据（参数：index, value，在index前面加入value）
rows = []
rows.insert(0, 0)
print(rows)
# output: [0]

#5 .remove() 删除指定数据,按值删除
rows = [0, 1, 2, 3, 4]
rows.remove(0)
print(rows)
# output: [1, 2, 3, 4]

#6 .sort() 排序,原地排序,不返回新列表
list = [2,1,6,3,0,8]

list.sort()
print(list)
# output: [0, 1, 2, 3, 6, 8]

#7 sorted() 排序,不改变原列表,返回新列表
list = [2,1,6,3,0,8]

li = sorted(list)
print(list)
print(li)
# output: [2, 1, 6, 3, 0, 8]
# output: [0, 1, 2, 3, 6, 8]

#8 切片
# 参数：start, end, step，end 不包含，step 步长。
# 不指定start，默认从0开始；不指定end，默认到末尾；不指定step，默认步长为1。
# step为负数时，从后往前取，end不包含，start不包含。
list = [2,1,6,3,0,8,10,124,99,24,29]

print(list[1:3])
print(list[::2])


## dict常用方法
#1 get(key, default=None) —— 安全取值
person = {
    "id": 1001,
    "name": "李四",
    "age": 30,
    "email": "lisi@example.com",
    "address": {
        "city": "上海",
        "street": "南京路 100 号"
    },
    "tags": ["vip", "premium"]
}
print(person.get('id',0))
print(person.get('tags',0))
print(person.get('address',0).get('city',0))
print(person.get('where',0))
# output:1001 ['vip', 'premium'] 上海 0

#2 keys() / values() / items()

#3 update(other_dict) —— 合并字段
base_user = {
    "user_id": 1001,
    "name": "张三",
    "age": 25
}

metrics = {
    "order_cnt_30d": 5,
    "pay_amount_30d": 1280.50
}
base_user.update(metrics)
print(base_user)
"""output:
{
    "user_id": 1001,
    "name": "张三",
    "age": 25,
    "order_cnt_30d": 5,
    "pay_amount_30d": 1280.5
}
"""

