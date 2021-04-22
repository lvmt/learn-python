#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/21 17:06
# @Email  13554221497@163.com
# @File   获取终端大小.py

import os
size = os.get_terminal_size()  # 返回类对象
size = size.columns
