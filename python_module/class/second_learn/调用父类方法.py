#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/14 16:40
# @Email  13554221497@163.com
# @File   调用父类方法.py


"""
参考文档:
https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html
"""

"""
为了调用父类(超类)的一个方法，可以使用 super() 函数，比如：
"""
# class A:
#     def spam(self):
#         print('A.spam')
#
#
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super(B, self).spam()
#
#
# b = B().spam()  # B.spam, A.spam


"""
super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中，比如：
"""

#
# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#
#     # delete attribute lookup to internal obj
#     def __getattr__(self, name):
#         return getattr(self._obj, name)
#
#     def __setattr__(self, name, value):
#         if name.startswith('_'):
#             super(Proxy, self).__setattr__(name, value)
#         else:
#             setattr(self._obj, name, value)
#
#
# c = Proxy('http')
# c.__setattr__('_mike', 'jack')
# print(c.__dict__)


"""

"""

#
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.init__')
#
#
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')
#
#
# c = C()
"""
结果中调用了2次Base.
Base.__init__
A.__init__
Base.__init__
B.init__
C.__init__
"""

#
#
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         super(A, self).__init__()
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         super(B, self).__init__()
#         print('B.init__')
#
#
# class C(A, B):
#     def __init__(self):
#         super(C, self).__init__()
#         print('C.__init__')
#
#
# c = C()
"""
Base.__init__
B.init__
A.__init__
C.__init__
"""

#
# class A:
#     def spam(self):
#         print('A.spam')
#         super(A, self).spam()  # super理解为父类,不如理解为__mro__中, 该类的下一个类.
#
#
# class B:
#     def spam(self):
#         print('B.spam')
#
#
# class D:
#     def spam(self):
#         print('D.spam1')
#
#
# class C(A, D, B):
#     pass
#
#
# c = C()
# c.spam()
# print(C.__mro__)
#
#
# import  logging
#
#
# class LoggingDict(dict):
#     def __setitem__(self, key, value):
#         logging.info('Setting {} to {}'.format(key, value))
#         super(LoggingDict, self).__setitem__(key, value)
#
#
#
# big_dict = LoggingDict()
# big_dict['a'] = 1
# big_dict['b'] = 2
# print(big_dict)