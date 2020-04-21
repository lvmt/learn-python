#!/usr/bin/env python
#-*- coding:utf-8 -*- 

"""在python脚本中，将文件导入到数据库中
"""

from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"   #how to hnow
MONGO_DB = "test"
MONGO_TABLE = "day1"

client = MongoClient(MONGO_URL)   # 生成mongodb对象
db = client[MONGO_DB]


## 定义插入数据的函数
def save_to_mongo(data):
    if db[MONGO_TABLE].insert(data):
        print("成功储存到MongoDB", data)
        return True 
    return False

data = {'name':'mike', 'score':99}
save_to_mongo(data) 