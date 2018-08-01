#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# yield浅析


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
class Feb(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

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