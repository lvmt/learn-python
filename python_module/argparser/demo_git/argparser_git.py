#!/usr/bin/env python
#-*- coding:utf-8 -*-

import argparse

def cli():
    """
    git 命令程序入口
    """
    parser = argparse.ArgumentParser(prog="git")
    subparser = parser.add_subparsers(
        title="These are common Git commands used in various situations",
        metavar="commands")

cli()