#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''学习threading多线程功能
多进程对爬虫脚本进行修改
'''

import time
import requests
import multiprocessing
from multiprocessing import Pool
from bs4 import BeautifulSoup

MAX_WORKER_NUM = multiprocessing.cpu_count()

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
        
        
# 多进程处理过程
# 刚开始测试的时候，p程序没有写在if __name 下面，程序报错 , 

if __name__ == '__main__':
    p = Pool(processes=2) # #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    for url in urls:
        #p.apply_async(job, args=(url,))
        p.apply(job, args=(url,))
    p.close() # #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    p.join()
        

    print('耗时：', time.time() - t1) 
    # 7S




    