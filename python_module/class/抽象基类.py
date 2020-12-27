#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/27 19:32
# @File 抽象基类.py


from abc import ABCMeta, abstractmethod

# 抽象类的一个特点是它不能直接被实例化
# 抽象类的目的就是让别的类继承它并实现特定的抽象方法


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


