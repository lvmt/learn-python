#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""最有用的形式是对一个或多个参数指定一个默认值。这样创建的函数，可以用比定义时允许的更少的参数调用
"""

# def ask(prompt, retries=4, reminder='please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0 :
#             raise ValueError('invalid user response')
#         print(reminder)
             
# if __name__ == "__main__":
#     print(ask('dd'))

"""默认值是在 定义过程 中在函数定义处计算的
"""
# i = 5
# def f(args=i):
#     print(args)

# i = 6
# f()
# # 5

"""默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）
时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:
"""
# def f(a, l=[]):
#     l.append(a)
#     return l

# print(f(1))
# print(f(2))
# print(f(3))

# # [1]
# # [1, 2]
# # [1, 2, 3]

"""如果在后续调用之间不想共享默认值,如下所示
"""
# def f(a, l=None):     # 增加默认值选项
#     if l is None:
#         l = []
#     l.append(a)
#     return l

# print(f(1))
# print(f(2))
# print(f(3))

# # [1]
# # [2]
# # [3]
