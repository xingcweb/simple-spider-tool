# decorator
装饰器方法

## `retry`
异常重试装饰器，可捕获指定一个或者多个异常；重试次数

`参数：`
* **num** () 重试次数，默认3次。`int`
* **fail_msg** () 指定错误提示文本。`str`
* **exceptions** () 指定异常，多个异常以元组格式传递。`Union[Exception, Tuple[Exception]]`
* **src_scheme** () 格式化时间格式，默认为`%Y-%m-%d %H:%M:%S`。`str`

`返回：`
* `Any`