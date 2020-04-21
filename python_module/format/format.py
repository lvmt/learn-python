#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
学习format的用法
"""

""" 基本用法 """

# print('{} {}'.format('hello', 'world')) 
# print('{0} {1}'.format('hello', 'world'))
# print('{0} {1} {0}'.format('hello', 'world')) 

# # hello world
# # hello world
# # hello world hello 


""" 关键词定位  """

# print('我的名字是{name}, 我今年{age}岁了'.format(name="小明", age="12")) 
# # 我的名字是小明, 我今年12岁了
# print('{name}说："我的名字是{name}, 我今年{age}岁了"'.format(name="小明", age="12")) 
# # 小明说："我的名字是小明, 我今年12岁了"


""" 可变参数 """

## 传入list

# data = ['hello', 'world']
# print('{0} {1}'.format(*data)) 
# # hello world 

## 传入dict
# data = {'name' : '小明',  'age' : 12}
# print('我的名字是{name}， 我今年{age}岁了'.format(**data))

# #我的名字是小明， 我今年12岁了 


## 混用
# data_1 = ['hello', 'world']
# data_2 = {'name': "小明", 'age': 12}

# print('{0} {1} 我的名字是{name}， 我今年{age}岁了.'.format(*data_1, **data_2)) 

# # hello world 我的名字是小明， 我今年12岁了. 


"""  固定宽度 
当字符串长度少于设定值的时候，默认用空格填充：
"""

# data = [ {"name":"Mary", "collage":"Tsinghua University"},
#         {"name":"Micheal", "collage":"Harvard University"},
#         {"name":"James", "collage":"Massachuasetts Institute of Tecgnology"}]

# ## 固定宽度输出

# for item in data:
#     print('{:10} {:40}'.format(item['name'], item['collage'])) 

# Mary       Tsinghua University
# Micheal    Harvard University
# James      Massachuasetts Institute of Tecgnology 

"""
对齐方式
"""

# data = [{'name': 'Mary', 'college': 'Tsinghua University'},
#         {'name': 'Micheal', 'college': 'Harvard University'},
#         {'name': 'James', 'college': 'Massachusetts Institute of Technology'}]


# print('{:-^50}'.format('居中'))
# for item in data:
#     print('{:^10}{:^40}'.format(item['name'], item['college']))

# print('{:-^50}'.format('左对齐'))
# for item in data:
#     print('{:<10}{:<40}'.format(item['name'], item['college']))

# print('{:-^50}'.format('右对齐'))
# for item in data:
#     print('{:>10}{:>40}'.format(item['name'], item['college'])) 


"""
数字格式化
"""
# # 取小数点后两位
# num = 3.1415926
# print('小数点后两位：{:.2f}'.format(num))

# # 带+/-输出
# num = -3.1415926
# print('带正/负符号：{:+.2f}'.format(num))

# # 转为百分比
# num = 0.34534
# print('百分比：{:.2%}'.format(num))

# # 科学计数法
# num = 12305800000
# print('科学计数法：{:.2e}'.format(num))

# # ,分隔
# num = 12305800000
# print('","分隔：{:,}'.format(num))

# # 转为二进制
# num = 15
# print('二进制：{:b}'.format(num))

# # 十六进制
# num = 15
# print('十六进制：{:x}'.format(num))

# # 八进制
# num = 15
# print('八进制：{:o}'.format(num)) 

# 小数点后两位：3.14
# 带正/负符号：-3.14
# 百分比：34.53%
# 科学计数法：1.23e+10
# ","分隔：12,305,800,000
# 二进制：1111
# 十六进制：f
# 八进制：17 


"""
输出 {} 花括号
"""

# 输出花括号
# print('我是{{{}}}'.format('Awesome_Tang')) 
# # 我是{Awesome_Tang}
  


"""
打印进度条
"""
import time

length = 1000
for i in range(1, length + 1):
    percent = i / length
    bar = '▉' * int(i // (length / 50))
    time.sleep(0.01)
    print('\r进度条：|{:<50}|{:>7.1%}'.format(bar, percent), end='')
print('\n')
