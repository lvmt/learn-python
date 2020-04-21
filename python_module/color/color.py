#!/usr/bin/env python
#-*- coding:utf-8 -*-

## 定义打印颜色
class Color(object):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    RED_BOLD = '\033[31;1m'  # 红色粗体字
    GREEN_BOLD = '\033[92;1m'
    BLUD_BOLD = '\033[94;1m'

    
print(Color.RED + "hello World!" + Color.END) 





