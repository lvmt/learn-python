#!/usr/bin/env python 
#-*- coding:utf-8 -*-

"""学习正则表达式的用法， 
"""

import re

"""match
"""
# result = re.match('abc', 'abcdddabc')
# print(result.group())
# # abc
# # match方法返回匹配对象(match object), 否则返回none
# # group方法返回字符串的匹配部分
# # re匹配默认从左向右匹配。如果匹配，就不会继续查找了

"""常见用法
"""
# \d
# print(re.match(r'\d+','123abc').group())    # \d 匹配数字
# 123

# # \D 
# print(re.match(r'\D+','hh123abc').group())    # \D 匹配非数字
# # hh

# # \s 
# print(re.match(r'\s', ' abc dbv').group())   # \s 匹配空格

# \S 匹配非空格

# # \w  
# print(re.match(r'\w', 'abcvd').group())     # \w 匹配单词字符
# # a 

# # .
# print(re.match(r'.', 'abcvd').group())    # . 匹配任意一个字符（除了\n）
# # a 
# print(re.match(r'...', 'abcvd').group())  
# # abc 

# # []
# print(re.match(r'1[0-3]', '137').group())    # [] 匹配[]中列举的字符
# # 13
# print(re.match(r'1[0-3]', '127').group())
# # 12

# ^ 取反

"""多字符匹配
"""
# * 匹配前一个字符出现0次或者无限次，即可有可无
# + 至少1次
# ？ 0 或者 1 次
# {m}  m 次
# {m, } 至少m次
# {m,n} m到n次

# print(re.match(r'\d*', '123456').group())
# # 123456
# print(re.match(r'\d+', '123456').group())
# # 123456
# print(re.match(r'\d?', '123456').group())
# # 1
# print(re.match(r'\d{3}', '123456').group())
# # 123
# print(re.match(r'\d{3,5}', '123456').group())
# # 12345
# print(re.match(r'\d{3,}', '123456').group())
# # 123456

"""边界问题
"""
# ^ 匹配字符串开头
# $ 匹配字符串结尾
# \b 匹配一个单词的边界
# \B 匹配非单词边界

"""匹配分组
"""
# | 匹配左右任意一个表达式
# (ab)  将括号中的字符作为一个分组
# \num  引用分组num匹配到的字符串
# 别名引用

""" |  任意选择
"""
# 匹配0~100间的数字
# print(re.match(r'[1-9]\d?$|0$|100$', '100'))
# # 100
# print(re.match(r'[1-9]\d?$|0$|100$','101'))
# # None

""" () 分组
"""
# print(re.match(r'<h1>(.*)</h1>','<h1>我的CSDN</h1>'))
# # <re.Match object; span=(0, 15), match='<h1>我的CSDN</h1>'> 

""" group 返回match.object对象的内容

group(1):第一个括号内的内容
group(0):匹配的所有内容

groups()函数，返回的是所有括号内的内容
"""
# result = re.match(r'<h1>(.*)</h1>','<h1>我的CSDN</h1>')
# print(result.group(0))
# # <h1>我的CSDN</h1>
# print(result.group(1))
# # 我的CSDN
# print(result.groups())
# # ('我的CSDN',)  

# result = re.match(r'<span>(\d+)</span><h1>(.*)</h1>','<span>1234</span><h1>我的CSDN</h1>')
# print(result.group(1))
# # 1234
# print(result.group(2))
# # 我的CSDN
# print(result.groups())
# # ('1234', '我的CSDN')

""" \num  引用分组
"""
# r'<(.+)><(.+)>.+</\2></\1>'
# 这个\2 和 \1。这个就是我们上面groups()中的内容索引
# 用法，检查html的标签是否是一致的 
# s = '<html><h1>my csdn</h1></h>'          #错误的标签格式
# print(re.match(r'<(.+)><(.+)>.+</\2></\1>', s))
# # None

# s1 = '<html><h1>my csdn</h1></html>'       #正确的标签格式
# result = re.match(r'<(.+)><(.+)>.+</\2></\1>',s1)
# print(result)
# # <re.Match object; span=(0, 29), match='<html><h1>my csdn</h1></html>'>
# print(result.groups())
# # ('html', 'h1') 


"""(?P<name>) 分组起别名 和 (?P=name) 引用别名
"""
# r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>'

# s = '<html><h1>my csdn</h1></h>'    #不正确的格式
# result = re.match(r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>',s)
# print(result)
# # None

# s = '<html><h1>my csdn</h1></html>'  #正确的格式
# result = re.match(r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>', s)
# print(result)
# # <re.Match object; span=(0, 29), match='<html><h1>my csdn</h1></html>'>
# print(result.groups())
# # ('html', 'h1')
# # 记住：(?P<name>)只是起了个别名，系统保存了别名，你不用也没关系，\num还是可以用的。
# print(re.match(r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></\1>',s)) 

