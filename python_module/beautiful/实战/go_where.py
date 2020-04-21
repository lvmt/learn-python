#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from fake_useragent import UserAgent      # 在请求头中伪装浏览器




# 定义请求头
HEADERS = {
    # 通过fake_useragent  组件随机生成浏览器请求头部信息
    'User-Agent': UserAgent().random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-U;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, defate, br',
    'Cookie': '',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}


# 新建写入景点的csv文件，文件的编码格式和书写方式
csvfile = open('去哪儿.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csvfile)
# 写入第一行的表头
writer.writerow(['区域', '名称', '景点ID', '类型', '级别', '热度', '地址', '特色', '经纬度'])

# 定义下载景点内容的函数
def download_page(url):
    try:
        # 请求景点页面， 获取景点信息
        data = requests.get(url, headers=HEADERS, allow_redirects=True).content
        return data
    except:
        pass
    

# 下载页面 如果返回状态不是200，就等待2s以后再下载
def download_soup_waiting(url):
    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=False, timeout=5)
        if response.status_code == 200:
            html = response.content
            html = html.decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        else:
            # 没有返回200， 等待2s，再次下载
            slepp(2)
            print('等待下载中')
            return download_soup_waiting(url)
    except:
        return ""
    
# 定义生成url的函数 （不同的景点类型）
def getTypes():
    types = ['文化古迹', '自然风光', '公园', '古建筑', '寺庙', '遗址', '宗教', '古镇', '故居']
    for type in types:
        url = 'https://piao.qunar.com/ticket/list_热门景点.html?keyword=热门景点&subject=' + type + '&page=1&sku='
        getType(type, url)
        

# 定义html解析函数
def getType(type, url):
    # 下载热点旅游数据为soup对象
    soup = download_soup_waiting(url)
    # 旅游景点对应的列表元素
    search_list = soup.find('div', attrs={'id':'search-list'})
    # 找到所有的旅游景点项目，并且对其进行遍历
    sight_items = search_list.findAll('div', attrs={'class':'sight_item'})
    for sight_item in sight_items:
        name = sight_item['data-sight-name']
        districts = sight_item['data-districts']
        point = sight_item['data-point']
        address = sight_item['data-address']
        data_id = sight_item['data-id']
        level = sight_item.find('span', attrs={'class':'level'})
        if level:
            level = level.text
        else:
            level = ""
        product_star_level = sight_item.find('span', attrs={'class':'product_star_level'}) 
        if product_star_level:
            product_star_level = product_star_level.text 
        else:
            product_star_level = ""
        intro = sight_item.find('div', attrs={'class':'intro'})
        if intro:
            intro = intro['title']
        else:
            intro = ""                   
    writer.writerow(
        [districts.replace("\n",""), name.replace("\n",""), data_id.replace("\n", ""), type.replace("\n", ""),
         level.replace("\n", ""), product_star_level.replace("\n", ""), address.replace("\n", ""), 
         intro.replace("\n", ""), point.replace("\n", "")])
    # 找到下载页的按钮， 如果发现，向下反页， 继续下载重点内容
    
    next = soup.find('a', attrs={'class':'next'})
    if next:
        next_url = "https://piao.qunar.com" + next['href']
        getType(type, next_url)
        

if __name__ == "__main__":
    getTypes()