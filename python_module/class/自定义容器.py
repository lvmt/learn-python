#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/27 20:35
# @File 自定义容器.py


from collections import abc
import bisect


class SortedItems(abc.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 3, 1])
print(list(items))
print(items[0])
items.add(2)
print(list(items))
print(items[1:3])


"""
使用 collections 中的抽象基类可以确保你自定义的容器实现了所有必要的方法。
并且还能简化类型检查。 你的自定义容器会满足大部分类型检查需要，
"""

items = SortedItems()
isinstance(items, abc.Iterable)
isinstance(items, abc.Sequence)
isinstance(items, abc.Container)
isinstance(items, abc.Sized)