"""re 函数
"""
# compile(pattern, flags=0)           # 使用任何可选的标记来编译正则表达式的模式，然后返回一个正则表达式对象
# match(pattern, string, flags=0)     # 尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回匹配对象； 如果失败，就返回 None
# search(pattern, string, flags=0)    # 使用可选标记搜索字符串中第一次出现的正则表达式模式。 如果匹配成功，则返回匹配对象； 如果失败，则返回 None
# findall(pattern, string, flags=0)   # 查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表
# finditer(pattern, string, flags=0)  # 与 findall()函数相同，但返回的不是一个列表，而是一个迭代器。 对于每一次匹配，迭代器都返回一个匹配对象
# split(pattern, string, max=0)       # 根据正则表达式的模式分隔符， split函数将字符串分割为列表，然后返回成功匹配的列表，分隔最多操作 max 次（默认分割所有匹配成功的位置）
# sub(pattern, repl, string, count)   # 使用 repl 替换所有正则表达式的模式在字符串中出现的位置，除非定义 count， 否则就将替换所有出现的位置（ 另见 subn()函数，该函数返回替换操作的数目）
# purge()                             # 清除隐式编译的正则表达式模式 

"""search 和 match 的对比

match的一个特点就是从左向右完整的去匹配，多出来的不管，少了就不行；
search是在给定字符串当中去搜索的符合正则表达式的内容。
match和search的语法都一样，都为re.xxxx(正则表达式，字符串)
"""

"""match 的限制性
"""
# print(re.match(r'\d', '123').group())
# # 1
# print(re.match(r'\d+', '1213d').group())
# # 1213
# print(re.match(r'\d', 'ab12'))
# # None
# ## 表明：match的匹配必须从左开始，如果一开始没有匹配上，就不会匹配上


"""search  用法
"""
# print(re.search(r'\d', 'ab12cd').group())      # match 无法匹配，search则可以
# # 1  

"""match 和 search的共性

都是一次性匹配， 只要匹配到内容，立马结束
"""
# print(re.search(r'\d+', '文章篇幅为123445个字, 共234页').group())
# # 123445

"""re.match与re.search的区别

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
"""
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

# No match!!
# search --> matchObj.group() :  dogs   

"""findall 用法
"""
# print(re.findall(r'\d+', '文章字数1234个字，共12页，有100张地图'))
# # ['1234', '12', '100']

"""替换匹配字符串 sub

思想：先匹配，再替换
"""

# re.sub(pattern, repl, string, count=0, flags=0)
# pattern 模式字符串
# repl replacement 被替换的字符串, repl可以是字符串也可以是函数
# string 

# test1 
# ret = re.sub(r'\d+', '80', 'math=60, English=50')
# print(ret)
# math=80, English=80 

# # test2 定义函数处理复杂情况
# def replace(result):   # 可以理解为匹配的str
#     print('the digit value is:', result.group())
#     r = int(result.group()) + 20
#     return str(r)

# r = re.sub(r'\d+', replace, 'match=60,English=50')
# print(r)
# # match=80,English=70

# # test3, 处理html页面
# str = """
# <html>
# <p>##python开发工程师</p>
# <p><span>+ python爬虫工程师</span></p>
# <p>负责大规模文本、图像等数据的抓取、结构化信息的提取、质量识别等工作。</p>
# <p>1、根据实际任务，进行高校大数据业务开发，满足市场需求；</p>
# <p>2、能独立完成项目开发文档的撰写工作；</p>
# </html>
# """
# # s1 = re.sub(r'<.+>', '', str)    # 贪婪匹配，全都置换了
# # print(s1)
# # # None
# # s2 = re.sub(r'<.+?>', '', str)  # 非贪婪匹配， ?
# # print(s2)
# # # 文字部分
# s3 = re.sub(r'</?\w+/?>', '', str)
# print(s3)
# # 文字部分内容 

"""split  根据匹配，进行切割字符串，并返回列表
"""
# # 以(:,逗号,-）来切割字符串："language:python,php,c,cpp-java" 
# s = "language:python,php,c,cpp-java"
# result = re.split(r':|,|-', s)
# print(result)
# # ['language', 'python', 'php', 'c', 'cpp', 'java'] 

"""贪婪匹配 and  非贪婪匹配

re模块默认是贪婪模式；在量词后面直接加上一个问号？就是非贪婪模式。
"""

"""贪婪匹配  

正则表达式一般趋向于最大长度匹配，总是尝试匹配尽可能多的字符，也就是所谓的贪婪匹配。
"""
# match_str = "abcdefc" 
# pattern = r'ab.*c'
# result = re.match(pattern, match_str)
# print(result)
# # <re.Match object; span=(0, 7), match='abcdefc'>

"""非贪婪匹配

非贪婪匹配就是匹配到结果就好，总是尝试匹配尽可能少的字符。
"""
# match_str = "abcdefc" 
# pattern = r'ab.*?c' 
# result = re.match(pattern, match_str)
# print(result)
# # <re.Match object; span=(0, 3), match='abc'>
 
 
""" compile

思想：先将需要匹配的字符串，写成pattern实例；然后使用pattern实例处理文本并获取匹配结果
一处编译，多处复用

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
re.compile(pattern, flags=0)

参数：

pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释 


"""  

# flags 是匹配模式， 

# pattern = re.compile(r'\w+', re.S)
# print(pattern.flags)
# # 48

# pattern = re.compile(r'\w+', re.DOTALL)
# print(pattern.flags)
# # 48

# pattern = re.compile(r'\w+', 48) 
# print(pattern.flags)
# # 48

# # re.S 、 re.DOTALL 、 16 三者等价;编译正则表达式时，也阔以使用数字指定匹配模式


