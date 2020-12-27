#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/27 10:08
# @File 简化数据结构初始化.py


"""
你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数
"""


import math


class Structure1:
    # class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # set the arguments:
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


c = Circle('aa')



"""
支持关键字参数
"""


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 设置位置参数
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 设置剩下的关键字参数
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # 检查其他未知参数
        if kwargs:  # 多余的关键字参数.
            raise TypeError('Invalid arguments {}'.format(','.join(kwargs)))


class Stock2(Structure2):
    _fields = ['name', 'shares', 'price']

#
# s1 = Stock2('ACE', 50, 91.1)
# s2 = Stock2('ACE', 50, price=91.1, d=10)
# # s3 = Stock2('ACE', 50, price=91.1, d=10)
# print(s1)
# print(s2.__dict__)


"""
将不再_fields中的名称添加到属性中
"""


class Structure3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('expected {} argument'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


class Stock3(Structure3):
    _fields = ['name', 'shares', 'price']


# s3 = Stock3('ACE', 50, 91)
# s4 = Stock3('ACE', 50, 91, age=27, likes='math')
# s5 = Stock3('ACE', 50, 91, age=27, likes='math', name='mike')

# print(s4.__dict__)

