#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""位置参数
"""

# def power(x):
#     return x * x

# def power2(x, n):
#     s = 1
#     while n > 0:
#         n = n -1
#         s = s * x 
#     return s

## x, n 都是位置参数，调用时，传入的2个值，按照顺序依次赋给x, n

"""默认参数
"""
# def power3(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# power3(5)  ,即power3(5, 2)

"""可变参数
"""
# 在函数内部，参数numbers接收到的是一个tuple，
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum

# print(calc(1, 2, 3)) 

""" 如果已经有一个list或者tuple，要调用一个可变参数
"""
# nums = [1, 2, 3]
# print(calc(nums[0], nums[1], nums[2])) 

"""简化版，Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
"""
# nums2 = [1, 2, 3]
# print(calc(*nums2))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


"""关键字参数  这些关键字参数在函数内部自动组装为一个dict
"""
# def person(name, age, **kw):
#     print('name:',name, 'age:',age, 'kw:',kw)

#print(person('Micheal', 30))

# 任意个关键字参数
# print(person('Bob', 35, city='beijing'))
# print(person('Adan', 40, gender='M', job='Engineer'))
# name: Adan age: 40 kw: {'gender': 'M', 'job': 'Engineer'}

"""将字典 传给关键字参数
"""
# extra = {'city':'beijing', 'job':'engineer'}
# print(person('jack', 40, **extra))

"""关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
"""

"""命名 关键字参数

命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
"""

# 限制关键字参数的名字， 可以使用命名关键字参数，例如只接受city和job作为关键字参数

# def person(name, age, *, city, job):
#     print(name, age, city, job) 
    
# # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# print(person('Jack', 24, city='Beijing', job='Engineer')) 

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name,age,*args,city,job):
#     print(name, age, args, city, job)
    
# 命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job) 
    
# print(person('Jack', 24, job='Engineer')) 

"""参数组合
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""
def f1(a,b,c=0,*args,**kw):
    print('a=',1,'b=',b,'c=',c,'args=',args,'kw=',kw)
    
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
    
#print(f1(1, 2))
# a= 1 b= 2 c= 0 args= () kw= {}
# print(f1(1,2,3))
# # a= 1 b= 2 c= 3 args= () kw= {}
# print(f1(1,2,c=3))
# a= 1 b= 2 c= 3 args= () kw= {}
#f2(1, 2, d=99, ext=None)
# a= 1 b= 2 c= 0 d= 99 kw= {'ext': None}

## 通过一个tuple 和 一个dict，调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

f1(*args,**kw)
# a= 1 b= 2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'}


"""参数习惯


Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

"""

