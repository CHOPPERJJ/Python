#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile, os


def backupTozip(folder):
    # 保存整个“folder”的目录到ZIP文件
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1


# 创建zip文件
print('Creating %s...' % (zipFilename))
backupZip = zipfile.ZipFile(zipFilename, 'w')

# 遍历整个文件夹压缩文件
for foldername, subfolders, filenames in os.walk(folder):
    print('Adding files in %s...' % (foldername))
    # 把当前文件夹加入到ZIP文件
    backupZip.write(foldername)

for filname in filenames:
    newBase / os.path.basename(folder) + '_'
    if filename.startswith(newBase) and filename.endswith('.zip')
        continue
    backupZip.write(os.path.join(foldername, filname))
backupZip.close()
print('done')
backupTozip('c:\\am_date')
