#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/1/7 17:31
# @Email  13554221497@163.com
# @File   属性的代理访问.py


"""
你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式。
"""


class A:
    def spam(self, x):
        return x

    def foo(self):
        pass


class B1:
    """简单代理"""

    def __init__(self):
        self._a = A()

    def spam(self, x):
        """delegate to the internal self._a instance"""
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2:
    """使用__getattr__的代理, 代理方法比较多时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # expose all of the methods define on class A
    def __getattr__(self, name):
        """
        这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found
        """
        return getattr(self._a, name)


# b = B2()
# b.bar()
# print(b.spam(12))


""" 属性的代理访问 """


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr: ', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            if isinstance(value, int):  # 可以做类型check.
                super().__setattr__(name, value)
            else:
                raise ValueError('need int type')
        else:
            print('name： ', name)  # x
            print('setattr: ', name, value)
            setattr(self._obj, name, value)

    def __delete__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('deleattr: ', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x, z):
        self.x = x
        self._z = z

    def bar(self, y):
        print('Spam.bar: ', self.x, y)


s = Spam(2, 5)
p = Proxy(s)

# print(p.x)
# p.x = 37

p.z = 'abc'
print(s.z)  # 修改后的值为28
