#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author:lvmengting
@Date:2022/07/27 16:17:11
'''


import asyncio
import time
import random


async def work(msg):
    print(f'收到的消息: {msg}')
    print('{}1{}'.format('*'*10, '*'*10))
    await asyncio.sleep(random.random)
    print('{}2{}'.format('*'*10, '*'*10))
    print(msg)
    
    
async def main():
    # 创建两个任务对象(携程), 并加入书剑循环中
    
    Coroutines1 = asyncio.create_task(work('hello'))
    Coroutines2 = asyncio.create_task(work('python'))
    print("开始时间: {}".format(time.asctime(time.localtime(time.time()))))
    await Coroutines1  # 此时并发运行Coroutines1和Coroutines2
    print("{}3{}".format("*"*10,"*"*10)) # 为了方便，展示结果
    await Coroutines2 # await相当于挂起当前任务，去执行其他任务，此时是堵塞的
    print("{}4{}".format("*"*10,"*"*10)) # 为了方便，展示结果
    print("结束时间:{}".format(time.asctime(time.localtime(time.time()))))
    
    
asyncio.run(main())


