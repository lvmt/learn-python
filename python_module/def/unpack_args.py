#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""测试一
"""
list(range(3, 6))
# [3, 4, 5]
args = [3, 6]
list(range(*args))   # range : 内置函数
# [3, 4, 5]

"""字典可以使用**运算符来提供关键字参数
"""
def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d =  {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)