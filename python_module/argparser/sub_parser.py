#!/usr/bin/env python 
#-*- coding:utf-8 -*-

"""sub parser的用法
"""


"""子命令模式

argparse可通过add_subparsers 以及add_parser来达到效果；
步骤1.在顶层的解析器下，先定义一个subparsers，它是一个子命令解析的对象，用来产生子命令解析器 （注意，每个解析器，只能有一个subparsers)
步骤2.在subparsers下，分别定义所需要的子解析器(一个subparsers下可以有多个parser)，子解析器间是互斥的关系，一个时刻只能匹配一个
""" 


import argparse


"""demo 1
"""

# ## 创建顶层parser
# parser = argparse.ArgumentParser(prog="PROG")
# parser.add_argument('--foo', action="store_true", help="foo help")

# subparser = parser.add_subparsers(help="sub-command help") 

# ## 创建子解析器， a  
# parser_a = subparser.add_parser("a", help="a help")
# parser_a.add_argument('bar', type=int, help="bar help")

# ## 创建子解析器，b
# parser_b = subparser.add_parser("b", help="b help")
# parser_b.add_argument("--baz", choices="xyz", help="baz help")

# parser.parse_args()


"""demo 2 

"""

## 添加子命令函数
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

## 创建上层解析器
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(title="subcommands",
                                    description="valid subcommands",
                                    help="additional help",
                                    dest="subparser_name")


## 创建子解析器 ‘foo’
parser_foo = subparser.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)    ## 将函数foo， 与子解析器foo绑定

## 创建子解析器bar
parser_bar = subparser.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)  ## 将函数bar与子解析器bar绑定

parser.parse_args()


## 函数调用
args = parser.parse_args()
# print(args)
# print(args.func(args)) 
parser.print_help()
exit()

 