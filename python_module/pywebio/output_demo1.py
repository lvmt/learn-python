#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server
import pywebio 


from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def main():
    # with use_scope('scope3'):
    #     put_text('text1 in scope3')   # output to current scope: scope3
    #     put_text('text in ROOT scope', scope='ROOT')   # output to ROOT Scope
    
    # put_text('text2 in scope3', scope='scope3')   # output to scope3


    def edit():
        put_text("You click edit button")
    def delete():
        put_text("You click delete button")

   
    put_buttons(['edit', 'delete'], onclick=[edit, delete])
    put_buttons(['yes', 'no'], onclick=[edit, delete])
    
    


    # put_tabs([
    #     {'title': 'Text', 'content': 'Hello world'},
    #     {'title': 'Markdown', 'content': put_markdown('~~Strikethrough~~')},
    #     {'title': 'More content', 'content': [
    #         put_table([
    #             ['Commodity', 'Price'],
    #             ['Apple', '5.5'],
    #             ['Banana', '7'],
    #         ]),
    #         put_link('pywebio', 'https://github.com/wang0618/PyWebIO')
    #     ]},
    # ])


    # put_collapse('Collapse title', [
    #     'text',
    #     put_markdown('~~Strikethrough~~'),
    #     put_table([
    #         ['Commodity', 'Price'],
    #         ['Apple', '5.5'],
    #     ])
    # ], open=True)
    
    

    # import time
    # put_scrollable(put_scope('scrollable'), height=200, keep_bottom=True)
    # put_text("You can click the area to prevent auto scroll.", scope='scrollable')
    
    # while 1:
    #     put_text(time.time(), scope='scrollable')
    #     time.sleep(0.5)






start_server(main, port=8080, debug=True)
