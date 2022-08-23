# Json相关

## Api

| 方法名         | 描述                                                                  |
|-------------|---------------------------------------------------------------------|
| format_json | 返回格式化展开的json字符串                                                     |
| jsonpath    | 基于原jsonpath增加功能，可设定默认（None）返回值，供定位不存在时使用 ；定位成功默认是获取完整匹配结果，可选获取第一个结果 |

## 示例
```python
from simple_spider_tools import format_json, jsonpath

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