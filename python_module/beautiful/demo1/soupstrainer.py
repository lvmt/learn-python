#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
learn soupstrainer 
解析部分文档，这样比较高效
"""

from  bs4 import  BeautifulSoup 
from  bs4 import SoupStrainer
import requests
from bs4.diagnose import diagnose

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
soup =  BeautifulSoup(html_doc, 'html.parser')

"""自定义 部分文档标签
"""
only_a_tags = SoupStrainer('a')
only_tags_with_id_link2 = SoupStrainer(id = 'link2')
def is_short_string(string):
    return len(string) < 10

onlt_short_strings = SoupStrainer(text = is_short_string)

#print(BeautifulSoup(html_doc, 'html.parser', parse_only=only_a_tags).prettify())               #只输出 a 标签
#print(BeautifulSoup(html_doc, 'html.parser', parse_only=only_tags_with_id_link2).prettify())   #只输出id = link2的内容
print(BeautifulSoup(html_doc, 'html.parser', parse_only=onlt_short_strings).prettify())         #根据定义的函数，输出制定长度的字符串

