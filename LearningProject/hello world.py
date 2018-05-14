# coding=utf-8
# 入门Python
# 遍历set,set中为tuple的项目，x[0]访问第一项，x[1]访问第二项
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x[0], ':', x[1])

# 更新set或者删除set中的元素
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for it in L:
    if it in s:
        s.remove(it)
    else:
        s.add(it)
print(s)

# python函数练习
L = []
for i in range(1, 101):
    L.append(i * i)
print(sum(L))


# 定义函数def
def square_of_sum(L):
    return sum(i * i for i in L)


print(square_of_sum([1, 2, 3, 4, 5]))
print(square_of_sum([-5, 0, 5, 15, 25]))

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解
# ax2 + bx + c = 0
import math


def quadratic_equation(a, b, c):
    y = math.sqrt(b * b - 4 * a * c)
    if y >= 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1, x2
    else:
        return none


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


# python递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 默认参数练习
def great(y='World'):
    print('Hello', y)


great()
great('Bart')


# 可变参数练习
def average(*args):
    if len(args) != 0:
        return sum(args) * 1.0 / len(args)
    else:
        return 'error'


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4, ))

# list和tuple切片
# L = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10，11--------100]
L = range(1, 101)
# 从索引0开始到索引10-1，取出10-0个元素
print(list(L[0:10]))
# 从索引2开始到结束，每隔3-1个元素取出
print(list(L[2::3]))
# 从索引4开始到索引50，每隔5-1个元素取出
print(list(L[4:50:5]))
# 从索引-10开始到索引-1，取出元素
print(list(L[-10:]))
# 从索引-10-1开始到索引结束，取出元素
print(list(L[:-10]))


# 字符串切片练习，设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
def firstCharUpper(s):
    s1 = s[0].upper()
    s2 = s[1:]
    return s1 + s2


print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))

# python的迭代就是for循环
for i in range(1, 101):
    if i % 7 == 0:
        print(i)

# 迭代函数enumerate()使用方法
L = ['Adam', 'Lisa', 'Bart', 'Paul']
t = zip(range(1, len(L) + 1), L)
for rank, name in t:
    print(rank, '--', name)

# values()和itervalues()方法都可以迭代dict,只是实现方式不
# 练习dict计算所有同学的平均分。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
avg = (sum(d.values()) + 0.0) / len(d.values())
print(avg)

# 迭代dict的key和value
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
for name, score in d.items():
    print(name, ':', score)
avg = (sum(d.values()) + 0.0) / len(d.values())
print('average', ':', avg)

# 列表生成
L = [x * (x + 1) for x in list(range(1, 100, 2))]
print(L)

# 复杂表达式
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, }


# def generate_tr(name, score):
#     if score < 60:
#         return '<tr><td>%s</td><td style = "color:red">%s</td></tr>' % (name, score)
#     return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
#
#
# tds = [generate_tr(name, score) for name, score in d.iteritems()]
# print('<table border="1">')
# print('<tr><th>Name</th><th>Score</th><tr>')
# print('\n'.join(tds))
# print('</table>')


# 条件过滤for循环的列表生成，编写一个函数，接受一个list,然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print(toUppers(['Hello', 'world', 101]))

# 多层表达式
L = [x*100 + y*10 + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z]
print(L)