#!/usr/bin/env python
#-*- coding:utf-8 -*- 

"""  常规用法： 先set， 在get  """
# class Student(object):

#     def get_score(self):
#         return self.__score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#         self.__score = value

# ss = Student()
# ss.set_score(99)
# print(ss.get_score())


"""
使用property方法，将方法变成属性

@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
"""

# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value 

# ss = Student()
# # ss.score = 'aaa'
# # ss.score = 999

""" 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性： """

# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, value):
#         self._birth = value
    
#     @property
#     def age(self):
#         return 2020 - self._birth

# ss = Student()
# ss.birth = 1991
# print(ss.age) 


"""  联系 """

class Screen(object):

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def resolution(self):
        return self._height * self._width


tt = Screen()
tt.width = 10
tt.height = 20
print(tt.resolution)
print(tt.__dict__)