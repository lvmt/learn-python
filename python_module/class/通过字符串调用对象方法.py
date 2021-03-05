#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/5 17:10
# @Email  13554221497@163.com
# @File   通过字符串调用对象方法.py



## getattr()

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 1)  # Calls p.distance(0, 1)

print(d)


# 方法二
import operator

print(operator.methodcaller('distance', 0, 1)(p))  # methodcaller创建一个可调用对象.



# 实际应用
points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]

points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)