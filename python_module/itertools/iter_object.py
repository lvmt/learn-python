#!/usr/bin/env python
#-*- coding:utf-8 -*-

class MyList(object):

    def __init__(self,num):
        self.data = num 

    def __iter__(self):
        return MyListIterator(self.data)  # 返回该可迭代对象的迭代器类的实例



class MyListIterator(object):
    
    def __init__(self,data):
        self.data = data
        self.now = 0

    def __iter__(self):
        return self

    def next(self):
        while self.now < self.data:
            self.now += 1
            return self.now - 1
        raise StopIteration


my_list = MyList(5)
print(type(my_list)) 


my_list_iter = iter(my_list)     # 得到该对象的迭代器实例，iter函数在下面会详细解释  
print(type(my_list_iter))  