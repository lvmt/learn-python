#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/14 17:44
# @Email  13554221497@163.com
# @File   property.py

#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     # Getter function
#     @property
#     def name(self):
#         return self._name
#
#     # Setter function
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._name = value
#
#     # Deleter function
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
#
#
# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#
#     @name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)
#         # 获取这个方法的唯一途径是使用类变量而不是实例变量来访问它
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self)
#
#
#
# s = SubPerson('Guido')
# print(s.name)
# s.name = "Lary"
# # s.name = 42
# print(dir(s))


"""
A descriptor
"""
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string.')
        instance.__dict__[self.name] = value


# a class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


# extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super(SubPerson, self).name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        return super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


p = SubPerson('mike')
print(p.name)






