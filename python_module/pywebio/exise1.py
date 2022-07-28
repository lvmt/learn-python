import pywebio 
from pywebio.input import *
from pywebio.output import * 
from pywebio import pin 
from pywebio import start_server

import pandas as pd  
import os 
from functools import partial
import time 



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
    
    def check_file(filename):
        if not os.path.exists(filename):
            put_text('文件不存在')
            
    
    def xls2excel():
        put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} xls2excel')
        
        if inputs['analysis_type'] == 'xls2excel':
            pd.read_csv(file_name, sep='\t').to_excel(f'{file_name}.xlsx', index=None)


    def excel2xls():
        put_text(f'{time.strftime("%Y-%m-%d %H:%M:%S")} excel2xls')
        if not file_name.endswith('xlsx'):
            put_warning(f'请确认输入文件与转换方式的正确性：\文件名：{file_name} 文件操作：{excel2xls}')
            exit()
        if inputs['analysis_type'] == 'xls2excel':
            put_warning('前后选择的操作类型不一致 analysis type: {inputs["analysis_type"]} comfirm excel2xls')
            exit()
        excel_reader=pd.ExcelFile(file_name)
        sheet_names = excel_reader.sheet_names     
        for _ in sheet_names:
            sheet_data = excel_reader.parse(sheet_name=_)
            sheet_data.to_excel(f'{file_name}.{_}.xlsx', index=None)
                
          
    inputs = input_group(
        '输入的需要内容：',
        [
            file_upload('请选择需要加载的数据', accept=['.xls', '.xlsx', '.csv', '.txt'], max_size='200M', required=True, name='_file'),
            input('请输入<输入文件目录>', required=True, name='path'),
            input('请输入<输出结果目录>', required=True, name='out'),
            select('Which analysis you want?', ['xls2excel', 'excel2xls'], name='analysis_type'),
            actions('actions', [
                                    {'label': 'Submit', 'value': 'submit'},
                                    {'label': 'Submit and next', 'value': 'save_and_continue'},
                                    {'label': 'Reset', 'type': 'reset', 'color': 'warning'},
                                    {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
                                ], name='action', help_text=''),
            
            
        ]
    ) 
    
    file_name = inputs['_file']['filename']
    file_path = inputs['path']
    file_out = inputs['out']
    print(inputs)
    file_name = os.path.join(file_path, file_name)
    print(file_name)
    check_file(file_name)

    
    put_buttons(
        ['xls2excel', 'excel2xls'],
        onclick=[xls2excel, excel2xls]
    )      
    
    





pywebio.start_server(main, port=8084)
    

    
    