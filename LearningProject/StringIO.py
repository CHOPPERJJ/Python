#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())