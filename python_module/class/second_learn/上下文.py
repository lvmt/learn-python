#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/25 16:57
# @Email  13554221497@163.com
# @File   上下文.py


"""
如果要写一个上下文管理器，你需要定义一个类，里面包含一个 __enter__() 和一个 __exit__() 方法
"""


import time


class timethis:
    def __init__(self, label):
        self.label = label


    def add(self):
        return sum(self.label)

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


ll = [1, 2, 3, 4]
with timethis(ll) as fl:
    print('fl', fl)
    print(fl.add())
    print('OK')
