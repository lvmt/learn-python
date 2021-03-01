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
from functools import wraps


def cal_time(func):
    """
    计算程序运行时间的装饰器
    """
    @wraps(func)
    def do_something(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print('time use', func.__name__, time.time() - start_time, sep=':  ')
    return do_something


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
    # 如何一个文件没有换行符, 大小为5个G, 占用内存会很大.


# 使用read方法分块读取, file.read(chunk_size)
def count_nine_v2(fname):
    """
    经过测试, 该方法虽然降低了内存, 但是运行时间提高.
    """
    count = 0
    block_size = 1024 * 8
    with open(fname) as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            count += chunk.count('9')
    return count


# 对方法2的代码进行解耦合
def chunked_file_reader(fp, block_size=1024 * 8):
    """
    利用生成器函数
    """
    while True:
        chunk = fp.read(block_size)
        if not chunk:
            break
        yield chunk


def count_nine_v3(fname):
    count = 0
    with open(fname) as fp:
        for chunk in chunked_file_reader(fp):
            count += chunk.count('9')
    return count




@cal_time
def Test():
    for i in range(1, 90000):
        count_nine('demo.txt')


@cal_time
def Test_v2():
    for i in range(1, 90000):
        count_nine_v2('demo.txt')


@cal_time
def Test_v3():
    for i in range(1, 90000):
        count_nine_v3('demo.txt')


Test()
Test_v2()
Test_v3()