#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性 

class Demo(object):

    __slots__ = ('name', 'age', 'score')

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def run(self):
        print('this is a test...')

dd = Demo('bob', 18, 88)
dd.weight = 70  ## 语法错误