from enum import EnumMeta
from tkinter import Button
import pywebio 
from pywebio.input import *
from pywebio.output import * 
from pywebio import pin 
from pywebio.pin import * 
from pywebio import start_server

import pandas as pd  
import os 
from functools import partial
import time 
from pywebio.session import defer_call, info as session_info, run_async




def main():
    import random 
    
    def edit_row():
        pass  
    
    def t(eng, chinese):
        """return English or Chinese text according to the user's browser language"""
        return chinese if 'zh' in session_info.user_language else eng
            
            
    add_question = [('1 + 2'), ('3 + 4')]
    for i in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        for index, q in enumerate(add_question):
            put_text(f'this is the {index} question')
            put_text(f'问题：{q}') 
            input(f'you_anser_{index}')
            



https://github.com/pywebio/PyWebIO/wiki/%5B%E4%B8%AD%E6%96%87%5D-Why-PyWebIO%3F
https://pythonmana.com/2022/02/202202112321433358.html
https://www.soumao.cc/search?q=pywebio+%E5%88%B6%E4%BD%9C%E7%AD%94%E9%A2%98%E7%B3%BB%E7%BB%9F
pywebio.start_server(main, port=3344)
    

    
    