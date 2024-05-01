
# special methods
# __init__ # python calls it directly
class Student:
    def __init__(self, name):
        self.grades = []
        self.name = name

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, i):
        return self.grades[i]

    def __repr__(self):
        return f'Student name:{self.name} , grades:{self.grades}'

    def __str__(self):
        return f'Student name:{self.name} , grades:{self.grades} using str function'


student1 = Student("Peter")
student1.grades.append(75)
student1.grades.append(89)
student1.grades.append(30)

print(len(student1))
print(student1[0])

print(student1.grades)

print(student1)


# repr -> used for debuging to print an object
# str ->  used to print an object