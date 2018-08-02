#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# yield浅析

from collections import Iterable
# # 函数的形式实现
# def fab(max):
#    n, a, b = 0, 0, 1
#    L = []
#    while n < max:
#        a, b = b, a + b
#        n = n + 1
#        L.append(b)
#    return L #list才是iterable对象
#
#
# for n in fab(5):
#     print(n)

# 类的方式实现
# class Feb(object):
#
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()

#
# # 使用yield的方式
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
#
# for n in fab(5):
#     print(n)

# class Bank():
#     crisis = False
#
#     def create_atm(self):
#         while not self.crisis:
#             yield '$100'
#
#
# hsbc = Bank()
# conner_street_atm = hsbc.create_atm()
# print(conner_street_atm.__next__())


# def htest():
#     i = 1
#     while i < 4:
#         n = yield i
#         if i == 3:
#             return 100
#         i += 1
#
#
# def itest():
#     val = yield from htest()
#     print(val)
#
#
# t = itest()
# t.send(None)
# j = 0
# while j < 3:
#     j += 1
#     try:
#         t.send(j)
#     except StopIteration as e:
#         print('异常了')
