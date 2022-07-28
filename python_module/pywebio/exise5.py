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
    
    def edit_row():
        pass  
    
    def t(eng, chinese):
        """return English or Chinese text according to the user's browser language"""
        return chinese if 'zh' in session_info.user_language else eng

    
    def check_file(filename):
        if not os.path.exists(filename):
            put_text('文件不存在')
            
            
    def convert_file():        
        # if inputs['analysis_type'] == 'xls2excel' and file_name.endswith(('.xls', '.csv', 'txt')):
        #     put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} xls2excel')
        #     pd.read_csv(file_name, sep='\t').to_excel(f'{file_name}.xlsx', index=None)
            
        # elif inputs['analysis_type'] == 'excel2xls' and file_name.endswith('.xlsx'):
        #     put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} excel2xls')
        #     excel_reader=pd.ExcelFile(file_name)
        #     sheet_names = excel_reader.sheet_names     
        #     for _ in sheet_names:
        #         sheet_data = excel_reader.parse(sheet_name=_)
        #         sheet_data.to_excel(f'{file_name}.{_}.xlsx', index=None)
        # else:
        #     put_warning('<文件类型> 和 <需要转换的格式> 存在差异, 请检查！！！')
        #     exit()
        pass 
       
                
    put_markdown('# 🗃 Manufacturing Data Pre-processing')
    put_text('This demo app only shows file selection function, and it does not upload your file.')
    
    input_file = file_upload('请选择需要加载的数据', accept=['.xls', '.xlsx', '.csv', '.txt'], max_size='200M', required=True)
    
    input_dir = put_input('input_dir', placeholder='输入目录')
    output_dir = put_input('output_dir', placeholder='输出目录')
    select = put_select('select', ['xls2excel', 'excel2xls'])
    actions = put_actions('action', buttons=[
                                                'submit', 'reset'
                                                
                                            ])
   
                                  
    
    put_button('文件转换', onclick=convert_file)


    
    # file_name = inputs['_file']['filename']
    # file_path = r'{path}'.format(**inputs)
    # file_out = inputs['out']
    # print(inputs)
    # file_name = os.path.join(file_path, file_name)
    # file_name = file_name.replace('\\', '/')
    # print(file_name)
    # check_file(file_name)

    # # put_buttons(['文件转换', '文件下载'], onclick=convert_file)

    
    
    





pywebio.start_server(main, port=8081)
    

    
    