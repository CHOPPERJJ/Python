# 返回函数值mul()
def count():
    L = []
    for i in range(1, 4):
        def mul():
            return i * i

        L.append(mul())
    return L


a, b, c = count()

print(count())
print(a, b, c)


# 返回函数mul,调用的函数并没有进行计算
def count():
    L = []
    for i in range(1, 4):
        def mul():
            return i * i

        L.append(mul)
    return L


a, b, c = count()
print(count())
print(a(), b(), c())


# 返回函数mul,调用的函数并没有进行计算
def count():
    L = []

    def mul(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        L.append(mul(i))
    return L


a, b, c = count()

print(a())
print(b())
print(c())

# time函数的用法
import time

# 输出时间戳
t = time.time()
# 输出时间元祖
mytime = time.localtime(t)
print('本地时间为：', mytime)

# 输出格式化的时间
formattime = time.asctime(mytime)
print(formattime)

# 输出格式化日期
# 格式化为YY-mm-dd H:M:S形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式化时间为Week mm dd H:M:S Y格式
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

# 将格式化字符串转换为时间戳
a = 'Thu May 17 15:41:56 2018'
b = time.strptime(a, '%a %b %d %H:%M:%S %Y')
print(time.mktime(b))

import functools


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


# 装饰器理解例子
import time


def deco(func):
    def wrapper(a, b):
        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('elapsed time: %f ms' % msecs)

    return wrapper


# @deco
# def myfunc():
#     print('start myfunc')
#     time.sleep(0.6)
#     print('end myfunc')

@deco
def addFunc(a, b):
    print('start addFun')
    time.sleep(0.6)
    print('result is %d' % (a + b))
    print('end addFun')


addFunc(3, 8)


# # 带参数的装饰器
#
# import time
#
#
# def performance(unit):
#     def perf_decorator(f):
#         def wrapper(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
#             print('call %s() in %f %s' % (f.__name__, t, unit))
#             return r
#
#         return wrapper
#
#     return perf_decorator
#
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
#
# print(factorial(10))


# 带参数的装饰器
# import time
#
# def performance(unit):
#     def perf_decorator(f):
#         def wrapper(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             t = (t2 - t1)*1000 if unit =='ms' else (t2 - t1)
#             print ('call %s() in %f %s'%(f.__name__, t, unit))
#             return r
#         return wrapper
#     return perf_decorator
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
#
# print (factorial(10))

# 类和实例，实例属性等
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

# 获取对象属性getattr(),setattr()
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())
