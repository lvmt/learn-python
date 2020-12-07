#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''将字符换转换为日期格式.
'''

from datetime import datetime 

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d') # 该方法的时间成本很高，如果存在大量的此种转换,建议自己函数实现.
print(y)


z = datetime.now()
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


