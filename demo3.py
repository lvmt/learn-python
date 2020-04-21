#!/usr/bin/env python
#-*- coding:utf-8 -*-

# def add(x, y):
#     return x + y

# def sum(*args):
#     return sum(args)



class Cat(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('{self.name} is {self.age} old'.format(**locals()))

cat = Cat('pet', 13)
cat.run()