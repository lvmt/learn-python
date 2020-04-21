#/usr/bin/python
#-*- coding:utf-8 -*-

import openpyxl
import sys

'''
https://openpyxl.readthedocs.io/en/stable/tutorial.html

https://openpyxl.readthedocs.io/en/latest/performance.html

'''

'''
练习python模块openpyxl的用法，设置单元格的字体，颜色，高亮等

openpyxl 只能打开xlsx，不能打开老式的xls

excel 文件的三个对象：
workbook, sheet, cell
'''

###############################################################################################
from openpyxl import load_workbook  #读取excel文件

# wb = load_workbook(sys.argv[1])

# #print(wb.get_sheet_names())

# a_sheet = wb.get_sheet_by_name("com")
#print(a_sheet.title)
#print(wb.get_active_sheet())

'''获取工作表  
'''
# ws = wb["filename"]  #通过工作表的名称
# ws = wb.get_sheet_by_name("filename")

# #不知道名字的，可以使用index
# sheet_names = wb.get_sheet_names()  #得到workbook的所有名字
# ws = wb.get_sheet_by_name(sheet_names(index))   #迂回的方法
# ws = wb.active

'''获得目前正在活动的表
'''
# wb.get_active_sheet().title


'''获取单元格的内容
'''
#print(a_sheet.cell(row=1,column=1).value)    #获取单元格的内容：cell方法，value方法


'''获取最大行和最大列
'''
# print(a_sheet.max_row)
# print(a_sheet.max_column)

'''获取行和列
a_sheet.rows为生成器，里面是每一行的数据，每一行又由一个tuple包裹
a_sheet.columns类似
'''
#print(a_sheet.columns)
#print(a_sheet.rows)

# for row in a_sheet.rows:
#     for cell in row:
#         print(cell.value)

# for column in a_sheet.columns:
#     for cell in column:
#         print(cell.value) 



'''获取某行的数据，将迭代器转换为list即可：list(a_sheet.rows)[2]
'''
#print(list(a_sheet.rows)[2])

'''使用range函数获取任意表格内的内容，注意range从1开始的，在openpyxl中的表达方式和excel保持一致，从1开始
'''
# for i in range(1,4):
#     for j in range(1,3):
#         print(a_sheet.cell(row=i,column=j).value)


'''根据excel表格的列名，获取单元格内容，下述表示的是列名为A-C，行数为3，很方便；类似于切片操作
'''
# for row_cell in a_sheet["A1":"C3"]:
#     for cell in row_cell:
#         print(cell.value)

'''根据字母获得列号，或者根据列号返回字母， openpyxl.utils
'''
# from openpyxl.utils import get_column_letter, column_index_from_string

# print(get_column_letter(2))  #B
# print(column_index_from_string("D")) #4

'''公式计算： formulae
'''
# ws["A1"] = 'SUM(1,1)'
# ws["A1"] = 'SUM(B1:C1)'

###################################################################################################
'''将数据写入excel表格里面 ，需要导入WorkBook
'''

'''
当一个表格被创建时，他不包含任何cell，
'''

from openpyxl import Workbook

wb = Workbook()   #新建了一个表格，尚未保存
print(wb.get_sheet_names)


ws1 = wb.create_sheet("Data", index=0)  #新建工作表，位置为第2个sheet

ws1.title = "new_data"    #修改sheet的名字，直接赋值即可


'''读取多个单元格
'''
# for row in ws1.iter_rows(min_row = 1, max_col = 3, max_row =2 ):
#     for cell in row:
#         print(cell)


'''复制一个sheet
'''
#target = wb.copy_worksheet(ws1)    #复制一个sheet，复制表格是有限制的，图片和图片无法复制

#del wb["Data"]         #删除工作表
#print(wb.get_sheet_names())

'''写入单元格
'''
# wb["Data"]["A1"] = "good"   #直接赋值
# print(wb.get_sheet_by_name("Data")["A1"].value)
# print(wb["Data"]["A1"].value)
# #写入均值
# wb["Data"]["B9"] = 'AVERAGE(B2:B8)'  #如果读取的时候加上data_only = True，这样返回的就是数字


