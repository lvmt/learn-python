#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
三个便捷的方法：wrap，fill和decent，
"""

import textwrap

"""
wrap: 这个方法是将一个字符串按照width的宽度进行切割，切割后返回list
"""

sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''

# print(sample_text)
# print(textwrap.wrap(sample_text,width=5))
# print(textwrap.wrap(sample_text2,width=5))

"""
aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk
['aaabb', 'bcccd', 'ddeee', 'edddd', 'dffff', 'fgggg', 'ghhhh', 'hhkkk', 'kkkk']
['aaa', 'bbb', 'ccc', 'ddd', 'eeee', 'ddddd', 'fffff', 'ggggg', 'hhhhh', 'h kkk', 'kkkk']
"""


"""  fill  """

# print(textwrap.fill(sample_text, width=5))
# print('*'*10)
# print(textwrap.fill(sample_text2, width=5))


""" dedent """

demo_text = """
    aaaaaaa
        bbbbbb
            ccccc
    """
    
print(textwrap.dedent(demo_text))
print(demo_text)

