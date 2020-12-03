#!/usr/bin/env python 
#-*- coding:utf-8 -*-

'''yaml 操作学习
''' 

import yaml
import pprint
with open('item.yaml', 'r') as fr:
    data = yaml.load(fr, Loader=yaml.FullLoader)
    pprint.pprint(data)