#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''了解python yield from的写法
'''

# 替代内容for循环

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
list(chain(s,t))
# ['A', 'B', 'C', 0, 1, 2]

# 
def chain2(*iterables):
    for i in iterables:
        yield from i 

list(chain2(s,t))
# ['A', 'B', 'C', 0, 1, 2]


# 树结构

class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)


    def add_child(self,node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)

    
    def depth_firth(self):
        yield self
        for c in self:
            yield from c.depth_firth()

    
if __name__ == '__main__':
    
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
 
    child1.add_child(Node(3))
    child1.add_child(Node(4))

    child3 = Node(3)
    child3.add_child(Node(6))
    child2.add_child(Node(5))

    for ch in root.depth_firth():
        print(ch)




