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
    def __init__(self, myname, sex, birth, **kw):
        self.name = myname
        self.sex = sex
        self.birth = birth
        self._title = 'Mr'
        # self.__dict__.update(kw)将job传到了**kw里，**kw相当于接收了任意关键字参数
        self.__dict__.update(kw)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print(xiaoming.name)
print(xiaoming.sex)
print(xiaoming.job)
print(xiaoming._title)


# python中访问限制
class Person(object):
    def __init__(self, name, score):
        self.__myname = name
        self.__score = score

    def get_myname(self):
        return self.__myname

    # 创建可以访问内部score的方法
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


p = Person('Bob', 59)
p.set_score(60)
print('p.get_myname()=', p.get_myname())
print('p.get_score()=', p.get_score())


# 创建类属性
class Person(object):
    count = 0

    def __init__(self, name):
        self.getname = name
        Person.count = Person.count + 1


p1 = Person('Bob')
print(Person.count)

p2 = Person('Alice')
print(Person.count)

p3 = Person('Tim')
print(Person.count)


# 定义实例的方法
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self, score):
        if score >= 90:
            return 'A'
        elif score >= 60:
            return 'B'
        else:
            return 'C'

    def get_grade_two(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_grade_three(self):
        if self.__score >= 90:
            a = 'A'
        elif self.__score >= 60:
            a = 'B'
        else:
            a = 'C'
            return a


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.name, p1.get_grade(90))
print(p2.name, p2.get_grade_two())
print(p3.name, p3.get_grade_three())


# 定义类方法__count为类的私有属性
class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())


# 继承和多态
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.gender)
print(t.course)


# python中判断类型
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print(t.gender)
print(isinstance(p, Person))
print(isinstance(s, Student))
print(isinstance(t, Teacher))
print(isinstance(s, Student))
print(isinstance(t, Person))
print(isinstance(t, object))


# python多态
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am Teacher, my name is %s' % self.name

    def who_am_i(x):
        print(x.whoAmI())


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print(p.whoAmI())
print(s.whoAmI())
print(t.whoAmI())

# File-like Object,把一个字符串r'["Tim", "Bob", "Alice"]'包装成File-like Obeject并由json.load()解析
import json


class Student(object):
    def __init__(self, name):
        self.name = name

    def read(self):
        return self.name


s = Student('["Tim", "Bob", "Alice"]')
print(json.load(s))


# python中—__str__和__repr__
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    # 给person加上__str__方法
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)


p = Person('Bob', 'male')
print(p)


# 给student类定义__str__和__repr__方法
class Person(object):
    def __init__(self, p_name, p_gender):
        self.name = p_name
        self.gender = p_gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)

    __repr__ = __str__


s = Student('BBob', 'male', 88)
print(s.name)
print(s)


# python中的__cmp__方法
class Student(object):
    def __init__(self, p_name, p_score):
        self.att_name = p_name
        self.att_score = p_score

    def __str__(self):
        return '(%s: %s)' % (self.att_name, self.att_score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.att_name < s.name:
            return -1
        elif self.att_name > s.name:
            return 1
        else:
            return 0


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print(s.name)


# python中的__len__函数的用法,编写一个斐波那契数Fib类(6-4)进阶篇
class Fib(object):
    def __init__(self, p_num):
        self.num = p_num
        a, b, L = 0, 1, []
        for x in range(p_num):
            L.append(a)
            a, b = b, a + b
        self.list = L

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)


f = Fib(10)
print(f)
print(len(f))


# python中数学运算,涉及传参的问题，注意理解里面参数的传递方式
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


class Rational(object):
    def __init__(self, p_a, p_b):
        self.a = p_a
        self.b = p_b

    def __add__(self, r):
        return Rational(self.a * r.b + self.b * r.a, self.b * r.b)

    def __sub__(self, r):
        return Rational(self.a * r.b - self.b * r.a, self.b * r.b)

    def __mul__(self, r):
        return Rational(self.a * r.a, self.b * r.b)

    def __truediv__(self, r):
        return Rational(self.a * r.b, self.b * r.a)

    def __str__(self):
        c = gcd(self.a, self.b)
        return '%s/%s' % (self.a / c, self.b / c)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)


# python 类型转换
class Rational(object):
    def __init__(self, p_a, p_b):
        self.a = p_a
        self.b = p_b

    def __int__(self):
        return self.a // self.b

    def __float__(self):
        return self.a / self.b


print(int(Rational(7, 2)))
print(int(Rational(1, 3)))
print(float(Rational(7, 2)))
print(float(Rational(1, 3)))


# python中的@property应用举例
class Student(object):
    def __init__(self, p_score):
        self.__score = p_score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, p_score):
        if p_score < 0 or p_score > 100:
            raise ValueError('invalid score')
        self.__score = p_score

    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


s = Student(59)
print(s.grade)

s.score = 60
print(s.grade)

s.score = 99
print(s.grade)


# python中使用__slots__限制实例添加属性
class Person(object):
    __slots__ = ('name', 'gender')

    def __init__(self, p_name, p_gender):
        self.name = p_name
        self.gender = p_gender


class Student(Person):
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, p_name, p_gender, p_score):
        self.name = p_name
        self.gender = p_gender
        self.gender = p_score


s = Student('Bob', 'male', '59')
s.name = 'Tim'
s.score = 99
print(s.name, s.score)