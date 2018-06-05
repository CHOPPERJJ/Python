class Student(object):
    def __init__(self, p_name, p_score):
        self.name = p_name
        self.__score = p_score

    @property
    def score(self):
        return self.__score

    def grade(self):
        return self.__grade

    @score.setter
    def score(self, p_score):
        if p_score < 0 or p_score > 100:
            raise ValueError('invalid score')
        self.__score = p_score

    @property
    def grade(self, p_score):
        if p_score >= 80:
            self.__grade = 'A'
        elif p_score > 60:
            self.__grade = 'B'
        else:
            self.__grade = 'C'


s = Student('Bob', 59)
s.score = 60
print(s.grade)
s.score = 99
print(s.grade)
