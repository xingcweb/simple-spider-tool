# Hash
加密相关方法


## md5
生成传入字符串的MD5值

### 参数
* **text** () 加密对象。`str`
* **encoding** (, Optional) 编码类型，默认`utf-8`。`str`

### 返回
* md5值`str`

### 示例

```python
from simple_spider_tool import md5

text = 'http://localhost/'
print(md5(text))
```