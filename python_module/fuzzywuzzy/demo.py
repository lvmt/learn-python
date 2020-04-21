#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""learn fuzzywuzzy
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

"""ratio  : 从输入文件来看，只能两两比对
"""
# ##simple ration
# score = fuzz.ratio('this is a test', 'this is a test!')
# print(score) 
# #97

# ##partial ratio
# score = fuzz.partial_ratio('this is a test', 'this is a test!')
# print(score)
# #100

# ##token sort ratio
# score1 = fuzz.ratio('fuzzy wuzzy was a bear', 'wuzzy fuzzy was a bear')
# score2 = fuzz.token_sort_ratio('fuzzy wuzzy was a bear', 'wuzzy fuzzy was a bear')
# print(score1, score2)
# #91  100 


# ##taken set ratio
# score1 = fuzz.token_sort_ratio('fuzzy was a bear.', 'fuzzy fuzzy was a bear.')
# score2 = fuzz.token_set_ratio('fuzzy was a bear.', 'fuzzy fuzzy was a bear.')
# print(score1, score2)
# #84  100

#  ## partial_token_sort_ratio
# score1 = fuzz.ratio('Tom and Jerry', 'Jerry and Tom and Ana')
# score2 = fuzz.partial_token_sort_ratio('Tom and Jerry', 'Jerry and Tom and Ana')
# print(score1, score2)
# ## 47 100

"""process : 从输入文件来看， 可能从多个字符串中，选择一个比对的较好的查询结果
"""
#process  
##可以理解为处理数据，作为数据查找的原来
# choices = ['Atlanta Falcons', 'New York Jets', 'New York Giants', 'Dallas Cowboys']
# result =  process.extract('new york jets', choices, limit=3)
# print(result) 
# [('New York Jets', 100), ('New York Giants', 79),('Atlanta Falcons', 29)]
# #结果的返回，是按照分数的高低进行排序的

# choices = ['Atlanta Falcons', 'New York Jets', 'New York Giants', 'Dallas Cowboys']
# result1 = process.extractOne('cowboys', choices)
# print(result1)
# #('Dallas Cowboys', 90)
# #输出匹配结果


## 实战练习

##test1
title_list = [u"数据分析师", u"数据挖掘工程师", u"大数据开发工程师", u"机器学习工程师", 
               u"算法工程师", u"数据库管理", u"商业分析师", u"数据科学家", u"首席数据官",
               u"数据产品经理", u"数据运营", u"大数据架构师"]

score1 = process.extractOne(u"数据挖掘", title_list)
score2 = process.extract(u'数据挖掘', title_list, limit=3)
score3 = process.extractBests(u'数据挖掘', title_list, limit=3)
score4 = ([(fuzz.partial_token_sort_ratio(u'数据挖掘', _), _) for _ in title_list])
print('score1', score1)
print('score2', score2)
print('score3', score3)
print('score4', score4)

"""从上面的测试可以看出，不同的模块使用方式下，各有弊端，应该针对不同的情况，使用不同的模块
"""
