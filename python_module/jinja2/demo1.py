#!/usr/bin/env python
#-*- coding:utf-8 -*-
import jinja2

"""测试jinja2的使用方法
"""

'''
三种语法
控制结构： {% %}
变量取值： {{}}
注释：     {# #}
'''

##测试1
import jinja2
from jinja2 import PackageLoader, Environment

env = Environment(loader = PackageLoader('result', 'templates'))
template = env.get_template('bast.html')


def write_result(content, out):
    with open(out, 'w') as out:
            out.write(content)
    
    
# content = template.render(name = 'Micheal')
# # print(content)

# content2 = template.render(name = 'Micheal chen', age = 28)
# print(content2)

##测试2： 过滤器
# content3 = template.render(apple = 'apple', orange = 'orange' )
# print(content3) 


##测试3： 条件判断语句

# content4 = template.render(daxin = 'aaa')
# print(content4)

##测试4：for 循环 +  if 条件判断语句
# listall = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listall = [[1, 3, 5], [2, 4, 'a']]
content5 = template.render(list_all = listall)

print(content5)
write_result(content5, 'result.html')

 

