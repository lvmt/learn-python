#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""learn the use of xlwt 
"""

import xlwt
import datetime

"""xlwt 的基本操作
"""

# # constract a workbook and set encoing style
# workbook = xlwt.Workbook(encoding="utf-8")  

# # constract a worksheet
# worksheet = workbook.add_sheet('My Worksheet')

# # write something 
# worksheet.write(1, 0, label = "this is a test")

# # save a book
# workbook.save('excel_test.xls')


"""设置excel 样式 测试
"""

workbook = xlwt.Workbook(encoding="ascii")
worksheet = workbook.add_sheet('test')

# style = xlwt.XFStyle()  #初始化样式
# font = xlwt.Font()      #为样式创建字体

# font.name = "Times New Roman"
# font.bold = True
# font.underline = True
# font.italic = True
# style.font = font   #设定样式

# worksheet.write(0, 0, 'Unformatted value')   #不带样式的写入
# worksheet.write(1, 0, 'Formatted value', style)   #带样式的写入

"""设置单元格 宽度
"""
# worksheet.col(0).width = 3333


"""输入 日期
"""
# style = xlwt.XFStyle() 
# style.num_format_str = 'M/D/YY'
# worksheet.write(2, 2, datetime.datetime.now(), style)

"""向单元格中添加一个公式
"""
# worksheet.write(0, 5, 5) # Outputs 5
# worksheet.write(0, 6, 2) # Outputs 2
# worksheet.write(1, 5, xlwt.Formula('F1*G1')) # Should output "10" (A1[5] * A2[2])
# worksheet.write(1, 6, xlwt.Formula('SUM(F1,G1)')) # Should output "7" (A1[5] + A2[2])

"""向单元格添加一个超链接
"""
#worksheet.write(7, 7, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")')) # Outputs the text "Google" linking to http://www.google.com


"""合并行和列
"""
# worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0's columns 0 through 3.
# font = xlwt.Font() # Create Font
# font.bold = True # Set font to Bold
# style = xlwt.XFStyle() # Create Style
# style.font = font # Add Bold Font to Style
# worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style) # Merges row 1 through 2's columns 0 through 3.   # 前面2个数字，为行数； 后面的2个数字为列数


"""设置单元格的内容的对其方式
"""
# alignment = xlwt.Alignment() # Create Alignment
# alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
# alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
# style = xlwt.XFStyle() # Create Style
# style.alignment = alignment # Add Alignment to Style
# worksheet.col(0).width = 3333
# worksheet.write(0, 0, 'Cell Contents', style)


"""为单元格添加边框
"""
# borders = xlwt.Borders() # Create Borders
# borders.left = xlwt.Borders.DASHED
# borders.right = xlwt.Borders.DASHED
# borders.top = xlwt.Borders.DASHED
# borders.bottom = xlwt.Borders.DASHED
# borders.left_colour = 0x40
# borders.right_colour = 0x40
# borders.top_colour = 0x40
# borders.bottom_colour = 0x40
# style = xlwt.XFStyle() # Create Style
# style.borders = borders # Add Borders to Style
# worksheet.write(0, 0, 'Cell Contents', style)

"""设置单元格 背景颜色
"""
pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style = xlwt.XFStyle() # Create the Pattern
style.pattern = pattern # Add Pattern to Style
worksheet.write(0, 0, 'Cell Contents', style)











workbook.save('format.xls')
