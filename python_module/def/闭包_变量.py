#!/usr/bin/env python
#-*- coding:utf-8 -*-

# def sample():
#     n = 0 
#     # closure funtion
#     def func():
#         print('n=',n)

#     # Accessor methods for n
#     def get_n():
#         return n

#     def set_n(value):
#         nonlocal n
#         n = value

#     # attach as funtion attributes 
#     func.get_n = get_n 
#     func.set_n =  set_n 

#     return func  

# # 上述函数是如何进行工作的 
# '''
# nonlocal声明可以让我们编写函数来修改内部变量的值.
# 函数属性允许我们使用一种很简单的方式,将访问方法绑定到闭包函数上.
# '''

# f = sample()
# f() 
# f.set_n(10)
# f()
# f.get_n()



import sys  

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals 

        # update instance dictonary with calllables  
        self.__dict__.update((key,value) for key,value in locals.items())

    def __len__(self):
        return self.__dict__['__len__']()


# example 
def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)

s.push(10)
s.push(20)
s.push('hello world')
print(len(s)) 

print(s.pop())
print(s.pop())
print(s.pop())


class Stack2:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


# 这个类会比上面的闭包函数运行的慢.

from timeit import timeit

s = Stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
# 0.5931404

s = Stack2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
# 0.6264803

