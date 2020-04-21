#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class Json2mongo(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 27017

    ## read json file
    def _open_file(self, filename):
        self.file = open(filename, 'r')
        self.client = MongoClient(self.host, self.port)
        # create database
        self.db = self.client.study
        self.collections = self.db.jobs

    ## close file
    def _close_file(self):
        self.file.close()

    ## write data
    def write_database(self, filename):
        self._open_file(filename)

        data = json.load(self.file)

        try:
            self.collections.insert(data)
            print('写入成功')
        except Exception as e:
            print(e)
        finally:
            self._close_file()

if __name__ == "__main__":
    j2m = Json2mongo()
    j2m.write_database('test.json')
    