#!/usr/bin/env python
#-*- coding:utf-8 -*-
# cli.py
import argparse

class WordsAction(argparse.Action):

    def __call__(self, parser, namespace, values,
                 option_string=None):
        print(f'parser = {parser}')
        print(f'values = {values!r}')
        print(f'option_string = {option_string!r}')

        values = [v.upper() for v in values]
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()
parser.add_argument('--words', nargs='*', action=WordsAction)

results = parser.parse_args()
print(results)








