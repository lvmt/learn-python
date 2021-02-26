#!/usr/bin/env python
#-*- coding:utf-8 -*- 

""" 定义二个类，一个用来装书籍属性，另一个用来封装书籍方法 """

print(__doc__)
class Book:
    
    def __init__(self,name,author,comment,state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        if self.state == 0:
            staty = '未借出'
        else:
            staty = '借出'
        return '书名：%s,作者：%s,评语：%s,状态：%s'%(self.name,self.author,self.comment,staty)

book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示')
print(book1.__dict__)

class Bookmanager:
   
    list = []
    
    def menu(self):
        print('欢迎来到xx图书馆')
        while True:
            choice=int(input('1：显示所有书籍\n2:添加书籍\n3:借阅书籍\n4:归还书籍\n5:退出系统\n请输入您的选择：\n'))
            if choice == 1:
                self.show_all()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('欢迎退出图书馆系统')
                exit()
            
    def __init__(self):   
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。')
        self.list.append(book1)
        self.list.append(book2)
        self.list.append(book3)
        
    def show_all(self):
        for i in self.list:
            print(i)

    def add_book(self):
        new_name = input('请输入书籍名称')
        new_author = input('请输入作者')
        new_comment = input('请输入评论')
        new_book = Book(new_name, new_author, new_comment)
        self.list.append(new_book)
        print('录入书籍成功')

    def lend_book(self):
        borrow_name = input('请输入要借阅的书籍名称')
        for j in self.list:
            if j.name == borrow_name:
                if j.state == 0:
                    print('太幸运啦，它没有借出，你可以拿走啦！')
                    j.state = 1
                    break
                else:
                    print('不好意思，你来晚了，他被借走了！')
                    break
            else:
                 print('输入错误，系统里面没有这本书哟！')
                 break


    def return_book(self):
        reback_name = input('请输入归还书籍名称：')
        for m in self.list:
            if reback_name == m.name:
                if m.state == 1:
                    print('归还成功！')
                    m.state == 0
                    break
                else:
                    print('该书籍还没有借出去哟，无法归还')
                    break
            else:
                print('输入错误，系统没有查阅到该书籍！')
                break


A=Bookmanager()
A.menu()