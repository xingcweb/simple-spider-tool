

一些简易、好用的爬虫工具，减少代码与文件冗余，能提升20%~50%的生产效率.

----
**文档地址：** <a href="/" target="_blank">https://127.0.0.1 </a>

**PyPi地址：** <a href="https://pypi.org/project/simple-spider-tool" target="_blank">https://pypi.org/project/simple-spider-tool </a>

**GitHub地址：** [https://github.com/xingcweb/simple-spider-tool](https://github.com/xingcweb/simple-spider-tool)

----
## 安装

<div class="termy">

```console
pip install simple-spider-tool
```

</div>

## 简单使用

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

## 依赖
内置依赖

- `datetime` Python Datetime module supplies classes to work with date and time.
- `hashlib` Secure hash and messag e digest algorithm library.
- `typing` Type Hints for Python.

第三方依赖

- `jsonpath` An XPath for JSON.

_注：依赖顺序排名不分先后_

## 许可证
该项目根据 **MIT** 许可条款获得许可.