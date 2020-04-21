#!/usr/bin/python2
#-*- coding:utf-8 -*- 

from bs4 import BeautifulSoup
import requests
import re

if __name__ == "__main__":
    server = 'http://fund.sciencenet.cn/'
    target = 'http://fund.sciencenet.cn/search?yearStart=2019&filter%5Bsubject%5D%5B0%5D=C&submit=list&page=1'
    req = requests.get(url = target)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    content = soup.find_all('div', class_='resultLst')  #为什么class下面要加个下划线_
    a_content_soup = BeautifulSoup(str(content[0]))
    print(a_content_soup)
    title = a_content_soup.find_all('a')
    span = a_content_soup.find_all('span')
    # for eachs in title:
    #     print(eachs.string)
    #     for each in span:
    #         i = each.children
    #         for child in i:
    #             print(child.string)
            

