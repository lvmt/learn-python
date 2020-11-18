#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
更进一步了解类属性
'''

class Demo(object):

    pass

a = Demo()
a.name = 'mike'
a.age = 12

print(dir(a))
