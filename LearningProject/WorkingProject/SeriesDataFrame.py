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



# # drop方法返回一个在指定轴上删除了指定值的新对象（我也看不懂什么意思）
# obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
# new_obj = obj.drop('c') #索引和索引对象都删除了
# print(new_obj)
#
# # DataFrame可以删除任意轴上的索引值
# data = DataFrame(np.arange(16).reshape((4, 4)),
#                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
#                  columns=['one', 'two', 'three', 'four'])
# print(data)
# new_data = data.drop(['Colorado', 'Ohio'])
# print(new_data)
# new_data2 = data.drop('one', axis=1)
# print(new_data2)



# # 索引选取和过滤，series的索引不是整数
# obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# bb = obj['b']
# print(bb)

# # DataFrame行上进行索引，使用引用字段ix
# data = DataFrame(np.arange(16).reshape((4, 4)),
#                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
#                  columns=['one', 'two', 'three', 'four'])
# print(data)
# data1 = data.ix['Colorado', ['two', 'three']]
# print(data1)
# data2 = data.ix[['Colorado', 'Utah'], ['two', 'three']]
# print(data2)
# data3 = data.ix[2]
# print(data3)
# data4 = data.ix[:'Utah', 'two']
# print(data4)




# # 算数运算和数据对齐
# s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
# print(s1 + s2)
#
# # DataFrame的对齐操作会同时发生在行和列上
# df1 = DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))
# df2 = DataFrame(np.arange(20).reshape((4, 5)), columns=list('abcde'))
# print(df2)
# print(df1 + df2)
# df3 = df1.add(df2, fill_value=0)
# print(df3)
# df4 = df1.reindex(columns=df2.columns, fill_value=0)
# print(df4)

# # DataFrame 和 Series之间的运算
# arr = np.arange(12).reshape((3, 4))
# print(arr)
# print(arr - arr[0])
# frame = DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'),
#                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# series = frame.ix[0]
# print(frame)
# print(series)
# print(frame - series)
#
# # 行上广播要使用算数云算法
# series3 = frame['d']
# print(series3)
# series4 = frame.sub(series3, axis=0)
# print(series4)




# 函数应用和映射numpy的ufuncs元素数组方法
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)