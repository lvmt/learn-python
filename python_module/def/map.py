#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""map 接受2个参数， 一个是函数，一个是Iterbale
map将传入的函数依次作用到每个元素，并把结果作为新的iterator返回

map()作为高阶函数，事实上它把运算规则抽象了
""" 

# test1
def f(x):
    return x * x

# r = map(f, [1, 2, 3])
# print(list(r))
# # [1, 4, 9]  

# # test2 
# print(list(map(str, [1, 2, 3, 4])))
# # ['1', '2', '3', '4']  

"""reduce 

reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
""" 
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4) 

# from functools import reduce
# def add(x,y):
#     return x + y 

# print(reduce(add, [1, 2, 3, 4]))
# # 10 

"""filter 函数

filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""

# test1 just odd number
# def is_odd(n):
#     return n % 2 == 1

# print(list(filter(is_odd, [1, 2, 3, 4, 5]))) 
# # [1, 3, 5]  

# # test2 删除空字符串
# def not_empyt(s):
#     return s and s.strip() 

# print(list(filter(not_empyt, ['A', 'B', 'None', 'C', ''])))
# # ['A', 'B', 'None', 'C']  

"""sorted 函数  
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
"""

# # sort by abs
# print(sorted([1, 2, -3, 5, 4, 1], key=abs)) 
# # [1, 1, 2, -3, 4, 5]  

# # test2
# list1 = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(list1)) 
# # ['Credit', 'Zoo', 'about', 'bob']  
# print(sorted(list1, key=str.upper)) 
# # ['about', 'bob', 'Credit', 'Zoo']  

# # 反向排序 
# print(sorted(list1, key=str.upper, reverse=True)) 
# # ['Zoo', 'Credit', 'bob', 'about'] 

#  test 4
# list2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # sort by name  :记住，key后边跟着的是函数
# def sort_by_name(str):
#     name = str[0]
#     return name.upper() 

# def sort_by_score(str):
#     score = str[1]
#     return score 

# print(sorted(list2, key=sort_by_name)) 
# # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
# print(sorted(list2, key=sort_by_score, reverse=True)) 
# # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]