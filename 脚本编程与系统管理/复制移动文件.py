#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/21 17:39
# @Email  13554221497@163.com
# @File   复制移动文件.py


import shutil

# cp src dst
shutil.copy('a.txt', 'a1.txt')

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2('a.txt', 'a2.txt')

shutil.copytree('src', 'dst')

shutil.move('src', 'dst')

# 如果你想保留被复制目录中的符号链接
shutil.copytree('src', 'dst', symlinks=True)

"""
copytree() 可以让你在复制过程中选择性的忽略某些文件或目录。
你可以提供一个忽略函数，接受一个目录名和文件名列表作为输入，
返回一个忽略的名称列表。例如：
"""


def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('pyc')]


shutil.copytree('src', 'dst', ignore=ignore_pyc_files)

# 内置函数
shutil.copytree('src', 'dst', ignore=shutil.ignore_patterns('*~', '*.pyc'))