# -*- coding: utf-8 -*-
# @Time : 2022/5/30 22:46
# @Author : xingc
# @File : jsons.py
# @Description : json相关工具
# @Software : PyCharm
import json
from typing import Union, Dict, List, Optional, Any

from jsonpath import jsonpath as super_jsonpath


def format_json(src_json: Union[Dict, List], indent: int = 4) -> str:
    return json.dumps(src_json, ensure_ascii=False, indent=indent)


def jsonpath(src_data: Union[Dict, List], expr: str, default: Optional[Any] = None, first: bool = False):
    """
    jsonpath解析
    :param src_data: 解析对象
    :param expr: jsonpath
    :param default: 未获取到返回默认值， 默认空字符串
    :param first: `True`只返回第一个， `False`返回全部
    :return: 解析值或者 default
    """
    values = super_jsonpath(src_data, expr)
    if values is False:
        return default

    if first is True:
        values = values[0]

    return values
