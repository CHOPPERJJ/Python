#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shelve
# 正常读写工作
baconFile = open('bacon.txt', 'w')
baconFile.write('#!/usr/bin/env python3\n# -*- coding: utf-8 -*-')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('\n1234567890')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

shelveFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelveFile['cats'] = cats
shelveFile.close()

