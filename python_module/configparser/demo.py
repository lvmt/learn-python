#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""learn the use of configparser
"""

import configparser

"""该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节（section），每个节可以有多个参数（键=值）。节与java原先的配置文件相同的格式
"""

"""生成配置文件
"""
# config = configparser.ConfigParser()    #实例化对象
# config['DEFAULT'] = {'ServerAliveInterval' : '45',
#                      'Compression' : 'yes',
#                      'CompressionLevel' : '9',
#                      'ForwardX11' : 'yes'
#                     }        ##类似于操作字典的形式

# config['bitbucket.org'] = {'User':'Atlan'} #类似于操作字典的形式

# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

# with open('example2.ini', 'w') as configfile:   #这种方式，有点难以理解
#     config.write(configfile)
    

"""读取配置文件的内容

[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = Atlan

[topsecret.server.com]
host port = 50022
forwardx11 = no

"""
# config = configparser.ConfigParser()

# #print(config.sections())   # []

# config.read('example.ini')    # read a ini.file

# print(config.sections()) 
# #['bitbucket.org', 'topsecret.server.com']  # not print default section


# print(config['bitbucket.org']['user'])
# # Atlan

# print(config['DEFAULT']['Compression'])
# # yes

# for key in config['topsecret.server.com']:
#     print(key)
    
# ## 除了本身sections的值外，还会输出default的值

# print(config['topsecret.server.com'])
# #  <Section: topsecret.server.com>

# print(config.options('topsecret.server.com'))
# # ['host port', 'forwardx11', 'serveraliveinterval', 'compression', 'compressionlevel']

# print(config.items('topsecret.server.com'))
# # [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'no'), ('host port', '50022')]

# print(config.get('bitbucket.org', 'user')) 
# # Atlan


"""修改配置文件
"""

# config = configparser.ConfigParser()

# config.read('example.ini')

# config.add_section('yuan')  #添加一个section

# config.remove_section('bitbucket.org')   #delete section

# config.remove_option('topsecret.server.com', 'forwardx11')   #delelt a config item

# ## add item to sections
# config.set('topsecret.server.com', 'k1', '11111')
# config.set('yuan', 'k2', '22222')
# with open('new2.ini', 'w') as f:
#     config.write(f)

