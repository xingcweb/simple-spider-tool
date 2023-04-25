# simple spider tool

在实际工作中，沉淀的一些简易、好用的爬虫工具，减少重复代码与文件冗余，希望一样能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xingcys@gmail.com](mailto:xingc<xingcys@gmail.com>) ）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

## 安装

```shell
pip install simple-spider-tool
```
## 简单使用

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
## 兼容使用
在`0.0.18`对包目录发生改变，由`simple_spider_tools`更改为`simple_spider_tool`，如有使用过低于`0.0.18`版本，请通过安装兼容扩展包以达到兼容使用
```shell
pip install simple-spider-tool[seventeen]
```

## 链接
Github：https://github.com/xingcweb/simple-spider-tool

在线文档：https://simple-spider-tool.xingc.top/