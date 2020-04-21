#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""学习在python中操作mongodb数据库
"""

import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
db = client['test']
collections = db['day4'] 
collections.insert({'name':'Jack', 'gender':'male'})

"""插入数据 ：
insert_one
insert_many
""" 

# insert data one
# student = {
#  'id': '20170101',
#  'name': 'Jordan',
#  'age': 20,
#  'gender': 'male'
# }

# result = collections.insert_one(student)  
# print(result) 
# # 通过inserted_id获取_id 
# print(result.inserted_id) 

#   insert data many 
#  对于insert_many()方法，我们可以将数据以 列表 形式传递
# student1 = {
#  'id': '20170101',
#  'name': 'Jordan',
#  'age': 20,
#  'gender': 'male'
# }
 
# student2 = {
#  'id': '20170202',
#  'name': 'Mike',
#  'age': 21,
#  'gender': 'male'
# } 
# result2 = collections.insert_many([student1, student2])
# print(result2.inserted_ids)  


"""查询 
插入数据后，我们可以利用find_one()或find()方法进行查询，其中find_one()查询得到的是单个结果，find()则返回一个生成器对象
""" 

# # find_one
# result1 = collections.find_one({'name':'Mike'})
# print(type(result1))
# print(result1) 
# # {'_id': ObjectId('5dd4e1716afc00083f946b27'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# # 如果查询结果不存在，则会返回None。 


# # 根据ObjectId查询， 使用bson里面的objectid
# from bson.objectid import ObjectId

# result = collections.find_one({'_id':ObjectId('5dd4e1716afc00083f946b27')})
# print(result)  

# # 查询多条数据 find
# results = collections.find({'age':20})
# print(results)
# for result in results:
#     print(result)

# # 查询年龄大于19 
# result = collections.find({'age':{'$gt':19}}) 
# print(result.count())
# # 21

# # 正则匹配查找
# result = collections.find({'name':{'$regex':'^M.*'}})
# for item in result:
#     print(item)

"""计数
count
"""
# count = collections.find().count()
# print(count)
# # 24 

# ## count 符合某个条件的
# count = collections.find({'age':20}).count()
# print(count)
# # 17

"""排序
sort
pymongo.ASCENDING ：升序
pymongo.DESCENDING 降序
"""
# results = collections.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results]) 
# #  ['Jordan', 'Mike'] 


"""偏移
skip 
"""
# results = collections.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
# print([result['name'] for result in results])
# # ['Mike']

"""数据更新
update
update()方法其实也是官方不推荐使用的方法。这里也分为update_one()方法和update_many()方法，
用法更加严格，它们的第二个参数需要使用$类型操作符作为字典的键名
"""
# condition = {'name':'Mike'}
# student = collections.find_one(condition)
# print(student)
# # {'_id': ObjectId('5dd50a43fd279fcc4cf7766a'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# student['age'] = 25
# result = collections.update(condition, student)
# print(result)
# #  {'n': 1, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}
# print(collections.find_one({'name':'Mike'}))
# # {'_id': ObjectId('5dd50a43fd279fcc4cf7766a'), 'id': '20170202', 'name': 'Mike', 'age': 25, 'gender': 'male'}

## 使用$set 更新
# result = collections.update(condition, {'$set':student})
# print(collections.find_one({'name':'Mike'}))
# # {'_id': ObjectId('5dd50a43fd279fcc4cf7766a'), 'id': '20170202', 'name': 'Mike', 'age': 25, 'gender': 'male'}
 
## update_one
# condition = {'age':{'$gt':20}}
# result = collections.update_one(condition, {'$inc':{'age':1}}) 
# print(result.matched_count, result.modified_count)
# # 1 1
# # 这里指定查询条件为年龄大于20，然后更新条件为{'$inc': {'age': 1}}，也就是年龄加1，
# # 执行之后会将第一条符合条件的数据年龄加1。

## update_many() 
##  如果调用update_many()方法，则会将所有符合条件的数据都更新，示例如下：
# condition = {'age': {'$gt':20}} 
# result = collections.update_many(condition, {'$inc':{'age':1}})
# print(result.matched_count, result.modified_count) 
# # 2 2


"""删除
remove
直接调用remove()方法指定删除的条件即可，此时符合条件的所有数据均会被删除
"""

# result = collections.remove({'name':'Mike'})
# print(result) 
# # {'n': 1, 'ok': 1.0} 

"""删除的新方法
delete_one,     delete_many
delete_one()即删除第一条符合条件的数据，delete_many()即删除所有符合条件的数据。
它们的返回结果都是DeleteResult类型，可以调用deleted_count属性获取删除的数据条数。
"""
# result = collections.delete_one({'name':'Jack'})
# print(result)
# # <pymongo.results.DeleteResult object at 0x0000027982E7A948>
# print(result.deleted_count)
# # 1  

# result = collections.delete_many({'age':{"$gt":25}})
# print(result.deleted_count) 
# # 2




