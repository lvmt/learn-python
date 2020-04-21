#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""从语义上来说，它们只是正常函数定义的语法糖。
"""
# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# f(0)
# # 42
# f(1)
# # 43
 
 
"""传递一个小函数作为参数
"""
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pairs:pairs[1])
print(pairs) 
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]