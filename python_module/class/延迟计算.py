#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/26 18:25
# @File 延迟计算.py


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius



c = Circle(4.0)
print(c.radius)
print(c.area)
print('---------')
print(c.area)
print('--------')
print(c.perimeter)
print('-'*10)
print(c.perimeter)
