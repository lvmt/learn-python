#!/usr/bin/env python3
#-*- coding:utf-8 -*-  
'''
@Author: lvmengting  
@Date: 2020-12-11 14:33:36  
@Last Modified by:   lvmengting  
@Last Modified time: 2020-12-11 14:33:36  
''' 

'''
改变对象的打印或者显示输出,让他们更具有可读性.
类的__repr__方法
'''

# class Pair:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return 'Pair({0.x|r}, {0.y|r})'.format(self)

#     def __str__(self):
#         return '({0.x|s}, {0.y|s})'.format(self)


'''自定义字符串的格式化
'''

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}-{d.day}-{d.year}',
    'dmy': '{d.day}-{d.month}-{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day 

    
    def __format__(self,code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

# example 
d = Date(2012, 12, 21)
print(format(d))

print(format(d, 'mdy'))

print('the date is {:ymd}'.format(d))

print('the date is {:mdy}'.format(d))
    

