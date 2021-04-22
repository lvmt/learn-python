#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/22 10:07
# @Email  13554221497@163.com
# @File   文本转置.py


"""
将输入的文件进行转置, 便于查看数据内容
"""

import pprint
import fileinput
default_width = 30  # 固定列宽, 每行需要几行，根据最长字符串进行计算.


def get_file_list():
    """
    按照行读取文件, 并进行转置
    """
    file_list = []
    with fileinput.input() as f:
        for line in f:
            linelist = line.strip().split('\t')
            file_list.append(linelist)

    return list(zip(*file_list))


def get_max_size(linelist):
    """
    linelist: 转置后每行列表
    """
    max_size = max(map(len, linelist))
    return max_size


def print_format(file_list):
    """
    格式化输出文件
    """

    print('\033[1;31m-\033[0m' * len(file_list[0]) * default_width)
    for linelist in file_list:
        max_size = get_max_size(linelist)
        if max_size < default_width:
            line = ''.join([item.ljust(default_width) for item in linelist])
            print('\033[1;32m{line}\033[0m'.format(**locals()))
            # print(line)
            print('\033[1;31m-\033[0m' * len(linelist) * default_width)
        else:
            need_line_num = int(max_size / default_width) + 2
            start = 0
            # end = 31
            for i in range(need_line_num):
                end = i * (default_width - 5) + default_width - 5
                line = ''.join([item[start:end].ljust(30) for item in linelist])
                print('\033[1;32m{line}\033[0m'.format(**locals()))
                # print(line)
                start = end
            print('\033[1;31m-\033[0m' * len(linelist) * default_width)


if __name__ == '__main__':

    file_list = get_file_list()
    print_format(file_list)




