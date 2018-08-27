#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# loads()读取json
stringOfJasonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ":null}'
jsonValue = json.loads(stringOfJasonData)
print(jsonValue)

# dumps()写入json
pythonValue = {'isCat':True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
Data = json.dumps(pythonValue, indent=4)
with open('dumps.json', 'w', encoding='utf-8') as f:
    f.write(Data)
print(Data)