# python的__getietm__()的特殊方法使用，让Fib表现的像list一样
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L


f = Fib()
print(f[2])


# python的__getattr__()特殊方法，链式调用
class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__
