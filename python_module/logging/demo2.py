#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging

def get_logger(
        level=logging.INFO,
        format='[%(asctime)s \033[1m%(funcName)s\033[0m %(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        verbose=False, **kwargs):

    if verbose:
        level = logging.DEBUG
 
        logging.basicConfig(level=level, format=format, datefmt=datefmt)
 
    return logging.getLogger(__name__)


print(get_logger('aa'))