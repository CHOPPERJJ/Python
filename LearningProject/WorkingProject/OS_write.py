#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, os, shutil, send2trash
datePattern = re.compile(r'''
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d)
  
    ''', re.VERBOSE)
path = 'c:\\am_date'
all = os.listdir(path)
for files in all:
    mo = datePattern.search(files)
    print(mo.group(1))
