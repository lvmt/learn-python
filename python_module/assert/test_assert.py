#!/usr/bin/python
#-*- coding:utf-8 -*-

"""学习python断言： assert
"""

"""
assert 断言语句和 if 分支有点类似，它用于对一个 bool 表达式进行断言，如果该 bool 表达式为 True，该程序可以继续向下执行；否则程序会引发 AssertionError 错误。
"""


s_age = input("请输入你的年龄：")
age = int(s_age)
assert 20 < age < 80
print("您输入的年龄在20到80之间")
