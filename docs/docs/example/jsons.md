# json
json相关方法


## `format_json`
生成格式化展开的json字符串 

`参数：`
* **src_json** () 需要格式化字典或者列表对象。`Union[Dict, List]`
* **src_json** () 换行缩进量。`int`

`返回`
* **`str`** 格式化后的文本内容

## `jsonpath`
基于原jsonpath增加功能，可设定默认（None）返回值，供定位不存在时使用 ；
定位成功默认是获取完整匹配结果，可选获取第一个结果

`参数：`
* **src_json** () 解析对象值。`Union[Dict, List]`
* **expr** () jsonpath。`str`
* **default** (, Optional) 未获取到返回默认值。`Any`
* **first** (, Optional) 是否取第一个值，默认为`false`。`bool`

`返回`
* **`Any`** 返回jsonpath匹配值，为匹配结果则返回`default`

## 示例

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

## jsonpath语法