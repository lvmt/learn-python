#!/usr/bin/env python 
#! -*- coding:utf-8 -*-

"""进程 and 线程
"""

import os

print('current id %s begin ' % os.getpid())
pid = os.fork()

if pid == 0:
    print('子进程%s, 父进程%s' % (os.getpid(), os.getpid()))
else:
    print('进程%s, 创建了子进程%s' % (os.getpid(), pid))