#!/usr/bin/env python 
#-*- coding:utf-8 -*-


"""
learn use of json
"""

import json


"""json.dumps  将Python对象编码为json字符串
"""
data = [ {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }]
resultjson = json.dumps(data)
print(resultjson)
print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))  #格式化输出


"""json.loads    解码json数据，返回python字段的数据类型
"""
# jsondata = '{"a" : 1, "b" : 2, "c" : 3, "e" : 4, "d" : 5}'  ##json 格式的数据， 内部必须是双引号
# resulttext = json.loads(jsondata)
# print(resulttext)


