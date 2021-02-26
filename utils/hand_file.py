#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/2/26 10:28
# @Email  13554221497@163.com
# @File   hand_file.py


"""
如何流式读取大文件
"""

import time


def cal_time(fun()):



# 标准做法
def count_nine(fname):
    """
    计算文件中含有多少个数字'9'
    """
    count = 0
    with open(fname) as file:
        for line in file:
            count += line.count('9')
    return count



start = time.time()
for i in range(1, 20000):
    count_nine('demo.txt')
print(time.time() - start)
