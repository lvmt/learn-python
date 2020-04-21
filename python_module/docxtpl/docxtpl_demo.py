#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""RichText
"""

import docxtpl

from docxtpl import DocxTemplate
from docxtpl import RichText

tpl = DocxTemplate("./tmp.docx")

##define

rt = RichText("an example of")
rt.add('a rich text', style="myrichtextstyle")
rt.add('some violet', color="#ff00ff")

context = {
    "example":rt
}

tpl.render(context)
tpl.save('./result.docx') 


"""
某些内容在office中可以显示，在WPS中则无法显示，注意


注意，对于RichText内容，在模板中的变量前面需要写上一个r, {{r <var>}}，注意r与花括号之间不能有空格；
如果没有r，在WPS中，无法显示RichText的内容
"""