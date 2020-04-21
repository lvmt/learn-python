#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""列表的特性
"""

# list.append(x)
# #在列表的末尾添加一个元素。相当于 a[len(a):] = [x] 。

# list.extend(iterable)
# #使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable 。

# list.insert(i, x)
# #在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。

# list.remove(x)
# #移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。

# list.pop([i])
# #删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。

# list.clear()
# #移除列表中的所有元素。等价于``del a[:]``

# list.index(x[, start[, end]])
# #返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常。

# #可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

# list.count(x)
# #返回元素 x 在列表中出现的次数。

# list.sort(key=None, reverse=False)
# #对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）。

# list.reverse()
# #翻转列表中的元素。

# list.copy()
# #返回列表的一个浅拷贝，等价于 a[:]。

"""练习
"""
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple')) 

# print(fruits.index('banana'))
# # 3

# print(fruits.index('banana', 4))     # Find next banana starting a position 4
# # 6 

# fruits.reverse()    # 对原始列表进行修改
# print(fruits)
# # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)      # 对原始列表进行修改
# # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

"""列表作为栈使用    后进先出
"""

"""列表作为队列使用     但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)
"""

# # 若要实现一个队列，可使用 collections.deque，它被设计成可以快速地从两端添加或弹出元素
# from collections import deque
# queue = deque(['Eric', 'John', 'Micheal'])
# queue.append('Terry') 
# queue.append('Graham')

# print(queue)
# a = queue.popleft()
# print(a)
# # Eric 

"""列表推导式
"""
