#/usr/bin/python
#!-*- coding:utf-8 -*-

"""练习正则表达式的使用
"""


"""验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

# import re


# def main():
#     username = input("请输入用户名称： ")
#     qq = input("请输入QQ号码：")
#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#     if not m1:
#         print("请输入有效的用户名：")
    
#     m2 = re.match(r'^[1-9\d{4,11}]$', qq)
#     if not m2:
#         print("请输入有效的qq号。")
#     if m1 and m2:
#         print("你输入的信息是有效的！")

# if __name__ == "__main__":
#     main()


"""从文字中提取电话号码
"""

# import re 

# def main():
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')  
#     sentence = """
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     """
#     #查找所有的匹配，并保存到一个列表中
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('--------华丽丽的分割线--------')
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('--------华丽丽的分割线--------')

#     #通过search函数指定搜索位置找出所有匹配
#     m = pattern.search(sentence)  ##找到第一个
#     print(m)   
#     print(m.end())    #返回找到字符串的尾部位置信息
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())

# if __name__ == "__main__":
#     main()


"""替换字符串中的不良内容
"""

# import re


# def main():
#     sentence = "你丫是傻叉吗？我操你大爷。Fuck you."
#     purified = re.sub('[操艹肏]|fuck|shit|傻[逼比箅吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)

#     print(purified)

# if __name__ == "__main__":
#     main()

"""拆分长字符串
"""

# import re 


# def main():
#     poem = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"
#     sentence_list = re.split(r'[，。, .]', poem)
#     while '' in sentence_list:
#         sentence_list.remove('')
#     print(sentence_list)

# if __name__ == "__main__":
#     main()

