# -*- coding: utf-8 -*-
import scrapy
from ..items import WeatherSpiderItem


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    #allowed_domains = ['www.aqistudy.cn/historydata']
    start_urls = ['http://www.aqistudy.cn/historydata/']

    # def parse(self, response):
    #     pass

    def parse(self, response):
        """follow 方法可以自动拼接url， 
        通过meta方法来传递需要保存的city名字， 
        通过callbak方法来调度下一个将爬取的URL
        """

        city_urls = response.xpath('//div[@class="all"]/div[@class="bottom"]//li/a/@href').extract()[16:17]
        city_names = response.xpath('//div[@class="all"]/div[@class="bottom"]//li/a/text()').extract()[16:17]
        self.logger.info('正在爬去{}城市url'.format(city_names[0]))
        for city_url, city_name in zip(city_urls, city_names):
            #  用的follow快捷方式，可以自动拼接url
            yield response.follow(url=city_url, meta={'city': city_name}, callback=self.parse_month)
            
                
    def parse_month(self, response):
        """
        解析月份的url
        :param response:
        :return:
        """
        city_name = response.meta['city']
        self.logger.info('正在爬取{}城市的月份url'.format(city_name[0]))
        # 由于爬取的信息太大了，所有先爬取前5个
        month_urls = response.xpath('//ul[@class="unstyled1"]/li/a/@href').extract()[0]
        for month_url in month_urls:
            yield response.follow(url=month_url, meta={'city': city_name, 'selenium': True}, callback=self.parse_day_data)
        


    def parse_day_data(self, response):
        """
            解析每天的数据
            :param response:
            :return:
            """

        node_list = response.xpath('//tr')
        # 去掉表头
        node_list.pop(0)
        print(response.body)
        print(response.url, 'test test')
        print('开始爬取……')
        print(node_list)
        for node in node_list:
            item = WeatherSpiderItem
            item['city'] = response.meta['city']
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['aqi'] = node.xpath('./td[2]/text()').extract_first()
            item['level'] = node.xpath('./td[3]//text()').extract_first()
            item['pm25'] = node.xpath('./td[4]/text()').extract_first()
            item['pm10'] = node.xpath('./td[5]/text()').extract_first()
            item['so2'] = node.xpath('./td[6]/text()').extract_first()
            item['co'] = node.xpath('./td[7]/text()').extract_first()
            item['no2'] = node.xpath('./td[8]/text()').extract_first()
            item['o3_8h'] = node.xpath('./td[9]/text()').extract_first()
            yield item
            
            
            