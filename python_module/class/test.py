#!/usr/bin/env python
#-*- coding:utf-8 -*-



# import argparse

# class Test(object):

#     def __init__(self):
#         self.name = args.get('name') if args['name'] else "None"
#         self.age = args.get('age') if args['age'] else  "None"

#     def _print(self):
#         print(Test().__dict__)
#         print("你的名字是{name}, 今年{age}岁。".format(**Test().__dict__))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--name')
#     parser.add_argument('--age')

#     args = vars(parser.parse_args())

#     test = Test()
#     test._print()


# import os
# filedir = os.path.dirname(os.path.abspath(__file__))
# print(filedir)
# # C:\Users\dell\Desktop\python_code\python_module\class

# dirname = os.path.dirname(os.path.dirname(filedir))
# print(dirname)
# # 
# # ]eC:\Users\dell\Desktop\python_code


# import argparse

# class Test(object):
#     def __init__(self, args):
#         self.name = args['name']
#         self.age = args['age']
#         self.height = args['height']
#         self.weight = args['weight']
#         self.guess = float(args['height']) * float(args['weight'])
#         print(self.__dict__)
        
#         new_map = {'aa':11, 'bb':22}
#         self.__dict__.update(**new_map)

#         print(self.__dict__)

#     def my_guess(self):
#         print(self.guess)
#         tt = self.guess * self.guess
#         print(tt)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--name')
#     parser.add_argument('--age')
#     parser.add_argument('--height', type=float)
#     parser.add_argument('--weight', type=float)

#     args = vars(parser.parse_args())
#     # print(args)

#     test = Test(args)
#     test.my_guess()
    
 
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-a')
# parser.add_argument('-b')
# args = vars(parser.parse_args())

# result = args['a']  or args['b']
# print(result)



from collections import defaultdict

all_dict = defaultdict(dict)

all_dict['mike']['age'] = 18
all_dict['bob']['age'] = 22

print(all_dict)
