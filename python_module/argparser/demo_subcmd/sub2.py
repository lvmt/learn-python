#!/usr/bin/env python
#-*- coding:utf-8 -*-


import argparse



class BamStat(object):

    # def __init__(self,parser):
    #     self.parser = parser

    def parser_add_depth(self,parser):

        parser.add_argument(
            'bam',
            help='bam文件'
        )

        parser.add_argument(
            '-r', 
            '--region',
            help='指定区间'
        )

        parser.add_argument(
            '-ref',
            '--refversion',
            help='参考基因组版本'
        ) 

        parser.set_defaults(func=self.stat_func)
        pass


    def parser_add_flag(self,parser):

        pass


    def stat_func(self,**args):
        print("这是统计字命令的输出{}".format(args['bam']))
        pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="subcommand")

    subparser = parser.add_subparsers(
        title="sub-commands",
        dest="subparser_name",
        metavar=""
    )

    demo = BamStat()

    # 0 统计深度
    parser_depth = subparser.add_parser(
        'depth',
        formatter_class=argparse.RawTextHelpFormatter,
        help='stat bam depth'
    )

    demo.parser_add_depth(parser_depth)


    # 1 统计flag
    parser_flag = subparser.add_parser(
        'flag',
        formatter_class=argparse.RawTextHelpFormatter,
        help='stat bam flag'
    )

    demo.parser_add_flag(parser_flag)


    args = parser.parse_args()
    print(args)
    print(type(args))
    args.func(**vars(args))


