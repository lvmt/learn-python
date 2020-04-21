#/usr/bin/python
# -*- coding=utf-8 -*-


'''面向对象编程：类（class） 和 实例（instance），
类是抽象的模板，比如student类，
实例是根据类创建出来的一个个具体的对象
每个对象都拥有相同的方法，但是各自的数据可能不同
'''

'''举例一：
 '''
# class Student(object):
#     pass

# #创建实例，通过类名+()实现的
# bart = Student()
# #给实例绑定一个属性
# bart.name = "Bart Simpson"


'''在创建类的时候，可以把一些认为必须绑定的属性强制填写进去，通过定义__init__的特殊方法
'''
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# #__init__方法的第一个参数永远是self，表示创建的实例本身，因此在__init__方法内部，就可以把各种属性绑定到self，因为self就是指向创建的实例本身。
# #有了__init__方式，在创建实例的时候，就不能传入空的函数了，必须传入与__init__方法匹配的参数，但是self不需要传参，python解释器自己家会把实例变量传进去；

# bart = Student("Bart Simpson", 59)
# print(bart.name)  #Bart Simpson
# print(bart.score)  #59

'''和普通函数相比，在类中定义的函数只有1点不同，就是第一个函数永远都是实例变量self，
并且调用时，不用传递该参数。除此之外，和普通的函数没有什么区别
'''

'''数据封装
如何访问实例本身的数据，类的方法
'''
#可以通过直接在student类的内部定义访问数据的函数，这样，就把数据给封装起来了。这些封装数据的函数和student类本身就是关联起来的。
#称之为类的方法

# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print("%s: %s" % (self.name, self.score))

#定义一个方法，出了第一个参数是self外，其他的和普通函数一样。
#调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常即可。

#bart.print_score()   #Bart Simpson:  59
#上述get_score方法表明：从外部看student类，只需要知道在创建实例时给出name和score，而如何打印，则是在类的内部定义的，这些数据的逻辑都被封装起来了，调用很容易，但是却不知道内容的细节。

'''
封装的另外一个好处： 给类增加新的方法
'''
# class Studnet(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 60:
#             return "B"
#         else:
#             return "C"
#lisa = Student("Lisa", 99)
#print(lisa.name, lisa.get_grade())


'''访问限制，私有变量
'''
#前面的例子中，外部代码是可以自由的修改一个实例的name或者score属性
#如果要让内部属性不被外部访问，可以把属性的名称前面加上2个下划线__，
#如果变量名时以__开头的，就是私有变量，只有内部可以访问，外部不能访问。

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print("%s: %s" % (self.__name, self.__score))

#bart = Student("Lisa", 88)
#print(bart.__name)  #会报错
#通过访问限制，代码更加强健；同时确保了外部代码不能随意更改对象内部的状态


'''如果外部代码要获取name和score，可以给Student类增加get_name和get_score方法
'''
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score
    
#     def set_score(self,score):   #该方法可以使外部代码修改score
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError("bad score")

# lisa = Student("Lisa", 88)
# print(lisa.get_score())
##也许觉得之前通过bart.score = 99也阔以直接修改，为什么一定要兜兜转转；因为在方法中，可以对参数做检查，避免传无效参数


'''python 中的变量
'''
# __var__： 双下划线开头，双下划线结尾的，是特殊变量，可以直接访问
#_var    ： 一个下划线开头外部变量可以访问，但是按照约定俗成的规定，请把这样的变量视为私有变量
#__var   ： 双下划线开头的变量，私有变量（其实也不是不能访问，只是访问的方式有所区别）(bart._Studen__name),不建议这么干


'''练习，把student对象gender字段对外隐藏起来，用get_gender()和set_gender()代替，同时检查参数的有效性
'''
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender

#     def set_gender(self, gender):
#         if gender == "M" or gender == "F":
#             self.__gender = gender
#         else:
#             raise ValueError

# lisa = Student("Lisa", "M")
# print(lisa)
# print(lisa.get_gender())
# lisa.set_gender("F")
# print(lisa.get_gender())

'''继承和多态

当我们定义一个class时， 可以从现有的class继承，新的class称为子类（subclass），而被继承的类称为基类，父类或者超类

继承可以把分类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不合适的覆盖重写
'''

