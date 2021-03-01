#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2021/1/7 18:18
# @Email  13554221497@163.com
# @File   代理属性_实例.py


class NotFindError(Exception):
    def __init__(self, msg):
        self.msg = msg


class RealSubject(object):
    def __init__(self):
        self.score = {
            "张三": 90,
            "李四": 59,
            "王二": 61
        }

    def num_students(self):
        num = len(self.score.keys())
        print("The number of students is {num}".format(num=num))

    def get_score(self, user_name):
        _score = self.score.get(user_name)
        print("The score of {user} is {score}".format(user=user_name,
                                                      score=_score))


class Proxy:
    def __init__(self):
        self.default_passwd = "9l0skjlsa"
        self.real_subject = RealSubject()

    def num_students(self):
        self.real_subject.num_students()

    def get_score(self, user_name):
        print("You are visiting {} score ...".format(user_name))
        passwd = input("Please input password : ")
        if passwd == self.default_passwd:
            if user_name in self.real_subject.score.keys():
                return self.real_subject.get_score(user_name)
            else:
                raise NotFindError("The student you are visiting not found.")
        else:
            raise ValueError("The password you provided is wrong!")


p = Proxy()
p.num_students()
p.get_score('张三')