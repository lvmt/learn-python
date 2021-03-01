#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Animal(object):

    def run(self):
        print('Animal is running...') 


class Dog(Animal):
    pass

class Cat(object):
    pass

dog = Dog()
dog.run() 

