#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/26 14:42
# @Email  13554221497@163.com
# @File   walk.py


"""
展示os.walk的骚气用法

os.walk可以遍历顶层目录下面的全部目录
"""


import os

def get_all_files(topdir):
    for path, dirs, files in os.walk(topdir):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.exists(fullpath):
                print(fullpath)



