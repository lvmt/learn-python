#!/usr/bin/env python
#-*- coding:utf-8 -*-



# class Student(object):
    
#     def __init__(self):
#         self.name = 'Michael'

# aa = Student()
# print(aa.name)
# # print(aa.score)   ##  报错， 无该属性


""" 注意，只有在没有找到属性的情况下，才调用__getattr__，
已有的属性，比如name，不会在__getattr__中查找。 """

class Student2(object):

    def __init__(self):
        self.name = 'mike'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        return attr
    
# bb = Student2()
# print(bb.score)    # 99
# print(bb.height)   # 100


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):    
        return Chain('%s/%s' % (self._path, path))    # 回调类自身

    def __str__(self):
        return self._path

    __repr__ = __str__ 


print(Chain().status.user.timeline.list)
# /status/user/timeline/list

















# class Chain(object):
#     def __init__(self, path=''):
#        self.__path = path

#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self.__path, path))

#     def __call__(self, path):
#         return Chain('%s/%s' % (self.__path, path))

#     def __str__(self):
#         return self.__path

#     __repr__ = __str__

# print(Chain().users('michael').repos) # /users/michael/repos
# print(Chain().__dict__) 