'''单元格赋值   的三种方式，逐个单元格的方式写
'''
# ws1.cell(row = 2, column = 3).value = 99
# ws1.cell(row = 2, column = 3, value = 99 )
# ws1["C2"] = 4 



'''append函数，可以一次添加多行数据，从第一行的空白处开始写入, 添加一行数据
'''
# row  = [1,2,3,4,5]
# wb["Data"].append(row)
# print(wb["Data"]["E1"].value)

# #添加多行数据
# rows = [
#     ["Number","data1","data2"],
#     [2,40,30],
#     [3,40,25],
#     [4,50,30]
# ]

# for cell in rows:
#     wb["Data"].append(cell)
# #print(wb["Data"].rows)

# #添加多列数据，将上面的数据转置就行：zip()，但是需要注意转置过程中可能会舍弃一部分结果

# zip_rows = zip(*rows)

# for cell in zip_rows:
#     wb["Data"].append(cell)
# wb.save("text.xlsx")                    #保存列表

'''设置单元格格式
'''

from openpyxl.styles import Font, colors, Alignment          #分别设置字体的相关：字体，颜色，对齐
from openpyxl.styles import Color
from openpyxl.styles import PatternFill

'''字体
直接使用cell的font属性即可
'''
# bold_itatic_24_font = Font(name="等线", size = 24, italic=True, color=colors.RED, bold=True)
# wb["Data"]["F10"].font = bold_itatic_24_font
# wb["Data"]["F10"] = "word_style"     #输出的就是带格式的内容

'''设置背景颜色
'''
bg_color = PatternFill(fill_type="solid", fgColor="FF0000")
ws1["A2"].fill = bg_color
ws1["A2"] = "color_style"
wb.save("bg_color.xlsx") 
 
'''对齐方式
直接使用cell属性的alignment,这里指定水平居中或者垂直居中，center，left，right
'''
# wb["Data"]["F10"].alignment = Alignment(horizontal="center", vertical="center")
# wb["Data"]["F10"] = "word_style"

'''设置行高和列宽  ; 好像有点问题
'''
# wb["Data"].row_dimensions[2].hight = 40
# wb["Data"].column_dimensions["C"] = 30
# wb["Data"]["C2"] = "hanghao"

'''合并 和 拆分 单元格
'''
# wb["Data"].merge_cells("B1:G1")  #合并后，只能往左上角写入数据
# wb["Data"]["B1"] = "style"

#wb["Data"].unmerge_cells("A1:C3")


'''更改sheet标签按钮的颜色，默认为白色
'''
ws1.sheet_properties.tabColor = "1072BA"


   

#wb.save("style.xlsx")  #该操作会覆盖已有的文件，且不会出现提示，需要注意


'''作为字节流保存
'''
from tempfile import NamedTemporaryFile
from openpyxl import Workbook

# wb = Workbook()
# with NamedTemporaryFile() as tmp:
#     wb.save(tmp.name)
#     tmp.seek(0)
#     stream = tmp.read()

# wb = load_workbook("100li_HLA_question.xlsx")
# wb.tmplate = True
# wb.save("document_template.xltx")


'''template属性的使用，没搞清楚这个
'''
# wb = load_workbook("100li_HLA_question.xlsx")
# wb.template = True
# wb.save("test.xltx") 

# wb = load_workbook("test.xltx")
# wb.template = False
# wb.save("test.xlsx")

'''在单元格内插入图片
'''

# from PIL import Image
# from openpyxl.drawing.image import Image


# ws1["A1"] ="You should see the three logos below"
# img = Image("logo.png")
# ws1.add_image(img, "A1")
# wb.save("logo.xlsx")


'''隐藏单元格
'''
# ws1.column_dimensions.group("A", "d", hidden = True)
# #ws1.row_dimensions.group(1,10,hidden=True)
# wb.save("hidden.xlsx")