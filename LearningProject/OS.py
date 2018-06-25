#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')
print('           Size          Last Modified Name')
print('-----------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getatime(f)).strftime('%Y %m %d %H:%M')
    flag = '/' if os.path.isdir(f)else ''
<<<<<<< HEAD
    print('%10d %s %s' % (fsize, mtime, f))
=======
    print('%10d %s %s%s' % (fsize, mtime, f, flag))
>>>>>>> 259c6158de7b9221ee04135160a9ef2e796409ed
