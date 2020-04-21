#!/usr/bin/env python 
#-*- coding:utf-8 -*-

"""学习返回函数，了解函数闭包操作 
""" 

# def calc_sum(*args):
#     ax = 0
#     for i in args:
#         ax += i 
#     return ax    

# print(calc_sum(1, 2, 3)) 
# # 6 

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax += n 
#         return ax 
#     return sum   

# print(lazy_sum(1, 2, 3, 4)) 
# # <function lazy_sum.<locals>.sum at 0x00000186440C3A68> 
# f = lazy_sum(1, 2, 3, 4)
# print(f()) 
# # 10
# # 调用函数f时，才真正计算求和的结果： 

"""
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
""" 
# f1 = lazy_sum(1, 2, 3, 4)
# f2 = lazy_sum(1, 2, 3, 4)
# print(f1 == f2)
# # False 