#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""定义一个app.py，可以处理3个url，
GET/: 首页，返回home
GET/signin：登录页， 显示登录表单
POST /signin：处理登录表单， 显示登录节结果
"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=["POST"])  
def signin():
    #需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'passwd':
        return '<h3>Hello admin!</h3>'
    return  '<h3>Bad username or password.</h3>'

if __name__ == "__main__":
    app.run() 

# http://localhost:5000/ 显示首页
# http://localhost:5000/signin 显示登录页


"""实际的Web app，应该拿到用户名和口令后，去数据库进行查找比对，来判断用户是否登录成功


    Django：全能型Web框架；

    web.py：一个小巧的Web框架；

    Bottle：和Flask类似的Web框架；

    Tornado：Facebook的开源异步Web框架。

"""