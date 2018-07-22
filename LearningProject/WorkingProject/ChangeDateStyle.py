#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MM-DD-YY美国时间表示转变为DD-MM-YY欧洲时间表示

import shutil. os, re

# 创建美国风格的正则表达式
datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3?\d)-
    ((19|20)\d\d)-
    (.*?)$
    ''', re.VERBOSE)

# 遍历循环文件，寻找满足正则表达式的日期
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# 略过没有时间的文本
    if mo == none:
        continue

# 获取日期不同的组成部分
brforePart = mo.group(1)
monthPart  = mo.group(2)
dayPart    = mo.group(4)
yearPart   = mo.group(6)
afterPart  = mo.group(8)