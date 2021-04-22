#!/usr/bin/env python

import fileinput

with fileinput.input('a.txt') as f:
    for line in f:
        # print(line, end='')
        print(f.filename(), f.lineno(), line, end='')
