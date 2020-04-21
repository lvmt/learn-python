import hashlib


# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf8'))    ##python3的 hashlib 前，需要使用encoding，
# print(md5.hexdigest)

"""设计一个用户登录的函数，根据用户输入的口令是否正确，返回True 或 False
"""

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, passwd):
    md5 = hashlib.md5(passwd.encode('utf8')).hexdigest()
    if user in db:
        if md5 == db[user]:
            print('True')
        else:
            print('False')
    else:
        print('not in db')
        
def main(user, passwd):
    login(user, passwd)
    

if __name__ == "__main__":
    user = input('input your name:')
    passwd = input('inout your password:')
    main(user, passwd) 