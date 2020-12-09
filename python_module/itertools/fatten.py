#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''展开嵌套序列
'''


from collections import Iterable

# 方法一: yield from
def flatten(items, ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)


# 方法二
def flatten2(items, ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten2(x):
                yield i 
        else:
            yield i


