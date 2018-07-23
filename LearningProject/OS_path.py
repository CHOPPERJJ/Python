#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
p = os.path.join('usr', 'bin', 'spam')
print(p)

p1 = os.getcwd()
print(p1)

# p2 = os.makedirs('c:\\delicies\\wanfe\\waswf')

p3 = os.path.abspath('.')
print(p3)

p4 = os.path.abspath('.\\script')
print(p4)

# 路径是相对路径返回False
p5 = os.path.isabs('.')
print(p5)

# 路径是绝对路径返回True
p6 = os.path.isabs(os.path.abspath('.'))
print(p6)

path = 'C:\\Windows\\System32\\calc.exe'
p7 = os.path.basename(path)
print(p7)