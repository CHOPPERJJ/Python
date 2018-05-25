# coding=utf-8
# 进阶Python

# 面向对象编程
class Person(object):
    pass


p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, key=lambda x: x.name)

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)


# Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
class Person(object):
    def __int__(self, name, sex, birth, **kw):
        self.name = name
        self.sex = sex
        self.birth = birth
        self.__dict__.update(kw)

    def print_things(self):
        print('%s, %s, %s, %s' % (self.name, self.sex, self.birth, self.job))


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print(xiaoming.name)
print(xiaoming.sex)
xiaoming.print_things()