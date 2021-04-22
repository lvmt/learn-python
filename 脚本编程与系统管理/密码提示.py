#!/usr/bin/env python

import getpass

# user = getpass.getuser()
user = 'lmt'
passwd = getpass.getpass()

print(user)
def login(user, passwd):
    if user == 'lmt' and passwd == '123456':
        return True
    else:
        return False


if login(user, passwd):
    print('Yay!')
else:
    print('Boo!')

