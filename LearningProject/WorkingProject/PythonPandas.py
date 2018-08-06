#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np


a = [4, 7, -5, 3]
b = {'Lucy': 4, 'Lilei': 7, 'Michal': -5, 'Dark': 3}
c = ['Lucy', 'Michal', 'Jack', 'Dark']
d = {'name': ['a', 'b', 'c'], 'num': [1, 2, 3]}
lt = [('a', 1), ('b', 2), ('c', 3)]
ld = [{'name': 'a', 'num': 1},
      {'name': 'b', 'num': 2},
      {'name': 'c', 'num': 3}]
ld1 = [{'a': 1}, {'b': 2}, {'c': 3}]
ls = [{'a', 1}, {'b', 2}, {'c', 3}]
d1 = {'a': 1, 'b': 2, 'c': 3}

# Series的索引可以通过赋值的方式修改
# obj = Series(a)
# obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# print(obj)

# obj2 = Series(a, index = ['d', 'b', 'a', 'c'])
# print(obj2)
# print(obj2[['c', 'a', 'd']])
# obj2['d'] = 6
# print(obj2[['c', 'a', 'd']])
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print(Series(d1))

# obj3 = Series(sdata)

# obj4 = Series(states)
# 算数运算自动对齐
# print(obj3 + obj4)

# print(Series(sdata, index=states))
# obj4.name = 'population'
# obj4.index.name = 'state'
# print(obj4)

# DataFrame的使用例子
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
frame = DataFrame(data)
print(frame)

framed = DataFrame(data, columns=['year', 'state', 'pop'])
print(framed)

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)

# 列的位置捕获
ff = frame2.state
print(ff)

# 行的位置捕获
ii = frame2.ix['three']
print(ii)

# 给空的'debt'赋值
frame2['debt'] = [2, 4, 5, 5, 6]
print(frame2)
frame2['debt'] = np.arange(5.)
print(frame2)
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(val)
print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
frame2['western'] = frame2.year == 2001
print(frame2)