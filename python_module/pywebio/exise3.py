from tkinter import Button
import pywebio 
from pywebio.input import *
from pywebio.output import * 
from pywebio import pin 
from pywebio import start_server

import pandas as pd  
import os 
from functools import partial
import time 
from pywebio.session import defer_call, info as session_info, run_async




def xls2excel(file_name):
    put_text('xls2excel')
    if not file_name.endswith(('xls', 'csv', 'txt')):
        exit()
    else:
        pd.read_csv(file_name, sep='\t').to_csv(f'{file_name}.xlsx')
    


def excel2xls(file_name):
    put_text('excel2xls')
    if not file_name.endswith('.xlsx'):
        exit()
    else:
        print('hhhh')








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
        if inputs['analysis_type'] == 'xls2excel' and file_name.endswith(('.xls', '.csv', 'txt')):
            put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} xls2excel')
            data = pd.read_csv(file_name, sep='\t').to_excel(f'{file_name}.xlsx', index=None)
            
        elif inputs['analysis_type'] == 'excel2xls' and file_name.endswith('.xlsx'):
            put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} excel2xls')
            excel_reader=pd.ExcelFile(file_name)
            sheet_names = excel_reader.sheet_names     
            for _ in sheet_names:
                sheet_data = excel_reader.parse(sheet_name=_)
                sheet_data.to_excel(f'{file_name}.{_}.xlsx', index=None)
        else:
            put_warning('<文件类型> 和 <需要转换的格式> 存在差异, 请检查！！！')
            exit()
       
                
    put_markdown('# 🗃 Manufacturing Data Pre-processing')
    put_text('This demo app only shows file selection function, and it does not upload your file.')
    
    inputs = input_group(
        '输入的需要内容：',
        [
            file_upload('请选择需要加载的数据', accept=['.xls', '.xlsx', '.csv', '.txt'], max_size='200M', required=True, name='_file'),
            input('请输入<输入文件目录>', required=True, name='path'),
            input('请输入<输出结果目录>', required=True, name='out'),
            select('Which analysis you want?', ['xls2excel', 'excel2xls'], name='analysis_type'),
            actions('', [
                                    {'label': 'Submit', 'value': 'submit'},
                                    {'label': 'Submit and next', 'value': 'save_and_continue'},
                                    {'label': 'Reset', 'type': 'reset', 'color': 'warning'},
                                    {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
                                ], name='action', help_text=''),
        ]
        
        
        
    ) 
    
    file_name = inputs['_file']['filename']
    file_path = r'{path}'.format(**inputs)
    file_out = inputs['out']
    print(inputs)
    file_name = os.path.join(file_path, file_name)
    file_name = file_name.replace('\\', '/')
    print(file_name)
    check_file(file_name)

    # put_buttons(['文件转换', '文件下载'], onclick=convert_file)

    put_button('文件转换', onclick=convert_file)

    
    





pywebio.start_server(main, port=8087)
    

    
    