#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''partial应用
'''

from functools import partial  

# # 固定某些值
# def spam(a,b,c,d):
#     print(a,b,c,d) 

# s1 = partial(spam, 1) # a = 1
# s1(2,3,4) # 1,2,3,4 

# # 原本不兼容的代码可以一起工作 
# import math 
# points = [(9,10), (3,4), (5,6), (7,8)]

# def distance(p1,p2):
#     x1, y1 = p1
#     x2, y2 = p2

#     return math.hypot(x2 - x1, y2 - y1)

# pt = (4, 3)
# print(sorted(points, key=partial(distance, pt))) # 固定distance其中的一个参数.


# 一个暂时看不懂的函数
def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

# A sample funtion
def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()

    p = Pool()
    p.apply_async(add, args=(3,4), callback=partial(output_result, log=log))
    p.close()
    p.join()

