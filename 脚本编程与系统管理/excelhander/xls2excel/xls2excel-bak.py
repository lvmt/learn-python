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

    def __init__(self, args):
        self.excel = args.get('excel')
        self.sheetfiles = args.get('sheetfiles')
        self.sep = args.get('sep')


    def get_df_data(self, sheetname):
        df = pd.read_csv(sheetname, sep=self.sep)
        return df

    def sheet2excel(self):
        excel_writer = pd.ExcelWriter(self.excel)
        for sheetname in self.sheetfiles:
            df = self.get_df_data(sheetname)
            df.to_excel(excel_writer, sheet_name=sheetname, index=False)
        excel_writer.save()
        excel_writer.close()


    def start(self):
        self.sheet2excel()
