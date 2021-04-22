#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/21 17:13
# @Email  13554221497@163.com
# @File   执行外部输出.py


# subprocess


import subprocess
out_bytes = subprocess.check_output(['netstat', '-a'])

# 获取文本形式
out_text = out_bytes.decode('utf-8')
