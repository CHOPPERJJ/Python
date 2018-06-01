class Student(object):
    self.name = name
    self.score = score

class Student(Person):

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print (sorted(L, key=lambda student:(student.score,student.name))