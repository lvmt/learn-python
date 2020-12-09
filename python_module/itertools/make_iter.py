#!/usr/bin/env python
#-*- coding:utf-8 -*-

# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []

#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)

#     def add_child(self,node):
#         self._children.append(node)

#     # def __iter__(self):
#     #     return iter(self._children)

#     def __iter__(self):
#         return self._children.__iter__()


# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)

#     root.add_child(child1)
#     root.add_child(child2)

#     for ch in root:
#         print(ch)
 
# class Countdown:
#     def __init__(self,start):
#         self.start = start

#     # forward iterator
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1

#     # reverse iterator  
#     def __reversed__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1


# for rr in reversed(Countdown(30)):
#     print(rr, end=' ') 

# # for rr in Countdown(30):
# #     print(rr, end=' ')



def count(n):
    while True:
        yield n 
        n += 1


c = count(100)

import itertools 
for x in itertools.islice(c, 10, 20):
    print(x, end=' ')


print('')
print('>>>',next(c)) # 迭代器消耗掉了前面的元素.