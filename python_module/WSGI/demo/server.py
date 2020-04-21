#!/usr/bin/env python
#-*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from hello import application

#创建一个服务器，
httpd = make_server('', 8001, application)
print('Server HTTP on port 8000...')

# 开始监听HTTP请求
httpd.serve_forever()

