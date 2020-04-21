#!/usr/bin/env python
#-*- coding:utf-8 -*- 

"""学习python urllib的用法
"""


"""web
https://www.jianshu.com/p/87d1e2f875b7 

"""
"""requests: GET
"""
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# # 返回了网页页面

"""request: POST
"""
# import urllib.parse
# import urllib.request

# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding="utf-8")
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())  

"""超时设置
"""
# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read()) 

# import socket
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

"""响应
"""
# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# # <class 'http.client.HTTPResponse'>
# print(response.status)
# # 200
# print(response.getheaders())
# # 头部信息
# print(response.getheader('Server'))
# # nginx 


###############################################################################
"""Get, request 
"""
# from  urllib import request
# with request.urlopen('https://www.uniprot.org/blast/?about=O08709[5-169]&key=Domain') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s ' % (k, v))
#     #print("Data: ", data.decode('utf-8'))  

"""模拟浏览器发送GET请求，Request 对象
"""
# from urllib import request
# req = request.Request('https://www.uniprot.org/blast/?about=O08709[5-169]&key=Domain') 
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') 
# with request.urlopen(req) as f:
#     print('Status: ', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s ' % (k, v))

#     #print('Data: %s' % f.read().decode('utf-8')) 


"""POST 请求， 如果需要发送一个请求，只需要把参数以bytes的形式传入
"""
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
]) 

req = request.Request('https://passport.weibo.cn/sso/login') 
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8')) 

## 登录成功的响应
# Data: {"retcode":20000000,"msg":"","data":{"loginresulturl":"https:\/\/passport.weibo.com。。。