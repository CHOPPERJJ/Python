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

# 匿名函数简化代码
l = lambda x: x and len(x.strip()) > 0
s = filter(l, ['test', None, '', 'str', ' ', 'END'])
print(list(s))

print(list(filter(lambda x: x and len(x.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])))


# 函数装饰器的应用
# hello.py
def now():
    print('2015-3-27')


# 函数也是对象，将函数now赋值给变量f
f = now
# f指向函数now，f() = now()
print(f.__name__)
f()
# 将函数值now()赋值给变量f
f = now()
print(now.__name__)


# 装饰器函数的使用解析，编写一个log,f = factorial
def log(f):
    # 创建一个装饰器函数fn,如果调用，fn返回的函数赋给了原函数factorial = fn(factorial),新factorial==f,旧的factorial就被隐藏了。
    def fn(x):
        # 打印日志
        print('call ' + f.__name__ + '()...')
        # 调用原函数也就是factorial()
        return f(x)
    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# 写一个@perfomance的函数，可以打印出函数调用的时间
import time

def performance(origin):
    def showtimes(*args, **kw):
        print('call ' + origin.__name__ + '() in ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        return origin(*args, **kw)
    return showtimes


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# 编写带参数的decorator，将上述函数增加一个参数，允许传入s或者ms
import time

def performance(unit):
    def decorator(f):
        def wrapper(*args, **kw):
            print('call' + f.__name__ + '() in ' + time.strftime('%a, %b, %d, %H:%M:%S', time.localtime()))
            return unit(*args, **kw)
        return wrapper
    return decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

factorial(10)