# objects
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Peter", [45, 78, 88, 45])
print(student_one.average())
print(student_one.__class__)