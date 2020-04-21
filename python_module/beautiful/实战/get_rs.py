#!/usr/bin/python
#-*- coding:utf-8 -*-

"""获取查询的rs信息
"""

import sys
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import colorama

kw = {'term':sys.argv[1]}

origin_url = 'https://www.ncbi.nlm.nih.gov/snp/?'

r = requests.get(origin_url,  kw)
r.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"

print(r.url)
r.encoding = r.apparent_encoding
html = r.text 
soup =  BeautifulSoup(html, 'html.parser')

##获取需要的标签
name_tag = []
value_tag = []
for i in soup.find('dl', class_ = 'snpsum_dl_left_align'):
    if i.name == 'dt':
        name_tag.append(i)
    elif i.name == 'dd':
        value_tag.append(i)

def add_color(text, color = colorama.Fore.CYAN):
    return '%s%s%s' % (color, text, colorama.Fore.RESET)

##形成输出文档
des_dict = defaultdict()
if len(name_tag) == len(value_tag):
    for index in range(len(name_tag)):
        key = name_tag[index].text
        value = ','.join(value_tag[index].text.split('\n'))
        des_dict[key] =  value

print('rs id is %s :' % (add_color(r.url.split('=')[-1])))
for k,v in des_dict.items():
    print( '{0:<30}{1}'.format(add_color(k, colorama.Fore.YELLOW), add_color(v, colorama.Fore.RED)))

