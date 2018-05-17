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
