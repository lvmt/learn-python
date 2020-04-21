#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):     ##好像是个默认或者习惯性函数
        urls = [
          'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]  
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 
            
            
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quote-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        

"""
start_requests方法返回 scrapy.Request对象。每收到一个，就实例化一个Response对象，
并调用和request绑定的调回方法（即parse），将response作为参数。
"""

##  scrapy crawl quotes


        