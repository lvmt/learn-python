#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
python 类方法的学习
"""
# https://www.cnblogs.com/wenm1128/p/11716219.html

# class Foo(object):
    
#     def __init__(self, name):
#         self.name = name 

#     def ord_func(self):
#         """ 定义普通(实例)方法，至少有一个self参数 """
#         print("普通方法")

#     @classmethod
#     def class_func(cls):
#         """ 定义类方法， 至少一个cls参数 """
#         print("类方法")

#     @staticmethod
#     def stat_func():
#         """ 定义静态方法， 无默认参数 """
#         print("静态方法")

# f = Foo("吴老师")
# f.ord_func()
# f.class_func()
# f.stat_func()  

# # 普通方法
# # 类方法
# # 静态方法



"""Test
"""

# class Test(object):

#     def __init__(self):
#         print("This is just my test.")

#     @classmethod
#     def hello(cls, name):
#         print("hello, " + name)

# name =  "mike"
# print(Test.hello(name))
# # hello, mike



""" 实例方法：参数要有self 

实例方法使用的时候，必须要实例化

调用方法：只能通过实例来调用
""" 

# class Person(object):

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

#     def get_name(self):
#         return self.name

# ## 方法一
# print(Person("吴老师", 'Male').get_name())     ##  #但是这种方法实例没有存到变量里，所以只能使用一次

# ## 方法二：
# wulaoshi = Person("吴老师", "Male")
# print(wulaoshi.get_name())

# # 吴老师
# # 吴老师


"""类方法： 用classmethod 来声明方法， 需要添加参数cls
类方法使用的时候不需要实例化
调用方法：
1、通过类名使用： 类名.get_instance_count()
2、通过实例对象调用， 实例对象.get_instance_count()
""" 
# class Person(object):
#     count = 0 # 类变量

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#         Person.count += 1

#     def get_name(self):
#         return self.name 
    
#     # 类方法： 可以使用类变量，不能使用实例变量
#     # 因为类方法参数没有self， 就不找到实例地址， 因此不能使用实例变量

#     @classmethod 
#     def get_instance_count(cls):
#         return Person.count

#     @classmethod 
#     def create_a_instance(cls):
#         return Person("张", "女")
    
# print(Person.count)
# # 0

# Person("吴老师", "Male")
# print(Person.count)
# # 1

# print(Person.get_instance_count())  ##  类调用
# # 1

# print(Person("吴老师", "Male").get_instance_count())   ## 实例调用
# # 2


"""静态方法：用staticmethod来声明，不需要使用参数self和cls
静态方法不需要使用实例化就可以使用

调用方法：
1、类名调用： 类名.get_nation()
2、实例调用： 实例.get_nation()
""" 

# class Person:
#     count = 0 
#     nation = "中国"

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#         Person.count += 1

#     def get_name(self):
#         return self.name 

#     @staticmethod
#     def get_nation():
#         return Person.nation

    
# print(Person.get_nation())
# print(Person("吴老师", "Male").get_nation())
# # 中国
# # 中国 


"""
一个静态方法使用的场景
"""

class FileUtil(object):
    
    @staticmethod
    def get_file_name(file_path):
        with open(file_path) as fp:
            return fp.name 
    
    @staticmethod
    def get_file_content(file_path):
        with open(file_path, encoding="utf-8") as fp:
            return fp.read()


print(FileUtil.get_file_name("a.txt"))
print(FileUtil.get_file_content('a.txt'))




   








