#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/22 15:36
# @Email  13554221497@163.com
# @File   excel2xls-bak.py


import pandas as pd


class Excel2xls:

    def parser_excel2xls(self, parser):
        parser.add_argument('--excel', help='excel to parse')
        parser.set_defaults(func = self.start)

    def get_excel_reader(self, **kwargs):
        """
        得到excel句柄
        """
        excel_reader = pd.ExcelFile(kwargs['excel'])
        return excel_reader

    def get_target_sheet(self, excel_reader):
        """
        如果只有1个sheet, 直接进行转换
        如果有多个sheet, 进行询问:
            all/空 全部进行转换
            名字: 只转换指定
        """
        sheet_names = excel_reader.sheet_names
        if len(sheet_names) == 1:
            return sheet_names
        else:
            choose = input(
                '{sheet_names}\nwhich sheet you want [all, enter,sheet_names]: \n'.format(
                    **locals()))
            if not choose or choose == 'all':
                return sheet_names
            else:
                choose_name = choose.split(',')
                for name in choose_name:
                    if name not in sheet_names:
                        exit('\033[1;33mwrong name: {name}\033[0m'.format(**locals()))
                return choose_name

    def save_data(self, sheet_names, excel_reader):
        for sheet in sheet_names:
            xls_name = sheet + '.xls'
            df_data = excel_reader.parse(sheet_name=sheet)
            df_data.to_csv(xls_name, sep='\t', index=False)

    def start(self, **args):
        excel_reader = self.get_excel_reader(**args)
        sheet_names = self.get_target_sheet(excel_reader)
        self.save_data(sheet_names, excel_reader)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='a subtool to abstract sheet for big excel.')
    parser.add_argument('excel', help='file contain sheet we need')

    args = parser.parse_args()
    excel = args.excel

    demo = Excel2xls(excel)
    demo.start()
