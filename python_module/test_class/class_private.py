#/ifs/TJPROJ3/DISEASE/share/Software/bin/python3
#-*- coding:utf-8 -*-

'''私有属性实例
'''
# class JustCounter:
#     __secretCount = 0  #2个下划线开头，私有变量
#     publicCount = 0   #公开变量

#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print("pub %s" % self.publicCount)
#         print("sec %s" % self.__secretCount)

# counter = JustCounter()
# counter.count()
# counter.count()

# print(counter.publicCount)

# print(counter.__sercteCount)  ##实例不能访问私有变量

'''类的私有方法
'''
# class Site:
#     def __init__(self, name, url):
#         self.name = name  #public
#         self.__url = url  #private

#     def who(self):
#         print("name : ",self.name)
#         print("url : ", self.__url)

#     def __foo(self):
#         print("this is private")

#     def foo(self):
#         print("this is public")
#         self.__foo()

# x = Site("cainiao_teach", "www.runbo.com")
# x.who()
# #x.foo()
# x.__foo()

# class Test:
#     # name = ""
#     # age = ""
#     def __init__(self,a,b):
#         self.name = a
#         self.age = b
#         print(self.name,self.age)

# t = Test(2,3)
# #print(t)

# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
        
#     def add(self):
#         print(self.x + self.y)

# a = A(3,4)
# a.add()

#python3中的静态方法，普通方法及类方法
'''
静态方法：用@staticmethod装饰的不带self参数的方法,可以直接使用类名调用。
普通方法：默认有个self参数，且只能被对象调用
类方法：默认有个cls参数，可以被类和对象调用，需要加上@classmethod装饰器
'''

# class Classname:
#     @staticmethod
#     def fun():
#         print("this is jin-tai method")

#     @classmethod
#     def a(cls):
#         print("lei-method")

#     def b(self):
#         print("normal method")

# # Classname.fun()
# # Classname.a()

# c = Classname()
# c.fun()
# c.a()
# c.b()
'''
子类继承父类的构造方法
'''
# class Father(object):
#     def __init__(self, name):
#         self.name = name
#         print("name: %s" % self.name)
#     def getName(self):
#         return 'Father ' + self.name

# class Son(Father):
#     def getName(self):
#         return 'Son ' + self.name

# if __name__ == '__main__':
#     son = Son("runbo")
#     print(son.getName())


'''
子类重写__init__构造方法
'''
# class Father(object):
#     def __init__(self,name):
#         self.name = name
#         print("name: %s "%(self.name))

#     def getName(self):
#         return 'Father ' + self.name

# class Son(Father):
#     def __init__(self,name):
#         super(Son,self).__init__(name) 
#         '''如果重写了__init__时，要继承父类的构造方法，可以使用super关键字
#         super(子类,self).__init__(参数1,参数2......)
#         or
#         父类名称.__init__(self,参数1,参数2.......)
#         '''
#         print("hi")
#         self.name = name
#     def getName(self):
#         return 'Son ' + self.name

# if __name__ == '__main__':
#     son = Son('jack')
#     print(son.getName())



