#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series
# d = {'name': ['a', 'b', 'c'], 'num': [1, 2, 3]}
# lt = [('a', 1), ('b', 2), ('c', 3)]
# ld = [{'name': 'a', 'num': 1},
#       {'name': 'b', 'num': 2},
#       {'name': 'c', 'num': 3}]
#
# ld1 = [{'a': 1}, {'b': 2}, {'c': 3}]
# ls = [{'a', 1}, {'b', 2}, {'c', 3}]
# d1 = {'a': 1, 'b': 2, 'c': 3}
# pd.DataFrame(d)
print('用一维数组生成Series')
x = Series([1, 2, 3, 4])
print(x)



