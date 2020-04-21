#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""也可以使用形如 kwarg=value 的 关键字参数  来调用函数。例如下面的函数:
"""
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
    

# 调用 :
"""接受一个必需的参数（voltage）和三个可选的参数（state, action，和 type）
"""
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

"""无效调用
"""
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

"""函数调用中的问题
1、关键字参数必须跟随在位置参数的后面
2、传递的所有关键字参数必须与函数接受的其中一个参数匹配
3、不能对同一个参数多次赋值。
"""

"""练习
"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch
