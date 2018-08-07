#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame
import numpy as np


# # reindex重新索引，创建一个适应新索引的新对象
# obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# print(obj)
# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# print(obj2)
#
# # method方法做一些插值处理
# obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj3)
# obj4 = obj3.reindex(range(6), method='ffill')
# print(obj4)
#
# # DataFrame和Series可以修改索引、行、列，或者两个都修改
# frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
#                   columns=['Ohio', 'Texas', 'California'])
# print(frame)
# frame2 = frame.reindex(['a', 'b', 'c', 'd'])
# print(frame2)
# states = ['Texas', 'Utah', 'California']
# frame3 = frame.reindex(columns=states)
# print(frame3)
# # 对行列同时进行重新索引
# frame4 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=states)
# print(frame4)
# frame5 = frame.ix[['a', 'b', 'c', 'd'], states]
# print(frame5)



# drop方法返回一个在指定轴上删除了指定值的新对象（我也看不懂什么意思）
obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c') #索引和索引对象都删除了
print(new_obj)

# DataFrame可以删除任意轴上的索引值
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data)
new_data = data.drop(['Colorado', 'Ohio'])
print(new_data)
new_data2 = data.drop('one', axis=1)
print(new_data2)