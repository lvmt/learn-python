#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author:lvmengting
@Date:2022/07/27 16:17:11
'''

import asyncio  
import time  


'''
所有的异步函数声明要加async
在一个async函数内，异步调用需要使用await或者其它方式“异步等待”
要运行一个async函数，需要使用asyncio.run来执行。
'''

# # 普通例子 使用async await语法实现的一个和串行程序等价的程序
# async def my_task(name):
#     print('# start ', name)
#     await asyncio.sleep(2)
#     print('# end ', name)
    
    
# async def main():
#     await my_task('run')
#     await my_task('eat')
#     await my_task('study')
    
    
# asyncio.run(main())


# 如果我们要理解async有什么好处，不妨先对执行代码记个时，如图。
# 如果用三个await按照顺序等待，浪费了时间，第一个my_task陷入sleep开始等待时，完全可以启动第二个my_task。
# t0 = time.time()

# async def my_task(name):
#     print(f'# start {name} @ {time.time() - t0:.2f}')
#     await asyncio.sleep(2)
#     print(f'# end {name} @ {time.time() - t0:.2f}')
    
    
# async def main():
#     await my_task('run')
#     await my_task('eat')
#     await my_task('study')
    
    
# asyncio.run(main())


# 改进如图，使用一个await等待3个，3个my_task使用asyncio.create_task依次创建，用asyncio.gether收集。
# 我们看到，执行3个任务总共2秒。看print输出，是3个先都启动，然后3个都结束。

t0 = time.time()

async def my_task(name):
    print(f'# start {name} @ {time.time() - t0:.2f}')
    await asyncio.sleep(2)
    print(f'# end {name} @ {time.time() - t0:.2f}')
    
    
async def main():
    await asyncio.gather(
        asyncio.create_task(my_task('run')),
        asyncio.create_task(my_task('eat')),
        asyncio.create_task(my_task('study'))
    )
    
    
asyncio.run(main())

