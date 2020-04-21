#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""测试子命令参数
"""

import argparse


def test_math():
    """math 程序接口
    """
    parser = argparse.ArgumentParser(prog="math test")
    parser.add_argument('-a')

    subparser = parser.add_subparsers(
        title="these are used for math",
        metavar="Commands")

    ## add
    add_parser = subparser.add_parser('add', help="add nums")
    add_parser.add_argument('-x', type=int)
    add_parser.add_argument('-y', type=int)
    add_parser.set_defaults(func=add)

    ## delelt
    delete_parser = subparser.add_parser('delete',help="delete nums")
    delete_parser.add_argument('-max', type=int)
    delete_parser.add_argument('-min', type=int)
    delete_parser.set_defaults(func=delete)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        print(args.__dict__)  ## 可以打印出 args对象拥有的属性 
        args.func(args)
    else:
        parser.print_help()

def add(args):
    result = args.x + args.y
    print(result)

def delete(args):
    result = args.max - args.min
    print(result)

if __name__ == "__main__":
    test_math()
    

    
