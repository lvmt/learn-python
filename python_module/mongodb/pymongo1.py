#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
database = client['test']
collection = database['col4']

sort = [('_id', -1)]
cursor = collection.find(sort=sort, limit=100)
try:
    for doc in cursor:
        print(doc)
finally:
    cursor.close()   # 记得关闭