#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
分数法
练习类的创建,自定义方法等
  - +
  - -
  - * 
  - /
'''


class Fraction(object):

    def __init__(self, top, buttom):
        self.num = top  # 分子
        self.den = buttom  # 分母

    def __str__(self):
        '''打印字符串本身
        '''
        return f'{self.num}/{self.den}' 


    def __add__(self, otherfraction):
        '''2个分数相加
        相加之前,必须统一分母才行
        '''
        newnum = self.num * otherfraction.den + otherfraction.num * self.den  
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        print(common)
        return Fraction(newnum//common,newden//common)


    def gcd(self,num1,num2):
        '''简化分数
        求取最大公约数
        '''
        if num1 < num2:
            num1,num2 = num2,num1

        v = num1 % num2
        while v != 0 :
            num1,num2 = num2,v
            v = num1 % num2

        return num2

    def __eq__(self,otherfraction):
        '''判断2分数串是否相等
        '''
        firstnum = self.num * otherfraction.den 
        secondnum = otherfraction.num * self.den
        return firstnum == secondnum


    def __gt__(self, otherfraction):
        '''判断大于
        '''
        firstnum = self.num * otherfraction.den 
        secondnum = otherfraction.num * self.den 
        if firstnum - secondnum > 0:
            return True
        return False


    def __lt__(self, otherfraction):
        '''判断小于
        '''
        pass
    

if __name__ == '__main__':
    f1 = Fraction(3,4)
    f2 = Fraction(3,2)
    print(f1 + f2)
    print(f1.__eq__(f2))
    print('f1 > f2', f1.__gt__(f2))
    #print(f1)
