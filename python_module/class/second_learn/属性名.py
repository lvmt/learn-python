#!/usr/bin/env python3
#-*- coding:utf-8 -*-  
'''
@Author: lvmengting  
@Date: 2020-12-11 15:14:45  
@Last Modified by:   lvmengting  
@Last Modified time: 2020-12-11 15:14:45  
''' 

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute 
        self.public = 1 # A public attribute 

    
    def public_method(self):
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):
        self.__private = 0 

    def __private_method(self):  # 这种属性通过继承是无法被覆盖的, 私有属性无法通过继承被覆盖.
        pass

    def public_method(self):
        pass 


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 

    def __private_method(self):
        pass  


if __name__ == '__main__':
    # a = A()
    # print(dir(a))

    # b = B()
    # print(b._B__private) # 访问私有属性
    # print(dir(b))

    c = C()
    # print(dir(c))
    print(c._B__private) # 0
    print(c._C__private) # 1