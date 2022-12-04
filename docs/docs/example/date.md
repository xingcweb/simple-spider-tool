# date

时间/日期相关方法

## `format_date`

`datetime`格式化成指定字符串格式

`参数：`
* **obj** () 时间对象。`datetime`
* **scheme** () 字符串格式，默认为`%Y-%m-%d %H:%M:%S`。`str`

`返回：`
* 根据指定格式生成字符串。`str`

## `current_date`
当前时间的对象或者字符串

`参数：`
* **is_fmt** () 是否格式化成字符串， 默认为`True`。`bool`
* **scheme** () 字符串格式，默认为`%Y-%m-%d %H:%M:%S`。`str`

`返回：`
* 时间对象或者字符串。`Union[datetime, str]`


## `date_parse`
文字时间解析成datetime对象，或者格式化成指定格式字符串

`参数：`
* **obj** () 解析对象。`str`
* **src_scheme** () 解析时间格式，默认为`%Y-%m-%d %H:%M:%S`。`str`
* **is_fmt** () 是否格式化成字符串， 默认为`True`。`bool`
* **src_scheme** () 格式化时间格式，默认为`%Y-%m-%d %H:%M:%S`。`str`

`返回：`
* 时间对象或者字符串。`Union[datetime, str]`


## `timestamp`
生成当前时间戳；默认单位为秒，可选毫秒

`参数：`
* **ms** () 生成毫秒时间戳。`bool`

`返回：`
* 时间戳。`int`


## `timestamp_parse`
时间戳解析为datetime对象，默认为格式化标准文本时间格式

`参数：`
* **obj** () 字符串时间戳。`str`
* **is_fmt** () 是否格式化成字符串， 默认为`True`。`bool`
* **src_scheme** () 格式化时间格式，默认为`%Y-%m-%d %H:%M:%S`。`str`

`返回：`
* 时间对象或者字符串。`Union[datetime, str]`