# class Animal(object):
#     def run(self):
#         print("Animal is running...")
    
# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# #继承的最大好处，就是子类获得了父类的全部功能。
# dog = Dog()
# print(dog.run())

'''多态

当子类和父类都存在相同的run()方法时，子类的方法会覆盖父类的方法，这样在代码运行的时候，就获得了继承的另外一个好处：多态
'''

# class Animal(object):
#     def run(self):
#         print("Animal is running...")

# class Dog(Animal):
#     def run(self):
#         print("Dog is running...")

# class Cat(Animal):
#     def run(self):
#         print("Cat is running...")

# cat = Cat()
# print(cat.run())

#多态的简单理解：同一种类型的东西的同一种属性，有不通过的内容

'''如何判断某个变量是否属于某种类型： isinstance()
'''
# a = list()
# isinstance(a, list)

'''理解多态的含义
'''
# class Animal(object):
#     def run(self):
#         print("Animal is running...")
    
#     def run_twice(animal):
#         print(animal.run())
#         print(animal.run())

# class Dog(Animal):
#     def run(self):
#         print("Dog is running...")

# class Cat(Animal):
#     def run(self):
#         print("Cat is running...")


# dog =  Dog()
# print(dog.run_twice())

'''获取对象信息

对象的类型，对象的方法
'''
# #type()
# print(type(123))
# print(type(str))
# #instance()
#dir() 获取一个对象的所有属性和方法


'''对象的getattr(), setattr(), hasattr()，利用这3个内置方法，可以直接操作一个对象的状态
'''
# class MyObject(object):
#     def __init__(self):
#         self.x = 9

#     def power(self):
#         return self.x * self.x

# obj = MyObject()
# #测试对象的属性
# print(hasattr(obj, "x"))  #TRUE 判断是否存在"x"属性
# print(hasattr(obj, "y"))  #FALSE
# setattr(obj, "y", 19)     #设置一个属性y
# print(hasattr(obj, "y"))
# print(getattr(obj, "y"))  #获取"y"属性
# #试图获取不存在的属性，会抛出AttributeError的错误；可以传入一个default参数，如果属性不存在，就返回默认值
# #getattr(obj, "z")
# getattr(obj, "z", 404)


'''实例属性和类属性
'''
#给实例绑定属性的方法是通过实例变量，或者通过self变量

# class Student(object):
#     def __init__(self, name):
#         self.name = name
    
# s = Student("Bob")
# s.score = 90
# print("%s: %s" % (s.name, s.score))

#如果Student()类本身需要绑定一个属性列，可以直接在class中定义属性，这种属性是类属性，归student类所有

# class Student(object):
#     name = "student"

# s = Student()
# print(s.name)  #student
# print(Student.name)  #student
# s.name = "Micheal"   #给实例绑定属性，
# print(s.name)        #Micheal: 实例属性高于类属性，因此他会屏蔽类的name属性
# del s.name   #删除实例的name属性
# print(s.name)   #由于实例的name属性没有找到，类的属性就显示出来了

##上述情况表明：在编程程序的时候，千万不要对实例属性和类属性使用相同的名字


'''类的举例,  统计学生的人数，增加去重，理解类属性和实例属性的差异
'''
class Student(object):
    count = 0 
    p_list = []
    def __init__(self, name):
        self.name = name
        if self.name in Student.p_list:
            pass
        else:
            Student.p_list.append(self.name)
            Student.count += 1

s1 = Student("Bob")
s2 = Student("Lisa")
s3 = Student("Bob")
print(Student.count)  #2
print(Student.p_list)
print(s1.count)    #2









# #如果父类的方法的功能不能满足需求，可以在子类中重写父类的方法

# class Parent:
#     def myMethod(self):
#         print("调用父类的方法")


# class Child(Parent):
#     def myMethod(self):
#         print("调用子类方法")


# c = Child()  #子类的实例化
# c.myMethod()  #子类调用重写方法
# super(Child,c).myMethod()  #用子类对象调用父类已被覆盖的方法

# '''
# super()函数是用于调用父类（超类）的一个方法
# 上述的输出结果为：
# 调用子类方法
# 调用父类方法
# '''
