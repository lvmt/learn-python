#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
python 类的私有变量
"""


## 私有变量使用__下划线开始

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("{}: {}".format(self.__name, self.__score))

    # 改完后，对于外部代码来说，没什么变动，
    # 但是已经无法从外部访问实例变量.__name和实例变量.__score了

    def get_name(self):         ## 定义方法获得名字
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):    # 大费周折，因为可以进行参数检查
        if isinstance(score, int): # 是代码更加健壮
            if 0 <= score <= 100:
                self.__score = score
            else:
                raise ValueError('bad score range(0~100)')
        else:
            raise ValueError('need int number')


