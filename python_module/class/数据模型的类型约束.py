#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/27 19:42
# @File 数据模型的类型约束.py


# Base class, Uses a descriptor to set a value


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__set__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInterger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass











#
# t = Typed(name='ss')
# print(t.__dict__)
# t.name = 'aa'
# print(t.__dict__)

# d = Descriptor('mike', age=12, like='math')
# print(d.__dict__)
# d.name = 'jack'
# print(d.__dict__)