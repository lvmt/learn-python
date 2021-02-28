#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/27 20:50
# @File 属性的代理访问.py


"""
你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式。
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """简单的代理"""
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass

