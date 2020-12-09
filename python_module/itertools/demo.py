#!/usr/bin/env python 
#-*- coding:utf-8 -*-


with open('aa.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


        