#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/26 9:13
# @Email  13554221497@163.com
# @File   spam.py


import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
# 包中包含代码需要去读取的数据文件, 建议使用pkgutil
