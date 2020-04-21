#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""用于跳出最近的for或者while循环
"""


"""demo1
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        # else 子句属于for循环

"""当和循环一起使用时，else 子句与 try 语句中的 else 子句的共同点多于 if 语句中的子句: 
try 语句中的 else 子句会在未发生异常时执行，而循环中的 else 子句则会在未发生 break 时执行。
"""