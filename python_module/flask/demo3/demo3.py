#!/usr/bin/env python 
#-*- coding:utf-8 -*-


from flask import Flask

app = Flask(__name__)  # 创建一个应用

@app.route('/')
def index():   # 定义根目录处理器
    return '<h1>hello world.</h1>'


if __name__ == '__main__':
    app.run()  # 启动服务