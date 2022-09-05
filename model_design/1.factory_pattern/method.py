#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-06-24 16:50:04
'''

import json
import xml.etree.ElementInclude as etree


class JSONConnector:

    def __init__(self, filepath):
        self.data = {}
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    
    @property
    def parsed_data(self):
        return self.data



class XMLConnector:
    
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)


    @property
    def parsed_data(self):
        return self.tree 



def connection_factory(filepath):
    '''工厂方法'''
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError(f'connot connect to {filepath}')
    return connector(filepath)

    

