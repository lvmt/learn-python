#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
学习如何捕获和处理异常
"""

def error1():
    while True:
        try:
            x = int(input('Please enter a number: '))
            break
        except:
            print('Oops! That was no valid number. Try again...')
            


error1()