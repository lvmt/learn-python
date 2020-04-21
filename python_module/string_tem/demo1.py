#!/usr/bin/python
#-*- coding:utf-8 -*-

"""学习string 的模板方法
"""

"""
通过将一个string设置为模板， 通过替换变量的方法，最终得到想要的string
"""

##测试1
# from string import Template
# template_string = '$who like2 $what'
# s = Template(template_string)
# d = {'who' : 'tim', 'what' : 'kung pao'}
# print(s.substitute(d))


'''string.Template 默认使用 $ 符号来标识出变量
也可以将$改为其他标识符
'''

##测试二， 修改template的分隔符
from string import Template
class MyTemplate(Template):
    delimiter = '%'

s = MyTemplate('%who knows?')
print(s.substitute(who = 'tim'))


'''
'''
