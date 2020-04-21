#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" test the use of colorama
"""

import colorama

##init 
colorama.init()

print(colorama.Fore.RED + 'this is a red text')
print(colorama.Back.GREEN + 'with a green background')  ## 会在1的基础上改变颜色
print(colorama.Style.DIM + 'and also with a DIM style')

# ##clear all  style
# print(colorama.Style.RESET_ALL)

#定义函数，修改文本颜色 

def add_color(text, color=colorama.Fore.BLUE):
    return '%s %s %s'% (color, text, colorama.Fore.RESET)

print(add_color('just a text', colorama.Fore.YELLOW))  
print(add_color('jsut b test', ))

print(colorama.Style.DIM + 'which this ' )

print(dir(colorama.Style))


