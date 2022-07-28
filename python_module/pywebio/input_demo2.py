

import pywebio 
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server


'''
输入函数大致分为两类，
一类是单项输入:
另一类是使用 input_group 的输入组:
'''


name = input("What's your name")
print("Your name is %s" % name)

info = input_group("User info",[
  input('Input your name', name='name'),   # 输入组中需要在每一项输入函数中提供 name 参数来用于在结果中标识不同输入项.
  input('Input your age', name='age', type=NUMBER)
])
put_text(info['name'], info['age'])