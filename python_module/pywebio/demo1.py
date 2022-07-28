#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server


import pywebio 
# from pywebio.input import input, FLOAT
# from pywebio.output import put_text



def bmi():
    
    height = input('请输入你的身高(cm): ', type=FLOAT)
    weight = input('请输入你的体重(kg): ', type=FLOAT)
    
    BMI = weight / (height / 100) ** 2
    
    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]
    
    for top, status in top_status:
        if BMI <= top:
            put_text(f'你的 BMI 值: {round(BMI, 2)}, 身体状态{status}')
            break 
            
            
if __name__ == '__main__':
    pywebio.start_server(bmi, port=80)
    # bmi()
    
    
