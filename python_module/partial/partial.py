#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
和装饰器一样，它可以扩展函数的功能，但又不完成等价于装饰器。
通常应用的场景是当我们要频繁调用某个函数时，其中某些参数是已知的固定值，
通常我们可以调用这个函数多次，但这样看上去似乎代码有些冗余，而偏函数的出现就是为了很少的解决这一个问题。
""" 

from functools import partial

## demo1 
def add(*agrs):
    return sum(agrs)

print(add(1, 2, 3) + 100)
print(add(5, 5, 5) + 100)

## demo2
def add2(*args):
    return sum(args) + 100

print(add(1, 2, 3))
print(add(5, 5, 5))

"""  上面2种方法存在的问题
但两种做法都会存在有问题：第一种，100这个固定值会返回出现，代码总感觉有重复；
第二种，就是当我们想要修改 100 这个固定值的时候，我们需要改动 add 这个方法
"""

## 使用偏函数实现
def  add3(*agrs):
    return sum(agrs)

add_100 = partial(add3, 100)  ## 构造新的函数，100，作为函数的固定值
print(add_100(1, 2, 3)) 

add_101 = partial(add3, 101)
print(add_101(1, 2, 3)) 


"""
我们再来看一下偏函数的定义：

类func = functools.partial(func, *args, **keywords)

我们可以看到，partial 一定接受三个参数，从之前的例子，我们也能大概知道这三个参数的作用，简单介绍下：

func: 需要被扩展的函数，返回的函数其实是一个类 func 的函数
*args: 需要被固定的位置参数
**kwargs: 需要被固定的关键字参数
# 如果在原来的函数 func 中关键字不存在，将会扩展，如果存在，则会覆盖


"""
