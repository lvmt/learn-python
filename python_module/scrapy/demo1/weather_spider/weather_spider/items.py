# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """对于scrapy, 第一步，必须编写item.py, 明确爬取的对象
    """
    
    """日期 AQI 质量等级 PM2.5 PM10 SO2 CO NO2 O3_8h"""
    
    city = scrapy.Field()
    date = scrapy.Field()
    aqi = scrapy.Field()
    level1 = scrapy.Field()
    pm25 = scrapy.Field()
    pm100 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o3_8h = scrapy.Field()
    
    
