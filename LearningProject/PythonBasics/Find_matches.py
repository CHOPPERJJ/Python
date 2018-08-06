#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip, re
phoneRegex = re.compile(r'''(--snip--)''')

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])