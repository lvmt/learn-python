#!/usr/bin/env python
# -*- coding:utf-8

from types import MethodType


"""面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，
而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
"""

"""类定义，实例创建
"""
# class Student(object):
#     pass

# bart = Student()   # 创建实例对象
# print(bart)
# # <__main__.Student object at 0x0000026544D6F988>

# # 给实例绑定属性
# bart.name = 'Bart Simpson '
# print(bart.name)
# # Bart Simpson

"""类的模板效应 

把认为必须的属性强制填进去，通过定义一个__init__方法，
"""
# class Student(object):

#     def __init__(self,name,score):
#         """self 说明

#         self表示的是实例本身；
#         init函数，有了参数之后，在创建实例的时候，就不能传入空函数了，
#         必须传入和init方法匹配的参数，但是self不需要传参
#         """
#         self.name = name
#         self.score = score

# bart = Student('Bart Simpson', 59)
# print(bart.name)
# # Bart Simpson
# print(bart.score)
# # 59

"""类函数 和 普通函数的差别

和普通的函数相比，在类中定义的函数只有一点不同，
就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、
可变参数、关键字参数和命名关键字参数。
"""

"""数据封装

封装数据的函数是和类本身关联起来的，称之为类的方法
"""
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):   # 因为self就是实例本身，所以不需要传参
#         print('%s: %s' % (self.name, self.score))

#     # 封装的另外一个好处，增加新的方法
#     def get_grade(self):
#         if self.score > 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# bart = Student('Bart Simpson', 78)
# print(bart.print_score())
# # Bart Simpson: 78

# lisa = Student('Lisa',89)
# print(lisa.get_grade())
# # B

"""访问限制 

实例的变量名称如果是以__开头，就变成了一个私有变量（private),
只有内部可以访问，外部不能访问。
"""

# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     # 修改实例名称
#     def set_name(self, name):
#         self.__name = name

#     # 修改实例分数
#     def set_score(self, score):
#         if 0 <= score <= 100:
#            self.__score = score
#         else:
#             raise ValueError('bad score')

# lisa = Student('lisa', 89)
# # print(lisa.__name)
# # AttributeError: 'Student' object has no attribute '__name'
# # 这样确保了外部代码无法随意改对象内部的状态，通过访问限制，
# # 代码更加强健

# # 如果想要外部代码获取name和score，可以给student增加get_name和get_score
# # 方法
# # print(lisa.get_name())
# # # lisa

# # # 如果想要外部代码修改name 和 score怎么办，增加set_name,set_score
# # lisa.set_name('lisa-new')
# # print(lisa.get_name())
# # # lisa-new

# # 注意下面的错误写法：
# bart = Student('Bart Simpson', 89)
# print(bart.get_name())
# # Bart Simpson
# bart.__name = 'New Name' # 设置__name变量 ！！
# print(bart.__name)
# # New Name
# print(bart.get_name())
# # Bart Simpson
# # 表明外部的__name 和 内部的__name不是一个变量，

"""继承 和 多态

当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

继承的最大好处： 获得父类的全部功能

多态：
当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
"""


class Animal(object):

    def run(self):
        print('Animal is running....')


# 如果我们需要些dog 或者 cat类时，可以直接从animal类继承

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# 子类可以继承父类的全部功能
# dog = Dog()
# print(dog.run())
# # Animal is running

# cat = Cat()
# print(cat.run())
# Animal is running
""" 
对子类增加一些方法  
"""

# class Dog(Animal):

#     def run(self):
#         print('Dog is running')

#     def eat(self):
#         print('Eating meat')

# class Cat(Animal):

#     def run(self):
#         print('Cat is running...')

# dog = Dog()
# cat = Cat()
# print(dog.run())
# print(cat.run())
# # Dog is running
# # Cat is running

# def run_twice(animal):
#     animal.run()
#     animal.run()

# print(run_twice(dog))
# # Dog is running
# # Dog is running

"""对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

鸭子类型
"""

# class Timer(object):

#     def run(self):
#         print('Start ....')


# timer = Timer()
# print(run_twice(timer))
# # Start ....
# # Start ....

"""实例属性 和 类属性 
由于Python是动态语言，根据类创建的实例，可以任意绑定属性 
"""

""" 给实例绑定属性的方法是通过实例变量，或者是通过self变量 
"""

# class Student(object):

#     def __init__(self, name):
#         self.name = name

# s = Student('Bob')   # 通过self变量
# s.score = 90     # 通过实例变量绑定
# print(dir(s))
# # ... name, score

"""定义 类属性

在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
"""
# class Student(object):
#     name = 'Student'     # 类属性

# s = Student()
# print(s.name)
# # Student
# print(Student.name)
# # Student
# s.name = 'Micheal'
# print(s.name)
# # Micheal
# print(Student.name)
# # Student
# del s.name
# print(s.name)
# # Student

"""为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
"""

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1


# a = Student('A')
# b = Student('B')
# print(Student.count)
# # 2

"""给实例绑定 属性 方法

给一个实例绑定的方法，对另外一个实例是不起作用的;因此可以给class绑定方法
"""

# class Student(object):
#     pass

# s = Student()
# s.name = 'Micheal'   # 动态给实例绑定属性

# # 给实例绑定一个方法
# def set_age(self, age):
#     self.age = age


# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25) # 调用实例方法
# print(s.age)
# # 25

"""限定实例的属性  __slots__
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
"""

# class Student(object):
#     __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

# # s = Student()
# # s.name = 'Micheal'
# # s.age = 25
# # s.score = 99
# # # 'Student' object has no attribute 'score'

# class GraduateStudent(Student):
#     pass

# g = GraduateStudent()
# g.score = 90
# print(g.score)
# # 90
# #  除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。


""" @property  

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
"""

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# s.score = 999   这样显然不合理

# class Student(object):

#     def get_score(self):
#         return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#         self._score = value

# s = Student()
# s.set_score(60)
# print(s.get_score())
# # 60
# s.set_score(9999)
# # ValueError: score must between 0 ~ 100
# # 但是上面的调用方法又略显复杂，没有直接使用属性这么直接简单

"""python 内置的property装饰器，就是负责把一个方法变成属性调用的  
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
#             raise ValueError('score must between 0 ~ 100')
#         self._score = value

# s = Student()
# s.score = 60
# print(s.score)
# 60
"""@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
"""

# 还可以定义只读属性，即只定义getter方法，不定义setter方法，

# class Student(object):

#     @property
#     def birth(self):             # getter
#         return self._birth

#     @birth.setter               # setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2015 - self._birth

# s = Student()
# s.birth = 1990
# print(s.age)
# # 25

"""@property 练习
"""

# class Screen(object):

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value

#     @property
#     def resolution(self):
#         return self._width * self._height

# s = Screen()
# s.width = 90
# s.height = 100
# print(s.resolution)
# # 9000

"""多重继承
通过多重继承，一个子类可以同时获取多个父类的所有功能
"""
