#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 批量修改文件名

import os, re
one_original_name = re.compile(r'(我的英雄学院_S2_.*)(.ass)')

path = 'G:\\我的英雄学院第二季字幕'
name = os.listdir(path)
# print(name)
for one_name in name:
    mo = one_original_name.search(one_name)
    print(mo.group())
    if mo == None:
        continue


two_original_name = re.compile(r'(\[Moozzi2\] Boku no Hero Academia S2 - )(\d\d)( \(BD 1920x1080 x\.264 Flac\))(\.mkv)')
path2 = 'H:\\Animation\\[Moozzi2] Boku no Hero Academia S2 - TV + OAD'
name2 = os.listdir(path2)
print(name2)
for two_name in name2:
    mo2 = two_original_name.search(two_name)
    print(mo2.group())
    if mo2 == None:
        continue

# filename = mo.group(1)
# fuffixname = mo.group(2)
#
# changename = filename + fuffixname

