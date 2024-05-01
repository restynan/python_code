# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, subject, salary):
        super().__init__(name, subject)
        self.salary = salary


work_student1 = WorkingStudent("Resty", "Math", "1000")
work_student1.marks.append(46)
work_student1.marks.append(30)
print(work_student1.average())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
