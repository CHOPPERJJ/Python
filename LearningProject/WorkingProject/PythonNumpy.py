#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Numerical Python高性能科学计算和数据分析基础包

import numpy as np

# data1 = [6, 7.5, 8, 0, 1]
# arr1 = np.array(data1)
# print(arr1)

# numpy的transpose函数的使用
arr = np.arange(16).reshape((2, 2, 4))
print(arr)

arr2 = arr.transpose((1, 0, 2))
print(arr2)