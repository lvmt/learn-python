#!/usr/bin/env python
#-*- coding:utf-8 -*- 

"""在python脚本中，登录数据库的方法
"""

from pymongo import MongoClient

# method1
client1 = MongoClient(host="127.0.0.1", port=27017)

# method2
client2 = MongoClient("mongodb://127.0.0.1:27017/")

# choose database
db = client1.test    # test database
# db = client2.test

# choose table
table = db['col9']

# get content
cursort =  table.find()

# print
for doc in cursort:
    print(doc)