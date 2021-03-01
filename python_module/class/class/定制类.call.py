#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '创建实例对象: {}'.format(self.name)

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    def __call__(self):
        print("My name is {}".format(self.name))

# s = Student('mike')
# print(s) 
# s()    # 因为有call方法， 所以可以被调用


class urls(object):

    def __init__(self, path='/users'):
        self.__path = path

    def __getattr__(self, path):
        return urls(('%s/%s' % (self.__path, path)))

    def __call__(self, path):
        return urls(('%s/%s' % (self.__path, path)))

    def __str__(self):
        return self.__path

    __repr__ = __str__

print(urls().user('mike').ll)
# /users/user/mike/ll

##  实现思想： 重建实例

