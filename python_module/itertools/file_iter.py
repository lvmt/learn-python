#!/usr/bin/env python3
#-*- coding:utf-8 -*-


'''管道符方式读取文件
'''

import os
import fnmatch
import gzip
import bz2
import re 


def gen_find(filepat, top):
    '''
    find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)


def gen_opener(filenames):
    '''
    open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close() 


def gen_concatenate(iterators):
    '''Chain a sequence of iterators togeter into a single sequence.
    '''
    for it in iterators:
        yield from it 


def gen_grep(pattern, lines):
    '''
    look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line  




