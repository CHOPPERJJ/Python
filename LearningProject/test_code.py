class Rational(object):
    def __init__(self, p_a, p_b):
        self.a = p_a
        self.b = p_b

    def __add__(self, r):
        return Rational(self.a * r.b + self.b * r.a, self.b * r.b)

    def __str__(self):
        return '%s/%s' % (self.a, self.b)

    __repr__ = __str__


r1 = Rational(1, 3)
r2 = Rational(1, 2)
print(r1 + r2)