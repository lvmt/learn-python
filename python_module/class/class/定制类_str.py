#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" __str__  """

class Student1(object):

    def __init__(self, name):
        self.name = name

print(Student1('Mike'))  
# <__main__.Student1 object at 0x0000020BD91F4C08>

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: {})'.format(self.name)

    # __repr__ = __str__

print(Student('Mike'))
