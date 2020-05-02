#!/usr/bin/env python 
#-*- coding:utf-8 -*-

class Animal(object):

    def run(self):
        print('Animal is running...')

    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run_twice()

