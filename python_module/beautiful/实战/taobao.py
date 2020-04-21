#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""内容：
1、淘宝搜索接口
2、翻页处理
技术路线：
requests-bs4-re
"""

import requests
from bs4 import BeautifulSoup
import re 

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
    
def parserPage(ilt, html):
    try:
        plt = re.fndall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findal(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            print(price, title)
            ilt.append([price, title])
    except:
        print('')
    
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))
       
    
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parserPage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
if __name__ == "__main__":
    main()
    
    
