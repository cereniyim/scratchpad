print("hello world!")

# Codecademy Classes Assignment
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)
            return self.grades

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self, score):
        if score >= self.minimum_passing:
            return print("pass")
        else:
            return print("fail")


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieters_grade = Grade(100)
pieter.add_grade(pieters_grade)
pieters_grade2 = Grade(40)
pieter.add_grade(pieters_grade2)

pieters_grade.is_passing(40)
roger.attendance = {"01-01-2019": 1, "02-01-2019": 0}
print(roger.attendance)