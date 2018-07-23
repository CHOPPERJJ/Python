#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, os, shutil, send2trash
datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)-
    (.*?)$
    ''', re.VERBOSE)
path = 'c:\\am_date'
all = os.listdir(path)
for files in all:
    mo = datePattern.search(files)
    print(mo.group(1))

# os.unlink('c:\\am_date\\file.txt')
# file1 = open('c:\\am_date\\我的日期是07-23-2018.txt', 'w')
# file2 = open('c:\\am_date\\我的日期是04-03-2017.txt', 'w')
# file3 = open('c:\\am_date\\我的日期是07-12-2016.txt', 'w')
# file4 = open('c:\\am_date\\我的日期是07-12-2016.txt', 'w')
# file5 = open('c:\\am_date\\我的日期是02-23-2019.txt', 'w')
# file6 = open('c:\\am_date\\我的日期是12-13-2018.txt', 'w')
# file7 = open('c:\\am_date\\我的日期是07-12-2016.txt', 'w')
# file8 = open('c:\\am_date\\我的日期是07-03-2018.txt', 'w')
# file9 = open('c:\\am_date\\我的日期是10-20-2017.txt', 'w')

