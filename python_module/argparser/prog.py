#/ifs/TJPROJ3/DISEASE/share/Software/bin/python3
#-*- coding:utf-8  -*-

'''\033[1;3;32m
    学习argparser的用法
  \033[0m'''

import argparse
import textwrap
import sys

parser = argparse.ArgumentParser()



#parser.parse_args()
#-h是唯一可以免费获得的选项

'''位置参数（positional arguments）
'''
# parser.add_argument('echo', help = 'echo the string you use here')
# args = parser.parse_args()
# print(args.echo)

# parser = argparse.ArgumentParser()
# parser.add_argument('square', help = 'display a square of a given number.', type = int)
# args = parser.parse_args()
# print(args.square**2)


'''可选参数（optional arguments）
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--verbosity', help = 'increase output verbosity', action = 'store_true')

# args = parser.parse_args()
# if args.verbosity:
#     print('verbosity turned on')

'''短横线参数
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('-v', '--verbose', help = 'increase output verbosity', action = 'store_true')

# args = parser.parse_args()

# if args.verbose:
#     print('verbosity turned on.')

'''组合位置参数和可变参数
'''
# parser = argparse.ArgumentParser()

# parser.add_argument('square', type = int, help = 'display a square of a given number.')
# parser.add_argument('-v', '--verbose', action = 'store_true', help = 'increase output verbosity.')

# args = parser.parse_args()

# answer = args.square ** 2

# if args.verbose:
#     print('the suqare of {} equal {}.'.format(args.square, answer))
# else:
#     print(answer)


'''根据参数不同，进行判断
'''
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)

'''限定可以参数可以选择的数值,choices
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('square', type = int, 
#             help = 'display a square of a given number.')
# parser.add_argument('-v', '--verbosity', type = int, choices=[0,1,2], 
#             help = 'increase output verbosity.')
# args = parser.parse_args()
# answer = args.square ** 2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)

'''代码进阶用法，
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('x', type = int, help = 'the base')
# parser.add_argument('y', type = int, help = 'the exponent')
# parser.add_argument('-v', '--verbosity',action = 'count', default = 0)

# args = parser.parse_args()

# answer = args.x ** args.y
# if args.verbosity >= 2:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# elif args.verbosity >= 1:
#     print("{}^{} == {}".format(args.x, args.y, answer))
# else:
#     print(answer)

'''冲突选项： conflicting options

add_mutually_exclusive_group()
'''
# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-v', '--verbose', action = 'store_true')
# group.add_argument('-q', '--quite', action = 'store_true')
# parser.add_argument('x', type = int, help = 'the base')
# parser.add_argument('y', type = int, help = 'the exponent')
# args = parser.parse_args()

# answer = args.x ** args.y

# if  args.quite:
#     print(answer)
# elif args.verbose:
#     print('{} to the power {} equals {}'.format(args.x, args.y, answer))
# else:
#     print('{} ^ {} == {}'.format(args.x, args.y, answer))

'''告诉别人你的项目目的是什么，description
'''
# epilog = textwrap.dedent('''\033[33mcontact:lvmengting4480@novogene.com''')
# parser = argparse.ArgumentParser(description=__doc__,epilog=epilog)
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y

# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# else:
#     print("{}^{} == {}".format(args.x, args.y, answer))


'''更改帮助信息中的脚本名称

prog
'''
# parser =  argparse.ArgumentParser(prog='myprogram')
# parser.add_argument('--foo', help = 'foo of the %(prog)s program')
# args = parser.parse_args()


'''usage=关键字，修改usage帮助信息
'''
# parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# args = parser.parse_args()


'''在帮助信息后面，显示额外的帮助信息
epilog
'''
# parser = argparse.ArgumentParser(prog='PROG', 
#         usage='%(prog)s [options]',
#         epilog='contact: lvmengting4480@novogene.com')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# args = parser.parse_args()


'''parents
少数解析器会使用同一系列的参数，单个解析器能够通过parents参数
给argumenparser而使用相同的参数，而不是重复定义这些参数。

没看懂
'''
# parent_parser = argparse.ArgumentParser(add_help=False)
# parent_parser.add_argument('--parent', type = int)

# foo_parser = argparse.ArgumentParser(parents=[parent_parser])  
# foo_parser.add_argument('foo')
# args_parent = parent_parser.parse_args()
# args_foo = foo_parser.parse_args()

# print(args_parent)
# print(args_foo)

'''formatter_class 

对文本内容，进行自定义格式化输出

'''
from argparse import RawDescriptionHelpFormatter         #choose
from argparse import RawTextHelpFormatter                #choose
from argparse import ArgumentDefaultsHelpFormatter


