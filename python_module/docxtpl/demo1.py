#!/usr/bin/python
#-*- coding:utf-8 -*-

"""练习docxtpl模板的使用方法，对于模板上面固定的内容，不需要每次重复输出，
   对比docx，比较简便
"""

from docxtpl import DocxTemplate
from docxtpl import RichText
from docxtpl import InlineImage

doc = DocxTemplate('tpl.docx')

##RichText 文本
rt = RichText('You can add an hyperlink, here to')
rt.add('google', url_id = doc.build_url_id('http://google.com'))


##测试插入图片
picture = InlineImage(doc, 'C:/Users/dell/Desktop/test.png')


##测试loop 循环
confirm = []

dict_tmp1 = {'col1':'NEU1', 'col2':'pos', 'col3':'aachange', 'col4':'acmgtag', 'col5':'GT_prob', 'col6':'disease', 'col7':'pubmid'}
confirm.append(dict_tmp1)

dict_tmp2 = {'col1':'atp7b', 'col2':'pos', 'col3':'aachange', 'col4':'acmgtag', 'col5':'GT_prob', 'col6':'disease', 'col7':'pubmid'}
confirm.append(dict_tmp2)

explain = "this just a comment and they are no use."

context = {'company_name' : 'world company', 'rt':rt, 'confirm' : confirm, 'explain' : explain, 'picture':picture }
doc.render(context)


doc.save('tpl.demo1.docx') 




