#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
使用任意数量的参数调用函数。
这些参数会被包含在一个元组里（参见 元组和序列 ）。在可变数量的参数之前，可能会出现零个或多个普通参数
"""

def  write_multiple_item(file, separator, *args):
    file.write(separator.join(args))
    
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep=".")) 
