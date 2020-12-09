#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''自定义迭代器
'''

class  Fib:

    def __init__(self,n):
        '''斐波拉数列的个数
        '''
        self.n = n
        self.index = 0
        self.num1 = 0
        self.num2 = 1


    def __next__(self):
        '''被next函数调用,来获取下一个数
        '''
        if self.index < self.n:
            num = self.num1
            self.num1,self.num2 = self.num2, self.num1 + self.num2
            self.index += 1
            return num 
        else:
            return StopIteration

    
    def __iter__(self):
        '''
        迭代器的__iter__返回自身即可
        '''
        return self 


    
if __name__ == '__main__':
    fb = Fib(20)
    print(fb.n)
    print(next(fb))
    print(next(fb))
    print(next(fb))
    # for num in fb:
    #     print(num) 



