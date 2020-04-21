#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
在实例化开始，给对象赋予方法
"""

# class MyClass(object):
#     i = 12345
    
#     def __init__(self):
#         self.data = [1, 2, 3]
    
#     def f(self):
#         return 'hello, world!'
    
# a = MyClass()
# print(a.data)
# print(a.__dict__)
# print(MyClass.__dict__)


# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index] 
    
# rev = Reverse('span')
# print(type(rev))
# for chr in rev:
#     print(chr)