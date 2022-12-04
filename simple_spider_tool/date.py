# -*- coding: utf-8 -*-
# @Time : 2022/5/30 23:22
# @Author : xingc
# @File : date.py
# @Description : 时间相关
# @Software : PyCharm
from typing import Union
from datetime import datetime

FmtDate = Union[datetime, str]
IntFmtDate = Union[datetime, int]
StrInt = Union[str, int]

default_fmt_scheme = '%Y-%m-%d %H:%M:%S'


def format_date(obj: datetime.now, scheme: str = None) -> str:
    if scheme is None:
        scheme = default_fmt_scheme
    return obj.strftime(scheme)


def current_date(is_fmt: bool = True, scheme: str = None) -> FmtDate:
    """当前时间对象，默认为格式化标准文本时间格式"""
    cur_time = datetime.now()
    if is_fmt:
        cur_time = format_date(obj=cur_time, scheme=scheme)

    return cur_time


def date_parse(obj: str, src_scheme: str = default_fmt_scheme, is_fmt: bool = True, scheme: str = None) -> FmtDate:
    """文字时间解析成datetime对象，可选再次格式化"""
    obj_date = datetime.strptime(obj, src_scheme)
    if is_fmt:
        obj_date = format_date(obj=obj_date, scheme=scheme)
    return obj_date


def timestamp(ms: bool = False) -> int:
    """当前时间戳生成，默认秒，可选毫秒"""
    cur_time = current_date(is_fmt=False).timestamp()
    if ms:
        cur_time = cur_time * 1000

    return round(cur_time)


def timestamp_parse(obj: StrInt, is_fmt: bool = True, scheme: str = None) -> IntFmtDate:
    """时间戳解析为datetime对象，默认为格式化标准文本时间格式"""
    if isinstance(obj, str):
        obj = int(obj)

    obj_date = datetime.fromtimestamp(obj)
    if is_fmt:
        obj_date = format_date(obj=obj_date, scheme=scheme)

    return obj_date
