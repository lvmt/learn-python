#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
demo
"""

# class File(object):
#     def __init__(self):
#         pass

#     def safeopen(self, filename, mode):
#         try:
#             if not filename.endswith('gz'):
#                 return open(filename, mode)
#             else:
#                 import gzip
#                 return gzip.open(filename, mode)
#         except IOError:
#             print(filename + ' do not exists!')

# ob = File()
# f = ob.safeopen('test.py', 'r')

# for line in f:
#     print(line.strip())
 

"""
demo2
"""
from collections import OrderedDict

class Check(object):

    def __init__(self):
        self.errors = OrderedDict()

ob1 = Check()
print(ob1.__dict__)

