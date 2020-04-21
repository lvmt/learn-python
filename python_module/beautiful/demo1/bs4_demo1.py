#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""爬虫小测试
"""

import requests
from bs4 import BeautifulSoup
from lxml import html
import xml
import xlrd
import xlwt
import os 
from  xlutils.copy import copy 

typeList = ['Gin', 'Run', 'Vodka', 'Tequila', 'Whisky', 'Brandy']
# drinkurl = 'http://www.drink8.cn/forum-Gin-1.html'
# drink = requests.get(drinkurl)
# bdrink = BeautifulSoup(drink.content, 'lxml')

# def changeUrl(typename):
#     index = 'http://www.drink8.cn/'
#     numList =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#     cUrl = []
#     for n in numList:
#         a = index + 'forum-' + typename + '-' + str(n) + '.html'
#         cUrl.append(a)
#     return cUrl

class enterDetail(object):
    
    #参数化url地址
    def changeUrl(typename):
        index = 'http://www.drink8.cn/'
        numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        cUrl = []
        for n in numList:
            a = index + 'forum-' + typename + '-' + str(n) + '.html'
            cUrl.append(a)
        print(cUrl)
        return cUrl
    
    def detailUrl(drinkurl):
        drink = requests.get(drinkurl)
        bdrink = BeautifulSoup(drink.content, 'lxml')
        #判断是否有文件，没有则创建一个表格
        if os.path.exists('indexUrL.xls'):
            openXls = xlrd.open_workbook('indexUrL.xls')
            newXls = copy(openXls)
            newsheet = newXls.get_sheet(0)
            sheet1 = openXls.sheet_by_index(0)   #获取第一张表
            nrows = sheet1.nrows 
        else:
            #创建表格
            newXls = xlwt.Workbook()
            newsheet = newXls.add_sheet('Gin-Url', cell_overwrite_ok=True)

        datasp = bdrink.find_all('h3', class_='xw0')
        a = 0

        for i, j in enumerate(datasp):
            a = a + 1
            print(j.find('a')['href'])
            # 判断变量是否存在，有三种方法：返回True/False
            # 'nrows' in dir()/locals.keys()/vars.keys()
            if 'nrows' in dir():
                newsheet.write(nrows + i, 0, j.find('a')['href'])
            else:
                newsheet.write(i, 0, j.find('a')['href'])

        newXls.save('indexUrL.xls')

            
if __name__ == '__main__':
    enterDetail.changeUrl(typeList[0])

    for l in range(0,len(typeList)):
        for i in enterDetail.changeUrl(typeList[l]):
            enterDetail.detailUrl(i)
    print('ok,生成爬取地址')

    