#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''练习装饰器的使用
'''


import time 
from functools import wraps

def tell_time(func):
    
    @wraps(func)
    def do_func(*args,**kwargs):
        print('\033[1;33m运行前时间: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))      
        print(f'\033[1;32m程序名称: {func.__name__}\033[0m')  
        func(*args,**kwargs)
        print(f'\033[1;33m运行后时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\033[0m')

    return do_func


@tell_time
def test():
    for i in range(20):
        time.sleep(1)
        print(i)
        
        
@tell_time
def sum_thing(x):
    aa = 0
    for i in range(x):
        aa += i
        time.sleep(0.2)
    print(aa)
        
# test()

sum_thing(100)