#当文字长度过长时,argumentparser对象会自动将description和epilog的文字自动换行
# parser = argparse.ArgumentParser(
#     prog = 'PROG',
#     description = '''this description
#     was indented weird 
#     but that is okay''',
#     epilog = '''
#     likewise for this epilog whose whitespace will
#     be cleaned up and whose words will be wrapped
#     across a couple lines''')

# print(parser.parse_args())   

'''传入参数：RawDescriptionHelpFormatter  
'''
# parser = argparse.ArgumentParser(
#     prog = 'PROG',
#     formatter_class=argparse.RawDescriptionHelpFormatter,
#     description = textwrap.dedent('''\
#     please do not mess up this text!
#     -------------------------------
#         this description
#         was indented weird 
#         but that is okay
#         '''))

# print(parser.parse_args())

'''RawTextHelpFormater保留所有种类文字的空格,包含参数的描述。但是，多重的空行会被替换为一行，如果想保留多余的空行，可以在空行之间加上空格。
'''

'''
传入参数： ArgumentDefaultsHelpFormatter
自动添加默认的值的信息到每一个帮助信息的参数中
'''
# parser = argparse.ArgumentParser(prog = 'PROG', formatter_class=ArgumentDefaultsHelpFormatter)
# parser.add_argument('--foo', type = int, default = 42, help = 'Foo!')
# parser.add_argument('bar', nargs = '*', default = [1,2,3], help = 'BAR!')

# args = parser.parse_args()

'''add_argument()方法
'''

'''name or  flags
一个命名或者一个选项字符串的列表，例如foo或-f.-foo
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '-foo')
# parser.add_argument('bar')

# print(parser.parse_args())
# print(parser.parse_args(['BAR']))

'''nargs的用法举例
'''

'''nargs  数值
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', nargs=2)
# parser.add_argument('bar', nargs=1)

# args = parser.parse_args()
# print(args.bar)
# print(args.foo)

'''nargs ?
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', nargs = '?', const = 'c', default = 'd')
# parser.add_argument('bar', nargs = '?', default = 'd')

# args = parser.parse_args()

# print(args.bar)
# print(args.foo)


'''nargs ? 允许可选的输入文件和输出文件
'''

# parser = argparse.ArgumentParser()
# parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
# parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
# args = parser.parse_args()

# print(args.infile)
# print(args.outfile)

'''nargs *  聚集命令行参数
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', nargs='*')
# parser.add_argument('--bar', nargs='*')
# parser.add_argument('baz', nargs='*')

# args = parser.parse_args()

# print(args.foo, args.bar, args.baz)

'''nargs + 参数至少需要一个值
'''
# parser =  argparse.ArgumentParser()
# parser.add_argument('foo', nargs='+')
# args = parser.parse_args()

# print(args.foo)

'''default 给命令行参数，添加默认值
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', default=42)

# args = parser.parse_args()
# print(args.foo)

'''default 配合type使用
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--length', default='10',type=int)
# parser.add_argument('--width', default=10.5, type=int)

# args = parser.parse_args()

# print(args.length, args.width)

'''default 配合nargs使用
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('foo', nargs='?', default=42)

# args = parser.parse_args()

# print(args.foo)

'''type的使用，
因为命令行参数，传入的值默认为字符串类型，
'''

# parser = argparse.ArgumentParser()
# parser.add_argument('foo', type=int)
# parser.add_argument('bar', type=open)

# args = parser.parse_args()

# inf = args.bar.readline()
# print(f)
# print(args.foo, args.bar)


'''tyep的文件读取，可以指定文件的类型，字节数，错误提示等
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('inf', type=argparse.FileType('r'))
# parser.add_argument('out', type=argparse.FileType('w'))

# args = parser.parse_args()

# indata = args.inf.readline()
# outdata = args.out.write(indata)
# print(indata)
# print(args.inf, args.out)

'''自定义type函数
'''
# import math

# def perfect_square(string):
#     value = int(string)
#     sqrt = math.sqrt(value)
#     if sqrt != int(sqrt):
#         msg = '%s is not a perfect square' % string
#         raise argparse.ArgumentTypeError(msg)
#     return value

# parser = argparse.ArgumentParser()
# parser.add_argument('foo', type=perfect_square)

# args = parser.parse_args()
# print(args.foo)

'''type选项结合choices选项
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('foo', type = int, choices=range(5,10))

# args = parser.parse_args()
# print(args.foo)

'''choices,限定参数可以选择的内容
'''

# parser = argparse.ArgumentParser()
# parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# args = parser.parse_args()

# print(args.move)

'''choices 搭配type选项,先进行type转化，在进行choices选择判断
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('door', type=int, choices=range(1,4))

