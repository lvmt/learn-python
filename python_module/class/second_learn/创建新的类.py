#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/18 17:02
# @Email  13554221497@163.com
# @File   创建新的类.py


"""
如果你想创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功能

一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类，
分别为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。
这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。
"""

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


"""
为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中。
"""


class Point:
    x = Integer('x')  # 这样的话, 可以进行类型检查
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# p = Point(2, 3)
#
# print(p.__dict__)
# print(p.x)
#
# print(Point.__dict__)
# print(Point.x)
# print(Point.y)



# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# class decorator that applies it to selected attributes

def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # attach a Typed descriptor to the class
            print('这个装饰器干啥的哈', kwargs)
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


# example
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('mike', 12, 21.8)
print(s.__dict__)






