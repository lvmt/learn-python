#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re 



## 链接本地mongo数据库
client = client = MongoClient('localhost', 27017)
db = client.spider
collection = db.douban_movie_pandas

class NoResponse(Exception):
    '''Used for waring something is wrong.
    '''

    def __init__(self,response):
        self.response = response

    def __str__(self):
        return '爬虫无返回值'



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

class SpiderDouBanMovie(object):

    def __init__(self, url, params):
        self.url = url
        self.params = params

    @staticmethod
    def get_collection():
        pass
            
    def get_response(self):
        try:
            response = requests.get(self.url, headers=headers,params=params)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except:
            return nan

    def get_soup(self,response):
        try:
            soup = BeautifulSoup(response, 'html.parser')
        except:
            soup = BeautifulSoup(response, 'xml')
        return soup

    def get_all_times(self,soup):
        items = soup.select('div.article div[class="mod"]')
        return items[1:]
    
    def get_detail_content(self,item):
        movie_id = item.select('div.hd')[0].text.strip()

        try:
            movie_title = item.select('div.title')[0].text.strip()
            movie_rating = item.select('div.rating span.rating_nums')[0].text.strip()
            movie_people = item.select('div.rating span')[-1].text.strip()
            movie_people = re.search(r'\d+', movie_people).group(0)
        except:
            movie_title = 'nan'
            movie_rating = 'nan'
            movie_people = 'nan'
        
        try:
            movie_abstract = [i.strip() for i in item.select('div.abstract')[0].text.strip().split('\n')]
            movie_abstract = dict([item.split(':') for item in movie_abstract if item])
            movie_author = movie_abstract.get('导演', 'nan')
            movie_actor = movie_abstract.get('主演', 'nan')
            movie_type = movie_abstract.get('类型', 'nan')
            movie_eare = movie_abstract.get('制片国家/地区', 'nan')
            movie_time = movie_abstract.get('年份', 'nan')
        except:       
            movie_author = 'nan'
            movie_actor = 'nan'
            movie_type = 'nan'
            movie_eare = 'nan'
            movie_time = 'nan'

        content_info = {
            '豆瓣id': movie_id,
            '电影标题': movie_title,
            '电影评分': movie_rating,
            '评价人数': movie_people,
            '导演': movie_author,
            '主演': movie_actor,
            '电影类型': movie_type,
            '制片国家/地区': movie_eare,
            '年份': movie_time
        }

        print(content_info)
        return content_info
    
    def start(self):
        response = self.get_response()
        if not response:
            raise NoResponse(response)
        soup = self.get_soup(response)
        items = self.get_all_times(soup)

        with open('demo.xls', 'a', encoding='utf-8') as fw:
            for item in items:
                content_info = self.get_detail_content(item)
                fw.write('{}\n'.format('\t'.join(content_info.values())))
                collection.insert_one(content_info)


if __name__ == '__main__':

    for i in range(0,200,25):
        print('\033[1;32m开始>>>>\033[0m')
        params = {
            'start': i,
            'sort': 'seq',
            'playable': 0,
            'sub_type': ''
        }

        url = 'https://www.douban.com/doulist/1253915/?'


        mm = SpiderDouBanMovie(url, params)
        mm.start()

        