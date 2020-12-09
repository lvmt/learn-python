#!/usr/bin/env python3
#-*- conding:utf-8 -*-

'''
你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
''' 

import heapq 
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a,b):
    print(c)


'''合并输出文件.
'''
with open('demo1.txt', 'rt') as file1, open('demo2.txt', 'rt') as file2,\
    open('out.txt', 'wt') as outf:

    for line in heapq.merge(file1,file2):
        outf.write(line)

