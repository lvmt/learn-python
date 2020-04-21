#/usr/bin/env python
#-*- coding:utf-8 -*-

"""continue  表示继续循环中的下一次迭代
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found a even number.", num)
        continue
    print('Found a number', num)