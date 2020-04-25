#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Cat(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('{self.name} is {self.age}'.format(**locals()))

    def sort_file(self, in_list):
        return sorted(in_list, key=lambda x: x[1])


cat = Cat('pet', 12)
cat.run() 

print(cat.sort_file([('a', 4), ('b', 2), ('c', 1)]))  

print('hello world')
