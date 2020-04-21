#!/usr/bin/python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

"""a test
"""

# soup = BeautifulSoup('<p>Hello</p>', 'html.parser')
# print(soup.p.string)



"""一个经典的例子
"""
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())   #可使html以一种优雅的方式展现
#获取元素的方法

##获取标题
# print(soup.title)
# print(soup.title.name)  
# print(soup.title.string)

##获取段落P： 默认是输出第一个
# print(soup.p)
# print(soup.p['class'])
# print(soup.p.string)

##获取a标签
# print(soup.a)
# print(soup.find_all('a'))

##可以理解为字典的价值对查找
# print(soup.find(id="link3"))
# print(soup.find(id="link3").string) 


##从文档中找到所有<a>标签的超链接
# for link in soup.find_all('a'):
#     print(link.get('href'), end = '\t')
#     print(link.string)

##从文档中获取所有的文字内容
# print(soup.get_text())

