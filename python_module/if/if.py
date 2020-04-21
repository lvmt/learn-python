#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""if 条件判断

多重if条件判断，一旦符合某个判断条件，就跳出判断
"""

age  =  25


""" demo1 """
if  age > 18:
    print("adult")
elif age > 10 :
    print("teenger")
else:
    print("child")

# ## adult


"""demo2"""

if  age > 10:
    print("teenger")
elif age > 18 :
    print("adult")
else:
    print("child")

## teenger 


"""
说明条件判断中条件的位置很重要
"""