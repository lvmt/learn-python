#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''可以理解为嵌套函数,返回值是内层函数
'''

def add(x):
    def add_2(y):
        return x + y 

    return add_2


print(add(12)(8)) # 这个方法也是奇奇怪怪 


# 测试2 
'''大多数情况下,可以使用闭包函数将单个方法的类转化为函数
'''
from urllib.request import urlopen

class UrlTemplate:
    def __init__(self,template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# example use 
yahoo = UrlTemplate('http://financa.yahoo.com/d/quotes.csv?s={names}&f={fileds}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='slic1v'):
    print(line.decode('utf-8'))

# 上述的类可以被一个更简单的函数替代
def urltemplate(template):
    def open(**kwargs):
        return urlopen(template.format_map(kwargs))
    return open 

# example use  
yahoo2 = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f{fields}')
for line in yahoo2(names='IBM.APPL,FB', fields='slic'):
    print(line.decode('utf-8'))

# 使用一个内部函数或者闭包的方案通常会更优雅一些.

