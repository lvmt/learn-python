#!/usr/bin/env python  
#-*- coding:utf-8 

"""
学习logger模块的用法
"""



"""
demo1
"""

# import logging
# import time 

# def logger():
#     logging.basicConfig(
#         format='[%(asctime)s %(funcName)s %(levelname)s] %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S',
#         level=logging.INFO)
#     return logging.getLogger(__name__)

# def spend_time():
#     return logger().info('time used: {:.1f}s'.format(time.time() ))

# print(spend_time()) 


"""
demo2
"""

# import logging

# logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(name)s - %(levelname)s %(message)s')
# logger = logging.getLogger(__name__)

# logger.info('start print log')
# logger.debug('Do something')
# logger.warning('something maybe fail')
# logger.info('finish')


"""
demo3： 将日志写入文件
"""

import logging  

# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler('log.txt')
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# logger.info('start print log')
# logger.debug('Do someting')
# logger.warning('something maybe fail.')
# logger.info('Finish')


"""
同时将日志文件输出到屏幕和文件中
"""

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
 
console = logging.StreamHandler()
console.setLevel(logging.INFO)
 
logger.addHandler(handler)
logger.addHandler(console)
 
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
