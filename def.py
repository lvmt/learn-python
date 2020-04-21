#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Cat(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('{self.name is self.age}'.format(self))


