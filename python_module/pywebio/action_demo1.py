#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server
import pywebio 




import json  
             
info = input_group('Add user', [
    input('username', type=TEXT, name='username', required=True),
    input('password', type=PASSWORD, name='password', required=True),
    actions('actions', [
        {'label': 'Save', 'value': 'save'},
        {'label': 'Save and add next', 'value': 'save_and_continue'},
        {'label': 'Reset', 'type': 'reset', 'color': 'warning'},
        {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
    ], name='action', help_text='actions'),
])
put_code('info = ' + json.dumps(info, indent=4))

if info is not None:
    if info['action'] == 'save_and_continue':
        put_text('Save and add next...')  