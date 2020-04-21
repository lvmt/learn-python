#!/usr/bin/env  python 
#-*- coding:utf-8 -*-

import requests
r = requests.get('https://api.github.com/events')    # Response 对象
print(r.status_code)
type(r)
print(r.headers)