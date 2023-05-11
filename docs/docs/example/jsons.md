# json

json相关方法

## format_json

生成格式化展开的json字符串

### 参数

* **src_json** () 需要格式化字典或者列表对象。`Union[Dict, List]`
* **src_json** () 换行缩进量。`int`

### 返回

* **`str`** 格式化后的文本内容

## jsonpath

基于原jsonpath增加功能，可设定默认（None）返回值，供定位不存在时使用 ；
定位成功默认是获取完整匹配结果，可选获取第一个结果

### 参数

* **src_json** () 解析对象值。`Union[Dict, List]`
* **expr** () jsonpath。`str`
* **default** (, Optional) 未获取到返回默认值。`Any`
* **first** (, Optional) 是否取第一个值，默认为`false`。`bool`

### 返回

* **`Any`** 返回jsonpath匹配值，为匹配结果则返回`default`

### 示例

```python
from simple_spider_tool import format_json, jsonpath

data = {
    "code": 200,
    "data": [
        {
            "id": 1,
            "username": "admin",
            "level": "boss"
        },
        {
            "id": 2,
            "username": "user",
            "level": "staff"
        }
    ]
}

boss_name = jsonpath(data, '$.data[?(@.level=="boss")].username', first=True)
all_user_info = jsonpath(data, '$.data[*].username')

print(boss_name)
print(format_json(all_user_info))
```

## 关于jsonpath

### 语法

| 语法     | 描述                                   |
|--------|--------------------------------------|
| `$`    | 根节点                                  |
| `.`    | 当前节点                                 |
| `..`   | 递归，可匹配任何深度的节点                        |
| `*`    | 通配符，可以匹配所有字段                         |
| `@`    | 当前对象，通常在过滤器条件中使用                     |
| `[]`   | 索引运算符，可以选择数组中的特定项或筛选数组中的元素           |
| `[()]` | 表达式运算符，例如`(@.length-1)`用于选择数组的最后一个元素 |
| `[,]`  | 多重索引运算符，例如`[0,2]`用于同时选择数组中的第1和第3个元素  |
| `()`   | 分组运算符                                |
| `?()`  | 表达式过滤器                               |
| `:`    | 切片运算符，可以选择数组的一部分                     |
| `*`    | 匹配任意字符                               |
| `?`    | 匹配单个字符                               |
| `n`    | 匹配任何数字                               |
| `@`    | 匹配当前对象                               |
| `()`   | 用于分组的括号                              |
| `!`    | 非运算符，可以在过滤器条件中使用                     |

### 示例

```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```

以下是一些能够使用全部JSONPath语法的示例：

1. 选择所有图书的价格：

   ```
   $.store.book[*].price
   ```

2. 选择第一个图书的标题和价格：

   ```
   $.store.book[0]['title', 'price']
   ```

3. 使用递归选择所有对象中的颜色属性：

   ```
   $..color
   ```

4. 使用通配符选择所有对象中的字符串值：

   ```
   $..*
   ```

5. 过滤出所有价格大于10的图书信息：

   ```
   $.store.book[?(@.price > 10)]
   ```

6. 使用切片运算符选择前两本书：

   ```
   $.store.book[:2]
   ```

7. 使用条件筛选数组中的元素：

   ```
   $.store.book[?(@.price <= $.store.bicycle.price)]
   ```