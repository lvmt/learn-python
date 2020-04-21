#!/usr/bin/env python 
#-*- coding:utf-8 -*-


"""learn use of pickle
""" 

import pickle


""" 生成pickle 文件
"""
data = {
    'a':[1, 2, 3, 4+6],
    'b':("character string", b"byte string"),
    'c':{None, True, False}
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
       
"""读取 pickle 文件
"""
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    
print(data)

##  {'a': [1, 2, 3, 10], 'b': ('character string', b'byte string'), 'c': {False, True, None}}  


