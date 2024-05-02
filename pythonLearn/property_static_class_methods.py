
class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def sum_test(value1, value2):
        return Student(value1, value2)

    @classmethod
    def sum_test2(cls,value1, value2):
        return cls(value1, value2)

    def __repr__(self):
        return f'< Student {self.name},{self.subject}>'


print(Student.sum_test("Richard", "Science"))
print(Student.sum_test2("Richard2", "Science2"))


class WorkingStudent(Student):
    def __init__(self, name, subject, salary):
        super().__init__(name, subject)
        self.salary = salary

    @property
    def weekly_salary(self):  # if a method only takes  self we can use the @property operator, we will not need
        # brackets when calling it
        return self.salary * 37

    def __repr__(self):
        return f'< WorkingStudent {self.name},{self.subject}, {self.salary}>'


work_student1 = WorkingStudent("Resty", "Math", 1000)
work_student1.marks.append(46)
work_student1.marks.append(30)
print(work_student1.average)
print(work_student1.salary)
print(work_student1.weekly_salary)