# args = parser.parse_args()
# print(args.door)

'''required选线，控制可选参数是否是必须的
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', required=True)

# args = parser.parse_args()
# print(args.foo)

'''help  编写帮助信息
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action='store_true', help='foo the bars before frobbling.')
# parser.add_argument('bar', nargs='+', help='one of the bars to be frobbled.')

# args = parser.parse_args()
# print(args.foo)
# print(args.bar)

'''beyond  sys.argv
'''

# parser = argparse.ArgumentParser()
# parser.add_argument(
#         'integers', metavar = 'int', type=int, choices=range(10),
#         nargs='+', help='an integer in the range 0..9')
# parser.add_argument(
#         '--sum', dest='accumulate', action='store_const', const=sum,
#         default=max, help='sum the integers (default:find the max)')

# args = parser.parse_args()
# print(args)

'''创建子命令  sub-commands
'''

# parser = argparse.ArgumentParser(prog = 'PROG')
# parser.add_argument('--foo', action='store_true', help='foo help')
# subparser = parser.add_subparsers(help='sub-command help')

# parser_a = subparser.add_parser('a', help='a help')
# parser_a.add_argument('bar', type=int, help='bar help')

# parser_b = subparser.add_parser('b', help='b help')
# parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# args = parser.parse_args()

# print(args.foo)
# print(args.bar)
#print(args.baz)

'''对子命令的帮助信息，做修改
'''
# parser = argparse.ArgumentParser()
# subparser = parser.add_subparsers(
#         title = 'subcommands',
#         description = 'valid subcommands',
#         help = 'additional help')

# subparser.add_parser('foo')
# subparser.add_parser('bar')

# args = parser.parse_args()

'''给命令一个别名：  alias
'''
# parser = argparse.ArgumentParser()
# subparser = parser.add_subparsers()
# checkout = subparser.add_parser('checkout', aliases=['co'])  #aliases 报错
# checkout.add_argument('foo')

# args = parser.parse_args()


'''给子命令添加默认函数方法  submmand-line  set_default
'''
# def foo(args):
#     print(args.x * args.y)

# def bar(args):
#     print('((%s))' % args.z)

# #creat top-level parser
# parser = argparse.ArgumentParser()
# subparser = parser.add_subparsers() 

# #create the parser for the 'foo' command
# parser_foo = subparser.add_parser('foo')
# parser_foo.add_argument('-x', type=int, default=1)
# parser_foo.add_argument('y', type=float)
# parser_foo.set_defaults(func=foo)

# #create the parser for 'bar' command
# parser_bar = subparser.add_parser('bar')
# parser_bar.add_argument('z')
# parser_bar.set_defaults(func=bar)

# args = parser.parse_args()
# print(args.func(args))

'''定义文件的读取  FileType
'''

# parser = argparse.ArgumentParser()
# parser.add_argument('--raw', type=argparse.FileType('wb', 0))
# parser.add_argument('out', type=argparse.FileType('w'))

# args = parser.parse_args()
# print(args.raw)
# print(args.out)

'''add_argument_group  ：按照指定的方式对参数进行分类
'''
# parser = argparse.ArgumentParser()
# group = parser.add_argument_group('group')
# group.add_argument('--foo', help='foo help')
# group.add_argument('bar', help='bar help')

# args = parser.parse_args()
# print(args.foo)
# print(args.group)


#实例二：

# parser = argparse.ArgumentParser(prog = 'PROG', add_help=False)
# group1 = parser.add_argument_group('group1', 'group1 description')
# group1.add_argument('foo', help='foo help')
# group2 = parser.add_argument_group('group2', 'group2 description')
# group2.add_argument('--bar', help='bar help')

# print(parser.print_help())

'''创建互斥组： mutual  exclusion
'''

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()

# group.add_argument('--foo', action='store_true')
# group.add_argument('--bar', action='store_true')

# args = parser.parse_args()

'''互斥组中的 required参数
'''

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('--foo', action='store_true')
# group.add_argument('--bar', action='store_false')

# args = parser.parse_args()

'''parser defaults
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('foo', type = int)
# parser.set_defaults(bar=42, baz='badger')

# args = parser.parse_args()

# print(args)

'''默认值的替换
'''

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', default='bar')
# parser.set_defaults(foo='spam')

# print(parser.parse_args())

'''get_default :获得命名空间中的默认值
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', default='badger')
# print(parser.get_default('foo'))

'''解析部分命令行参数
'''
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action='store_true')
# parser.add_argument('bar')

# print(parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam']))


"""
argsparser：再次学习的方法
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nums', metavar='num', type=int, nargs='+',
                    help='a num for the accumulator.')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    htlp='sum the nums (default: find the max)') 










