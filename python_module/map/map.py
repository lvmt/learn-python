#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""python的map函数
""" 

"""map() 会根据提供的函数对指定序列做映射。
map(function, iterable, ...)
Python 2.x 返回列表。

Python 3.x 返回迭代器。
""" 

# ## demo1
# def square(x):
#     return x ** 2

# result = map(square, [1, 2, 3, 4])
# print(result)
# # <map object at 0x000001E3EABD8308>


## demo2 对上述结果进行简化
# result = map(lambda x: x ** 2, [1, 2, 3, 4]) 
# print(result) 
# # <map object at 0x00000127503B8208>  

## demo3 提供2个列表，对相同位置的列表参数进行相加
result = map(lambda x,y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(result)
# <map object at 0x0000020D77A59448>
print([x for x in result])
# [3, 7, 11, 15, 19] 


