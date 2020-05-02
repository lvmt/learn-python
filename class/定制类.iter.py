#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Fib(object):

    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b 

        if self.a > self.limit:
            raise StopIteration()
        return self.a

print(Fib(100)) 
for i in Fib(1000):
    print(i) 

