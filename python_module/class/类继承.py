#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''python继承
'''

import os
import gzip

class FileHandle(object):

    def mkdir(self,dirname):
        if os.path.exists(dirname):
            pass
        else:
            os.mkdir(dirname)
    
    def safe_open(self,filename,mode='r'):
        if not filename.endswith('.gz'):
            return open(filename,mode)
        elif filename.endswith('.gz'):
            import gzip
            return gzip.open(filename,mode)
        else:
            print('文件不存咋')



class TestU(FileHandle):

    def __init__(self,args):
        self.filename = args['filename']
        self.dirname = args['dirname']

    
    def print_content(self):
        '''测试类的继承方法,以及try..except的直奔主流
        '''
        if self.dirname:
            print('>>> 创建目录')
            self.mkdir(self.dirname)
        else:
            print('无需创建目录')

        for line in self.safe_open(self.filename, 'r'):
            line = line.strip()
            print(line)
        

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='JUST A TEST')
    parser.add_argument('--filename', help='the input file.')
    parser.add_argument('--dirname', help='output dirname')

    args = vars(parser.parse_args())

    tt = TestU(args)
    tt.print_content()






