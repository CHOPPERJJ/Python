#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile, os, shutil, re

# 爱心输出
# print('\n'.join([''.join([('python!'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)