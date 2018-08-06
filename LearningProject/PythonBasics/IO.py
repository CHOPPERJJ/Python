#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IO编程
from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y - %m - %d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

# write to StringIO
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


# read to stringIO
f = StringIO('Helloooo!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
print(s.strip())


# write to BytesIO
from io import BytesIO

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

# read to BytesIO
date = '两情若是久长时，又岂在朝朝暮暮。'.encode('utf-8')
bi = BytesIO(date)
print(bi.read())
