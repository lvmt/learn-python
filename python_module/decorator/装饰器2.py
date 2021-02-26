#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/18 15:49
# @Email  13554221497@163.com
# @File   装饰器2.py


"""
有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同

装饰器的使用方法很固定

    先定义一个装饰器（帽子）

    再定义你的业务函数或者类（人）

    最后把这装饰器（帽子）扣在这个函数（人）头上
"""


def decorator(func):
    def wrapper(*args, **kw):
        print('\033[1;32mJust a hat.\033[0m')
        return func()
    return wrapper


@decorator
def function():
    print('hello decorator.')


#  普通装饰器
def logger(func):
    def wrapper(*args, **kw):
        print('我准备开始执行: {}函数了:'.format(func.__name__))
        func(*args, **kw)
        print('执行完成')
    return wrapper

@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))


# 带参数的装饰器

def say_hello(country):
    def wrapper(func):
        def deco(*args, **kw):
            if country == 'china':
                print('你好')
            elif country == 'america':
                print('hello')
            else:
                print('guess')
            func(*args, **kw)
        return deco
    return wrapper


@say_hello('china')
def xiaoming():
    pass


@say_hello('america')
def mike():
    pass


# 不带参数的类装饰器
"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__ ：接收被装饰函数
__call__ ：实现装饰逻辑。
"""


class logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[INFO]: the function {func}() is running...'.format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@logger
def say(something):
    print('say {}!'.format(something))



# 带参数的类装饰器
"""
参数和不带参数的类装饰器有很大的不同。
__init__ ：不再接收被装饰函数，而是接收传入参数。
__call__ ：接收被装饰函数，实现装饰逻辑。
"""


class logger:
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('[{level}]: the function {func}() is running...'\
                  .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper


@logger(level='WARNING')
def say(something):
    print('say {}!'.format(something))



# 使用偏函数与类实现装饰器
"""
事实上，Python 对某个对象是否能通过装饰器（ @decorator）形式使用只有一个要求：
decorator 必须是一个“可被调用（callable）的对象。
除函数之外，类也可以是 callable 对象，只要实现了__call__ 函数（上面几个例子已经接触过了）。
"""


import time
import functools


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """
    装饰器： 推迟某个函数的执行
    同时提供 .eager_call 方法立即执行
    """
    return functools.partial(DelayFunc, duration)

@delay(duration=2)
def add(a, b):
    return a+b






if __name__ == '__main__':
    add(4, 6)

