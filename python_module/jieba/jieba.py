#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""jieba  中文分词

精确模式
全模式
搜索引擎模式


"""  
import sys
import jieba  
from wordcloud import WordCloud

seg_list = jieba.cut('我来到北京清华大学') 
print(dir(jieba.jieba))
#print('Full mode: ' + '\t'.join(seg_list)) 
