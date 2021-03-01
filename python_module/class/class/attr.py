#!/usr/bin/env python 
#-*- coding:utf-8 -*-

""" 
类型判断 
"""

a = [1, 2, 3]
print(isinstance(a, list))  # True

b = (1, 2, 3)
print(isinstance(b, (list, tuple)))  # True  

"""
attr 方法
"""

class Test(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Test()

## 测试是否拥有 属性
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))  # False

## 设置一个属性
setattr(obj, 'y', 19)
print(hasattr(obj, 'y')) # True

## 获取属性
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 'None'))   # None

# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。


"""
用法举例
"""

def readfile(obj):
    f = open(obj, 'r')
    if hasattr(f, 'readline'):
        return f
    return None

print(readfile('README.md'))

class Demo(object):
    count = 1

    def __init__(self, name):
        self.name = name
        Demo.count += 1

dd = Demo('b')
cc = Demo('c')
print(Demo.count)