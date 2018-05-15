# coding=utf-8
# 进阶Python

# 高阶函数
import math


def add(x, y, f):
    return f(x) + f(y)


print(add(25, 9, math.sqrt))


# map()函数应用,capitalize()首字母大写的函数
def format_name(s):
    return s.capitalize()


print(list(map(format_name, ['adam', 'LISA', 'barT'])))

# 用reduce()函数求积
from functools import reduce


def prod(x, y):
    return x * y


print(reduce(prod, [2, 4, 5, 7, 12]))

# filter()函数过滤出1-100中平方根是整数的数
import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(is_sqr, list(range(1, 101)))))

# sorted()自定义排序函数
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


# 写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def plus(x, y):
        return x * y

    return reduce(plus, lst)


f = calc_prod([1, 2, 3, 4])
print(f)
