#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""scrpay python 爬虫的简单应用
"""

import scrapy
import requests
from bs4 import BeautifulSoup

class StackOverflowSpider(scrapy.Spider):
    name = "stackOverflow"
    start_url = ["https://stackoverflow.com/questions?sort=votes"]
    
    def parser(self, response):   #clas  的第一个函数，必须是 parser
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback = self.parse_question)
            
    def  parse_question(self, response):
        yield {
            'title' : response.css('h1 a::text').extract()[0],
            'votes' : response.css('.question .vote-count-post::text').extract()[0],
            'body'  : response.css('.question .post-text').extract()[0],
            'tags' : response.css('.queestion .post-tag::text').extract()[0],
            'link' : response.url
        }