#!/usr/bin/python
# -*- coding:utf-8 -*-

"""豆瓣电影评分爬取
"""

import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('sucess')
            return response.text 
        else:
            return None
    except EOFError:
        return None
    
    
def parse_page(html):
    pattern = re.compile('<li.*?list-item.*?data-title=(".*?").*?data-scode=(".*?").*?>.*?<img.*?src=(".*?").*?/>', re.S)
    items =  re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'title' : item[0],
            'score' : item[1],
            'image' : item[2]
        }

def write_to_file(content):
    with open('movie.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content))) 
        f.write(json.dumps(content, ensure_ascii=False))
        
def main():
    url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)
        
if __name__ == "__main__":
    main()
    
