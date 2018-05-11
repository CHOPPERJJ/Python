# coding=utf-8
# 遍历set,set中为tuple的项目，x[0]访问第一项，x[1]访问第二项
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
<<<<<<< HEAD
    print(x[0], ':', x[1])
=======
    print (x[0], ':', x[1])
>>>>>>> 1ecd9dbb021578ae5e1aa7c8628cff8e619a42b6

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
L = range(1, 101)
W = []
print(list(L[:11]))
for i in L:
    x = L[i]
    if x % 3 == 0:
        W.append(x)
