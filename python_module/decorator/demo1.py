#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""学习python装饰器的作用
""" 

"""作用：
修改其他函数的功能的函数 
使代码更加简洁
更pyhonic
"""

"""一切皆对象
"""
# def hi(name="yasoob"):
#     return "hi " + name

# print(hi())
# # hi yasoob
# greet = hi  # 没有使用(), 因为这里并不是调用函数
# print(greet())
# # hi yasoob
# del hi
# # print(hi())
# # # hi is not defined
# print(greet())
# # hi yasoob 

"""在函数中定义函数
"""
# def hi(name="yasoob"):
#     print('now you are inside the hi() function.')

#     def greet():
#         return "now you are in the greet() function."

#     def welcome():
#         return "now you are in the welcome() function."

#     print(greet())
#     print(welcome())
#     print("now you are in the hi() function.")

# print(hi())
# # now you are inside the hi() function.
# # now you are in the greet() function.
# # now you are in the welcome() function.
# # now you are in the hi() function.
# print(greet())
# # NameError: name 'greet' is not defined 

# ## 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# ## 然后greet()和welcome()函数在hi()函数之外是不能访问的 

"""从函数中返回函数
"""
# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function."

#     def welcome():
#         return "now you are in the welcome function."

#     if name == 'yasoob':
#         return greet
#     else:
#         return welcome

# a = hi()
# print(a)
# # <function hi.<locals>.greet at 0x000001E9857EB288>
# # a 指向了hi()函数的greet()函数
# print(a())
# # now you are in the greet() function. 

"""将函数作为参数传给另外一个函数
"""
# def hi():
#     return 'hi yasoob!'

# def doSomethingBeforeHi(func):
#     print('I am doing some boring work before executing hi().')
#     print(func())

# doSomethingBeforeHi(hi)
# # I am doing some boring work before executing hi().
# # hi yasoob! 

"""装饰器让你在一个函数前后去执行代码
"""

"""test 1
"""
# def a_new_decorator(a_func):

#     def wrapTheFunction():
#         print('I am doing some boring work before executing a_func()')

#         a_func()

#         print("I am doing some boring work after executing a_func()")

#     return wrapTheFunction

# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration) 

# print(a_function_requiring_decoration())
# # I am doing some boring work before executing a_func()
# # I am the function which needs some decoration to remove my foul smell
# # I am doing some boring work after executing a_func()

"""使用装饰器
"""
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to remove my foul smell")

# print(a_function_requiring_decoration())
# # I am doing some boring work before executing a_func()
# # I am the function which needs some decoration to remove my foul smell
# # I am doing some boring work after executing a_func() 
# print(a_function_requiring_decoration.__name__)
# # wrapTheFunction 
# # 这并不是我们想要的！Ouput输出应该是"a_function_requiring_decoration"。这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。 

"""对上述实例进行重写：functools.wraps
"""

# from functools import wraps

# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print('I am doing some boring work after exexcuting a_func()')

#     return wrapTheFunction

# @a_new_decorator
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my soul smell")

# print(a_function_requiring_decoration())
# # I am doing some boring work before executing a_func()
# # I am the function which needs some decoration to remove my soul smell
# # I am doing some boring work after exexcuting a_func()
# print(a_function_requiring_decoration.__name__)
# # a_function_requiring_decoration


"""使用蓝本规范
"""
# from functools import wraps
# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#     return decorated 

# @decorator_name
# def func():
#     return('Fucntion is running')

# can_run = True
# print(func())
# # Fucntion is running 

# can_run = False
# print(func())
# Function will not run
# 注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

"""装饰器的运用场景
"""

"""日志文档（logging）
"""
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + ' was called')
        return func(*args, **kwargs)
    return with_logging 

@logit
def add_function(x):
    """Do some math"""
    return x + x 

result = add_function(5)
print(result)
# add_function was called
# 10

