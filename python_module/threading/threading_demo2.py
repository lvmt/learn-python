#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''学习threading多线程功能
多线程对爬虫脚本进行修改
'''

import time
import requests
import threading
from bs4 import BeautifulSoup

t1 = time.time()

urls = [
    'http://movie.douban.com/top250?start={}&filter='.format(i) 
    for i in range(0, 226, 25)
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def job(url):
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    
    items = soup.select('div.item')
    print('\033[1;33m{}\033[0m'.format(url))
    for item in items:
        print(item.select('span.title')[0].text)
        
        
# 多线程处理过程
threads = [
    threading.Thread(target=job, args=(url,)) for url in urls
]

for i in threads:
    i.start()
    i.join()
        

print('耗时：', time.time() - t1) 
# 7S




    