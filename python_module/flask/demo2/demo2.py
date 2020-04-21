#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run() 


""" 模板技术： MVC
model --> View --> Controller

用户请求 -- 脚本处理 -- 模板替换 -- 用户看到

C: python 处理url的函数
V：最终输出
M：传给View的数据
""" 

"""flask 的默认模板：jinja2

    除了Jinja2，常见的模板还有：

    Mako：用<% ... %>和${xxx}的一个模板；

    Cheetah：也是用<% ... %>和${xxx}的一个模板；

    Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

"""


