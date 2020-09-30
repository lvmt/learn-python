#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''自定义异常
'''

class InvalidCharError(Exception):
    pass

class NotChinaTelError(Exception):
    pass


def register():
    tel = input('请注册您的电话号码: ')
    
    # 如果有非数字字符
    if not tel.isdigit():
        raise InvalidCharError
    
    # 如果不是以86开头，则不是中国号码
    if not tel.startswith('86'):
        raise NotChinaTelError
    
    return tel
    
    
def check_register():
    try:
        ret = register()
    except InvalidCharError:
        print('电话号码中有错误字符')
    except NotChinaTelError:
        print('非中国手机号码') 
        
if __name__ == '__main__':
    
    check_register()
    
    

