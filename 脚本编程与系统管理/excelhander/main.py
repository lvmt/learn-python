#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/4/22 15:35
# @Email  13554221497@163.com
# @File   main.py


from excel2xls import excel2xls
from xls2excel import xls2excel


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='excel handle toolkit')
    subparser = parser.add_subparsers(title='sub-command')

    # excel2xls 子解析器
    e2x = excel2xls.Excel2xls()
    subparser_excel2xls = subparser.add_parser('excel2xls', help='change excel to xls')
    e2x.parser_excel2xls(subparser_excel2xls)

    # xls2excel 子解析器
    x2e = xls2excel.Xls2Excel()
    subparser_xls2excel = subparser.add_parser('xls2excel', help='combine xls to excel')
    x2e.parser_xls2excel(subparser_xls2excel)


    args = parser.parse_args()
    print(args)
    args.func(**vars(args))

    #
    # excel2xls.hello()

    # # excel2xsl 测试
    # excel2xls2.Excel2xls().start()

    # # 测试 xls2excel
    # xls2excel.Xls2Excel(args).start()
