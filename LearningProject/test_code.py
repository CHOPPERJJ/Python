class Fib(object):
    def __init__(self, p_num):
        self.num = p_num
        a, b, L = 0, 1, []
        for x in range(p_num):
            L.append(a)
            a, b = b, a + b
        self.list = L

    def __call__(self, p):
        print('Fib is %s' % self.list)


# 调用实例对象f，f即是函数也是对象，函数可以被调用，也就是直接调用实例对象函数
f = Fib(10)
print(f(10))


class Fib(object):
    def __call__(self, p_num):
        self.num = p_num
        a, b, L = 0, 1, []
        for x in range(p_num):
            L.append(a)
            a, b = b, a + b
        return L


f = Fib()
print(f(10))
