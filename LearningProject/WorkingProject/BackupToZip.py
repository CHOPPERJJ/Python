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