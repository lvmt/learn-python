#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/26 17:23
# @Email  13554221497@163.com
# @File   Timer.py


"""
实现一个计时器
"""


import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')

        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()


    def __exit__(self, *args):
        self.stop()



def countdown(n):
    while n > 0:
        n -= 1



if __name__ == '__main__':
    t = Timer()
    t.start()
    countdown(10000)
    t.stop()
    print(t.elapsed)

