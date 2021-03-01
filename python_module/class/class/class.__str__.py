#!/usr/bin/env python
#-*- coding:utf-8 -*- 

class Car(object):
    
    def __init__(self,wheelnum,color):
        self.wheelnum = wheelnum
        self.color = color

    def __str__(self):
        msg = '嘿... 我的颜色是' + self.color + ', 我有' + str(self.wheelnum) + '个轮胎...'
        return msg

    def move(self):
        print('车在跑, 目标：夏威夷')

BMW = Car(4, '白色')
print(BMW)






















# class Book:
    
#     def __init__(self,name,author,comment,state=0):
#         self.name = name
#         self.author = author
#         self.comment = comment
#         self.state = state

#     def __str__(self):
#         if self.state == 0:
#             staty = '未借出'
#         else:
#             staty = '借出'
#         return '书名：%s,作者：%s,评语：%s,状态：%s'%(self.name,self.author,self.comment,staty)

# book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示')

# print(book1)