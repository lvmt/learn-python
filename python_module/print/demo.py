#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""learn the use of print
"""

import time


## demo 1
# num = 20
# for i in range(num):
#     print('#')

## demo 2
# num = 20
# for i in range(num):
#     print('#', end="")

## demo 3
# num = 20
# for i in range(num):
#     print('#', end="", flush=True)   # flush 默认是 False
#     time.sleep(1)
    
## demo 4
days = 365
for i in range(days):
    print('\r', '进度百分比：{0}%'.format(round((i + 1) * 100 / days)), end = "", flush=True)    # \r  转移字符， 可以做大每次都回到开头
    time.sleep(0.02)
    
