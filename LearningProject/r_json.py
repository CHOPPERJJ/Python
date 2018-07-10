#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd

with open('movies.json', encoding='utf-8') as f:
    s = f.read()
data = json.loads(s)
df = pd.DataFrame(data)
print(df)