#!/usr/bin/python
#-*- coding:utf-8 -*-

"""爬取豆瓣最新电影评分
"""

import requests
from bs4 import BeautifulSoup
import re

def gethtml(url):
    try:
        response = requests.get(url)
        response.raise_for_status
        response.encoding = response.apparent_encoding
        html = response.text
        return html
    except IOError:
        return None
    
def getsoup(html):
    soup = BeautifulSoup(html, 'html.parser')
    items =  soup.find_all('li', class_ = 'list-item')
    listall = []
    for item in items:
        #print(type(item))
        title =  item.attrs['data-title']
        if  'data-score' in item.attrs:
            socre = item.attrs['data-score']
            print('have')
        else:
            print('no score')
            socre = '暂无评分'
        listall.extend([title, socre])
    return listall

def write_to_file(content, out):
    with open(out, 'a', encoding='utf-8') as outdata:
        outdata.write(content)
         
def main():
    url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
    html = gethtml(url)
    allitem = getsoup(html)
    for i in allitem:
        write_to_file(';'.join(i), 'douban.txt')
    print(allitem)

if __name__ == "__main__":
    main()    
