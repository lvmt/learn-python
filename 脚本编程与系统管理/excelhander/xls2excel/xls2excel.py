#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/22 16:21
# @Email  13554221497@163.com
# @File   xls2excel.py


"""
既可以将单个xls转换为excel
也可以将多个sheet并入一个excel中
"""


import pandas as pd


class Xls2Excel:

    def parser_xls2excel(self, parser):
        parser.add_argument('--excel', help='output excel name')
        parser.add_argument('--sheetnames', nargs='*', help='sheet which to combine')
        parser.add_argument('--sep', help='seperate')
        parser.set_defaults(func=self.start)

    def get_df_data(self, sheetname, **kwargs):
        df = pd.read_csv(sheetname, sep=kwargs['sep'])
        return df

    def sheet2excel(self, **kwargs):
        excel_writer = pd.ExcelWriter(kwargs['excel'])
        for sheetname in kwargs['sheetnames']:
            df = self.get_df_data(sheetname, **kwargs)
            df.to_excel(excel_writer, sheet_name=sheetname, index=False)
        excel_writer.save()
        excel_writer.close()


    def start(self, **args):
        self.sheet2excel(**args)
