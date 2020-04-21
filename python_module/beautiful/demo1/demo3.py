#!/usr/bin/python
#-*- coding:utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import sys
 

url = "https://www.runoob.com/python/python-reg-expressions.html"
html = requests.get(url)
html.encoding = html.apparent_encoding  ##解决编码问题
html = html.text 

soup = BeautifulSoup(html, 'html.parser')

labels = soup.find_all('a', target = '_top')

f = open('demo3.txt', 'w', encoding = "utf8")
for label in labels:
    title = label.get('title')
    ref =  label.get('href')
    print(title, ref)
    f.write('%s\t%s\n'  % (title, "https://www.runoob.com"+ref))

f.close()


