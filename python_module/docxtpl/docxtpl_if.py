#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
测试模板中的if条件判断

""" 
from docxtpl import DocxTemplate
from collections import defaultdict
tpl = DocxTemplate('./scienceReport_template.docx')

is_family = True  ## False  则不会展示 家系样本有关表格

sample_titles = {'sample_name':'mike',
               'name':'mike',
               'relation':'child',
               'sex':'male',
               'symptom':'p'
               }

context = defaultdict()
sample_list = []
sample_list.append(sample_titles)

context['is_family'] = is_family
context['samples_titles'] = sample_list
print(context)

tpl.render(context)
tpl.save('if.docx')