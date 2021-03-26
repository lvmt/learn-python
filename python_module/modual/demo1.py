#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/25 17:24
# @Email  13554221497@163.com
# @File   demo1.py


"""
包的学习
"""

class A:
    def __init__(self):
        self.name = 'mike'

    def pp(self):
        return B(self)


class B:
    def __init__(self, guess):
        self.guess = guess

    def __repr__(self):
        return 'class bbB: {}'.format(self.guess)

a = A()
print(a.pp().guess.name)