#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/3/26 10:26
# @Email  13554221497@163.com
# @File   new方法.py


"""
__new__
new方法的调用是发生在init之前的

init 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
new 通常用于控制生成一个新实例的过程。它是类级别的方法
new至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
new必须要有返回值，返回实例化出来的实例，这点在自己实现new时要特别注意，可以return父类new出来的实例，或者直接是object的new出来的实例

"""


class DemoClass:
    instance_created = 0

    def __new__(cls, *args, **kwargs):
        print('__new__(): ', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created += 1
        return instance

    def __init__(self, attribute):
        print('__init__(): ', self, attribute)
        self.attribute = attribute


# test1 = DemoClass('abc')
# test2 = DemoClass('xyz')
#
# print(test1.number, test1.instance_created)
# print(test2.number, test2.instance_created)


# class PositiveInteger(int):
#     def __init__(self, value):
#         # super(PositiveInteger, self).__init__(self, abs(value))
#         super().__init__(self, value)
#         self.value = value
#
# i = PositiveInteger(-9)
# print(i)


class PositiveInteger(int):
    def __new__(cls, value):
        # 通过重载new, 实现的输入全部转换为正数.
        return super(PositiveInteger, cls).__new__(cls, abs(value))


l = PositiveInteger(-9)
print(l)


