#!/usr/bin/python
#-*- coding:utf-8 -*-

"""learn the use of xlrd
"""
import os
import sys

import xlrd

#open xls

# infile = sys.argv[1]
# data = xlrd.open_workbook(infile)

"""常用语法：获取book中一个工作表
"""
# # 通过索引获取book中的一个sheet
#table = data.sheets[0]  

# # 通过索引获取一个sheet
#  table = data.sheet_by_index(sheet_index) 


# # 通过名字，获取sheet
# table = data.sheet_by_name(sheet_name)

# # 返回book中 所有工作表的名字
# name = data.sheet_names() 

# # 检查某个sheet是否导入完毕
# data.sheet_loaded(sheet_name or index)


"""获取行数 或者 列数
"""
# nrows = table.nrows
# ncols = table.ncols

"""获取整行 或者 整列的数值 （返回列表）
"""
# row_list = table.row_values(i)
# col_list = table.col_values(i)

"""循环 行列表数据
"""
# for i in range(nrows):
#     print(table.row_values(i))
    
"""单元格 操作
"""
# cell_value = table.cell(rowx, colx)
# cell_A1 = table.cell(0,0).value
# cell_C4 = table.cell(3,2).value

"""使用 行列 索引
"""    
# cell_A1 = table.row(0)[0].value
# cell_A2 = table.col(1)[0].value

"""常用的 单元格中的类型
"""
# 0  empty
# 1  string
# 2  number
# 3  date 
# 4  boolean
# 5  error
# 6  blank


"""xls  操作练习
"""

infile =  sys.argv[1]

# open a book
book =  xlrd.open_workbook(infile)

# print sheet names
print(book.sheet_names())

#get needed sheet
sheet1 = book.sheet_by_index(0)
sheet2 = book.sheet_by_name('test_2')

print(sheet1, sheet2)

# get row or col 
nrow = sheet1.nrows
ncol = sheet1.ncols
print(nrow, ncol)
# 4 2

# get content of row or col, return a list
row_list = sheet1.row_values(0)
print(row_list)
# ['a', 'e']
col_list = sheet1.col_values(0)
print(col_list)
# ['a', 'b', 'c', 'd']

# circel the content of xls
for i in range(nrow):
    print(sheet1.row_values(i))
    

# get cell value 
cell_A1 = sheet1.cell(0,0).value
print(cell_A1)
# a

