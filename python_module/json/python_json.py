#/usr/bin/python
#-*- coding:utf-8 -*-

'''用于学习pythonjson的使用
'''

'''
json.dumps    #将python对象编码成json字符串

json.loads    #将已经编码的json字符串解码为python对象
'''

'''json.dumps   语法

json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
'''

# import json

# data = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5} ]

# json = json.dumps(data)

# print(json)


'''json.loads

用于解码json数据，该函数返回python字段的数据类型

json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
'''
# import json

# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

# text = json.loads(jsonData)
# print(text)



'''如何更新Python中的JSON数据
'''






def update_json():
    input_data = {"details": [{"first": [
                             {"id": "111", "flag": "T", "planName": "PP111"},
                             {"id": "123", "flag": "F", "planName": "PP133"},
                             {"id": "133", "flag": "T", "planName": "PP133"}],
             "second": [{"planName": "PPO", "planRank": "3"},
                         {"planName": "HMO", "planRank": "4"},
                         {"planName": "MA", "planRank": "7"}]}]}

    with open('final.json') as f:
        data = json.load(f)

    for x in input_data['details'][0]['first']:
        for y in range(len(data['first'])):
            if x['id'] == data['first'][y]['id']:
                data['first'][y]['planName'] = x['planName']
                data['first'][y]['flag'] = x['flag']

    for j in input_data['details'][0]['second']:
        for k in range(len(data['second'])):
            if j['planName'] == data['second'][k]['planName']:
                data['second'][k]['planRank'] = j['planRank']

    with open(("final.json"), 'w') as file:
        value = json.dumps(data)
        file.write(value)

    return "value"

update_json()



import json
import sys

input_data =  sys.argv[1]
update_date = sys.argv[2]

def update_json():
    with open(input_data, "r") as inf, open(update_date, "r") as inf2:
        indata = json.load(inf)    #输出json字符串
        updata = json.load(inf2)
        