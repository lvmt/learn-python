#/usr/bin/python
# -*- coding:utf-8 -*-

##类学习

class People:
    #定义基本属性
    name = ""
    age = ""
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    ##定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print ("%s says: i  %d years, weight %d" % (self.name,self.age,self.__weight))

    
# p  = People("Runob", 10, 30)
# p.speak()

class Student(People):
    grade = ""
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        People.__init__(self,n,a,w)
        self.grade = g
        #复写父类的方法
    def speak(self):
         print("%s says: i %s years, read in %s grades" % (self.name, self.age,self.grade))

#s = Student("ken", 10,60,3)
#s.speak()

#另外一个类
class speaker():
    topic = ""
    name = ""
    def __init__(self, n , t):
        self.name = n
        self.topic = t

    def speak(self):
        print("name is %s, i'm a talker, and my topic is %s " % (self.name, self.topic))

class sample(speaker,Student):
    a = ""
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim", 25, 80, 4, "python")
test.speak()
##输出结果为：name is Tim, i'm a talker, and my topic is python  
##方法名相同，默认调用的是在括号中排名靠前的父类的方法

###类的方法重写
