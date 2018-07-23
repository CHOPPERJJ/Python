#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MM-DD-YY美国时间表示转变为DD-MM-YY欧洲时间表示

import os, re, shutil

# 创建美国风格的正则表达式
datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

# 遍历循环文件，寻找满足正则表达式的日期
path = 'c:\\am_date'
for amerFilename in os.listdir(path):
    mo = datePattern.search(amerFilename)
    # print(mo.group(1) + mo.group(2) + mo.group(4) + mo.group(6) + mo.group(8))
    # 略过没有时间的文本
    if mo == None:
        continue

# 获取日期不同的组成部分
beforePart = mo.group(1)
monthPart = mo.group(2)
dayPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)

# # 转变为欧洲时间格式
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
absWorkingDir = os.path.abspath('am_date')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
print(absWorkingDir)
print(amerFilename)
print(euroFilename)
# 重命名文件
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
# shutil.move(amerFilename, euroFilename)
