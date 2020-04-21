#!/usr/bin/env python
#-*- coding:utf-8 -*-


# # 1. 定义接口描述
# """Num accumulator.

# Usage:
#   cmd.py [--sum] <num>...
#   cmd.py (-h | --help)

# Options:
#   -h --help     Show help.
#   --sum         Sum the nums (default: find the max).
# """

# from docopt import docopt

# # 2. 解析命令行
# arguments = docopt(__doc__, options_first=True)

# # 3. 业务逻辑
# nums = (int(num) for num in arguments['<num>'])

# if arguments['--sum']:
#     result = sum(nums)
# else:
#     result = max(nums)

# print(result)



"""
Usage:
  cli [options]

Options:
  -n, --name NAME   Set name.
"""
from docopt import docopt

arguments = docopt(__doc__, argv=['-n', 'Eric'])
print(arguments)

arguments = docopt(__doc__, argv=['-nEric'])
print(arguments)

arguments = docopt(__doc__, argv=['--name', 'Eric'])
print(arguments)

arguments = docopt(__doc__, argv=['--name=Eric'])
print(arguments)




