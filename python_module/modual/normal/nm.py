#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/25 17:23
# @Email  13554221497@163.com
# @File   nm.py


def spam():
    pass

def grok():
    pass


def __test__():
    print('test')
    pass


__all__ = ['spam', 'grok', '__test__']   # 可以限定import * 中*的内容

# 如果你将 __all__ 定义成一个空列表, 没有东西将被导入。 如果 __all__ 包含未定义的名字, 在导入时引起AttributeError