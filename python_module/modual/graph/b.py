#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/25 17:37
# @Email  13554221497@163.com
# @File   b.py


from .a import A


class B(A):
    def bar(self):
        print('B.bar')
