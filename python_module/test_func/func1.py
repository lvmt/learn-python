#/ifs/TJPROJ3/DISEASE/share/Software/bin/python3
#-*- coding:utf-8 -*-

 
# https://docs.python.org/zh-cn/3/tutorial/appetite.html  #python官方中文文档

'''函数调用时，常见的报错类型
'''
#参数数量错误
# abs(1,2)   #TypeError : abs() takes exactly one argument (2 given)

#参数类型错误
# abs("a")     #TypeError: bad operand type for abs(): 'str'

'''常用的内置函数
'''
# max(1,2,5,4,2)  #5
# min(1,2,3,6,2)  #1
# int("124")      #124
# int(12.34)      #12
# float("12.34")  #12.34
# str(1.23)       #"1.23"
# bool(1)         #True
# bool("")        #False

'''定义函数
'''
#python中定义函数，使用def语句，一次写出函数名-括号-括号中的参数-冒号；然后在缩进块中编写函数体，函数的返回值用return语句返回。

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-99))
# print(my_abs("abc"))     #python2返回abc，python3报错

# #函数一旦执行到return，函数就执行完毕，并将结果返回；
#如果没有return语句，函数执行完毕也会返回结果，只是结果为None。

'''空函数
'''
#定义空函数，作为占位符
def nop():
    pass


'''设置参数检查
'''
#调用函数时，如果个数不对，python解释器会自动检查出列，并抛出TypeError
#但是如果参数类型不对，python解释器就无法帮我们检查
#isinstance()

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError("bad operand type")
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs("abc"))

'''返回多个值
'''
#返回的多个值，其实只是一个tuple
# import math

# def move(x, y, step, angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

'''练习-求解平方根
'''
# import math 

# def quadratic(a, b, c):
#     x1 = (-b + math.sqrt(b*b - 4*a*c)) / 2*a
#     x2 = (-b - math.sqrt(b*b - 4*a*c)) / 2*a
#     return(x1, x2)

# print(quadratic(1,4,1))