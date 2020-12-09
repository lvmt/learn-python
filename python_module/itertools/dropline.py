#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import dropwhile


'''丢掉开始的注释行
'''

# with open('aa.txt', 'r') as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):  # 丢掉开始的注释行.
#         print(line)


'''冗余代码
'''
with open('aa.txt', 'r') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    
    while line:
        print(line, end='')
        line = next(f, None)



