#!/usr/bin/python
#-*- coding:utf-8 -*-

"""练习docx的用法
"""

import docx
from docx import Document
from docx.shared import Inches


#新建文档
document = Document()  ##打开一个空白文档，好像也可以打开一个指定文档
document.add_heading('Document Title', 0)      ##add_heading：添加标题头部信息，

p = document.add_paragraph('A plain paragraph having some')
p.add_run('bold').bold = True                                ##添加True, 更改文字的字体及其颜色等属性
p.add_run(' and some ')
p.add_run('italic').italic = True


document.add_heading('Heading, level 1', level = 1)                 ##level 标题的等级
document.add_paragraph('Intense quote', style = 'Intense Quote')    ##样式 style

document.add_paragraph(
    'first item in unordered list', style = 'List Bullet'           ##列表样式
)
document.add_paragraph(
    'first item in ordered list', style = 'List Number'
)

document.add_picture('C:/Users/dell/Desktop/test1.png', width = Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

new_cell = table.add_row().cells
new_cell[0].text = '第一列'
new_cell[1].text = '第二列'
new_cell[2].text = '第三列'

document.add_page_break()

document.save('demo.docx')

