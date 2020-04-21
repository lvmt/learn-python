#!/usr/bin/python
#-*- coding:utf-8 -*- 

import requests

"""爬虫实战
"""
# def gethtmltext(url, timeout=30):
#     try:
#         head = {'user-agent':'Mozilla/5/0'}       ##修改头部关键字，有的网站会识别头部信息
        
#         r = requests.get(url, headers=head)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         #print(r.request.headers)
#         print(r.text)
#     except:
#         print("爬取失败")

"""爬取京东没有问题
"""
# jd = "https://item.jd.com/100003395445.html"
# print(gethtmltext(jd))


"""爬取亚马逊信息
"""
# ymx = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# print(gethtmltext(ymx))



"""百度、360关键字提交
"""
#百度搜索借口
#http://www.baidu.com/s?wd=keyword  
#360搜索借口
#http://www.so.com/s?q=keyword

# keyword = 'python'
# try:
#     kv = {'wd':keyword}
#     r = requests.get('http://www.baidu.com/s', params=kv)
#     r.raise_for_status()
#     print(r.text)
# except:
#     print('爬取失败')
#     print('fail')

"""网络图片的获取
"""
# import os
# import requests
# url = 'http://image.ngchina.com.cn/2019/0807/20190807062901395.jpg'
# root = 'C:/Users/dell/Desktop/test/'
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print('文件保存成功111')
#     else:
#         print('文件保存失败222')
# except:
#     print('爬取失败333')


"""自动查询IP地址
"""
import requests
url = 'http://m.ip138.com/ip.asp?ip='
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')

